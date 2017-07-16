from gcodeparser import GCodeParser
import csv

class FileOperator():

    def __init__(self, motor, x_mil, y_mil, z_mil):
        """Initialize."""
        self.motor = motor
        self.x_millimeter = x_mil
        self.y_millimeter = y_mil
        self.z_millimeter = z_mil

    def printfile(self, filepath):
        with open(filepath, 'r') as fp:
            reader = csv.reader(fp, delimiter=';')
            data = [row for row in reader]

        lastrow = data[0]
        for row in data:
            delta_step = self.relative_steps(lastrow, row)
            corrected_coords = self.corrected_coords(delta_step)
            self.motor.move(corrected_coords)
            lastrow = row

    def relative_steps(self, lastrow, row):
        """Calculates steps needed to get from lastrow to current row"""
        if len(row) != 3:
            row = lastrow
        last_x = float(lastrow[0])
        x = float(row[0])
        last_y = float(lastrow[1])
        y = float(row[1])
        last_z = float(lastrow[2])
        z = float(row[2])
        # subtracting the value of each coordinate to get the required movement
        delta_step = [last_x - x, last_y - y, last_z - z]
        return delta_step

    def corrected_coords(self, delta_step):
        """Takes array[x,y,z] of millimeters and returns steps for motor"""
        # Needs to be rounded to int for whole steps
        x_move = int(delta_step[0] * x_millimeter)
        y_move = int(delta_step[1] * y_millimeter)
        z_move = int(delta_step[2] * z_millimeter)
        print('move')
        print([x_move, y_move, z_move])
        return([x_move, y_move, z_move])

    @staticmethod
    def OpenFile(filename):
        data = GCodeParser.OpenFile(filename)
        # the data of the file is stored as a list on a Variable
        FileOperator.data = data
        length = len(data)
        FileOperator.length = length
        return length

    @staticmethod
    def GetLine(line):
        # returns the line which was described in the input as a list
        new_position = GCodeParser.FromLine(FileOperator.data, line)
        return(new_position)

    @staticmethod
    def NextMove(newline):
        # after getting the input of the row which is next in line, this function returns the movement needed to get there
        lastline = newline  - 1
        # retrieving the two rows
        initial_step = FileOperator.GetLine(lastline)
        next_step = FileOperator.GetLine(newline)
        # saving the list entrys of each row as "float" to be able to subtract without loosing precicion
        initial_x = float(initial_step[0])    
        next_x = float(next_step[0])
        initial_y = float(initial_step[1])    
        next_y = float(next_step[1])
        initial_z = float(initial_step[2])    
        next_z = float(next_step[2]) 
        # subtracting the value of each coordinate to get the required movement pattern 
        delta_step = (initial_x - next_x, initial_y - next_y, initial_z - next_z)
        return(delta_step)

    @staticmethod
    def MoveCorrect(next_move):
        # Translates the requiered movement from mm to steps the stepper will have to complete
        # factores are set in the variables file
        # input and output are lists. saved as "int" to round to full steps
        x_move = int(next_move[0] * x_step_p_millimeter) 
        y_move = int(next_move[1] * y_step_p_millimeter) 
        z_move = int(next_move[2] * z_step_p_millimeter) 
        return(x_move, y_move, z_move)

    # def MoveToPosition (addition)

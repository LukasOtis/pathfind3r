from gcodeparser import GCodeParser
from variables import Variables

x_step_p_millimeter = Variables.x_step_p_millimeter
y_step_p_millimeter = Variables.y_step_p_millimeter
z_step_p_millimeter = Variables.z_step_p_millimeter
filename = Variables.filename

class FileOperator():
    @staticmethod
    def OpenFile():
        # opens the csv file which is set in the variables and returns the lentgh
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
from test_gcodeparser import GCodeParser
from variables import Variables

x_step_p_millimeter = Variables.x_step_p_millimeter
y_step_p_millimeter = Variables.y_step_p_millimeter
z_step_p_millimeter = Variables.z_step_p_millimeter

class FileOperator():
    def OpenFile():
        filename = 'test.csv'
        data = GCodeParser.OpenFile(filename)
        FileOperator.data = data
        length = len(data)
        FileOperator.length = length
        return length

    @staticmethod
    def GetLine(line):
        new_position = GCodeParser.FromLine(FileOperator.data, line)
        return(new_position)

    @staticmethod
    def NextMove(newline):
        lastline = newline  - 1
        initial_step = FileOperator.GetLine(lastline)
        next_step = FileOperator.GetLine(newline)
        initial_x = float(initial_step[0])    
        next_x = float(next_step[0])
        initial_y = float(initial_step[1])    
        next_y = float(next_step[1])
        initial_z = float(initial_step[2])    
        next_z = float(next_step[2])  
        delta_step = (initial_x - next_x, initial_y - next_y, initial_z - next_z)
        return(delta_step)

    def MoveCorrect(next_move):
        x_move = int(next_move[0] * x_step_p_millimeter) 
        y_move = int(next_move[1] * y_step_p_millimeter) 
        z_move = int(next_move[2] * z_step_p_millimeter) 
        return(x_move, y_move, z_move)
from gcodeparser import GCodeParser

class FileOperator():
    def OpenFile():
        filename = 'test.csv'
        filesize = GCodeParser.OpenFile(filename)
        length = filesize[0]
        data = filesize[1]
        FileOperator.data = data
        FileOperator.length = length
        return

    def GetLine(line):
        new_position = GCodeParser.FromLine(FileOperator.data, line)
        print(new_position)


""""Open file, get lentgh"""
FileOperator.OpenFile()
print(FileOperator.length)

"""Get first line"""
initial_step = FileOperator.GetLine(1)
print(initial_step)
x_ini = initial_step[0]


print(x_initial_step)
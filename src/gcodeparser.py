class GCodeParser:
    def __init__(self, xcoord, ycoord, zcoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord

    @staticmethod
    def fromLine(line):
        if len(line) == 0:
            return None

        if line[0] == 'G':
            xcoord = float(0)
            ycoord = float(0)
            zcoord = float(0)

            # Extract X coordinate
            if 'X' in line:
                temp = line[line.index('X'):]
                temp = temp[1:GCodeParser.getDelimiter(temp)]
                xcoord = float(temp)

            # Extract Y coordinate
            if 'Y' in line:
                temp = line[line.index('Y'):]
                temp = temp[1:GCodeParser.getDelimiter(temp)]
                ycoord = float(temp)

            # Extract Z coordinate
            if 'Z' in line:
                temp = line[line.index('Z'):]
                temp = temp[1:GCodeParser.getDelimiter(temp)]

                zcoord = float(temp)
            return GCodeParser(xcoord, ycoord, zcoord)
        elif line[0] == 'M':
            return GCodeParser(0, 0, 0)
        else:
            return None

    @staticmethod
    def getDelimiter(string):
        if ' ' in string:
            index = string.index(' ')
        else:
            return len(string)

        offset = len(string) - index
        offset = offset * -1
        return offset

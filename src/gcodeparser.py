import csv

class GCodeParser:
    def __init__(filename):
        file = open('filename')
        reader = csv.reader(file)
        data = list(reader)
        length=len(data)
        return GCodeParser(length)

    @staticmethod
    def fromLine(line):
        if data(line) == '':
            return None

        else
            row = data[line]
            value = (row[0])
            xcoord = float(0)
            ycoord = float(0)
            zcoord = float(0)

            # Extract X coordinate
            index_one = value.index(';')
            x_value = value[0:index_one]
            xcoord = float(x_value)

            # Extract Y coordinate
            temp = value[index_one+1:len(value)]
            index_two = temp.index(';')
            y_value = temp[0:index_two]
            ycoord = float(y_value)

            # Extract Z coordinate
            z_value = temp[index_two+1:len(temp)]
            zcoord = float(z_value)
            
            coords=list(xcoord, ycoord, zcoord)
        return GCodeParser(coords)


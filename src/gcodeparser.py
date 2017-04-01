import csv

class GCodeParser:
    def __init__(self, xcoord, ycoord, zcoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord

        csv.register_dialect('excel', delimiter=',')
        file = open('test.csv')
        reader = csv.reader(file)
        data = list(reader)

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
            
        return GCodeParser(xcoord, ycoord, zcoord)


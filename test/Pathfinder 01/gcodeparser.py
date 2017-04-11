import csv
class GCodeParser:
    @staticmethod
    def OpenFile(filename):
        file = open(filename)
        reader = csv.reader(file)
        data = list(reader)
        length = len(data)
        return data

    @staticmethod
    def FromLine(data, line):
        row = data[line]
        value = (row[0])
        coordinates = []

        # Extract X coordinate
        index_one = value.index(';')
        xcoord = value[0:index_one]

        # Extract Y coordinate
        temp = value[index_one+1:len(value)]
        index_two = temp.index(';')
        ycoord = temp[0:index_two]

        # Extract Z coordinate
        zcoord = temp[index_two+1:len(temp)]

        # return Coordinates
        coordinates.append(xcoord)
        coordinates.append(ycoord)
        coordinates.append(zcoord)
        return (coordinates)
        
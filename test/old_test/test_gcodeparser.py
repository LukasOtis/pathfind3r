import csv
class GCodeParser:
    @staticmethod
    def OpenFile(filename):
        file = open(filename)
        reader = csv.reader(file)
        data = list(reader)
        length = len(data)
        return length, data

    @staticmethod
    def FromLine(data, line):
        row = data[line]
        value = (row[0])

        # Extract X coordinate
        index_one = value.index(';')
        xcoord = value[0:index_one]
        print(xcoord)
        # Extract Y coordinate
        temp = value[index_one+1:len(value)]
        index_two = temp.index(';')
        ycoord = temp[0:index_two]

        # Extract Z coordinate
        zcoord = temp[index_two+1:len(temp)]

        # return Coordinates
        coords = (xcoord, ycoord, zcoord)
        print(coords)
        coordinates = list(coords)
        print(coordinates)
        return coordinates



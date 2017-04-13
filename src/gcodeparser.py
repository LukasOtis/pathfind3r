import csv
class GCodeParser:
    @staticmethod
    def OpenFile(filename):
        # after retrieving the filename, the function opens this file ans returns the data as a list
        file = open(filename)
        # to open the file the csv-libary wich has been inported at the beginning of the file is needed
        reader = csv.reader(file)
        data = list(reader)
        # each list etry consists of the x,y,z cooridantes of one position
        return data

    @staticmethod
    def FromLine(data, line):
        # formates the line discribed in the input so each indivitual coordinate can be stored and used
        # input is a list-entry with the format: (x_coordinate; y_cooridnate; z_coordinate)
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
        



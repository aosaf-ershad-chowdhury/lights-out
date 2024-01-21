# This file defines a single function printMap
# Since printing the game board/map is particularly
# very important, the function has been separated
# from the rest of the files

def printMap(currentMap):
    # Takes a 2D array containing the map as a parameter

    # The following lines basically creates a list
    # The list will support in printing the x-axis
    # at the bottom
    i = int(len(currentMap)-1)

    # The first list is the numbers in the x-axis
    # The second list is the symbols
    xCoordinate = [[0], [' ']]
    line = []

    for i in range(0, len(currentMap[len(currentMap)-1])+1):
        xCoordinate[0].append(' -')
        xCoordinate[1].append(" " + str(i))
    
    # Some padding is made for the UI
    print()
    print()

    numberOfRow = int(len(currentMap))

    for row in reversed(currentMap):
        print("                                 ", end=" ") # Some extra padding to the left
        if numberOfRow > 9:
            print(numberOfRow, '| ', end = ' ')
        else:
            print(numberOfRow, ' | ', end = ' ')
        print(*row, sep = '  ') # Prints the main row of the game
        numberOfRow -= 1
    
    # Prints the x-axis
    for row in xCoordinate:
        print("                                 ", end=" ")
        print(*row, sep = ' ')



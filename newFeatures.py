# This is a test file which will be used to 
# incorporate new features, such as colors
# into the final game as we develop it further
# in private forks and repositories after the
# submission deadline

# It has been included to show possible extensions
# but may contain some non-conventional coding
# since they have not gone through rigorous testing
# to be included into the final game

def makeYourGame():
    lightOnColor = input('Light color(red, green, blue, gray, yellow): ')
    wallColor = input('wall color(red, green, blue, gray, yellow): ')
    lightOffColor = 'black'
    
    possibleInput = ['0', '1', 'X']
    dict = {'black': "\033[40;30m \033[0m", 'red': "\033[41;31m \033[0m", 'green': "\033[42;32m \033[0m", 'blue': "\033[44;34m \033[0m", 'gray': "\033[47;33m \033[0m", 'yellow': "\033[43;33m \033[0m"}
    
    lst = []
    lst1 = []
    
    userMap = ''
    coloredUserMap = ''
    
    print(coloredUserMap)
    print('Instruction: ')
    print('1. 0 = light off, 1 = light on, X = wall. Other than these three values considered as invalid')
    print('2. X should surround 0 and 1.')
    print('3. Their should be at least one light on')
    print('4. You will type your map one line, so if you are done with a line, enter your output')
    print('5. If users complete their map, they can type complete, and then system will check if the map is vaild or not')
    print('6. If users type invalid map, game returns to option for making a game or try our own game section')
    print('7. Users do not have to make rectangular map, but the number of input in each line should be consistent.')
    print('For example: ')
    print('Valid: ')
    print('XXXXXX\nXX010X\nX1011X\nX0X00X\nXXXXXX')
    print('Invalid: ')
    print('XXXXX\nXX010X\nX1011X\nX0X00X\nXXXXXX')
    print('Now you can create map: ') 
    
    while True:
        createdMap = input()
        if createdMap == 'done':
            break
        lst = list(map(str, createdMap))
        lst1.append(lst)
    
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst[0] != lst[i]:
                return 'invalid'
            if lst1[i][j] not in possibleInput:
                return 'invalid'
            if i == 0 or i == len(lst1) -1 or j == 0 or j == len(lst1[0])-1:
                if lst1[i][j] != 'X':
                    return 'invalid'
    
    print(lst1)
    
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j] == 'X':
                coloredUserMap += dict[wallColor]  
            if lst1[i][j] == '0':
                coloredUserMap += dict[lightOnColor]
            if lst1[i][j] == '1':
                coloredUserMap += dict[lightOffColor]
        coloredUserMap += '\n'
    
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            userMap += lst1[i][j]
        userMap += '\n'            
    
    mapName = input('What is your map name? ')
    with open(f'{mapName}', 'w') as f:
        f.write(coloredUserMap)


def bringUserGameaWithColor():
    mapName = input('What is a map name that you want to play? ')
    try: 
        f = open(f'{mapName}', 'r')
        return(f.read())
    except: 
        return


makeYourGame()
bringUserGame()

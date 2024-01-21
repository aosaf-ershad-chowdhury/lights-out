# Contains the main() function which makes extensive use
# of all the other defined functions in this and other files
# to produce a final working game
# Also contains a few subsidiary important functions

# os is used for clearing terminal
# time is used for the timings and animation effect
# random is used to display a random custom map (please check
# main function for more info)


import os
import time
import random

from uiAnimations import *
from messageUI import *
from gameMechanics import *
from printMap import printMap


def getUserMove():
    # Obtains the user move and returns in relevant format for further processing

    print("                             Enter coordinates(x, y) or 'END' to give up:") # A slight left padding
    inputList = list(input("                                               ").split()) # Input with left padding added

    if inputList[0] == "END":
        return "END", "END" # Using this, the main() function can easily break out
    
    moveX, moveY = inputList

    try:
        return int(moveX), int(moveY)
    except:
        return moveX, moveY # In case the inputs are not numbers


def printSignOrLog():
    # This functions will provide an interface asking whether
    # the user would like to sign up or log in (or just exit the game)

    # Clear the terminal first
    os.system('cls' if os.name == 'nt' else 'clear')

    # Some top and left padding added
    # Although technically 'unnecessary', the spaces are added in the print
    # statements to aid the programmer and reader get a slight idea about the positioning
    # of the interface
    print("                                                                              ")
    print("                                                                              ")
    print("                              ###############################################################")
    print("                              ###############################################################")
    print("                                                                              ")
    print("                                                  What would you like to do?                 ")
    print("                                                                              ")
    print("                              ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                       1. SIGN UP")
    print("                                                       2. LOG IN")
    print("                                                       3. EXIT")
    print("                                                                              ")
    print("                              ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                 Enter the instruction number:")
    userInstruction = input("                                                             ")
    
    # Handles potential wrong inputs by the user
    try:
        userInstruction = int(userInstruction)
        if userInstruction != 1 and userInstruction !=2 and userInstruction != 3:
            handleInvalidInitialInstruction()
            userInstruction = printSignOrLog()
    except:
        handleInvalidInitialInstruction() # User inputted a string
        userInstruction = printSignOrLog()
    return userInstruction


def signUp():
    # Provides a user interface for the user to sign up
    # Returns whether the registration was successful
    # Also returns the username

    os.system('cls' if os.name == 'nt' else 'clear')
    print("                                                                              ")
    print("                                                                              ")
    print("                              ###############################################################")
    print("                              ###############################################################")
    print("                                                                              ")
    print("                                                  Create a New Account                 ")
    print("                                                                                             ")
    print("                              ---------------------------------------------------------------")
    print("                                                                              ")
    userName = input('                                           Enter Username(must be one word): ')
    
    # Handles spaces in username and empty username
    if " " in userName or userName == "":
        handleInvalidInitialInstruction()
        return False, 0
    
    # Checks the case whether username already exists
    currentFile = open('userAccount.txt','r')
    currentFileContents = currentFile.readlines()
    for line in currentFileContents:
        currentName = list(line.split())
        if currentName!=[] and currentName[0] == userName:
                handleUsernameTaken()
                return False, 0
    currentFile.close()

    print("                                                                              ") # Adds a padding for a better interface
    userPassword = input('                    Enter Password(must be one word containing alphanumeric characters and $@!& only): ')
    
    for char in userPassword:
        if not char.isalnum() and char != '$' and char != '@' and char != '!' and char != '&':
            handleInvalidInitialInstruction()
            return False, 0
    
    currentFile = open('userAccount.txt','a')
    currentFile.write(f"{userName} {userPassword} 1-- 2-- 3-- 4-- 5-- 6-- 7-- 8-- 9-- 10-- 11-- 12-- 13-- 14-- 15-- 16-- 17-- 18-- 19-- 20--\n")
    currentFile.close()

    return True, userName


def logIn():
    # Provides the user an interface to log into
    # their accounts

    # Terminal screen cleared and padding added
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                                                                              ")
    print("                                                                              ")
    print("                              ###############################################################")
    print("                              ###############################################################")
    print("                                                                              ")
    print("                                                          Log In                 ")
    print("                                                                              ")
    print("                              ---------------------------------------------------------------")
    print("                                                                              ")

    userName = input('                                                     Enter Username: ')
    userPassword = input('                                                     Enter Password: ')

    # Checks for presence of the user account
    accountFile = open('userAccount.txt','r')
    accountFileContents = accountFile.readlines()
    userFound = False # For checking if the user is in the file at all

    for line in accountFileContents:
        currentUser = list(line.split())
        if currentUser != "[]" and currentUser != "['\n']":
            if currentUser[0] == userName:
                userFound = True
                if currentUser[1] == userPassword:
                    return True, userName
                else:
                    handleWrongPassword()
                    return False, 0
    
    # Handkes the case where username was not found
    if not userFound:
        handleUserNotFound()
        return False, 0


def printPlayScreen():
    # Creates one of the main interfaces of the game 'lobby'
    # The "Welcome!" ASCII art was made with
    # https://www.asciiart.eu/image-to-ascii
    # However, the space formatting was done by us

    os.system('cls' if os.name == 'nt' else 'clear')
    print("                                                                              ")
    print("                                                                              ")
    print("                           ###############################################################")
    print("                           ###############################################################")
    print("""
                                    __        __   _                          _
                                    \ \      / /__| | ___ ___  _ __ ___   ___| |
                                     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
                                      \ V  V /  __/ | (_| (_) | | | | | |  __/_|
                                       \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
    
    """)
    print("                           ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                What would you like to do?")
    print("                                                1. PLAY ORIGINAL LEVELS")
    print("                                                2. PLAY CUSTOM LEVELS")
    print("                                                3. MAKE YOUR OWN BOARD")
    print("                                                4. HOW TO PLAY")
    print("                                                5. EXIT")
    print("                                                                                          ")
    print("                           ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                              Enter the instruction number:")
    userInstruction = input("                                                          ")

    try:
        userInstruction = int(userInstruction)
        if userInstruction != 1 and userInstruction !=2 and userInstruction != 3 and userInstruction!=4 and userInstruction != 5:
            handleInvalidInitialInstruction()
            userInstruction = printPlayScreen()
    except:
        # When user inputs a non-numeric character
        handleInvalidInitialInstruction()
        userInstruction = printPlayScreen()

    return userInstruction


def playGame(level, currentMap):
    # The 'game' itself defined by the map
    # as well as the interface and padding
    # is displayed through the code
    # Also takes note of the number of moves taken by the user
    # to solve the board and returns it, together with whether
    # the user was successful in solving the board

    numMoves = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("               ###############################################################")
        print("               ###############################################################")
        print("                                                                              ")
        print(f"                                             LEVEL {level}                       ")
        print("                                                                              ")
        print("               ---------------------------------------------------------------")
        printMap(currentMap)
        print("                                                                              ")
        print("               ---------------------------------------------------------------")
        print("                                                                              ")
        
        # The value 1 must be subtracted from these move values
        # to get the original coordinates

        try:
            moveY, moveX = getUserMove() # Flipped moves because of the way 2D lists work
        except:
            handleInvalidInitialInstruction()
            continue
        
        # When the user gives up
        if moveX == moveY and moveY == "END":
            handlePlayerLoss()
            return -1
        
        # Handles invalid moves, otherwise makes the move
        if checkMove(moveX, moveY, currentMap) == 0:
            handleInvalidCoordinates()
        elif checkMove(moveX, moveY, currentMap) == 2:
            handleNonTileSelected()
        else:
            makeMove(moveX-1, moveY-1, currentMap)
            numMoves += 1
        
        # Checks whether the board is solved
        if checkEndGame(currentMap):
            printBulbForwardLoad()
            handlePlayerWin()
            return numMoves


def getMapName(levelInfo, userName):
    # Displays all the playable levels for the user
    # and shows the lowest number of moves in that level by the user

    os.system('cls' if os.name == 'nt' else 'clear')
    print("               ###############################################################") # Some extra hash to handle user scrolling up
    print("               ###############################################################")
    print("               ###############################################################")
    print("               ###############################################################")
    print("                                                                              ")
    print(f"                                {userName} User Details")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                           Level                  Best Number of Moves     ")

    # Checks whether the user has completed the level or not
    # Makes adjustment to the output based on whether the level number
    # is one digit or two digits
    for level in levelInfo:
        if levelInfo[level] == "":
            if int(level) > 9:
                print(f"                             {level}                           -")
            else:
                print(f"                             {level}                            -")
        else:
            if int(levelInfo[level]) <= 9:
                if int(level) < 9:
                    print(f"                             {level}                            {levelInfo[level]}")
                else:
                    print(f"                             {level}                           {levelInfo[level]}")
            else:
                if int(level) < 9:
                    print(f"                             {level}                           {levelInfo[level]}")
                else:
                    print(f"                             {level}                          {levelInfo[level]}")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                  Which level would you like to play?")
    userInput = input("                                                 ")
    
    # Handles invalid user inputs such as non-numeric inputs
    # as well as out of range levels
    try:
        userInput = int(userInput)
        if userInput < 1 and userInput >20:
            handleInvalidInitialInstruction()
            userInput = getMapName(levelInfo, userName)
    except:
        handleInvalidInitialInstruction()
        userInput = getMapName(levelInfo, userName)
    
    return userInput


def customGameMake(username):
    # Allows the user to make their own custom game

    os.system('cls' if os.name == 'nt' else 'clear')

    # Starts off with an interface to make the game-making
    # process more satisfying
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                                                              ")
    print("                                 Enter your map here (press ENTER twice if you have completed)                 ")
    print("                                                                              ")
    print("                                ---------------------------------------------------------------")
    print("                                                                              ")
    
    # Stores the user input line by line in a list
    userMap = []
    while True:
        line = input("                                                                ")
        if line =="":
            # When user has pressed enter, the game-making process has been completed
            break
        userMap.append(line)
    
    try:
        charNum = len(userMap[0])
    except:
        handleLessMakeChars()
        customGameMake(username)
        return

    # Checks for mistakes in the user input
    for line in userMap:
        for char in line:
            # Checks for invalid characters in each line
            if char != "X" and char != "0" and char != "1":
                handleInvalidMakeChars()
                customGameMake(username)
                return
        
        # Checks whether empty input provided
        if len(line) < 1:
            handleLessMakeChars()
            customGameMake(username)
            return
        
        # Checks whether the number of columns is more thant 9
        if len(line) > 9:
            handleExcessMakeChars()
            customGameMake(username)
            return
        
        # Checks whether each row contains the same number of characters
        if len(line) != charNum:
            handleInconsistentMakeChars()
            customGameMake(username)
            return
    
    # Checks whether a solved board is made by the user
    if checkEndGame(userMap):
        handleSolvedBoard()
        customGameMake(username)
        return()
    
    # Checks whether there are more than 9 rows in the user's map/board
    if len(userMap) > 9:
        handleExcessMakeChars()
        customGameMake(username)
        return

    # The first line contains the number of games made
    # So the new file must have a name with that plus 1
    accountFile = open('customMapInfo.txt','r')
    accountFileContents = accountFile.readlines()
    newFileNumber = int(accountFileContents[0].strip()) + 1
    accountFile.close()

    # Update number of custom maps available
    accountFile = open('customMapInfo.txt','w')
    for i in range(len(accountFileContents)):
        if i == 0:
            accountFile.write(f"{newFileNumber}\n")
        else:
            accountFile.write("".join(accountFileContents[i]))
    accountFile.close()

    # Adds the user who made a particular game in the text
    # file for proper credits
    accountFile = open('customMapInfo.txt', 'a')
    accountFile.write(f"{newFileNumber} {username}\n")
    accountFile.close()

    # Makes the game file
    newFile = open(f"maps/custom_maps/{newFileNumber}.map", 'w')
    for line in userMap:
        newFile.write(f"{''.join(line)}\n")
    newFile.close()

    # Inform the user that game making has been successful
    handleSuccessfulGameMake()


def playCustomGame():
    # The user can play games made by other users
    # through this function
    
    accountFile = open('customMapInfo.txt','r')
    accountFileContents = accountFile.readlines()
    maxNumFiles = int(accountFileContents[0].strip())
    accountFile.close()

    currentMapName = random.randint(1, maxNumFiles)
    currentMap = readMap(f'maps/custom_maps/{currentMapName}.map')

    accountFile = open('customMapInfo.txt','r')
    accountFileContents = accountFile.readlines()
    mapMaker = (accountFileContents[currentMapName].strip()).split()[1]
    accountFile.close()

    numMoves = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("               ###############################################################")
        print("               ###############################################################")
        print("                                                                              ")
        print(f"                                             GAME BY: {mapMaker}                     ")
        print("                                                                              ")
        print("               ---------------------------------------------------------------")
        printMap(currentMap)
        print("                                                                              ")
        print("               ---------------------------------------------------------------")
        print("                                                                              ")
        
        # The value 1 must be subtracted from these move values
        # to get the original coordinates

        try:
            moveY, moveX = getUserMove() # Flipped moves because of the way 2D lists work
        except:
            handleInvalidInitialInstruction()
            continue
        
        # When the user gives up
        if moveX == moveY and moveY == "END":
            handlePlayerLoss()
            return -1
        
        # Handles invalid moves, otherwise makes the move
        if checkMove(moveX, moveY, currentMap) == 0:
            handleInvalidCoordinates()
        elif checkMove(moveX, moveY, currentMap) == 2:
            handleNonTileSelected()
        else:
            makeMove(moveX-1, moveY-1, currentMap)
            numMoves += 1
        
        # Checks whether the board is solved
        if checkEndGame(currentMap):
            printBulbForwardLoad()
            handlePlayerWin()
            return numMoves

def main():
    # This ties up all the functions and displays
    # a fully functioning game

    # For the user to stay in the game
    while True:
        # Animation to get user's attention
        printOpeningScreen()

        # Allows the user to sign up or log in based on their interests
        # Continuous prompting is done until user finishes the task
        currentInstruction = printSignOrLog()
        if currentInstruction == 1:
            user = signUp()
            userName = user[1]
            while not user[0]:
                user = signUp()
                userName = user[1]
        elif currentInstruction == 2:
            user = logIn()
            userName = user[1]
            while not user[0]:
                user = logIn()
                userName = user[1]
        else:
            # Provides some closing animation to keep user satisfied
            sayThanks()
            endAnimation()
            break
        
        # Once logged in or signed up, this animation will add
        # a game-like experience
        printBulbForwardLoad()

        # User kept in the lobby unless he/she wants to exit
        while True:
            # Prints a nice interface asking the user for relevant commands
            userInstruction = printPlayScreen()

            if userInstruction == 1:
                # User wants to play
                
                # Details are extracted from the relevant file
                # to provide context about user progress with different levels
                userDetails = extractUserDetails(userName)

                currentMapName = getMapName(userDetails, userName) # Relevant map (level) name is obtained from the user
                currentMap = readMap(f'maps/default_maps/map{currentMapName}.map') # Reads corresponding map
                
                # The user plays the game and the number of moves needed to win is obtained
                numMoves = playGame(currentMapName, currentMap)

                # If the user was successful in completing the level, the number of moves
                # is checked in the context of whether it is a new best score
                # If it is, then the file is updated
                if numMoves != -1:
                    if userDetails[str(currentMapName)] == "":
                        updateUserDetails(userName, currentMapName, numMoves)
                    elif int(userDetails[str(currentMapName)]) > numMoves:
                        handleHighScore() # Prints a nice interface congratulating the user
                        updateUserDetails(userName, currentMapName, numMoves)
                
                # Another animation bringing a 'game-like' experience
                returningToLobby()

            elif userInstruction == 5:
                # User wants to leave the game
                # Some animation and some thanks are added to keep user satisfied
                sayThanks()
                endAnimation()
                break

            elif userInstruction == 4:
                # User wants to see the instructions
                # The instructions are displayed and user prompted to press enter
                # to return to the lobby
                showGameInstructions()
                returningToLobby()

            elif userInstruction == 3:
                # User wants to make their own game
                
                # First instructions are shown to the user
                showMakeInstructions()

                # Allow the user to make their game
                customGameMake(userName)

                # Annimation added to satisfy user
                returningToLobby()
            else:
                # Allow user to play a custom game
                playCustomGame()
                
                # Another animation bringing a 'game-like' experience
                returningToLobby()
    
        break

main()

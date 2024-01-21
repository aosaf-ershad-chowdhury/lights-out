# This file contains all functions which display
# a prticular message to the user
# Since the functions mostly play a role in displaying
# something, they are segregated from the rest of the files

# os is used for clearing terminal
# time is used for the timings and animation effect


import os
import time


def handleInvalidInitialInstruction():
    # Provides a message when user inputs something invalid

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                               Invalid Input! Please try again!              ")
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleUsernameTaken():
    # Provides a message when user inputs a username already taken during sign up process

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                        Username is already taken! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleWrongPassword():
    # Provides a message when user inputs the wrong password when logging in

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                      ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                      Wrong Password! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                      ---------------------------------------------------------------")

    time.sleep(1.5) # Sleep added to give user time to read


def handleUserNotFound():
    # Provides a message when user tries to log in with a username which doesnt exist

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                      ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                    Username Not Found! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                      ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handlePlayerLoss():
    # Provides a message when user is unable to solve a board
    # This ASCII art was partially made through
    # https://www.asciiart.eu/image-to-ascii

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                       ---------------------------------------------------------------")
    print("                                                                              ")
    print("""
                            __   __            _              _   _      __
                            \ \ / /__  _   _  | |    ___  ___| |_| |  _ / /
                             \ V / _ \| | | | | |   / _ \/ __| __| | (_) | 
                              | | (_) | |_| | | |__| (_) \__ \ |_|_|  _| | 
                              |_|\___/ \__,_| |_____\___/|___/\__(_) (_) | 
                                                                       \__\
    """)
    print("                                                                              ")
    print("                       ---------------------------------------------------------------")

    time.sleep(1.5) # Sleep added to give user time to read


def handleInvalidCoordinates():
    # Provides a message when user inputs invalid coordinates in the game board

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                             Invalid Coordinates! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")

    time.sleep(1.5) # Sleep added to give user time to read


def handleNonTileSelected():
    # Provides a message when user tries to select a non-tile element

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                             You cannot select a non-tile element!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handlePlayerWin():
    # Provides a message when user completes a level
    # This ASCII art was partially made through
    # https://www.asciiart.eu/image-to-ascii

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                           ---------------------------------------------------------------")
    print("                                                                              ")
    print("""
                                  __   _____  _   _  __        _____ _   _ _      ___  
                                  \ \ / / _ \| | | | \ \      / /_ _| \ | | |  _ / _ \ 
                                   \ V / | | | | | |  \ \ /\ / / | ||  \| | | (_) | | |
                                    | || |_| | |_| |   \ V  V /  | || |\  |_|  _| |_| |
                                    |_| \___/ \___/     \_/\_/  |___|_| \_(_) (_)\___/ 
    """)
    print("                                                                              ")
    print("                           ---------------------------------------------------------------")

    time.sleep(1.5) # Sleep added to give user time to read


def handleHighScore():
    # Provides a message when user finishes a level with the best number of moves
    # This ASCII art was partially made through
    # https://www.asciiart.eu/image-to-ascii

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("""
                              __        _______        ___ 
                              \ \      / / _ \ \      / / |
                               \ \ /\ / / | | \ \ /\ / /| |
                                \ V  V /| |_| |\ V  V / |_|
                                 \_/\_/  \___/  \_/\_/  (_)

    """)
    print("                                                                              ")
    print("               ---------------------------------------------------------------")
    print("                                                                              ")
    print("                        YOU JUST MADE A HIGH SCORE WITH THE CURRENT LEVEL!")

    time.sleep(3) # Sleep added to give user time to read


def sayThanks():
    # Provides a message when user is exiting the game
    # This ASCII art was partially made through
    # https://www.asciiart.eu/image-to-ascii

    os.system('cls' if os.name == 'nt' else 'clear')
    print("                                                                              ")

    print("                                                                              ")
    print("                                     ---------------------------------------------------------------")
    print("                                                                              ")
    print("""

                                          _____ _   _    _    _   _ _  __ __   _____  _   _ _ 
                                         |_   _| | | |  / \  | \ | | |/ / \ \ / / _ \| | | | |
                                           | | | |_| | / _ \ |  \| | ' /   \ V / | | | | | | |
                                           | | |  _  |/ ___ \| |\  | . \    | || |_| | |_| |_|
                                           |_| |_| |_/_/   \_\_| \_|_|\_\   |_| \___/ \___/(_)


    """)
    print("                                                                              ")
    print("                                     ---------------------------------------------------------------")

    time.sleep(1.5) # Sleep added to give user time to read


def showGameInstructions():
    # Provides relevant information when user wants to view the instructions of playing the game
    # Instead of a pre-defined time, the screen is kept until the user presses ENTER

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                INSTRUCTIONS                 ")
    print("                                                                              ")
    print("                                ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                      1. The board contains a number of tiles representing lights")
    print("                                      2. In the board, '1' implies that the light is switched on")
    print("                                      3. In the board, '0' implies that the light is switched off")
    print("                          4. In the board, 'X' implies that it is a non-tile element and hence cannot be flipped")
    print("                           5. In order to win the game, you need to turn off all the lights on the game board")
    print("                                    6. To turn on/off a light, enter the coordinates of that light")
    print("                             7. The coordinates should be entered in the format: x-coordinate y-coordinate")
    print("                               8. Action on a light will flip its current state (turning on/off the light)")
    print("                   9. By turning on/off a light, 4 other lights around it (up, down, right and left) would also be flipped")
    print("                                     10. Keep flipping lights until all the lights are turned off")
    print("                                                                              ")
    print("                                ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                 Press ENTER to go back to lobby")

    input()


def showMakeInstructions():
    # Provides relevant instructions to the user when the user wants to produce their own game
    # Instead of a pre-defined time, the screen is kept until the user presses ENTER

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                ###############################################################")
    print("                                                 Instructions for making your game")
    print("                                                                              ")
    print("                                ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                1. The board will contain a number of tiles representing lights")
    print("                                 2. In the board, '0' = Lights-off, '1' = Light-on, 'X' = Wall")
    print("                        3. If you input any character other than '0', '1', and 'X', your map will be invalid")
    print("                  4. Although not necessary, it is recommended to surround the entire board by 'X' for a better look!")
    print("                                        5. There should be at least one light turned on")
    print("                           6. Due to aesthetic reasons, your board should have a maximum size of 9x9")
    print("                                        7. Your board should have a minimum size of 1x1")
    print("                        8. You will enter the map one line at a time; after finishing the line, press ENTER")
    print("                          9. If you have finished making the map, press enter in the line after the last")
    print("                10. You do not have to make rectangular map, but the number of elemnts in each line should be consistent")
    print("                                                                              ") 
    print('                                                          For example: ')
    print()
    print("""
                                     Valid          Invalid         Invalid         Invalid
                                    XXXXXXX         XXXXXXX         XyXXXXX        XXXXXXXXXX
                                    01110XX         000000X         01110XX        010101011X
    """)
    print()
    print("                                ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                 Press ENTER to start inputting your game")

    input()


def handleInvalidMakeChars():
    # Provides a message when user tries make a game with invalid characters

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                           You entered invalid characters! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleLessMakeChars():
    # Provides a message when user tries make a game with too less characters

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                           You entered too few characters! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleExcessMakeChars():
    # Provides a message when user tries make a game with too many characters

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                           You entered too many characters! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleSolvedBoard():
    # Provides a message when user tries make a game which is already solved

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                           Your game is already solved! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleInconsistentMakeChars():
    # Provides a message when user tries make a game which has inconsistent
    # number of characters per row

    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                            Your game contains inconsistent number of characters per row! Please try again!          ")
    print("                                                                              ")
    print("                                                                              ")
    print("                                   ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read


def handleSuccessfulGameMake():
    # Provides a message when user makes a new game successfully

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("                                                                              ")
    print("                                                                              ")
    print("                            ---------------------------------------------------------------")
    print("                                                                              ")
    print("                                                                              ")
    print("                                            Game creation successful!              ")
    print("                                                                              ")
    print("                                                                              ")
    print("                            ---------------------------------------------------------------")
    
    time.sleep(1.5) # Sleep added to give user time to read

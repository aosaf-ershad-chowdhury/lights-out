# Lights Out

Lights out is puzzle game in which the objective is to, in essence, turn off all the lights in a given board. In this 
implementation of the game, this would mean turning all values in the map/board to a 0 (except the borders(represented
by an X)).


## Getting Started (How to run the game)

First remember to maximize the size of the terminal. Our game is tailor made for the terminal in its maximum size. There
-fore, to see all the animations properly, you should set the terminal in its maximum size.

In the terminal, type `python main.py`. The game will now run.

After the intro animations, you will be given the option to sign up(by typing '1'), log in(by typing '2'), or exit(by 
typing '3'). After typing the number indicating your choice, press ENTER.

If this is your first time playing, you must create an account to play the game as you cannot play without an account.
Keep in mind that when signing up, the username can only be ONE word and make sure the username isn't already taken.
Remember that your username will be displayed whenever you make a new game so keep it creative! 

If you are already a current user, you can directly log into the game by entering your username and password. If
successful, you will be entered into the game lobby after being shown an animation.


## Usage (How to play the game)

After logging in, you will be shown a menu (game lobby) with 5 options. Type '1' to play the original levels(created by
us!), '2' to play custom levels(created by your friends and peers), '3' to make your own game, '4' to check the
instruction on how to play the game and '5' to exit.

The original levels are levels that have been created by the developers(i.e. us :D) and are ordered in terms of
difficulty(with level 1 being the easiest and level 20 being the hardest).

Custom maps are maps that are made by users, you can also create your own maps by pressing '3' in the lobby and hitting
enter. Other than creating normal rectangular boards, you can also make the boards in your desired custom shape by
entering an appropriate number of 'X's. Let the creativity go forth!

For creating maps please note the following points.

                            1. The board will contain a number of tiles representing lights
                            2. In the board, '0' = Lights-off, '1' = Lights-on, 'X' = Wall
                  3. If you input any character other than '0', '1', and 'X', your map will be invalid  
          4. Although not necessary, it is recommended to surround the entire board by 'X' for a better look!
                                    5. There should be at least one light turned on
                      6. Due to aesthetic reasons, your board should have a maximum size of 9x9
                                    7. Your board should have a minimum size of 1x1
                  8. You will enter the map one line at a time; after finishing the line, press ENTER
                      9. If you have finished making the map, press enter in the line after the last
        10. You do not have to make rectangular map, but the number of elemnts in each line should be consistent
                                                                              
                                                          For example: 


                                     Valid          Invalid         Invalid         Invalid
                                    XXXXXXX         XXXXXXX         XyXXXXX        XXXXXXXXXX
                                    01110XX         000000X         01110XX        010101011X


Here are the rules to play the game itself:

                                  1. The board contains a number of tiles representing lights
                                  2. In the board, '1' implies that the light is switched on
                                  3. In the board, '0' implies that the light is switched off
                      4. In the board, 'X' implies that it is a non-tile element and hence cannot be flipped
                        5. In order to win the game, you need to turn off all the lights on the game board
                                6. To turn on/off a light, enter the coordinates of that light
                          7. The coordinates should be entered in the format: x-coordinate y-coordinate
                            8. Action on a light will flip its current state (turning on/off the light)
                9. By turning on/off a light, 4 other lights around it (up, down, right and left) would also be flipped
                                  10. Keep flipping lights until all the lights are turned off


## Acknowledgements

Thank you to all the members of the group for their invaluable contribution to this challenging, yet entertaining 
project.

Thank you to all the TAs, STAs and professors for their unwavering support and guidance during the development of our 
project.

Thank you to the original owners to the online resources we have used in this projects (where important online sources
have been directly used, we have acknowledged them in the relevant section of the code)

And lastly, thank you to you, the user, for playing this. We hope you enjoy playing this just as much as we enjoyed
creating it.












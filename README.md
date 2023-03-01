# Game1

Program Versions:
* Windows 11 - I normally execute in the IDLE shell for Python
* Python v. 3.11.1
* Pygame 2.1.3.dev8

Motication: I knew I wanted to build a game where you collect some sort of objects for points. And I think dinosaurs are cute and thought it would be funny to have a game where you have to feed them people. 

Reasoning: I originally wanted to structure it so that each of my components was separate that way it was reusable. I managed to do this with the exception of the Win/Lose screen functions and my game loop. Because of the way I set up my "Play", "Play Again", and "Exit" buttons I could not separate the functions for the win/lose screens from the game loop without getting an error from a cyclical import. 

(Image)

Future Work: 

Game Components:
* Game Loop:
* * Updates position of character
* * Updates score
*  

Model:
* Character: position, collison


View:
* Gameboard
* Score
* Timer
* Win/lose alert

Controller:
* Movement of character (arrows)

Entities:
* Main character (circle to move around and collect points)
* Point blocks 

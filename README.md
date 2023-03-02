# Game1

Program Versions:
* Windows 11 - I normally execute in the IDLE shell for Python
* Python v. 3.11.1
* Pygame 2.1.3.dev8

Motivation: I knew I wanted to build a game where you collect some sort of objects for points. And I think dinosaurs are cute and thought it would be funny to have a game where you have to feed them people. 

Reasoning: For view, I have the main screen that is in the game loop. I also have the introScreen, winScreen, and loseScreen functions. For controller, in the dino class, it takes in the keypad presses to then move the dinosaur. In the buttons function, it takes in the mouse presses and if the press is over the space where the button is located it response appropriately. For model, I have the food group, the dinosaur group, score, these are all in the game loop; and in this it is also checking to see if there is a collision between the dinosaur group and the food group in order to update the screen and remove food as appropriate; with the score keeping track of how many food has been eaten. Each of my model pieces are loose in the game loop, I originally wrote this as all one file and had to seperate it out in doing that I ran out of time - ideally I would construct a class to contain them. I also would have ideally been able to seperate my win screen and lose screen out from my file with my game loop but when I tried to give each their own file I kept getting an error because it was a cyclical import  due to how I linked the buttons to the assigned functions - either the game loop or to exit. I couldn't figure out how to fix this error without redoing that entire function so I left it alone for now. 

![diagram](https://user-images.githubusercontent.com/33873660/222286894-775c04a6-2b85-4a40-b7ab-845eb68c7e16.jpg)


Future Work: 
* For this game specifically I would like to add an element where you can do something with the food. So either you have an extra element of hiding the food and the dinosaur has to find and uncover it somehow or by providing some sort of enemy, maybe that the food runs away or fights back. 
* This game could be generalized to any sort of collection game - you could replace the dinosaur and people/food with anything, maybe have people collecting coins. I also have the player (dinosaur), items (food/people), as well as the button, and text_objects separated out into files so each of these could be applied to other games that might use them. 

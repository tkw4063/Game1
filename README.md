# Game1

Program Versions:
* Windows 11 - I normally execute in the IDLE shell for Python
* Python v. 3.11.1
* Pygame 2.1.3.dev8

Motivation: I knew I wanted to build a game where you collect some sort of objects for points. And I think dinosaurs are cute and thought it would be funny to have a game where you have to feed them people. 

Reasoning: For view, I have the main screen that is in the game loop. I also have the introScreen, winScreen, and loseScreen functions. For controller, in the dino class, it takes in the keypad presses to then move the dinosaur. In the buttons function, it takes in the mouse presses and if the press is over the space where the button is located it response appropriately. For model, I have the food group, the dinosaur group, score, these are all in the game loop; and in this it is also checking to see if there is a collision between the dinosaur group and the food group in order to update the screen and remove food as appropriate; with the score keeping track of how many food has been eaten. Each of my model pieces are loose in the game loop, I originally wrote this as all one file and had to seperate it out in doing that I ran out of time - ideally I wcould construct a class to contain them. I also would have ideally been able to seperate my win screen and lose screen out from my file with my game loop but when I tried to give each their own file I kept getting an error because it was a cyclical import  due oto how I liked the buttons to the ap

![diagram](https://user-images.githubusercontent.com/33873660/222286894-775c04a6-2b85-4a40-b7ab-845eb68c7e16.jpg)


Future Work: 


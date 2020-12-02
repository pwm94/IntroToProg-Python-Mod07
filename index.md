# IntroToProg-Python-Mod07
```
Homework Mod 7 repository
Paul Mitchell
December 1, 2020
IT FDN 110 A - Intro to Python Programming 
Assignment 7
https://github.com/pwm94/IntroToProg-Python-Mod07
```

## Assignment 7 - Using Exceptions & Pickles

### Introduction & Problem Statement
The task set forth in this assignment was to create a script that utilized both exceptions and pickles and finding a way to integrate both into the same script. For this assignment, I decided to continue the trend of using a menu of numerical options, using the exception function to ensure proper input, and using pickling and unpickling to save and store data in an external file. 

### Creating the Menu
First I decided to model my menu off of a Dog Adoption Database. To do so, I created the menu with the following options: (1) Adding Dogs to the List; (2) Displaying the Current Dogs; (3) Unpickle & Reload List of Dogs from File; (4) Pickle and Save to File; (5) Exit Program. See Figure 1 for Menu display. User input was collected as a string input and saved as Variable UserInput.

![Figure 1](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%201.png "Figure 1")
### Figure 1

### Exceptions
I decided to utilize the exception function to ensure the user only input 1 through 5 as options in the menu. I accomplished this by converting the UserInput string to integer variable y. I declared variable x to be 5.0 and set variable z to be x - abs(y). This would ensure any number greater than 5 would return a negative value. Combined with a squareroot function of z, this would test for an exception. Similarly I set a testforzero variable to equal 1 / y in case the user input 0. I realize this would allow a -1 through -5 input, but decided that those would still be allowed to correlate to their positive inverses. See Figure 2. For the Exception messages, I used ValueError and ZeroDivisionError. See Figure 3. 

![Figure 2](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%202.png "Figure 2")
### Figure 2

![Figure 3](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%203.png "Figure 3")
### Figure 3


### Pickling and Menu Execution
If the user correctly input 1 thorugh 5 (or negative 1 through 5) as their menu choice, no exception would occur, and the While(True) loop would run. It contained if and elif statements for each menu item. Menu Items (1), (2), and (5) are the same as previous assignments, so I will not go into detailed descriptions. However, for Menu Items (3) and (4), new pickling script was added to save the data as a pickle instead of a list or dictionary, as we did previously. See Figure 4.

![Figure 4](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%204.png "Figure 4")
### Figure 4

### Final Code
Final code is attached and a demonstration of it working in an IDLE shell is below (Figures 5 and 6). Figure 7 shows the picked data saved externally. 

![Figure 5](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%205.png "Figure 5")
### Figure 5

![Figure 6](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%206.png "Figure 6")
### Figure 6

![Figure 7](https://github.com/pwm94/IntroToProg-Python-Mod07/blob/docs/Fig%207.png "Figure 7")
### Figure 7


Resources
The resources I used to complete this assignment are as follows:
- https://docs.python.org/3/library/exceptions.html#ValueError
 - I liked this resource because it was quickly searchable and had great description of many different types of exceptions 
- https://medium.com/dev-genius/python-error-handling-8bed3f5b5769
 - I liked this resource because of the way it demonstrated multiple exception stacking
- https://www.journaldev.com/33500/python-valueerror-exception-handling-examples
 - I liked this resource because it used clear examples
- https://www.youtube.com/watch?v=2Tw39kZIbhs 
 - I liked this resource because it gave a step by step guide on how to use the pickle and unpickle functions
- https://medium.com/swlh/pickling-in-python-ac3c7a045ae5
 - I liked this resource because it clearly outlined what pickles are (seems similar to blockchain) and make them easily understandable

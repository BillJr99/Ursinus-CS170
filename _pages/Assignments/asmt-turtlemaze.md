---
layout: assignment
permalink: /Assignments/TurtleMaze
title: "CS170: Programming for the World Around Us - Turtle Maze"


info:
  coursenum: CS170
  points: 100
  goals:
    - To issue instructions using the Python language to move an object on screen to the goal
  rubric:
    - weight: 90
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
    
tags:
  - python
  
---

In this icebreaker assignment, you will use the Python [turtle](https://docs.python.org/3/library/turtle.html) software package to control an object on the screen.  This object is called a "sprite," which is a 2D graphic that you can move around on a screen as in a video game.  In this case, the sprite is a picture of a turtle, and you will write instructions in Python to navigate that turtle through a maze.

The turtle has a number of operations that it can perform, and we will use a few of them in this assignment:

* `turtle.forward(100)` - move the turtle forward by a certain number of dots (called "pixels") on the screen.  In this case, it will move 100 pixels straight ahead in the direction the turtle is facing.
* `turtle.right(90)` - turn the turtle to the right by a certain number of degrees.  In this case, the turtle will rotate 90 degrees and face right from where it was facing before.
* `turtle.left(90)` - the opposite of `turtle.right`

For example, to turn my turtle in a square with right-hand turns, I would write the following code:

```python
# Let's walk in a square!
turtle.forward(100) # move to the right on the screen
turtle.right(90)    # turn to face downard
turtle.forward(100) # move forward down the screen
turtle.right(90)    # turn right to face left
turtle.forward(100) # move forward on the screen (to the left)
turtle.right(90)    # turn right to face up
turtle.forward(100) # move forward up the screen, to the original spot
```

Notice the `#` character on each line: this is called a **comment**, and we can annotate our code to tell the reader what's going on.  This won't be seen as code by the computer, so we can write anything we want on a line following the `#` character.

## What to Do

### Create a New Project
First, create a new project.  Create a new Python text file, and name it `turtlemaze.py`.  **Do NOT name it `turtle.py` since we are using a library called turtle!**

### Download the Maze Image
On the [https://www.pythonclassroom.com/turtle-graphics/turtle-maze](https://www.pythonclassroom.com/turtle-graphics/turtle-maze) website, download the **Problem 1** maze and save it into your new project folder.  The maze can be downloaded from [here](../images/asmt-turtlemaze/maze1.png).  

### Planning Your Solution
**Write down and describe the steps you think your turtle would need to make to move from the arrow at the top of the maze to the arrow at the bottom of the maze, without going through any walls.** You can use the `forward`, `right`, and `left` steps to do this.  Don't worry if you don't get it right - we'll write a program to try out our steps and revise them later!  Compare your steps with a partner, and discuss until you agree.

### Implement the Solution in Code!
Individually, write the code representing each step as a Python program.  The template code to load the maze is given on the [https://www.pythonclassroom.com/turtle-graphics/turtle-maze](https://www.pythonclassroom.com/turtle-graphics/turtle-maze) website.  This code loads the maze image onto the screen and puts the turtle in the right place for you to start moving around.  You will paste this code into your program, and add your steps in under the line that says `# write your code below`.  For reference, here is a copy of that code:

```python
# From https://www.pythonclassroom.com/turtle-graphics/turtle-maze
import turtle
turtle.showturtle()
turtle.shape("turtle")
# load the appropriate image
turtle.bgpic('maze1.png')
turtle.penup()
# bring the turtle to the starting point
turtle.goto(-70, 210)
turtle.pendown()
turtle.pencolor("red")
# write your code below



# press enter in the Terminal to exit the program
input()
```  

### Testing Your Program
Run your program.  Did it work?  Compare your result with your partner, and decide on any changes you need to make as a pair.  Then, implement those changes together on one of your projects until you get it right.  Once you do, go ahead and make the revisions on the other partner's program.

### Complete the Remaining Mazes
Create a new Python file in the same project, and repeat the process with the mazes in problems 2, 3, and 4.  Save the maze image as `maze2.png`, `maze3.png`, and `maze4.png`, and update your code to open this file instead of `maze1.png`.  Here are links to [maze2](../images/asmt-turtlemaze/maze2.png), [maze3](../images/asmt-turtlemaze/maze3.png), and [maze4](../images/asmt-turtlemaze/maze4.png).  **If your turtle is not at the beginning of the maze when you first run the program, you can update the line that says `turtle.goto(-70, 210)` to move it to the proper place!**

### Extra Credit (10%): Generating Your Own Maze

In a paint program on your computer, generate your own maze.  Exchange it with a partner, and try to solve it in a separate Python file.  Submit your maze and the solution!

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## References

1. [https://www.pythonclassroom.com/turtle-graphics/turtle-maze](https://www.pythonclassroom.com/turtle-graphics/turtle-maze)

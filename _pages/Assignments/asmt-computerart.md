---
layout: assignment
permalink: /Assignments/ComputerArt
title: "CS170: Programming for the World Around Us - Computer Art Generator"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use iteration to generate pixel colors
    - To use a random number generator to draw random pixels
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, descriptive comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, descriptive comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions    
      
tags:
  - python
  - graphics
  
---

Computer graphics are drawn by creating pixels of various colors and displaying them on a screen.  A pixel (short for "picture element") is the smallest unit of drawing size on the screen - one of the many "dots" that make up the screen.  You can use one of several libraries in Python to draw on the screen, and here is an example that uses one of them:

```python
import ezgraphics 

width = 640
height = 480

win = ezgraphics.GraphicsWindow(width, height)
win.setTitle("My First Drawing")

canvas = win.canvas()

canvas.setFill(255, 0, 0) # red, green, blue; each from 0-255
canvas.drawRectangle(40, 40, 100, 200) # top, left, width, height

canvas.setFill(255, 255, 255)
canvas.setOutline(0, 255, 0)
canvas.drawRectangle(200, 200, 150, 50) # top, left, width, height

win.wait()
``` 

### Installing the EZGraphics Library
You can install the EzGraphics library in your shell by typing this command:

```
python3 -m pip install http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz
```

On Mac, you can run these commands if the above command does not work:

```
brew install python-tk
python3 -m venv .venv
source .venv/bin/activate
./.venv/bin/activate .venv
./.venv/bin/python -m pip install http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz
```

On Chromebook or other machines, the last command might look slightly different, like one of the following:

```
activate/Scripts/python -m pip install http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz
.venv/bin/python -m pip install http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz
```

## What to Do
Begin by defining a window width and height.  a 4:3 ratio is common, so a width of 640 and a height of 480, or a width of 800 and a height of 600, are typical window sizes.  You can choose anything you like!

Create a window of that size, and write a loop that iterates from 0 to the width, and from 0 to the height.  This allows us to draw each pixel on the window, one by one.

Each pixel is defined by its color.  In the RGB color standard, colors are defined by a mixture of red, green, and blue (R, G, and B) light, each with a level of 0 through 255. ***How many possibly color combinations are there?***  Use a random number generator to pick three numbers between 0 and 255 (an example on how to do this is given below), and use those to create a colored pixel on the screen.  You can use a rectangle whose width and height are 1 to do this.

```python
import random

x = random.randint(1, 10)
```

### Computer Art

Now, explore the [EzGraphics library](http://www.ezgraphics.org/UserGuide/UserGuide).  It provides other operations besides `drawRectangle` that you can use.  Try drawing lines and other shapes.  You can create functions to create complex images (for example, a house, or a person).  Consider [complementary colors](https://en.wikipedia.org/wiki/Complementary_colors) to help inform your choices, and draw some shapes on the screen.  You can use randomness to do this.  See if you can guess the RGB values for your favorite colors, or use [this tool](https://www.rapidtables.com/web/color/RGB_Color.html) to look some up.

#### Extra Credit (10%): Animations

You can even use the `win.pause(1000)` function to insert a delay in between drawing your shapes, and create an animation effect.  Unlike `time.sleep()`, which uses seconds, `win.pause()` uses milliseconds, so 1000 equals one second here.  That's because when animating, your pauses are very short, in the millisecond scale.

This [Starfield Simulation](https://www.youtube.com/watch?v=hIFu3Lzsvvk) can work by drawing a black rectangle on the whole window, then drawing white pixels on the screen, pausing, replacing those with black rectangles again, and drawing white rectangles a few pixels away, all using a loop.  **How do you think the [Mystify](https://www.youtube.com/watch?v=yE3BTTtPKB4) screen saver worked?**

You get to be totally creative here - use a loop to come up with the most interesting computer generated artwork or animation that you can!  

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

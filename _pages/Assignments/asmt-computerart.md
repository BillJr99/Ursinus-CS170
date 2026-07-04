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
      preemerging: "The program does not run (for example, ezgraphics is not installed or imported, or the window is never created), or no pixels are drawn to the screen"
      beginning: "The program runs but the random-pixel drawing has a logic slip, such as loops that do not cover the full window width and height, random color values outside the 0-255 range, or rectangles larger than one pixel that overwrite neighboring pixels"
      progressing: "The nested loops fill the window with randomly colored one-pixel rectangles, but the original artwork portion is minimal (for example, a single shape) or is drawn with one long copy-pasted sequence of drawing calls that a loop or function could replace"
      proficient: "The program fills a window of a chosen size with randomly colored pixels using nested loops over the width and height and three random RGB values from 0 to 255 per pixel, and the artwork portion uses loops and/or functions to compose an original drawing of multiple shapes that would still work if the window dimensions were changed"
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: "Indentation and spacing are inconsistent enough to make the program hard to follow, or indentation errors in the nested pixel loops prevent the program from running"
      beginning: "Indentation and spacing are mostly consistent, with a few isolated issues such as the inner loop body not indented one level beyond the outer loop"
      progressing: "Indentation and spacing are consistent, with only a minor adjustment needed (for example, uneven blank lines between the pixel loop and the artwork section)"
      proficient: "Indentation and spacing are consistent throughout: the inner loop body is indented one level beyond the outer loop, function arguments are uniformly spaced, and blank lines separate the window setup, the pixel loop, and the artwork sections"
    - weight: 10
      description: Code Quality
      preemerging: "The code has not been run through pylint, and there are widespread style issues such as single-letter variable names or large copy-pasted blocks of drawing calls"
      beginning: "pylint reports several warnings that were not addressed (for example, unused imports or variables), or repeated drawing code appears where a loop or function would do"
      progressing: "The code runs nearly clean through pylint with only one or two unaddressed warnings; window dimensions are stored in variables rather than repeated as magic numbers, with a few isolated style issues remaining"
      proficient: "The code follows the course style guide and runs cleanly through pylint (no warnings other than those the instructor has designated as acceptable): descriptive snake_case names, window dimensions kept in variables like width and height instead of repeated magic numbers, no unused variables, and no duplicated drawing blocks that a loop or function could replace"
    - weight: 10
      description: Code Documentation
      preemerging: "The code contains no comments, or comments are so sparse that a reader cannot follow how the drawing is produced"
      beginning: "Some sections are commented, but key steps such as the nested pixel loops or the random color choice are unexplained"
      progressing: "Comments are present at each major step, but they mostly restate the code (for example, 'draw a rectangle') rather than explaining why or what the section contributes to the artwork"
      proficient: "Every function (for example, shape-drawing helpers for a house or a person) has a comment or docstring stating its purpose, inputs, and output; non-obvious steps such as why the loops run over the width and height and how the three random values form an RGB color are explained; comments explain why, not just what"
    - weight: 10
      description: Writeup and Submission
      preemerging: "No README.md is committed to the repository, or the repository is missing the Python files needed to run the program"
      beginning: "A README.md is committed, but it does not answer the bolded questions (how many possible RGB color combinations there are, and how the Mystify screen saver worked), or the final version of the code was not pushed to GitHub before the deadline"
      progressing: "The README.md answers the bolded questions and describes the artwork and how to run the program, with a minor omission such as not describing one of the helper functions"
      proficient: "The README.md answers both bolded questions, describes your artwork and how to run the program, explains the functions you wrote and how another student would use them, and the final version of all files is committed and pushed to GitHub"
      
tags:
  - python
  - graphics
  
---

## Purpose

Every image you see on a screen - every photo, video game, and movie effect - is built from tiny colored dots called pixels.  In this assignment, you will become a digital artist: you'll use loops and a random number generator to paint pixels and shapes on the screen, and discover how a few lines of code can produce artwork (and even animation) that would be impractical to draw by hand.  Along the way, you'll practice the core programming skill of iteration - doing something thousands of times with just a few lines of code.

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

### Getting Started with GitHub

Accept the assignment invitation using the GitHub Classroom link, and clone your repository to your computer to get started.  As you work, commit your changes early and often with meaningful messages, and push them before the deadline: your latest pushed commit is what is graded.  If this is new to you, the [Using Git and GitHub](../Modules/Github/Module) and [Cloning an Assignment with GitHub Classroom](../Modules/GithubClassroom/Module) modules walk you through it step-by-step.

Your Code Quality score is informed by pylint: see the [Code Quality and Linting module](../Modules/Pylint/Module) for how to run it and read its output.

### Drawing Random Pixels

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

When you're done, write a `README.md` file in your repository, save all your files, and commit and push everything (your Python files and your README) to GitHub.  There is no need to export your project to ZIP: your pushed repository is your submission, and your latest pushed commit before the deadline is what will be graded.  If a Canvas submission link is posted, you may also paste your repository's URL there as a secondary confirmation.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## Before You Submit: Self-Check

Before you submit, walk through this checklist - if you can check every box, you're in great shape!

- [ ] My program runs from top to bottom without errors when I run it fresh (after installing `ezgraphics`).
- [ ] My nested loops fill the entire window - every row and column from 0 to the width and height - with randomly colored pixels.
- [ ] Each pixel's color uses three random values between 0 and 255 for red, green, and blue.
- [ ] My artwork section draws an original composition using loops and/or functions rather than one long copy-pasted list of drawing calls.
- [ ] I ran my code through pylint and addressed the warnings (see the [Code Quality and Linting module](../Modules/Pylint/Module)).
- [ ] Every function I wrote has a comment or docstring explaining its purpose, inputs, and output.
- [ ] My `README.md` answers both bolded questions (the number of possible color combinations, and how Mystify worked) and describes my artwork.
- [ ] I committed AND pushed my work to GitHub, and I can see my final version on github.com in my browser.

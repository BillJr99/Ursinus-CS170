---
layout: assignment
permalink: /Labs/Debugging
title: "CS170: Programming for the World Around Us - Debugging"


info:
  coursenum: CS170
  points: 100
  goals:
    - To debug a Python program and to fix errors
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
    
tags:
  - debugging
  
---

## What to Do

### Part 1: Using the Debugger
Enter the following program into a new project:

```python
totalcredits = 0
gradepoints = 0

done = False
while not done:
    credits = input("Enter the number of credits (4 or 3, etc., or -1 when done):")
    credits = float(credits)
    grade = input("Enter the grade you received, where an A is worth 4, B+ is worth 3.67, B- is worth 3.33, B is worth 3, and so on, or -1 when done:")
    grade = float(grade)

    if credits > -1 and grade > -1:
        totalcredits += credits
        gradepoints += grade * credits

    # no more grades
    if credits == -1 or grade == -1:
        done = True

gpa = totalcredits / gradepoints

print("Your GPA is {0:.2f}".format(gpa))
```

This program contains an error.  Run it and enter some grades (for example, a 4 credit A and a 4 credit B should result in a GPA of 3.5).  Notice that this is not the answer!

In the code margin, click to the left of line 19 to set a breakpoint there.  On the left side, click `Run and Debug` or press Control-Shift-G to bring up the debugger.  Click `Run and Debug` to begin.  Enter your inputs and notice that the program pauses at your breakpont.  

On the left, you'll see a tab pane called `Watch`.  Right-click in this space and click `Add Expression`.  Type in the name of your variable `totalcredits` that you wish to observe, and you should see its current value.  Do the same for the `gradepoints` variable.  How would you use these two variables to compute your GPA of 3.5?  How does this differ from the code on line 19?  Go ahead and fix the program, and re-run it to verify that it works!

### Part 2: Stepping through a Program
Now, enter this program:

```python
temperature = input("Enter the temperature in degrees Farenheit:")
temperature = float(temperature)

if temperature >= 72:
    print("Turn on the heat!")

if temperature <= 72:
    print("Turn on the air conditioning!")
```

There are two bugs in this program.  Set the breakpoint at Line 4 and start the debugger to break there.  Add a watch for the `temperature` variable.  Enter a temperature like 75.  What should happen?

At the top you'll see a toolbar of 6 icon buttons.  The second one is labeled `step over` and is shaped like an arrow jumping over a dot.  Click on this to execute the next line of the program.  The temperature is above 72, so we enter the body of the `if` statement.  What happens next is incorrect!  Fix this bug in the program so that the output is correct.

Now, re-run the program and enter 72 as the temperature.  We don't need the heat or the air conditioner at this temperature, but use the step buttons to see that both print statements execute.  Fix this bug as well.

### Bug Hunt

On the class activities discussion board, post at least two bugs that you've found in your own code.  Let us know whether it was a syntax error (a typo that prevented your program from running) or a logic error (a program that ran but did something you didn't expect).  Let us know the error message you received, what the problem was, and how you fixed it.  Each student that is the first to discover and report a unique bug will receive 3 points of extra credit on this lab, and up to 15 extra points total!

## Trivia

The first computer "bug" is attributed to Grace Hopper, when an actual bug was found in the circuitry of a system, causing the program being executed to fail!  Here's a picture from their engineering journal.

<a title="Courtesy of the Naval Surface Warfare Center, Dahlgren, VA., 1988., Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:First_Computer_Bug,_1945.jpg"><img width="512" alt="First Computer Bug, 1945" src="https://upload.wikimedia.org/wikipedia/commons/f/ff/First_Computer_Bug%2C_1945.jpg"></a>

Did you know that the most copied StackOverflow code snippet (as of 2018) [contained a bug that was only fixed 9 years later](https://www.zdnet.com/article/the-most-copied-stackoverflow-java-code-snippet-contains-a-bug/)?

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?
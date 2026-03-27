---
layout: assignment
permalink: /Labs/MicrobitDice
title: "CS170: Programming for the World Around Us - Random Dice Throwing with the micro:bit"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use a random number generator with the micro:bit
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
  - microbit
  - rng
  
---

## What to Do
Write a program to generate a random number between 1 and 6 every time a button is pressed, and display that number on the screen.  You can do this by computing a random number using the formula we [developed in class](../Activities/MicrobitPRNG), but instead of displaying the calculated random number, create a new variable whose value is the remainder of the random number when divided by 6.  This will give you a number between 0 and 5, to which you can add 1 before displaying the value.

Be careful not to modify the original random number variable, so that we don't lose the pseudorandom number sequence!  You can create a new variable and mathematical expression, instead.  I also suggest choosing large values for your initial variable values: 4 digit values should be good.  This will help ensure that you get a relatively uniform sequence of random number values.  If you see the same pattern over and over, try varying these variable values somewhat!

### Extra Credit (10%): Display the dice image
Modify the program to display each dice image on the LED screen!

## What to Turn In
When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

---
layout: assignment
permalink: /Labs/HideAndSeekSound
title: "CS170: Programming for the World Around Us - Accessible Hide-and-Seek with Sound"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use an alternative modality to enhance program accessibility
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
  - accessibility
  
---

Building upon the [Hide and Seek Activity](../Activities/HideAndSeek), we will add an audible feedback loop to help determine if one is getting "hotter or colder" relative to the item being searched for.  Additionally, you will make a few improvements to the program we developed in class.

## What to Do

### Step 1: Sound Modality
Modify the Hide and Seek program to play a sound when the radio receives a value.  If the current RSSI has become stronger, play a higher pitched sound, and if it has become weaker, play a lower pitched sound.  You can control the pitch using a variable that you increase or decrease (by any amount you like!  You could add or multiply it for warmer, or subtract or divide it for cooler, as you prefer.), and play the sound as a tone in the loop.

I suggest creating a variable called `frequency`, and using the `Math`:`Map` feature to convert the current RSSI to a sound frequency.  You can map the RSSI value from a low of -70 to a high of -30, and map that to a frequency low of 200 and a high of 1000.

**What other modalities could you imagine incorporating into this for visually or hearing impaired users?**

### Step 2: Conserving Energy
Set your radio group to the same value as your partner's (and to something different from everyone else's!), and add a `Forever` loop that sends a radio signal (the value doesn't matter).  Add a pause block to cause a delay in the program so that you don't send signals so quickly that you drain the battery too quickly.  

**What delay time is appropriate and why?**

### Step 3: Building a Threshold for Detecting Changes in RSSI
Create a new variable to represent the change in RSSI between the prior signal strength and the current signal strength.  When you receive a message, set this new variable to the difference between the current RSSI level and the prior RSSI level, and display that difference value on the screen.  Use this to determine how much the RSSI fluctuates while the micro:bit devices are sitting still, and modify your `if` statement to only display an output or play a sound when the difference is greater than some threshold that you can choose (for example, 2 dB).  For example, if the RSSI fluctuates by 7 dB while the micro:bit devices are sitting still, a threshold of 7 or 8 dB might be appropriate.  Use the values you observe to decide on a reasonable threshold, and implement it in your program.

**Why do you think the RSSI fluctuates so much even when the micro:bit is stationary?**

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

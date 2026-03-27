---
layout: assignment
permalink: /Assignments/RespiratoryTracker
title: "CS170: Programming for the World Around Us - Respiratory Tracker"


info:
  coursenum: CS170
  points: 100
  goals:
    - To design computing solutions to math and scientific through numeric processing
    - To use lists to store and analyze data
    - To create parallel arrays to represent associated data
    - To iterate over lists of data
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
  - numeric
  - scientific
  - functions
  - iteration
  
---

Take a deep breath - inhale, and exhale!  It's nice when a homework assignment starts out that way.  Could you feel your shoulders rise and fall like a wave?  Indeed, our respiratory patterns are sinusoidal.  In, and out; up, and down; over and over again.  Count how many breaths you take in a minute.  How did you do it?  Chances are, you counted once for every inhale, or once for every exhale, over 60 seconds.  Your breathing might have sped up and slowed down during that time, but in general, you have an idea of how many "breaths per minute" you took.

In this assignment we'll write a computer program to track one's respiratory rate by analyzing a graph of their chest wall movement.  We will model this movement as a sine wave, such as the one below:

<p align="center">
<img src="../files/asmt-respiratorytracker/respiratorytracker.png" alt="Respiratory Model as a Sinusoidal Graph" style="max-width:100%;">
</p>

## What to Do
Download [this file](../files/asmt-respiratorytracker/respiratoryexample.csv) containing time and a sinusoidal model of chest wall rise.  Add it to your project.  This is a "comma separated file," meaning that each line contains the time and the value, in this format:

```
T,Y
0.1,-0.9
0.2,-0.8
0.3,-0.7
```

Each line contains the time (in seconds), followed by a comma, followed by the value at that time.  The first line is called the "header" line and it contains the titles (T for time and Y for the value).  We'll skip that line when we process, since it's not numeric data (it's just there as a convenience for the human, to remember what order the data is in!).

This particular file represents breathing at a rate of 20 breaths per minute (BPM) for 20 seconds, followed by a respiratory rate of 12 BPM for 20 seconds, followed by a respiratory rate of 15 BPM for 20 seconds.

### Reading the File
You could open this file and process it in pure Python:

```python
f = open("respiratoryexample.csv")
for line in f: # read each line
    data = line.split(",") # split the data up by the comma into its two parts
    time = data[0] # time is first
    y = data[1] # the sinusoidal value is second
```

However, there is a convenience library called `csv` for "comma separated values" that does some of the work for you.  Begin by importing the `csv` library, and you can do this instead:

```python
f = open('respiratorygenerator.csv')
csvfile = csv.reader(f)
for row in csvfile:
    time = row[0]
    y = row[1]
```

This doesn't look like much of a savings at first, but sometimes CSV files contain commas in the data, or have other formatting considerations, that the library takes care of automatically.  You may choose either approach.

#### Skipping the Header Row
Next, add a variable to track how many rows you have read.  Increment it each time through the loop.  Only extract the `time` and `y` values if this is not the header row.

#### Converting the Values to Numeric Variables
You can convert your `time` and `y` values to numeric variables using the `float` function, for example:

```python
time = float(time)
```

#### Reading the Data into a List
Create two `list` variables to hold the times and the y values; within your loop as you read the file row-by-row, append the time and the y value to your lists.

### Processing the File
Now, write a loop that iterates over these two arrays.  They should have the same length, so you can iterate from 0 to the length of either one of them.  This is called a set of "parallel arrays," because each array is the same size, and each item in the array corresponds to the item in the same position in the other array.

#### Finding the Next Peak
Your goal is to look for the next peak in the graph, and determine how much time has gone by between those peaks.  You really want to look from the peak to the next peak, or the trough to the next trough, which is like counting a breath after every inhale, or after every exhale.  You could also count the time between the peak and the trough (the inhale and the exhale), but you would count twice as many breaths.  That's ok, too, because you could simply multiply the time between these peaks by 2 to estimate the full peak-to-peak time (since inhale-to-exhale is one-half of a breath).  This is your choice, and any of these three approaches will work!  If you look for all peaks (top and bottom), just remember to multiply your index period delta by 2.

**Which of these approaches do you think would give the most accurate estimation of the BPM, and why?**

Write a function called `find_next_slope_change` that takes in the array of `y` values, and a starting index position.  Loop from that position to the end of the array, and calculate the difference between the y value and the next y value, and the next y value and the one after that.  If their signs differ, then the graph has changed direction, and you've found a peak.  Return that index!

**What are some ways that we might get an incorrect result by simply finding when the respiratory signal changes its sign?  Do humans always breathe in sinusoidal patterns?  What could we do to improve the quality of our data before we process with this approach? You don't have to implement your ideas here, just brainstorm your thoughts!**

Call this function from the main loop that iterates over your parallel arrays.  Every time you get a "slope change position," subtract it from the one you saw previously.  There are two ways to do this.  First, you can save the prior slope change position in a variable inside your loop, and subtract the current change position from the prior one, to get the period.  Alternatively, you can create a list of all of the slope change positions, and use the numpy `np.diff()` function, which takes a list of values, and returns the "derivative" or differences between each pair of values as a new list automatically.

#### Compute the Respiratory Rate
Once you have the current slope change position and the prior one, subtract them.  This delta is the distance in time between your breath peaks.  Our file samples at 0.1 seconds per entry (or 10 rows per second, or 10 Hz), so if your period is 20 rows, that's really 2 seconds.  To compute the respiratory rate, divide the sample rate by your period delta, which will give you breaths per second.  Multiply this by 60 and you have your estimate of BPM!

**At the boundaries when the respiratory rate changes, you might find that your estimate is not exactly right.  This is normal, but why do you think this is happening?**

#### Alerting
Respiratory monitors should alert if the respiratory rate goes too low or too high.  If the respiratory rate drops below 15 (an arbitrary non-medical limit, just for experimentation!), print a warning to the screen.

## Program Structure
Your final program might look something like this:

```python
import csv
import numpy as np

SAMPLE_RATE = 10 # each X is worth 0.1 seconds

# Given the array of sinusoidal values y, and a starting index, 
# calculate two successive changes in y (dy1, and dy2).
# Continue until the sign of dy1 is different from the sign of dy2
# (for example, one is negative and one is positive).
# Return the index where that occurs.
# Hint: the numpy function np.sign(x) returns -1, 0, or 1 if the sign
# of the value is negative, zero, or positive
def find_next_slope_change(y, idx):
    # TODO: Write this function
    pass
    
f = open('respiratorygenerator.csv')
csvfile = csv.reader(f)

# TODO: create lists for time and y
for row in csvfile:
# TODO: add all the numeric values in the csvfile 
# to those lists, one row at a time.
# Be careful not to add the header row, and 
# remember to convert the values to floats.
    
# TODO: loop over the time and y arrays
# and call the find_next_slope_change function
# to find the next change in slope.  Once this happens,
# you know how much time has gone by in-between breaths,
# or at least from inhale to exhale.  Multiply this delta by 2
# to get peak to peak breath time.  

# TODO: Each time you find a delta, compute
# the sample rate times 60 seconds, divided by 2*delta,
# to compute the respiratory rate in breaths per minute.
# Print this out

# TODO: If the respiratory rate drops below 15, print 
# an alert to the screen.
```

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?
---
layout: assignment
permalink: /Labs/RefeedingTimerSensor
title: "CS170: Programming for the World Around Us - Refeeding Timer Sensor"


info:
  coursenum: CS170
  points: 100
  goals:
    - To explore ubiquitous sensors and actuators via the Internet-of-Things
    - To design an algorithm for an agruicultural solution
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
  - iot
  - agriculture
  - radio
  
---

In this lab, you will build upon the [Social Vicinity Tracker](../Activities/SocialVicinity) activity by timing how long two sensors are in proximity to one another on the micro:bit, and sounding an alarm after a certain period of time.

Imagine a chicken feeder filled with food.  Your job is to ensure that this feeder is always filled with food.  But how can you know when it is nearly empty without taking it apart?  Suppose you had one micro:bit at the bottom of the feeder (encased in plastic to shield it from the food, of course!), and another at the top.  When their radios get closer together, you'd see the increase in signal strength, and know that the food supply was decreasing! 

<!-- CC 2.0 License https://creativecommons.org/licenses/by/2.0/ -->
<a data-flickr-embed="true" href="https://www.flickr.com/photos/11921146@N03/4436519654" title="homemade chicken feeder"><img src="https://live.staticflickr.com/4065/4436519654_ebbfa9767a_k.jpg" width="1365" height="2048" alt="homemade chicken feeder"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## What to Do
Using the micro:bit, modify the Social Vicinity program to check when the signal strength crosses a certain threshold for a certain period of time, and then sound an audible alarm.

**How do you decide what threshold to use for the signal strength and the time?  Suppose you want to sound the alarm when the two radios are two inches apart (or some other distance); what could you measure to get the threshold right?  What measurement do you obtain when you do so?**

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?
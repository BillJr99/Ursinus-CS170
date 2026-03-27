---
layout: assignment
permalink: /Labs/CardDeck
title: "CS170: Programming for the World Around Us - Deck of Cards"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use iteration to create a nested loop
    - To write conditionals using loop counter variables
    - To establish proper ranges for for loop counters
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
  - python
  - iteration
  - conditionals
  
---
In this lab, we will practice writing `for` loops using the `range` function to iterate over decks of cards, and then use a loop to simulate the effects of monthly credit card debt.

## What to Do

### Part 1: Card Deck

The `range` function takes two forms:

* `range(N)`: generates all values from `0` to `N-1`
* `range(start, end)`: generates all values from `start` to `end-1`

Write a `for` loop that loops 4 times over a variable called `i`.  Inside this loop, loop from all values between `1` and `14` (inclusive) over a variable called `j`.

Within the inner loop, check the value of `i`.  If it is `0`, set a `suit` variable to `Clubs`.  Do this for each of the remaining values, for `Hearts`, `Diamonds`, and `Spades`.

Then, check the value of `j`.  If it is 11, set a variable `card` to `Jack`.  Similarly, set `card` to `Queen` for `12`, `King` for `13`, and `Ace` for 14.  If the value is anything else, just set `card` to that value (the numeric card value).

Finally, print the value of the card.  When you run this program, you should see all 52 cards in the "deck."

### Part 2: Credit Card Debt Simulator

In a separate program, loop over each of 12 months.  Within each simulated month, ask the user how much money they paid off by the due date, and subtract this from their prior balance.  

Next, if their balance is greater than 0, charge an interest rate of 6% to their **original** balance (not the amount after making the payment!  Be careful not to subtract from the balance right away so that you maintain their current balance, or save the old balance in a separate variable).  

Then, ask them how much money they spent on their credit card.  Add this value to their running balance, and repeat.

After the loop has ended, print out the total amount they spent over the 12 months, and how much money they paid back in interest.  You'll need additional variables to keep track of these running totals in your loop!

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

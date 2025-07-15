---
layout: assignment
permalink: /Labs/StoryTelling
title: "CS170: Programming for the World Around Us - Interactive Story Telling"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use a dictionary data structure to tell a choose-your-own adventure style story
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
  - dictionary
  
---

## What to Do
In this lab, you will use `HashMap`s to tell a dynamic story.  

### The Story
Create a `dict` called `story` that define the different places you can go in your story. 

Each key in the `story` dictionary should be a place, like a room in your story.  The value should be another dictionary, for example:

```python
story = {}
story['start'] = {} # the starting room is also a dictionary! it will contain the story narrative and your reader's choices.  do this for all the places you can go
```

Within this dictionary, have a key called `story` whose value is a narration of your story upon entering that location:

```python
story['start']['narrative'] = "It was a dark and stormy night..."
``` 

Now, add another key to `story['start']` called `next` that is a list.  In this list, add the names of the rooms you can go to next.

### Telling the Story
Set the starting room to `start`.  Print `story[room]['narrative']` to the screen, as well as `story[room]['next']` so that the user knows where they can go next.  Input the next room until it is equal to one of the choices in `story[room]['next']`, and repeat until the story is done!  You can check if the choice the user entered is in the dictionary using this `if` statement: `if nextroom in story[room]['next']`, where `nextroom` is what the user inputs as part of the loop to ask for the next destination.

Here is an example dictionary value:

|    room   |        narrative           |            moves               |
|:---------:|:--------------------------:|:------------------------------:|
| start     | This is the starting room! | "classroom", "courtyard"       |
| classroom | I am in a classroom!       | "start", "courtyard", "end"    |
| courtyard | Welcome to the courtyard!  | "start", "classroom", "end"    |
| end       | The end!                   |                                |

**You should have at least 5 possible rooms, and at least 3 of those rooms should have a choice of at least 2 possible next locations.**

### Ending the Story

You can decide how to end the story.  One idea is to add another key to the `story` dictionary called `end` which is `True` if this ends the story and `False` otherwise.  Another way is to have `moves` be an empty list for ending rooms, and check if the length of the list is 0 to end the loop.  You get to decide!

**What happens if you call `story[room]` with a room that doesn't exist in your program?  How can you ensure that the user keeps entering a room until they enter a valid one?  Hint: you can check if a string is in a list by asking if `newroom in story[room]['moves'] - and loop while this is false!**

**In your README, include a graph (either a drawing or in text is fine!) that shows the progression of your rooms from one to the next.**

#### Multiple Endings

You'll want each room in your story to have a unique key (i.e., don't have two places called `forest` - call them `forest1` and `forest2` instead).  But, you might have multiple endings by having places called `end1`, `end2`, and `end3`.  You could have your `while` loop terminate when the room begins with the word `end`.  To do this, your while loop might look like this:

```python
while not room.startswith("end"):
```

### Getting Started Template
Here is a template to help you begin:

```python
story = {}
story['start'] = {}
story['start']['narrative'] = "It was a dark and stormy night..."
story['start']['next'] = ['forest', 'diner']

room = 'start'

print(story[room]['narrative'])
print("Where to next? {}".format(story[room]['next']))
```

Once you put this into a loop, you'll notice that your last room doesn't print out.  That's because the loop terminates when your room equals the ending room (without printing the story for that room in the loop!).  Copy your print statement to just below the loop so that it executes one last time on the last room of your story.

### Extra Credit (Up to 15%): Best Story Competition
Creativity is encouraged, but not required for a grade!  Let me know in your documentation if you'd like to demo your story to the class - I hope you do!  You will receive 7.5% extra credit for entering your submission, and the class will vote on their favorite story (the winner will receive an additional 7.5% extra credit).

### Extra Credit (10%): Conditional Rooms
Modify your program to have conditionals, in which your rooms print certain things depending on whether other conditions have been met.  For example, if you reach one room after visiting another, print something different in your story.

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

---
layout: assignment
permalink: /Assignments/Semitone
title: "CS170: Programming for the World Around Us - Semitone Note Generator"


info:
  coursenum: CS170
  points: 100
  goals:
    - To write a Python program that implements a mathematical expression
    - To obtain user input from the keyboard in a Python program
    - To explore the relationship between audio pitch and frequency
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
  - music
  - math
  
---

In this assignment, you will write a program to execute a mathematical formula to calculate the frequency for a note.  Specifically, we will use this formula to compute a note's frequency some number of half-steps above or below a base frequency.  Often, we use the "Concert A" frequency of 440 Hz (known as the A4 note), which you can hear on the [Online Tone Generator](https://www.szynalski.com/tone-generator/) website.  If you know your base frequency (440), and the number of half-steps you wish to go above or below that frequency, you can calculate the new frequency using this formula:

<span>\\(pitch = base \times (2^{\frac{1}{12}})^{step}\\)</span>

For example, one half step above A4 is A#4 ("A sharp 4"), and its frequency of 466.16 is obtained by calculating <span>\\(pitch = base \times (2^{\frac{1}{12}})^{step} = 440 \times (2^{\frac{1}{12}})^{1} = 466.16\\)</span>.  Two half-steps above A4 is B4, whose frequency of 493.88 can be obtained by computing <span>\\(pitch = base \times (2^{\frac{1}{12}})^{step} = 440 \times (2^{\frac{1}{12}})^{2} = 493.88\\)</span>.  One half-step below A4 is G#4, whose frequency of 392 is computed via <span>\\(pitch = base \times (2^{\frac{1}{12}})^{step} = 440 \times (2^{\frac{1}{12}})^{-1} = 415.3\\)</span>.  You can find a table of notes and frequencies [here](https://web.archive.org/web/20170720171942/https://pages.mtu.edu/~suits/notefreqs.html).

## What to Do

### Calculate the Frequency
Create a Python project and ask the user to input the base frequency and the number of half-steps you want to calculate.  To get user input from the keyboard on-screen, you can use this code:

```python
# First, print a prompt to the screen to ask the user for a value, and store what they type into a variable called base
base = input("Please enter the base frequency as a whole number (example: 440):")

# Since we know this should be a whole number, convert the variable's value to an integer
base = int(base)
```

Calculate the new frequency and print that value to the screen.  Call your variable `frequency`.  Verify that it is correct on the [table of frequencies](https://web.archive.org/web/20170720171942/https://pages.mtu.edu/~suits/notefreqs.html), and play the notes on the [Online Tone Generator](https://www.szynalski.com/tone-generator/) to hear what they would sound like when played on an instrument.

As a hint, the mathematical operators are: `*` to multiply, `/` to divide, `+` to add, `-` to subtract, and `**` to raise a number to an exponent power.

### Installing Required Software
In your terminal window (**not** in your code!), type this command and press enter, which will install some library software that we'll use:

```
python3 -m pip install scipy pyaudio
```

**If you have a Mac computer, please see my note below about a few commands you can run to install some software required by this command.**

### Play the Note

Download [this file](../files/asmt-semitone/sounds.py) which contains code to play a note on your computer given its frequency.  You can save it into your project folder to use it.  **Be sure that you see the `sounds.py` file in your project!**  At the top of your program, add this line:

```python
# import code into my program that I can use
import sounds
```

Now, you can use that code to play sounds!  To play a tone, write this line at the bottom of your program:

```python
sounds.sine_tone(frequency, 1, volume=0.25) # play the given frequency for 1 seconds and 25% volume
```

Re-run your program and try it for a few different notes.  Verify that they're correct using the [Online Tone Generator](https://www.szynalski.com/tone-generator/).

**As the frequency increases, what happens to the pitch of the sound?**

### Play a Song
Create a new Python file within your project.  Using the `sounds.sine_tone` function, play several frequency notes to put together a song.  You can make up your own song, or use the [table of frequencies](https://web.archive.org/web/20170815053408/https://pages.mtu.edu/~suits/notefreqs.html) to play a known song.  For example, here's the "alphabet song" (based on [Twinkle Twinkle Little Star](https://en.wikipedia.org/wiki/Twinkle,_Twinkle,_Little_Star)):

```
C4 C4 G4 G4 A4 A4 G4(1/2 note)
F4 F4 E4 E4 D4(1/8th note) D4(1/8th note) D4(1/8th note) D4(1/8th note) C4(1/2 note)
G4 G4 F4 (rest 1/16th note) E4 E4 D4(1/2 note)
G4(1/8th note) G4(1/8th note) G4(1/8th note) F4 (rest 1/16th note) E4 E4 D4(1/2 note)
C4 C4 G4 G4 A4 A4 G4(1/2 note)
F4 F4 E4 E4 D4 D4 C4(1/2 note)
```

A **1/2 note** just means to play at half the duration of your other notes.  You can create a variable called duration and set it to `1/2`, `1/8`, or `1/16` as approrpiate.  All the other notes are **1/4 notes**.

For fun, you might notice there is a "rest" in the song.  A rest means to pause.  We can actually pause our program by importing another software package into our program called `time` (at the top):

```python
import time
```

and calling `time.sleep(1/16)` to pause for one sixteenth of a second.

### Mixing Sounds
A chord effectively mixes to sounds together - the sound waves are added together to create a mixed wave.  

In a new Python file, call this function:

```python
sounds.dtmf_tone(350, 440, 2, volume=0.25)
```

Note that we put two numbers into the function for the frequency instead of just one.  This will cause them to mix together.  We use brackets in Python to store variables that are collections of things (for example, multiple frequencies instead of a single frequency value).  Run this program; does it sound familiar?  Landline telephones use mixed tones (called dual-tones) to represent each button you could push on the phone.

Using these frequency combinations, try writing a program that plays the tones for your phone number.  Interestingly, if you held your computer speaker up to an old telephone and ran this program, it would actually dial that number!

| **Digit** | **Frequency 1** | **Frequency 2** |
|-----------|-----------------|-----------------|
| **1**     | 697             | 1209            |
| **2**     | 697             | 1336            |
| **3**     | 697             | 1477            |
| **4**     | 770             | 1209            |
| **5**     | 770             | 1336            |
| **6**     | 770             | 1477            |
| **7**     | 852             | 1209            |
| **8**     | 852             | 1336            |
| **9**     | 852             | 1477            |
| **0**     | 941             | 1336            |

**If you looked at an audio sound graph like you might find on a stereo system, and saw the following output, what digit would you guess is being dialed on the phone?**

<p align="center">
<img src="https://sparse-plex.readthedocs.io/en/latest/_images/dtmf_4507_periodogram.png" style="max-width:100%;" alt="DTMF Spectrogram">
</p>

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## Note: For Mac Users

If you get an error while trying to install pyaudio using the `pip` command above, you can execute the following commands in a Terminal window:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
/opt/homebrew/bin/brew install portaudio gfortran
CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install scipy pyaudio
python3 -m venv .venv
source .venv/bin/activate
```

You may be prompted to enter your password and press enter once or twice by the first command - this is OK!

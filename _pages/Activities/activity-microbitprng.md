---
layout: activity
permalink: /Activities/MicrobitPRNG
title: "CS170: Programming for the World Around Us - The micro:bit and Pseudorandom Number Generators"


info:
  additional_reading:
    - title: "Saving MakeCode Projects on GitHub"
      link: "https://makecode.microbit.org/github/getting-started"
  goals: 
    - To introduce the microbit as a programming device
    - To explain why computers cannot generate truly random numbers
    - To explain how computers generate pseudorandom numbers
    - To explain the role of seed values in pseudorandom number generators (PRNG)
    - To provide examples of mechanisms that computers use to seed PRNGs
    - To develop an algorithm to generate pseudorandom numbers with a computer
    - To implement an algorithm using the micro:bit blocks language
    - To create and use a GitHub account to save your micro:bit MakeCode project
    - To create and manipulate variables in a computer program
    - To implement a mathematical formula using code
  models:
    - title: "Random Numbers"
      model: |
        <!-- https://uicookies.com/css-blockquote/ and https://codepen.io/jonitrythall/pen/XbENPM-->
        <blockquote style="margin: 3.7em auto; padding: 2em; background: linear-gradient(white, white) padding-box, url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/80625/sea.jpg) border-box  0 / cover; border: 2em solid transparent; box-shadow: 5px 3px 30px black; font-size: 1.4em; font-style: italic; line-height: 1.5; width: 40%;">From where we stand the rain seems random.  If we could stand somewhere else, we would see the order in it.
        <footer style="padding-top: 1.3em;">&mdash;
          <cite style="font-style: normal; font-size: 1.2em; font-weight: bold;">
              Tony Hillerman, Coyote Waits
          </cite>
        </footer>
        </blockquote>
      questions: 
        - Pick three numbers from 1 to 10 at random, and write them on the board.
        - What do you notice about the distribution of those numbers?
        - How did you come up with those numbers?  How did you ensure they were truly quot;random?&quot;
        - What does it mean to be &quot;random?&quot;
    - title: "Computers and Random Numbers"
      model: |
        <iframe width="560" height="315" src="https://www.youtube.com/embed/nl_62s1xqCo" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      questions: 
        - How do computers pick numbers &quot;at random?&quot;
        - How do they decide when to spawn certain &quot;random&quot; events?
        - Is this video game player really good at the game?
    - title: "Pseudorandom Number Generation"
      model: |
        <img src="../files/activity-microbitprng/PRNG.png" alt="Pseudonumber Random Number Generator (PRNG) formula">
        <br>
        <a title="Cmglee, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Linear_congruential_generator_visualisation.svg"><img width="512" alt="Linear congruential generator visualisation" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Linear_congruential_generator_visualisation.svg"></a>
      questions: 
        - "The <a href=\"https://en.wikipedia.org/wiki/Linear_congruential_generator\">Linear Congruential Generator</a> is one way to generate a pseudo-random number computationally.  Choose a starting value and generate 3 random numbers using this formula."
        - What would happen if two people used the same starting value (called a &quot;seed&quot;)?
        - How might video games generate a seed?
    - title: "Introduction to the micro:bit"
      model: |
        <a href="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Micro-bit_v1_%26_v2.JPG"><img src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Micro-bit_v1_%26_v2.JPG" alt="Micro-bit v1 &amp; v2.JPG: Creative Commons Zero, Public Domain Dedication"></a>
        <br>
        <div style="text-align: left;">
        micro:bit devices are &quot;programmable units&quot; that have:
        <ul>
        <li>electrical connections</li>
        <li>LED output display</li>
        <li>radios</li>
        <li>compass</li>
        <li>accelerometer</li>
        <li>speakers</li>
        <li>light sensors</li>
        <li>buttons</li>
        </ul>
        </div>
      questions: 
        - "Using the micro:bit, create variables for a, b, c, and X: call them <code>multiplier</code>, <code>adder</code>, <code>modulus</code>, and <code>current</code>."
        - Give them any values you want by setting their values in <code>on start</code>.
        - When the user presses the A button, set the value of the X variable (<code>current</code>) using the formula, and show X on the screen.
        - Is it ok that the X variable appears on the left and the right side of the equals sign?  Why or why not?
        - On start, show the value of X on the screen.
        - When you're done, click on the Python tab at the top.  What do you notice about each block from the original program?
        - Save your project to a GitHub account; you can create one for free!

tags:
  - microbit
  - prng
  
---

### Pairing the Microbit to your Computer

You can connect the micro:bit to your computer by plugging in the USB cable.  However, some computers do not have a compatible mac cable.  If you don't have an adapter, your computer may support Bluetooth, a wireless protocol that you can use to connect to the micro:bit.  You can do this by holding down the A and B buttons of the micro:bit, and, while holding them down, press and release the reset button.  You'll see the words "PAIRING MODE" appear on the micro:bit display.  Open a bluetooth application on your computer (on the Mac, one such program is called LightBlue), and select the BBC micro:bit to pair.  The micro:bit will prompt you to press the A button and a 6-digit code will appear on the screen.  Type that code on your mac and you should have access to the storage of the micro:bit!  You can download your code from Makecode, and then drag the `.hex` file from your Downloads directory to the micro:bit disk.  It will restart and launch your app automatically.  Here is a video describing the process on a Mac, although the process is similar on other Bluetooth enabled computers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bIMv63Ue1C0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Notes and Walkthrough

Computers are deterministic machines: given the same instructions and the same starting information, they will do exactly the same thing every time.  That's usually a feature!  But it means a computer can't truly "pick a number at random" the way you might feel like you do.  Instead, computers use a **pseudorandom number generator** (PRNG): a formula that produces a sequence of numbers that *looks* random, even though each number is completely determined by the one before it.  "Pseudo" just means "sort of" or "fake" - these numbers only pretend to be random!

One classic PRNG is the **Linear Congruential Generator** (LCG).  Don't let the name scare you; it's just this formula:

\\(X_{next} = (a \times X_{current} + c) \bmod m\\)

In plain English: take your current number, multiply it by some constant `a` (the **multiplier**), add another constant `c` (the **adder**), and then take the remainder after dividing by `m` (the **modulus**).  That remainder becomes your next "random" number.  The very first value of `X` is called the **seed**: it's where the sequence starts, and anyone who uses the same seed (and the same `a`, `c`, and `m`) will get exactly the same sequence of "random" numbers.  That's why video games often seed their generators with something that's different every time, like the number of milliseconds since the device powered on.

### A Worked Example on the micro:bit

Here's a complete MakeCode Python program that sets up the formula's variables in `on start`, and generates (and shows) the next pseudorandom number each time you press the A button:

```python
multiplier = 5
adder = 3
modulus = 16
current = 7  # this is our seed!

basic.show_number(current)

def on_button_pressed_a():
    global current
    current = (multiplier * current + adder) % modulus
    basic.show_number(current)
input.on_button_pressed(Button.A, on_button_pressed_a)
```

When this program starts, the LED display scrolls the seed value `7`.  Then, each time you press A, the display scrolls the next number in the sequence.  Notice the line `global current` - because we're *changing* the variable inside a function, we have to tell Python that we mean the `current` variable from the main program, not a brand-new one that lives only inside the function.

### Tracing the Formula

Let's trace three presses of the A button by hand, using `a = 5`, `c = 3`, and `m = 16`, starting from the seed `7`.  Tracing means playing computer: we compute each step ourselves with concrete numbers.

| Press | `current` before | \\(a \times X + c\\) | \\(\bmod~16\\) (remainder) | `current` after (shown on screen) |
|-------|------------------|----------------------|----------------------------|-----------------------------------|
| 1     | 7                | \\(5 \times 7 + 3 = 38\\)  | \\(38 \bmod 16 = 6\\)      | 6                                 |
| 2     | 6                | \\(5 \times 6 + 3 = 33\\)  | \\(33 \bmod 16 = 1\\)      | 1                                 |
| 3     | 1                | \\(5 \times 1 + 3 = 8\\)   | \\(8 \bmod 16 = 8\\)       | 8                                 |

The sequence 7, 6, 1, 8, ... looks scattered and unpredictable - but if your neighbor starts with seed 7 too, they'll get 6, 1, 8 in exactly the same order.  Also notice that the result of `mod 16` is always between 0 and 15, so this generator can only ever produce numbers in that range.

### Common Mistakes

* **Forgetting `global`**: if you assign to `current` inside a function without `global current`, Python quietly creates a new local variable, and your sequence never advances.
* **Confusing `mod` with division**: `38 % 16` is the *remainder* (6), not the quotient (2).
* **Reusing the seed**: if you set `current` back to the seed inside the button handler, you'll get the same number every press instead of a sequence.
* **Choosing `m = 0`**: you can't take a remainder after dividing by zero - the program will crash.

## Practice Exercises

All of these can be done in the [MakeCode simulator](https://makecode.microbit.org/) without any hardware - just click the on-screen A button!

### Exercise 1 (warm-up)

By hand (no computer!), trace the LCG with `a = 3`, `c = 1`, `m = 10`, and seed `X = 4` for three steps.  What three numbers do you get?

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
# Step 1: (3 * 4 + 1) % 10 = 13 % 10 = 3
# Step 2: (3 * 3 + 1) % 10 = 10 % 10 = 0
# Step 3: (3 * 0 + 1) % 10 =  1 % 10 = 1
# The sequence is 3, 0, 1
```

Each step feeds its answer back in as the new `X`.  Because we're taking `mod 10`, every number in the sequence is a single digit from 0 to 9.

</details>

### Exercise 2

Type the worked example above into MakeCode and run it in the simulator.  Then change only the seed (`current`) to a different starting value and press A a few times.  Does the sequence change?  Now change it back to `7` - do you get 6, 1, 8 again?

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
multiplier = 5
adder = 3
modulus = 16
current = 12  # try a new seed here

basic.show_number(current)

def on_button_pressed_a():
    global current
    current = (multiplier * current + adder) % modulus
    basic.show_number(current)
input.on_button_pressed(Button.A, on_button_pressed_a)
```

With seed 12 you get 63 % 16 = 15, then 78 % 16 = 14, and so on - a different sequence.  Returning the seed to 7 reproduces 6, 1, 8 exactly, which demonstrates why these numbers are "pseudo" random: the same seed always gives the same sequence.

</details>

### Exercise 3

Our generator produces numbers from 0 to 15, but suppose you want to simulate a six-sided die (numbers 1 through 6).  Modify the button handler so that, after computing `current`, it shows `(current % 6) + 1` instead.  Why do we add the 1?

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
def on_button_pressed_a():
    global current
    current = (multiplier * current + adder) % modulus
    basic.show_number((current % 6) + 1)
input.on_button_pressed(Button.A, on_button_pressed_a)
```

`current % 6` gives a remainder between 0 and 5, so adding 1 shifts the range to 1 through 6, just like a real die.  Without the `+ 1`, you could roll a zero - and never roll a six!

</details>

### Exercise 4 (challenge)

Every micro:bit running the same program produces the same sequence - not very useful for games!  Add an `on shake` event that changes the seed, for example by setting `current` to `input.running_time() % modulus` (the number of milliseconds since the program started).  Why does this make the sequence hard to predict?

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
def on_gesture_shake():
    global current
    current = input.running_time() % modulus
    basic.show_icon(IconNames.DIAMOND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
```

Nobody can predict the exact millisecond at which you'll shake the device, so the seed - and therefore the entire sequence that follows - is different every run.  This is exactly how real programs seed their PRNGs: they grab something unpredictable from the outside world, like the clock.

</details>



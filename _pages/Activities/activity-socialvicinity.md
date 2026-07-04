---
layout: activity
permalink: /Activities/SocialVicinity
title: "CS170: Programming for the World Around Us - Social Vicinity Tracking with the micro:bit"


info:
  teacher_highlights:
    - "Teachers can set up a MakeCode Classroom environment by activating this <a href=\"../files/activity-socialvicinity/socialvicinity-20220705-0406-microbit-classroom-resume-activity.html\">template</a>."
  goals: 
    - To use arrays to store collections of data
  models:
    - title: "Social Vicinity Tracker using the micro:bit"
      model: |
        <!-- https://uicookies.com/css-blockquote/ and https://codepen.io/jonitrythall/pen/XbENPM-->
        <blockquote style="margin: 3.7em auto; padding: 2em; background: linear-gradient(white, white) padding-box, url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/80625/sea.jpg) border-box  0 / cover; border: 2em solid transparent; box-shadow: 5px 3px 30px black; font-size: 1.4em; font-style: italic; line-height: 1.5; width: 40%;">If you take me out of it, I find &quot;six degrees&quot; to be a beautiful concept that we should try to live by.
        <footer style="padding-top: 1.3em;">&mdash;
          <cite style="font-style: normal; font-size: 1.2em; font-weight: bold;">
              Kevin Bacon
          </cite>
        </footer>
        </blockquote>
      questions: 
        - Turn to the people around you and say hello to them, and tell them where you’re from.
        - As best you can, count how many words you hear each person in the room say.  You might need some paper for this!
        - How did you keep track?
    - title: "Tracking Collections of Data"
      model: |
        <a title="No machine-readable author provided. Jarkko Piiroinen assumed (based on copyright claims)., Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Array1.svg"><img width="256" alt="Array1" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Array1.svg"></a>
      questions: 
        - "You can create &quot;arrays&quot; of data to do this automatically!  In python, this creates a table for each of 5 of your friends, each set to 0 words: <code>friends = [0,0,0,0,0]</code>"
        - Where do you see tables like this in your own life?
        - What should you do each time you receive a radio message from a friend?
        - How can you keep track of which person you're communicating with?
        - The radio received event can send a number!  Send a different number for each person.  How should we store this special &quot;radio number?&quot;
        - Modify the program so that each person can pick their unique radio number by incrementing the variable by 1 every time the A button is pressed.  Perhaps display it on the screen so you know which radio number you will use (and make sure no-one else is using it).
        - When you press the other button, show one of the values from the array on screen.  You can use another variable for this.
        - Why send <code>hello = radio_number</code> rather than just the radio number like we did before?  Either way works, but what additional flexibility do you gain by using this block?
        - "How can you modify this program so that instead of showing the number of messages you've received, you show instead the number of seconds you were near one another?  What would you need to do to figure out a conversion between messages seen and time?  As a hint: can you guess how long someone was speaking by counting the number of words you heard them say?  How might you do this?"

tags:
  - microbit
  - arrays
  
---

*Note: this activity is offered as an **optional enrichment activity**.  The class session it previously occupied is now used for more hands-on Python practice - but if it looks fun (it is!), you are warmly encouraged to try it with a partner during open lab time or office hours.*

## Notes and Walkthrough

Imagine trying to count how many times *each* person in the room says hello to you.  With two or three people, you could use a separate variable for each: `alice_count`, `bob_count`, `carol_count`...  But what about 30 people?  Creating 30 variables (and 30 nearly identical pieces of code to update them) would be exhausting.  This is exactly the problem **arrays** solve.  An array is a single variable that holds a whole numbered list of values.  In Python:

```python
seen = [0, 0, 0, 0, 0]
```

creates one variable, `seen`, holding five counters.  Each slot has an **index** - its position in the list - and (here's the part everyone trips on at first) **indices start at 0**, not 1.  So `seen[0]` is the first slot and `seen[4]` is the last.  The magic is that the index can be a *variable*: `seen[radio_number]` means "the counter belonging to whichever device number just messaged me."  One line of code updates the right counter no matter who is talking!

In this activity, each person's micro:bit repeatedly broadcasts its own ID number (its "radio number"), and everyone else counts the messages they hear from each ID.  The more messages you've heard from someone, the longer you've been near them - just like the "vicinity tracking" that contact-tracing apps performed during the COVID-19 pandemic.

### A Worked Example

Here's a complete program.  Each device broadcasts its own `radio_number` every second; when it hears a number from someone else, it adds 1 to that person's slot in the array.  Pressing A picks your ID; pressing B cycles through the array and shows each count.

```python
radio.set_group(1)
seen = [0, 0, 0, 0, 0]
radio_number = 0
show_index = 0

def on_forever():
    radio.send_number(radio_number)
    basic.pause(1000)
basic.forever(on_forever)

def on_received_number(receivedNumber):
    global seen
    if receivedNumber != radio_number:
        seen[receivedNumber] = seen[receivedNumber] + 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global radio_number
    radio_number = (radio_number + 1) % 5
    basic.show_number(radio_number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global show_index
    basic.show_number(seen[show_index])
    show_index = (show_index + 1) % 5
input.on_button_pressed(Button.B, on_button_pressed_b)
```

On the LED display: pressing A scrolls your own ID number, and each press of B scrolls the message count for the next person in the array.  The `% 5` keeps both numbers inside the array's valid indices, 0 through 4 - a bigger number would crash the program.

### Tracing the Array

Suppose you are device 2, and devices 1 and 3 are nearby broadcasting once per second.  Let's trace your `seen` array as messages arrive:

| Event | `receivedNumber` | Is it my own ID (2)? | `seen` array after |
|--------------------------|------------------|----------------------|---------------------|
| Program starts           | -                | -                    | `[0, 0, 0, 0, 0]`   |
| Message from device 1    | 1                | No - count it        | `[0, 1, 0, 0, 0]`   |
| Message from device 3    | 3                | No - count it        | `[0, 1, 0, 1, 0]`   |
| Message from device 1    | 1                | No - count it        | `[0, 2, 0, 1, 0]`   |
| Message from device 3    | 3                | No - count it        | `[0, 2, 0, 2, 0]`   |
| Message from device 1    | 1                | No - count it        | `[0, 3, 0, 2, 0]`   |

After five messages, `seen[1]` is 3 and `seen[3]` is 2: you've been near device 1 for about 3 seconds and device 3 for about 2 seconds.  Notice that only one slot changes per message, and the received number itself picks the slot.  Since each device broadcasts once per second, *messages heard ≈ seconds spent nearby* - that's the conversion the last model question asks about.

### Common Mistakes

* **Off-by-one indexing**: the first slot is `seen[0]`, and a 5-slot array has no `seen[5]`.  Asking for an index that doesn't exist stops the program.
* **Forgetting `radio.set_group(...)`**: devices on different groups never hear each other, and every count stays 0.
* **Two people with the same radio number**: their messages land in the same array slot, and the counts get merged.  That's why you display your ID when choosing it - so you can make sure it's unique.
* **Counting your own broadcasts**: without the `receivedNumber != radio_number` check, some radio setups can let you hear yourself, inflating your own slot.

## Practice Exercises

All of these run in the [MakeCode simulator](https://makecode.microbit.org/) - a second micro:bit appears automatically when your program uses the radio.  Exercise 4 is best with a partner and real devices.

### Exercise 1 (warm-up)

Without a computer, trace this code by hand and write down the final array: start with `counts = [0, 0, 0]`, then run `counts[1] = counts[1] + 1`, then `counts[0] = counts[0] + 5`, then `counts[1] = counts[1] + 1`.

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
counts = [0, 0, 0]
counts[1] = counts[1] + 1   # [0, 1, 0]
counts[0] = counts[0] + 5   # [5, 1, 0]
counts[1] = counts[1] + 1   # [5, 2, 0]
# final answer: [5, 2, 0]
```

Each line changes exactly one slot and leaves the others alone.  Note that `counts[1]` is the *second* slot, because indices start at 0.

</details>

### Exercise 2

In the simulator, build a mini version: when A is pressed, send the number 1 over the radio; when a number is received, add 1 to that slot of a `seen = [0, 0]` array and show the updated count.  Press A on one simulated micro:bit and watch the other.

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
radio.set_group(1)
seen = [0, 0]

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_number(receivedNumber):
    global seen
    seen[receivedNumber] = seen[receivedNumber] + 1
    basic.show_number(seen[receivedNumber])
radio.on_received_number(on_received_number)
```

Every press of A on one device makes the other device's count climb: 1, 2, 3...  The received number (1) is used directly as the array index, so the message itself tells us *whose* counter to increase.

</details>

### Exercise 3

Our array has 5 slots, but the A button uses `% 5` so IDs run from 0 to 4.  Change the program to support 10 people.  What (at least) two lines must change, and what happens if you change only one of them?

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
seen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def on_button_pressed_a():
    global radio_number
    radio_number = (radio_number + 1) % 10
    basic.show_number(radio_number)
input.on_button_pressed(Button.A, on_button_pressed_a)
```

Both the array size and the `% 10` (in the A *and* B handlers) must agree.  If you enlarge only the `%` but not the array, someone can choose ID 7 - and the first message from them tries to update `seen[7]`, a slot that doesn't exist, crashing the program.  Keeping related numbers in sync is a classic source of bugs!

</details>

### Exercise 4 (partner)

With a partner (in the simulator or on hardware), run the full program.  Pick different IDs, let the devices chat for 30 seconds or so, then press B to read your counts.  Do the counts roughly match the number of seconds you were "near" each other?  Discuss: how would you convert "messages heard" into "seconds together" if the broadcast paused 2000 ms instead of 1000 ms?

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
# With a 2000 ms pause, each heard message represents about 2 seconds:
seconds_together = seen[show_index] * 2
basic.show_number(seconds_together)
```

Since each broadcast is one message every 2 seconds, multiplying the count by 2 estimates the time spent nearby.  This is like guessing how long someone spoke by counting their words and multiplying by the average time per word - the model questions above were hinting at exactly this!

</details>


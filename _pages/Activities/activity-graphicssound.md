---
layout: activity
permalink: /Activities/GraphicsSound
title: "CS170: Programming for the World Around Us - Graphics and Sound with Python"


info:
  goals: 
    - To use graphics and sound capabilities in Python
  models:
    - title: "Graphics"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        from ezgraphics import GraphicsWindow

        win = GraphicsWindow(640, 480)
        win.setTitle("My First Drawing")

        canvas = win.canvas()

        canvas.setFill(255, 0, 0)
        canvas.drawRectangle(40, 40, 100, 200)

        canvas.setFill(255, 255, 255)
        canvas.setOutline(0, 255, 0)
        canvas.drawRectangle(200, 200, 150, 50)

        win.wait()
        ]]></script>  
      questions: 
        - "Run this code in your terminal: <code>http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz && pip install ezgraphics-2.2.tar.gz</code> to install the ezgraphics library, and run this program.  What does it do?"
        - "Experiment with the functions and generate your own shapes.  Can you draw a house or a stick figure?  Make a function that does this, given the <code>x</code> and <code>y</code> midpoint as parameters."
    - title: "Animation"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        from ezgraphics import GraphicsWindow
        import random

        win = GraphicsWindow(640, 480)
        win.setTitle("My First Drawing")

        i = 0
        j = 0
        lasti = -1
        lastj = -1

        canvas = win.canvas()

        canvas.setFill(0,0,0)
        canvas.drawRectangle(0, 0, 640, 480)

        while True:
          if i > 0 and j > 0:
            canvas.setFill(0,0,0)
            canvas.drawRectangle(i-1, j-1, 10, 20)
            
          canvas.setFill(255, 255, 255)
          canvas.drawRectangle(i, j, 10, 20)

          lasti = i
          lastj = j
          
          i = i + random.randint(-1, 1)
          j = j + random.randint(-1, 1)

          if i > 640:
            i = 639
          if j > 480:
            j = 479

          if i < 0:
            i = 1
          if j < 0:
            j = 1

          win.pause(1)
          
        win.wait()
        ]]></script>  
      questions: 
        - "Comment this program; what does it do?  You will find it helpful to run the program first, and may find it helpful to set a breakpoint and use the debugger!"
    - title: "Sound"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        # https://stackoverflow.com/questions/974071/python-library-for-playing-fixed-frequency-sound

        """Play a fixed frequency sound."""
        from __future__ import division
        import math
        from scipy import signal
        from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

        try:
            from itertools import izip
        except ImportError: # Python 3
            izip = zip
            xrange = range

        def sine_tone(frequency, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)
                            
            s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
            samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()

        def square_tone(frequency, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)

            s = lambda t: volume * signal.square(2 * math.pi * frequency * t / sample_rate)
            samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()    

        def dtmf_tone(frequency1, frequency2, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate 

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)
                            
            s1 = lambda t: volume * math.sin(2 * math.pi * frequency1 * t / sample_rate)
            s2 = lambda t: volume * math.sin(2 * math.pi * frequency2 * t / sample_rate)
            samples = (int(s1(t) * 0x3f + 0x40) + int(s2(t) * 0x3f + 0x40) for t in xrange(n_samples)) # scale to 0-255

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()

        def sine_chord(frequencies, duration, volume=1, sample_rate=22050):
            if len(frequencies) >= 6:
                frequencies = frequencies[:6]

            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate 

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)

            s = []
            k = len(frequencies)
            for i in range(k):                
                f = frequencies[i]
                sf = lambda t: volume * math.sin((2 * math.pi * f * t / sample_rate))
                s.append(sf)

            z = lambda t: sum([int(x(t) * (2**(8-k)-1) + 2**(8-k)) for x in s])
            samples = (z(t) for t in xrange(n_samples)) # scale to 0-255

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()    
        ]]></script>  
        <br>
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        import sounds

        # https://github.com/cleversonahum/dtmf-generator/blob/main/dtmf-generator.py
        DTMF_TABLE = {
            "1": [1209, 697],
            "2": [1336, 697],
            "3": [1477, 697],
            "A": [1633, 697],
            "4": [1209, 770],
            "5": [1336, 770],
            "6": [1477, 770],
            "B": [1633, 770],
            "7": [1209, 852],
            "8": [1336, 852],
            "9": [1477, 852],
            "C": [1633, 852],
            "*": [1209, 941],
            "0": [1336, 941],
            "#": [1477, 941],
            "D": [1633, 941],
            "dial_tone": [350, 440]
        }

        #sounds.sine_tone(2000, 0.5, volume=0.25)
        #sounds.square_tone(2000, 0.25, volume=0.25)

        sounds.dtmf_tone(*DTMF_TABLE['dial_tone'], 2, volume=0.25) # dial tone: 350, 400
        sounds.dtmf_tone(*DTMF_TABLE['6'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['1'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['0'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['4'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['0'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['9'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['3'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['2'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['6'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['8'], 0.25, volume=0.25)

        C = 261.63
        E = 329.63
        G = 392
        sounds.sine_chord([C, E, G], 1, volume=0.25)
        ]]></script>         
      questions: 
        - "Save these two files into your program (call the first one <code>sounds.py</code> since we <code>import sounds</code> in the second file!) and run it."
        - "Look up DTMF tones; what is this program doing?"
        - "Make a song with some tones and play the program.  You might try this with the microbit to see what kinds of notes it plays when you play a melody; you can copy the frequencies into this program."
        
tags:
  - python
  - graphics
  - sound
  
---

## Notes and Walkthrough

Up to now, our programs have talked to us through text.  Today we'll give them a face and a voice!  Before we dive into the models above, let's build up the vocabulary we need to think about pictures and sounds the way the computer does.

### How the computer thinks about pictures

Your screen is a giant grid of tiny colored dots called **pixels** (short for "picture elements").  To draw anything, we tell the computer which pixels to color.  We locate a pixel with a **coordinate**: a pair of numbers `(x, y)`, where `x` counts how far *right* from the left edge, and `y` counts how far *down* from the top.

That last part surprises everyone: on a computer screen, **y increases downward**, not upward like the graphs in math class!  The point `(0, 0)` is the *top-left* corner of the window.  So in our first model above, a `GraphicsWindow(640, 480)` is 640 pixels wide and 480 pixels tall, `(639, 0)` is the top-*right* corner, and `(0, 479)` is the *bottom*-left.

The `ezgraphics` library that this activity uses gives us two objects to work with.  The **window** (`win`) is the frame that appears on your screen, and the **canvas** (`canvas = win.canvas()`) is the drawing surface inside it — like a real painter's canvas mounted in a frame.  We paint on the canvas by calling its drawing functions.

Colors are described with three numbers from 0 to 255 for the amounts of **red, green, and blue** light to mix (this is called **RGB**).  `(255, 0, 0)` is pure red, `(0, 0, 0)` is black (no light), and `(255, 255, 255)` is white (all the light).  In `ezgraphics`, `canvas.setFill(r, g, b)` picks the color used to fill the *inside* of shapes, and `canvas.setOutline(r, g, b)` picks the color of their border — and each stays in effect for every shape you draw afterward, until you change it.

Let's put that together in a small example.  Text first, then code: we'll open a window, paint the sky, and draw a sun in the top-right area.

```python
from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 300)
win.setTitle("Sunny Day")

canvas = win.canvas()

# sky: a light blue rectangle covering the whole canvas
canvas.setFill(135, 206, 235)
canvas.drawRectangle(0, 0, 400, 300)

# sun: a yellow oval near the top-right corner
canvas.setFill(255, 255, 0)
canvas.drawOval(300, 30, 60, 60)

win.wait()
```

This program prints nothing, but a 400-by-300 window appears titled "Sunny Day": the entire window is light blue, with a yellow circle 60 pixels across whose top-left corner sits at `(300, 30)` — up near the right edge.  The window stays open until you close it, because `win.wait()` tells the program to pause and wait for you.

Notice the *order* of the calls.  The sky rectangle covers the whole canvas, so we draw it **first**; anything drawn earlier gets painted over by anything drawn later, just like layers of paint.  What do you think would happen if you swapped the sky and the sun?  Try it out — the sun disappears behind the sky!

### How animation works: repaint, nudge, pause

Movies and video games don't really move — they show a rapid sequence of still pictures called **frames**, and our eyes blend them into motion.  Look back at the Animation model above: each trip through the `while True:` loop draws one frame.  The recipe inside the loop is always the same three steps:

1. **Erase** the old drawing (here, by painting a black rectangle over where the shape used to be — black because the background is black).
2. **Draw** the shape at its new position.
3. **Pause** briefly (`win.pause(1)`) so the frame stays on screen long enough to see, then repeat.

Here's a conceptual frame-by-frame trace of the Animation model, supposing the random nudges happen to come out as shown.  The shape is a 10-by-20 white rectangle starting at `i = 0, j = 0`:

| Step | Call | Variable values | What appears on screen |
|------|------|-----------------|------------------------|
| 1 | `canvas.setFill(0,0,0)` / `canvas.drawRectangle(0, 0, 640, 480)` | `i` = 0, `j` = 0 | The whole canvas is painted black: our background. |
| 2 | `if i > 0 and j > 0:` | `i` = 0, `j` = 0 | False on the first frame — there's no old rectangle to erase yet, so we skip the erase step. |
| 3 | `canvas.setFill(255,255,255)` / `canvas.drawRectangle(0, 0, 10, 20)` | `i` = 0, `j` = 0 | Frame 1: a white 10x20 rectangle appears in the top-left corner. |
| 4 | `i = i + random.randint(-1, 1)` etc. | `i` = 1, `j` = 1 (say the dice rolled +1, +1) | Nothing visible changes yet — we've only updated the numbers. |
| 5 | `win.pause(1)` | `i` = 1, `j` = 1 | The picture holds for a moment so our eyes can see frame 1. |
| 6 | `canvas.setFill(0,0,0)` / `canvas.drawRectangle(0, 0, 10, 20)` | `i` = 1, `j` = 1 | A black rectangle is painted over the old spot, "erasing" frame 1's rectangle. |
| 7 | `canvas.setFill(255,255,255)` / `canvas.drawRectangle(1, 1, 10, 20)` | `i` = 1, `j` = 1 | Frame 2: the white rectangle reappears one pixel right and one pixel *down* (remember, bigger `j` means lower!). |
| 8 | `i = i + ...`, `j = j + ...` | `i` = 1, `j` = 2 (dice: 0, +1) | Position updated for the next frame. |
| 9 | `win.pause(1)` | `i` = 1, `j` = 2 | Frame 2 holds; the loop repeats, and the rectangle wanders randomly around the window forever. |

The `if i > 640: i = 639` checks at the bottom of the loop are guard rails: they keep the rectangle from wandering off the edge of the 640x480 canvas.  Nothing stops you from drawing at `x = 900` — you just won't see it, because it's beyond the window!

### How the computer thinks about sound

Sound is a vibration in the air.  The **frequency** of the vibration — how many times it wiggles back and forth per second, measured in **hertz (Hz)** — determines the pitch: more wiggles per second means a higher note.  Middle C is about 261.63 Hz; the A that orchestras tune to is 440 Hz.

A computer can't wiggle the air directly, so it plays sound the same way it shows animation: with lots of tiny snapshots.  Each snapshot of the wave's height is called a **sample**, and the **sample rate** is how many samples are played per second (our `sounds.py` model uses 22050 per second).  The `sine_tone` function in the model computes each sample using the `sin` function from math — that's why a pure, smooth whistle-like tone is called a **sine tone** — and hands the samples to the speaker through the PyAudio library.  The `square_tone` function uses a square-shaped wave instead, which sounds buzzier (this is the classic retro-video-game sound!).  You don't need to follow every line inside `sounds.py`; the important thing is what its functions let *you* say: "play this frequency, for this long, at this volume."

Using the `sounds` module from the model above, here's a tiny melody — the first three notes of a major scale, each half a second long:

```python
import sounds

C = 261.63
D = 293.66
E = 329.63

sounds.sine_tone(C, 0.5, volume=0.25)
sounds.sine_tone(D, 0.5, volume=0.25)
sounds.sine_tone(E, 0.5, volume=0.25)
```

This program prints nothing, but you hear three smooth ascending beeps — do, re, mi — one after another, each lasting half a second.  Notice the notes play in sequence, not at once: each `sine_tone` call finishes before the next begins, just like `print` statements run one at a time.  When you *do* want notes at the same time, that's a **chord**, and the model's `sine_chord` function plays a list of frequencies together.

The DTMF example in the model deserves one note (pun intended): **DTMF** stands for Dual-Tone Multi-Frequency — it's the system touch-tone telephones use, where every key on the keypad plays *two* frequencies at once (one from its row, one from its column) so the phone company's equipment can tell which key you pressed.  That's why the `DTMF_TABLE` maps each key to a pair of numbers, and why the model program sounds exactly like dialing a phone.

### Common mistakes to avoid

* **Forgetting that y increases downward.**  If your shape moves the "wrong way" vertically, remember that *adding* to `y` moves the shape *down* the screen, and `(0, 0)` is the top-left corner.
* **Drawing in the wrong order.**  Later drawings paint over earlier ones.  Draw your background first and your foreground shapes last, or they'll be hidden.
* **Forgetting that `setFill` is "sticky."**  The fill color stays in effect for every shape until you change it.  If your sun comes out sky-blue, you probably forgot to call `setFill` again before drawing it.
* **Forgetting to erase between frames.**  If you move a shape without painting over its old position, you get a smear of copies across the screen.  (Sometimes that's a fun effect — but usually it's a bug!)
* **Forgetting `win.pause(...)` in an animation loop.**  Without a pause, the loop runs as fast as the computer can go and the animation is an invisible blur (and the window may freeze up, since it never gets a chance to breathe).
* **Forgetting `win.wait()` at the end of a non-animated drawing.**  The program ends the instant the last line runs, and the window vanishes before you can see your masterpiece.
* **Drawing off the edge of the canvas.**  Coordinates beyond the window's width and height aren't errors — the shapes are just invisible.  Keep `x` between 0 and the width, and `y` between 0 and the height (that's what the boundary `if` statements in the Animation model are for).
* **Saving the sound helper file under the wrong name.**  The second sound program says `import sounds`, so the first file must be saved as exactly `sounds.py`, in the same folder.

## Practice Exercises

Try each one on your own before revealing the solution!  The graphics exercises assume `ezgraphics` is installed (see the first model above), and the sound exercises assume you saved the model's helper file as `sounds.py`.

### Exercise 1 (warm-up): A traffic light

Draw a traffic light: a tall dark-gray rectangle with three circles inside it — red on top, yellow in the middle, green on the bottom.  Remember: smaller `y` values are *higher* on the screen!

Expected result: a window showing a gray vertical rectangle with red, yellow, and green circles stacked top to bottom inside it, staying open until you close it.

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
from ezgraphics import GraphicsWindow

win = GraphicsWindow(200, 400)
win.setTitle("Traffic Light")

canvas = win.canvas()

# the housing: draw the background rectangle FIRST so the lights sit on top
canvas.setFill(60, 60, 60)
canvas.drawRectangle(50, 40, 100, 320)

# red light on top (smallest y)
canvas.setFill(255, 0, 0)
canvas.drawOval(70, 60, 60, 60)

# yellow light in the middle
canvas.setFill(255, 255, 0)
canvas.drawOval(70, 170, 60, 60)

# green light on the bottom (largest y)
canvas.setFill(0, 200, 0)
canvas.drawOval(70, 280, 60, 60)

win.wait()
```

The two key ideas: the housing is drawn first so the circles paint on top of it, and the red light gets the *smallest* y coordinate because y grows downward.

</details>

### Exercise 2: A row of shapes with a loop

Use a `for` loop to draw five blue squares in a horizontal row across the middle of a 640x480 window, each 50 pixels wide with a 20-pixel gap between them.  Hint: only the x coordinate changes from square to square — can you compute it from the loop variable?

Expected result: five evenly spaced blue squares in a row across the middle of the window.

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
from ezgraphics import GraphicsWindow

win = GraphicsWindow(640, 480)
win.setTitle("Row of Squares")

canvas = win.canvas()
canvas.setFill(0, 0, 255)

for i in range(5):
    # each square starts 70 pixels right of the previous one (50 wide + 20 gap)
    x = 40 + i * 70
    canvas.drawRectangle(x, 215, 50, 50)

win.wait()
```

The formula `x = 40 + i * 70` is the whole trick: as `i` counts 0, 1, 2, 3, 4, the x coordinate steps 40, 110, 180, 250, 320.  Whenever you find yourself copying and pasting a drawing call with one number changed, a loop with a formula can do it for you.

</details>

### Exercise 3: A bouncing ball

Modify the Animation model so that, instead of wandering randomly, a small white square moves steadily to the right by 2 pixels per frame, and when it reaches the right edge it reverses direction and comes back — bouncing back and forth forever.  Hint: keep the amount to move in a variable (say `speed = 2`), and flip its sign (`speed = -speed`) at the edges.

Expected result: a white square gliding left and right across a black window, bouncing off both side walls.

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
from ezgraphics import GraphicsWindow

win = GraphicsWindow(640, 480)
win.setTitle("Bouncing Ball")

canvas = win.canvas()

# black background
canvas.setFill(0, 0, 0)
canvas.drawRectangle(0, 0, 640, 480)

i = 0
j = 230
speed = 2

while True:
    # erase the square at its old position by painting background over it
    canvas.setFill(0, 0, 0)
    canvas.drawRectangle(i, j, 10, 10)

    # move, and bounce off the left and right walls by reversing the speed
    i = i + speed
    if i <= 0 or i >= 630:
        speed = -speed

    # draw the square at its new position
    canvas.setFill(255, 255, 255)
    canvas.drawRectangle(i, j, 10, 10)

    win.pause(10)
```

The bounce is just one line: when the square touches a wall, `speed = -speed` turns +2 into -2 (or back), so the same `i = i + speed` line now moves it the other way.  We check `i >= 630` rather than 640 because the square itself is 10 pixels wide.

</details>

### Exercise 4 (challenge): Play "Hot Cross Buns"

Using the `sounds` module from the model, play the melody "Hot Cross Buns": E, D, C, (rest), E, D, C.  Use E = 329.63, D = 293.66, C = 261.63, half a second per note.  For the rest (a moment of silence), you can play a tone at `volume=0` — or think of another way!  Bonus: store the melody in a *list* of frequencies and play it with a `for` loop.

Expected result: you hear the seven-note tune — three descending notes, a beat of silence, then the same three notes again.

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
import sounds

C = 261.63
D = 293.66
E = 329.63
REST = 0     # we'll treat 0 as "silence"

# the melody as a list, so a loop can play it
melody = [E, D, C, REST, E, D, C]

for note in melody:
    if note == REST:
        # a "note" at zero volume is a moment of silence
        sounds.sine_tone(440, 0.5, volume=0)
    else:
        sounds.sine_tone(note, 0.5, volume=0.25)
```

Putting the melody in a list means the playing code never changes when the song does — to play a different tune, you only edit the data.  That separation of *data* from *instructions* is one of the most powerful ideas in programming.

</details>

### Exercise 5 (challenge): Dial your phone number

Using the `DTMF_TABLE` from the model, write a program that asks the user for a phone number with `input()`, then plays a 2-second dial tone followed by the DTMF tone for each digit (0.25 seconds each).  Hint: a string is a sequence you can loop over with `for digit in number:` — and each `digit` is exactly the kind of string key the table expects.

Sample run:

```text
Enter a phone number: 6105551234
```

Expected result: after you press enter, you hear a dial tone, then the familiar touch-tone beeps of the number being dialed, one digit at a time.

<details>
<summary>Click to reveal a solution to Exercise 5</summary>

```python
import sounds

DTMF_TABLE = {
    "1": [1209, 697], "2": [1336, 697], "3": [1477, 697],
    "4": [1209, 770], "5": [1336, 770], "6": [1477, 770],
    "7": [1209, 852], "8": [1336, 852], "9": [1477, 852],
    "*": [1209, 941], "0": [1336, 941], "#": [1477, 941],
    "dial_tone": [350, 440]
}

number = input("Enter a phone number: ")

# pick up the phone: play the dial tone first
sounds.dtmf_tone(*DTMF_TABLE["dial_tone"], 2, volume=0.25)

# dial each digit in turn
for digit in number:
    if digit in DTMF_TABLE:
        sounds.dtmf_tone(*DTMF_TABLE[digit], 0.25, volume=0.25)
```

Looping over the string visits one character at a time, and each character is used as a key to look up its pair of frequencies in the table.  The `if digit in DTMF_TABLE` check politely skips anything that isn't a phone key, like spaces or dashes the user might type.

</details>

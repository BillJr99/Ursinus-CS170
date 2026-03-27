---
layout: activity
permalink: /Activities/TinFoilPiano
title: "CS170: Programming for the World Around Us - Tin Foil Piano with the micro:bit"


info:
  teacher_highlights:
    - "Teachers can set up a MakeCode Classroom environment by activating this <a href=\"../files/activity-tinfoilpiano/tinfoilpiano-20220705-0334-microbit-classroom-resume-activity.html\">template</a>."
  goals: 
    - To use loops to create repetition in a program
    - To implement code in functions for easy reuse
    - To use the micro:bit pin interface to read sensor data from the environment
  models:
    - title: "Tin Foil Piano using the micro:bit"
      model: |
        <!-- https://uicookies.com/css-blockquote/ and https://codepen.io/jonitrythall/pen/XbENPM-->
        <blockquote style="margin: 3.7em auto; padding: 2em; background: linear-gradient(white, white) padding-box, url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/80625/sea.jpg) border-box  0 / cover; border: 2em solid transparent; box-shadow: 5px 3px 30px black; font-size: 1.4em; font-style: italic; line-height: 1.5; width: 40%;">There's nothing remarkable about (the piano).  All one has to do is hit the right keys at the right time and the instrument plays itself.
        <footer style="padding-top: 1.3em;">&mdash;
          <cite style="font-style: normal; font-size: 1.2em; font-weight: bold;">
              Johann Sebastian Bach
          </cite>
        </footer>
        </blockquote>
        <br>
        <img src="../files/activity-tinfoilpiano/pinout.png" alt="Pinout for the micro:bit to use headphones and allegator clips to tin foil pads">
      questions: 
        - "The micro:bit comes with 5 pins: P0, P1, P2, a 3-Volt connection, and an electrical ground.  We can measure the current on P0, P1, and P2, related to the voltage difference between the pin and ground.  With alligator clips, connect two pieces of tin foil to ground and P1."
        - You can hook up headphones if you like, but the micro:bit v2 has speakers built in!
        - When the P1 pin is pressed (that is, when you touch the P1 tin foil while touching the ground tin foil), play a sound.
        - "<strong>Be very careful never to connect the 3V pad to ground.  Only connect the P0, P1, and P2 pads to ground!</strong>"
    - title: "Changing the Sound"
      model: |
        <span>\(pitch = base \times (2^{\frac{1}{12}})^{step} = base \times 1.05946309436^{step}\)</span>
      questions: 
        - A note's pitch is determined by its frequency.  Each successive note can be calculated as a &quot;half step&quot; above or below a base frequency.  The formula is given above.  Using a calculator, what is the frequency of the note right above Middle C (which is 262 Hz), and the note right below Middle C?
        - "What note do these two frequencies correspond to?  Use <a href=\"https://pages.mtu.edu/~suits/notefreqs.html\">this table</a> to look up a note by its frequency."
        - "Using the <a href=\"https://www.onlinemictest.com/tuners/pitch-detector/\">online pitch detector</a>, sing &quot;do-re-me&quot; into the computer.  If you're not in the mood for singing, you can use this <a href=\"https://www.musicca.com/piano\">online piano player</a> instead.  What notes do you hear?  What frequencies are they?  Do higher frequencies correspond to higher pitched sounds or lower pitched sounds?"
        - Create a variable called <code>frequency</code>, and on start, set it to some note (like Middle C, or Concert A, which is 440 Hz).  Play that note when P1 is pressed.
        - Create another variable called step that increments by 1 when you press B, and decrements by 1 when you press A.  Then, calculate frequency using the formula above.
        - Modify this program to use a loop to play a crescendo of 10 notes when the A+B button is pressed, by setting <code>step</code> to <code>step + 1</code>, calling calculateFrequencies, and playing the resulting tone.
        - Modify this program to play a second (different) note when P2 is pressed.  You'll need a new variable to keep track of the frequency and step.
        - "Modify the program to allow the user to do something to change the beat (like shaking the microbit).  Start with one-eighth beat, and keep adding one-eighth until the beat reaches 2; then go back to one-eighth.  Hint: you can use an <code>if</code> statement to &quot;wrap around&quot; the value if it is 2, and add one-eighth to it otherwise (this is called an <code>else</code> statement)!"
        
tags:
  - microbit
  - loops
  - pins
  - functions
  
---


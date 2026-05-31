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



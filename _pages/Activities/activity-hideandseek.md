---
layout: activity
permalink: /Activities/HideAndSeek
title: "CS170: Programming for the World Around Us - Hide and Seek with the micro:bit"


info:
  teacher_highlights:
    - "Teachers can set up a MakeCode Classroom environment by activating this <a href=\"../files/activity-hideandseek/hideandseek-20220705-0243-microbit-classroom-resume-activity.html\">template</a>."
  goals: 
    - To use the radio interface of the micro:bit
    - To design a workflow and algorithm to play Hide and Seek with two micro:bit devices
    - To implement an algorithm using the micro:bit block language
    - To create button events using the micro:bit
    - To use <code>if</code> statements to make decisions in a program
  models:
    - title: "Hide and Seek using the micro:bit"
      model: |
        <!-- https://uicookies.com/css-blockquote/ and https://codepen.io/jonitrythall/pen/XbENPM-->
        <blockquote style="margin: 3.7em auto; padding: 2em; background: linear-gradient(white, white) padding-box, url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/80625/sea.jpg) border-box  0 / cover; border: 2em solid transparent; box-shadow: 5px 3px 30px black; font-size: 1.4em; font-style: italic; line-height: 1.5; width: 40%;">But I still haven't found what I'm looking for.
        <footer style="padding-top: 1.3em;">&mdash;
          <cite style="font-style: normal; font-size: 1.2em; font-weight: bold;">
              U2
          </cite>
        </footer>
        </blockquote>
      questions: 
        - How do you think Tiles or Apple AirTag devices might work?
        - What equipment do you think these devices require?
        - "What features of the micro:bit might help us locate our item?  As a hint, think of the game <a href=\"https://en.wikipedia.org/wiki/Marco_Polo_(game)\">Marco Polo</a>."
        - Develop a flowchart for the Marco Polo or Hide-and-Seek game (who says what, and who does what).  For this flowchart, let's decide if we're getting &quot;warmer&quot; or &quot;colder&quot; at each step.
    - title: "Designing an Algorithm with a Flowchart and Implementing the Algorithm"
      model: |
        <img src="../files/activity-hideandseek/flowchart.png" alt="An algorithm flowchart for the Hide-and-Seek game">
      questions: 
        - What is unique about the diamond shapes on this flowchart?
        - Using MakeCode, represent the strength of the radio signal as a variable.
        - Each time you receive a radio message, copy the current signal strength to a new variable that represents the previous signal strength, so that we can compare the two to see if the current one is stronger (larger) or weaker (smaller).  We’ll do this every time we receive a radio message (“on radio received”)
        - When should you update the “previous signal strength” variable, and to what should we set it?
        - What should we do if the signal is stronger or weaker?
    - title: "Enhancing the Program"
      model: |
        <a title="Berrely, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Apple_AirTag.svg"><img width="512" alt="Apple AirTag" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Apple_AirTag.svg"></a>
      questions: 
        - When should we send a radio signal (i.e., &quot;Marco!&quot;)
        - Should we do this over and over again, or pause in between?  Why or why not?
        - Which two devices are playing the Hide-and-Seek game here?  How can we modify the program to allow each pair to communicate with one another without interfering with the others?
        - Modify the program to set <code>radioNumber</code> to <code>radioNumber + 1 mod 30</code> and display the <code>radioNumber</code> variable value each time the B button is pressed.
        - Why was it important to check if <code>receivedNumber = radioNumber</code> when a message was received?  Why was it helpful to send the <code>radioNumber</code> as the message?
        - "Why did we initially set the RSSI variables to -100 on start?  What would happen if we set these variables to 0 instead, or to something else?"
        - Modify the program to display the current signal strength value when the A+B buttons are pressed together (at the same time).
        - How might you display the hot-and-cold result as a numeric value in feet or meters, rather than a generic &quot;warmer&quot; or &quot;colder&quot;?  How might we figure out the best way to convert the RSSI signal value to a distance?
        
tags:
  - microbit
  - radio
  - conditionals
  
---


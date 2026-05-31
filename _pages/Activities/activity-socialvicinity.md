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


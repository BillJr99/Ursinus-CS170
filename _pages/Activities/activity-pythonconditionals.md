---
layout: activity
permalink: /Activities/PythonConditionals
title: "CS170: Programming for the World Around Us - Conditionals in Python"


info:
  goals: 
    - To be able to write an <code>if</code> statement
    - To be able to write an <code>else</code> statement
    - To design boolean expressions for conditionals
    - To combine the <code>if</code> and <code>else</code> blocks to form conditionals that utilize the <code>else if</code> construct
    - To implement complex conditional statements using boolean expression operators
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        age = 38
        
        if age >= 35:
            print("You are old enough to run for President of the United States!")
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code> Statements
      questions:
        - Try running the above program for different ages (say, 18, 34, 35, and 36).
        - "What is the purpose of the indented text below the <code>if</code> line?  What would happen if you removed that indentation, or added another print statement below that was not indented?"
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        age = 38
        
        if age >= 35:
            print("You are old enough to run for President of the United States!")
        else:
            print("You're too young to run for President.")
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code>/<code>else</code> Statements        
      questions:
        - Write and execute an <code>if</code>/<code>else</code> statement that determines if it is warm and not raining outside, and prints out whether or not it is appropriate to go outside.
    - model: |
        <div>
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        age = 38
        
        if age >= 18:
            print("You are old enough to vote!")
            
            if age >= 35:
                print("... and you are old enough to run for President!")
            else:
                print("... but not old enough to run for President!")
        else:
            print("You're too young to run for President, and too young to vote.")
        ]]></script>    
        </div>
        <br>
        <div>
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        age = 21
            
        if age >= 35:
            print("You are old enough to run for President of the United States!")
        elif age >= 18:
            print("You can’t run for President, but you are old enough to vote!")
        else:
            print("You’re too young to run for President, and too young to vote.")
        ]]></script>  
        </div>
      title: Creating a Waterfall of Possibilities by combining <code>else</code> and <code>if</code>
      questions:
        - Which code structure above do you prefer and why?
        - "What does it mean to put an <code>if</code> statement inside of the body of another <code>if</code> statement?  Give a scenario in which each line of code will execute, and a scenario in which it will not."
        - "Can you switch the order of the <code>if</code> statements in either example?  Why or why not?"
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        age = 25
        
        if age >= 18 and age < 35: # Why < 35 and not <= 35?
            print("???") # What should we say here?
        ]]></script>      
      title: "Compound <code>if</code> conditionals"
      questions: 
        - What text should go into the <code>print</code> statement to indicate whether the person can vote (at least age 18) but also is too young to run for president (at least age 35)?
        - "Can you switch the order of the checks inside the <code>if</code> statement?  Why or why not?"
        - "Consider the letter grade breakdown table on our <a href=\"../#grading\">course syllabus</a>.  Write a series of compound <code>if</code> statements that determines if your grade is an A+, an A, or an A-."
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        print("You are in a forest. You see two paths.")
        choice = input("Do you go left or right? ")

        if choice == "left":
            print("You encounter a friendly squirrel.")
        elif choice == "right":
            print("You find a treasure chest!")
        else:
            print("You stand still, unsure of what to do.")
        ]]></script>           
      title: "Try It Out!"
      questions:
        - "What does the <code>==</code> operator do?  Why do you think it is different from a single <code>=</code> sign?"
        - "With a partner, write a short program that either tells an interactive story or treasure hunt, asks a user to guess a secret number (and tells them if they are correct), plays rock-paper-scizzors, plays a question and answer quiz game, or tells you whether you should turn on the heater or air conditioner.  Be prepared to share this with the class!"      
    - model: |
        <a title="P. Kemp, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:If-Then-Else-diagram.svg"><img width="256" alt="If-Then-Else-diagram" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/If-Then-Else-diagram.svg/256px-If-Then-Else-diagram.svg.png"></a>
      title: "Using Flow Charts to Observe Conditional Program Flow"
      questions:
        - "Draw a flowchart diagram that illustrates the control flow of your Venn Diagram program."
        - "Draw a flowchart of a conditional that checks if your grade is within range for each letter grade in the class."        
    - model: |
        <img src="../images/venn3.png" alt="Empty 3-way Venn Diagram">
      title: "Putting It All Together: Implementing a Venn Diagram"
      questions:
        - "Make up a 3-way <a href=\"https://en.wikipedia.org/wiki/Venn_diagram\">Venn Diagram</a> of your choosing; you can look one up on the Internet if you wish."
        - "Label the three large circles \"A\", \"B\", and \"C\".  In each of the 7 regions within the Venn Diagram, which elements are true and which are false?"
        - "Write a series of <code>if</code> statements that may use <code>else</code> and <code>else if</code> blocks that print out the different states of your Venn Diagram.  There are a few ways to go about this, so we will discuss and compare approaches as a class."  
    - model: |
        <a title="P. Kemp, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:If-Then-Else-diagram.svg"><img width="256" alt="If-Then-Else-diagram" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/If-Then-Else-diagram.svg/256px-If-Then-Else-diagram.svg.png"></a>
      title: "Using Flow Charts to Observe Conditional Program Flow"
      questions:
        - "Draw a flowchart diagram that illustrates the control flow of your Venn Diagram program."
        - "Draw a flowchart of a conditional that checks if your grade is within range for each letter grade in the class."        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/conditional/toctree.html
      title: Conditional Execution
      
tags:
  - conditionals
  - python
  
---


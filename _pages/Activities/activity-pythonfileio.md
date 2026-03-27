---
layout: activity
permalink: /Activities/PythonFileIO
title: "CS170: Programming for the World Around Us - File I/O with Python"


info:
  goals: 
    - To read and write files with Python
  models:
    - title: "File I/O in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        file = open("input.txt", "r")
        lines = file.readlines()
        
        for line in lines:
            print(line)
        ]]></script>  
      questions: 
        - "Create a file called <code>input.txt</code> and run this program.  What does it do?"
        - "Modify this program to count the number of words in each line, and print that to the screen."
    - title: "Writing Files in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        file = open("input.txt", "w")
        file.write("High Score: 100")
        file.close()
        ]]></script>  
      questions: 
        - "Run this program, then write a program to read this file, read the line, split it on the <code>:</code> character, and print the high score value (just the 100)."        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/files/toctree.html
      title: Files
      
tags:
  - python
  - io
  
---


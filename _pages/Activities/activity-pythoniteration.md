---
layout: activity
permalink: /Activities/PythonIteration
title: "CS170: Programming for the World Around Us - Iteration with Python"


info:
  goals: 
    - To be able to explain the uses of the <code>while</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>while</code> loop    
    - To be able to explain the uses of the <code>for</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>for</code> loop    
  models:
    - model: |
        Conditionals can be used to repeatedly execute code.  There are two varieties of these &quot;loops:&quot; the for loop (which is useful when counting the number of iterations that are needed), and the while loop (which is useful for executing until something is true).
        <br>    
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        import random
        
        def checkIfRaining():
            return True
        
        raining = False;

        while not raining:
            randVal = random.random() # 0 to 1
            minutes = round(randVal * 20) # whole numbers 0 to 20

            print("Play outside for {} minutes!".format(minutes))

            raining = checkIfRaining() # made up function!
        ]]></script>        
      title: The <code>while</code> Loop
      questions:
        - Modify this code to implement a <code>checkIfRaining()</code> function that generates a random number between 1 and 10, and returns <code>true</code> if the number is greater than 7 (and return <code>false</code> otherwise).
        - "Modify this program to ensure that the number of minutes is never 0 (make it at least 1)."
        - "Write a program to ask the user for their age, but keep asking until they enter a positive number."       
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        i = 0
        while i < 10:
            print(i)
            i += 1
        ]]></script>    
      title: The <code>for</code> Loop
      questions:
        - The code prints the numbers from 0 through 9.  Why doesn’t it also print the value 10?
        - What could you do to change this to print the values 0 through 10?  
        - What could you do to print the values 1 through 10?
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        i = 0
        j = 0
        
        while i < 10:
            print("Team {}".format(i))
            
            while j < 10:
                print("Team {}, turn #{}".format(i, j))
                
                j += 1
                
            i += 1
        ]]></script>     
      title: Nested Loops
      questions:
        - How many times does the inner loop print statement execute?
        - How many times does the outer loop print statement execute?
        - How many times does the first print statement execute, and why?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        heads = 0
        
        for i in range(10):
            randomNumber = random.random() # 0 to 1
            
            if randomNumber > 0.5:
                heads += 1
                
            print(heads)
        ]]></script>     
      title: Flipping a Coin
      questions:
        - "What does <code>range(10)</code> do?  Try printing <code>range(10)</code> to the screen; how does it work?"
        - "Rewrite this program to use a <code>for</code> loop instead."
        - "Modify this program to only print the number of heads once after the loop has finished."
        - How many times would you expect to land on heads?
        - What would you change to flip the coin 100 times?  How many heads would you expect then?
        - What would be the effect of changing the constant in the program from 0.5 to 0.3?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        str = "The quick brown fox"
        for letter in str:
            print(letter)
        ]]></script>     
      title: Iterating over Text Characters
      questions:
        - "What does this program do?"
        - "Modify this program to count the number of vowels in the string, and print out the result."
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/iterations/toctree.html
      title: Iteration
      
tags:
  - python
  - iteration
  
---


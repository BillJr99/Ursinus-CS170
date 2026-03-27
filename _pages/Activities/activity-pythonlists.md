---
layout: activity
permalink: /Activities/PythonLists
title: "CS170: Programming for the World Around Us - Lists with Python"


info:
  goals: 
    - To design and implement algorithms using lists
    - To be able to explain that a list is an ordered collection of data
    - To be able to create a list and assign its elements
    - To be able to access an element from a list by its index
    - To explain that strings are lists of characters, and to manipulate them accordingly
    - To be able to iterate over a list
    - To create an manipulate multidimensional lists
  models:
    - title: "Lists in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        grades = []
        
        for i in range(10):
            grades.append(90 + i)
            
        for i in range(len(grades)):
            print(grades[i])
        ]]></script>  
      questions: 
        - "Comment each line of this program.  What do you think it does?  Try running it."
        - What is the size of the <code>grades</code> list?
        - What are the indices of the <code>grades</code> list?        
        - "How would you modify the program above to play a game of &quot;Duck-Duck-Goose&quot; -- that is, iterating through the array until a certain value is reached (say, <code>92</code>), and printing that index where it is found?"
    - title: "Comparing Lists in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [1, 2, 3, 4, 5]        
        ]]></script>  
      questions: 
        - "Write a loop to check if these two lists are the same (that is, have the same size and contain the same values)."
        - "What do you think <code>del list1[5]</code> does?  Try it and then see if your lists are the same!"
        - "Comment out the <code>del</code> line, and try <code>list2.insert(4, 6)</code> instead."
        - "What does <code>list1.extend(list2)</code> do?  Print it out and see."
    - title: "2D Lists in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        schedule = [
            ["9 AM", "ECON101"],
            ["10 AM", "CS173"]
        ]
        ]]></script>  
      questions: 
        - "Write a program to print your daily schedule."
        - "Modify this program to add a third dimension to the list representing each day of the week."
    - title: "Strings in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        str = "The quick brown fox jumped over the lazy dog."
        words = str.split(" ")
        for word in words:
            print("{} has length {}".format(word, len(word))
        ]]></script>  
      questions: 
        - "What does this program do when you run it?"
        - "What are strings in Python?"        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/lists/toctree.html
      title: Lists
    - link: https://runestone.academy/ns/books/published/py4e-int/strings/toctree.html
      title: Strings
      
tags:
  - python
  - list
  
---


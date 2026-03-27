---
layout: activity
permalink: /Activities/PythonNumbersText
title: "CS170: Programming for the World Around Us - Representing Numbers and Text with Python"


info:
  goals: 
    - To explore numeric operators and variables in Python
    - To obtain user input in a Python program
  models:
    - title: "Numeric Operations"
      model: |
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;}
        .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
          overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
          font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
        .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
        </style>
        <table class="tg">
        <thead>
          <tr>
            <th class="tg-fymr">Operator</th>
            <th class="tg-fymr">Meaning</th>
            <th class="tg-fymr">Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="tg-0pky"><span style="font-weight:bold">+</span></td>
            <td class="tg-0pky">Addition</td>
            <td class="tg-0pky">z = x + 5</td>
          </tr>
          <tr>
            <td class="tg-fymr">-</td>
            <td class="tg-0pky">Subtraction</td>
            <td class="tg-0pky">z = a - b</td>
          </tr>
          <tr>
            <td class="tg-fymr">*</td>
            <td class="tg-0pky">Multiplication</td>
            <td class="tg-0pky">slices = pizzas * 8</td>
          </tr>
          <tr>
            <td class="tg-fymr">/</td>
            <td class="tg-0pky">Division</td>
            <td class="tg-0pky">average = people / teams</td>
          </tr>
          <tr>
            <td class="tg-fymr">**</td>
            <td class="tg-0pky">Exponentiation</td>
            <td class="tg-0pky">radius_squared = r ** 2</td>
          </tr>
          <tr>
            <td class="tg-fymr">%</td>
            <td class="tg-0pky">Modulus (remainder)</td>
            <td class="tg-0pky">remainder = 8 % 3</td>
          </tr>
        </tbody>
        </table>
      questions: 
        - "What is an expression for the number of semesters one attends class, assuming a 4-year college degree program?"  
        - "What is an expression to compute the total cost of items purchased at a store with 6 percent state sales tax?"
    - title: "A First Python Program"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        print("Hi, I'm Python!")
        name = input("What's your name?")
        print("Nice to meet you, " + name + "!")
        ]]></script>  
      questions: 
        - "Create a project in Python, paste and run this code."
        - "Modify the program to ask for your major and where you're from, and print that." 
        - "The <code>x = int(x)</code> function converts the variable <code>x</code> from text to a whole number.  Ask for the year you'll graduate, convert it to a number, and subtract the current year from it.  Print that value to show how many years it will be until you graduate."
        - "Write a program to ask the user to input their street address, city, state, and zip code, and print out their address like one would on an mailing envelope."
        - "Print the total cost after tax from the prior example using this print statement: <code>print(&quot;${0:,.2f}&quot;.format(totalcost))</code>.  What do you think <code>{0:,.2f}</code> means?  As a hint, try purchasing over $1000 worth of items in your formula!"
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/variables/toctree.html
      title: "Variables, Expressions, and Statements"
      
tags:
  - python
  - variables
  - input
  - text
  - expressions
---


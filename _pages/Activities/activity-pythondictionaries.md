---
layout: activity
permalink: /Activities/PythonDictionaries
title: "CS170: Programming for the World Around Us - Dictionaries with Python"


info:
  goals: 
    - To associate data using the Python dictionary
  models:
    - model: |
       <a title="Larousse / Public domain" href="https://commons.wikimedia.org/wiki/File:Nouveau_Dictionnaire_Larousse_page.JPG"><img width="512" alt="Nouveau Dictionnaire Larousse page" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Nouveau_Dictionnaire_Larousse_page.JPG"></a> 
       <br>
       <a title="© 2010 by Tomasz Sienicki [user: tsca, mail: tomasz.sienicki at gmail.com] / CC BY (https://creativecommons.org/licenses/by/3.0)" href="https://commons.wikimedia.org/wiki/File:Telefonbog_ubt-1.JPG"><img width="512" alt="Telefonbog ubt-1" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Telefonbog_ubt-1.JPG"></a>
      title: "Data Maps"
      questions:
        - "Consider the dictionary and phone book above.  When you look something up in each of them, what are you looking up, and what are you looking <strong>for</strong>?  What are the data types?"
        - What are some ways that we make these lookups easier?  How are the data organized, and what part of the data is organized that way?  
        - A phone book maps ______ to ______, and a dictionary maps ______ to ______.
        - In computing, we tend to say that we map keys to values.  For the phone book and dictionary, what is the key, and what is the value?  
    - title: "Dictionaries in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[   
        courses = {}
        
        courses["CS170"] = "Prof. Mongan"
        courses["CS174"] = "Prof. Tralie"
        courses["CS274"] = "Prof. Schilling"
        
        print("CS170 is taught by: {}".format(courses["CS170"]))
        
        for key, value in courses.items():
            print("{} is taught by: {}".format(key, value))
        ]]></script>  
      questions: 
        - What would you change in the program above to store the number of students enrolled in each course, instead of the instructor of each course?
        - "Suppose you are developing a web browser that accesses web pages.  You want to <strong>cache</strong> the pages, so that you only access them once, to save on I/O, network calls, and your data plan.  How might a <code>HashMap</code> help you to do this?  What would be the key and the value?"
    - title: "Complex Dictionaries in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[   
        courses = {}
        
        courses["CS170"] = {}
        courses["CS170"]["instructor"] = "Prof. Mongan"
        courses["CS170"]["enrollment"] = 15
        courses["CS170"]["students"] = []
        courses["CS170"]["students"].append("Alex")
        courses["CS170"]["students"].append("Lee")
        ]]></script>  
      questions: 
        - "Add a few more courses to this dictionary."
        - "Write a program to print the instructor, the enrollment, and all the students in all classes."
        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/dictionaries/toctree.html
      title: Dictionaries
      
tags:
  - python
  - dictionary
  
---


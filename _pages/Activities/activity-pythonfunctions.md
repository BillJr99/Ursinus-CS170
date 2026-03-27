---
layout: activity
permalink: /Activities/PythonFunctions
title: "CS170: Programming for the World Around Us - Functions with Python"


info:
  goals: 
    - To be able to call methods in various configurations (parameters, return values)
    - To use functions with return values
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        import math
        
        # Return the area of a circle, given its radius
        # param radius: the radius of the circle
        # Precondition: radius >= 0
        # return: the area of the circle in square units of the radius  
        def circleArea(radius):
            area = math.pi * (radius ** 2)
            return area
            
        def triangleArea(base, height):       
            area = (base * height) / 2
            return area
            
        def main():
            r = 10
            area = circleArea(r)
            print("The area of the circle is {0:.,2f}".format(area))
            
        if __name__ == "__main__":
            main()
        ]]></script>     
      title: Writing and Invoking Functions to Re-Use Code Logic
      questions:
        - Try running the sample program above.
        - What does <code>return</code> mean in the <code>circleArea</code> function above?
        - Notice that functions have data types before their function names, just like variables do.  What is the return type of <code>circleArea()</code>?
        - Modify the program to write an additional function circleDiameter() that computes the diameter (<span>\(2 \times \pi \times r\)</span>) given the radius of the circle.  Call that function from main() and print the value.
        - Modify the program to write and call <code>triangleArea()</code> from <code>main()</code> and then print the area of a triangle whose dimensions you choose.
        - "Write an if statement to tell if room temperature is between 70 and 74 degrees (you can print out a message saying whether or not it is in this range).  Then, migrate this to a function that accepts the temperature as a parameter, and call this function at least twice from <code>main()</code>.  Next, add a second parameter to this function to represent the humidity, and display a separate message indicating whether it is within a range of 30 and 50 percent.  Finally, modify your function to return a <code>boolean</code> if both conditions are met.  How might you use this logic to control a thermostat device?"   
        - "Write comments for the <code>triangleArea()</code> function similar to the <code>circleArea</code> function." 
  reflective_prompts:
    - Notice the comments above the <code>circleArea</code> function.  What do you think a precondition means?
    - Write comments for the <code>triangleArea</code> function in a similar spirit to those of the <code>circleArea</code> function.        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/functions/toctree.html
      title: Functions
      
tags:
  - python
  - functions
  
---


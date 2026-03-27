---
layout: assignment
permalink: /Labs/UnitTesting
title: "CS170: Programming for the World Around Us - Unit Testing"


info:
  coursenum: CS170
  points: 100
  goals:
    - To implement an arithmetic expression into executable code
    - To map variables to expression parameters
    - To identify and implement appropriate unit test cases
  rubric:
    - weight: 40
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 20
      description: Test Cases
      preemerging: Testing was performed outside of the unit test framework, or not performed at all
      beginning: Trivial test cases are provided in a unit test framework
      progressing: Test cases that cover some, but not all, boundary cases and branches of the program are provided
      proficient: Test cases that cover all boundary cases and branches of the program are provided
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  questions:
    - "On paper, how much financial aid would a household receive if their income is $35,000 with one child?  What questions did you have to ask to determine which rule to apply, and how did you compute the amount once you had the correct rule?"      

tags:
  - testing
  - conditionals
  
---

## Warm-Up: Unit Testing Tutorial
Create a project and a new text file called `gpa.py`.  Paste the following code into it:

```python
# These are not guaranteed to be official, just an example!
def get_grade(gpa):
    result = "F"

    if gpa >= 4.0:
        result = "A+"
    elif gpa >= 3.67:
        result = "A"
    elif gpa >= 3.33:
        result = "A-"
    elif gpa >= 3:
        result = "B+"
    elif gpa >= 2.67:
        result = "B"
    elif gpa >= 2.33:
        reuslt = "B-"
    elif gpa > 2:
        result = "C+"
    elif gpa >= 1.67:
        result = "C"
    elif gpa >= 1.33:
        result = "C-"
    elif gpa >= 1:
        result = "D+"
    elif gpa >= 0.67:
        result = "D"
    else:
        result = "F"

    return result

def main():
    gpanum = input("Enter GPA:")
    gpanum = float(gpanum)

    grade = get_grade(gpanum)
    print(grade)

if __name__ == "__main__":
    main()
```

We will test this file.  Create a second file called `test_gpa.py` and paste the following code:

```python
import unittest   
import gpa

class Test_GPA(unittest.TestCase):
    def test_get_grade_BPlus(self):
        testvalue = 3.25
        result = gpa.get_grade(testvalue)
        expected = "B+"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```

This test imports our original `gpa` file so that it can call the `get_grade` function.  Then, it defines a function `test_get_grade_BPlus` that provides a GPA (3.25), calls the function to get the result, and compares that result to the expected answer (a B+).  `assertEqual` causes the program to fail the test if the two parameters are not equal to each other (that is, the result we got and the answer we expect).

### Running the Test File
These tests are called **unit tests** because they are testing individual units of the program (that is, functions).  To use these, click on the Testing button in the left menu pane, and click `Configure Python Tests`.  In the menu at the top, choose the `unittest` library, then the root directory, and tell the unit tester that you will name your test files with `test_*` file names (as we have done with `test_gpa.py` above!).

To test this file, you can either click the `Run` button with this test file open, or click the run button next to the name of the test in the margin, or click the play button next to the test in the testing pane.  You should see that your test passed!  Try changing the gpa input from 3.25 to 2.0 and test that; you'll see that it presents a red failure icon instead!

**What other test cases would you need to write to fully test this program?  In other words, what inputs do you need to try?  Write one more test case and run it.**

## What to Do
In this lab \[[^1]\], you will practice with `if` statements and `if`/`else` statements, as well as with unit tests with JUnit. It will also serve as practice writing and calling functions (also known as "methods").

A non-governmental organization got a large donation to help families in need, but they have so many families to help that they need a program to help automate calculating the amount of financial assistance for each family. The amount of aid depends both on the annual household income and the number of children in the family. The rules are as follows:

* If the annual household income is greater than $40,000, then no aid is provided.
* If the annual household income is between $30,000 (inclusive) and $40,000 (inclusive), then apply the following rules:
    * If the household has three or more children, provide $1,000 per child.
    * If the household has two or fewer children, provide $500 per child.
* If the annual household income is from $20,000 (inclusive) to $30,000 (not inclusive), then apply the following rules:
    * If the household has at least two children, then provide $1,500 per child.
    * If the household has only one child (don't forget to use `==` for this!), then provide $2,000 total.
    * If the household has no children, then no aid is provided.
* If the annual household income is less than $20,000, then provide $2,100 per child.

**Hint**: remember that numeric values in Python do not include the commas; these are only there for your reading convenience!  Also, make sure you don't return a negative value for aid if someone mistakenly reports a negative number of children (how can you check for this, and what should you calculate as the aid amount instead?)!

### Part 1: Soliciting User Input (15% of the Implementation Grade)

Create a new project as usual.  Call your initial python file `FinancialAid.py`.  

In `main()`, complete an input prompt asking the user to input an integer representing the number of kids who need assistance (this is by far the quicker part) using the `input` function.  

You can create a `main` function as follows:

```python
def main():
   # your code here
   
# call main when you click run or load this file
if __name__ == "__main__":
    main()
```

You will pass these values to a `computeAssitance` function that you will create, and then print the resulting financial assistance returned by `computeAssistance` in `main`.  

### Part 2: Financial Assistance Calculator (85% of the Implementation Grade)

Create a method `computeAssistance(income, numKids)`.  Fill in the method that computes the proper amount of assistance, following the rules above, and return the variable that contains the amount of financial aid assistance.

Do not print anything in this function!  I suggest calculating the value of `assistanceAmount` in each `if` statement, and then you can use one single `return` statement at the bottom of the function to return that value.  See this example for the general layout.  You can print the result in your `main` function instead, and that way, you only have to write one print statement for the whole program.

```python
# Compute the amount of financial assistance given to a family, 
# given their income and number of children.
# income: The annual family income
# numKids: The number of children in the family
# return: The amount of financial assistance in dollars and cents (a double)
def computeAssistance(income, numKids):
    assistanceAmount = 0.0 # We'll start with $0 assistance as a placeholder value
    
    # Your code goes here; update assistanceAmount to the correct value according to the rules above
    # You can just update assistanceAmount inside the if statements, since we declared it at the top of this function.
    
    return assistanceAmount
```

#### Hints

It is possible to do this assignment with a single stream of `if`/`else` blocks that use boolean expressions, but you may instead want to do it with nested if statements in some of them (it's your choice). Recall that a nested if statement is a statement such as the following:

```python
if a > b:
    # Outer block
    if c > d:
        # Inner block 1
    else:
        # Inner block 2
else:
    # Inner block 3
```

In this example, we don't even check `c > d` unless `a > b` passes. Just for contrast, the way to get to inner block 1 without nested if statements is with a boolean expression:

```python
if a > b and c > d:
    #Inner block 1
elif a > b:
   # Inner block 2
else:
   # Inner block 3
```

### Part 3: Unit Tests

Coming up with proper test cases is an important part of software engineering that, when done properly, saves everyone a huge headache. Good software testing frameworks allow the programmer to write a whole battery of tests that get applied every time the code is changed so that they don't have to manually input all of the tests every time.  

**Before you begin, list the tests you'll need to write, and incldue this list in your README.  Specifically, which unit tests are needed to test all rules, including boundary cases and potential error values like a negative number of children or income?**

#### Creating Unit Tests

Create a unit test class with functions to test your program.  Name this file `test_aid.py`, and you can populate it initially with this code:

```python
import unittest
import FinancialAid

class Test_Aid(unittest.TestCase):
  def test_aid_1(self):
    testincome = 40000
    testkids = 1
    expected = 0 # the expected answer goes here
    
    result = FinancialAid.computeAssistance(testincome, testkids)
    
    self.assertEqual(result, expected)
    
if __name__ == "__main__":
  unittest.main()
```

To create additional tests, copy the `test_aid_1` function, give it a new name (like `test_aid_2`), and set the `testincome`, `testkids`, and `expected` variables to known values.  You should have one test for each of the bulleted rules above!

#### Running Unit Tests

To run these tests, click the `Testing` toolbar menu icon on the left side of your screen.  Click `Configure Tests`.  Choose the `unittest` option, the `root directory (.)` option, and the `test_*` option: this tells Visual Studio to use the correct unit testing framework library, and what file(s) contain your test cases.

On the left side of your screen, you should see your unit test file.  There is a little run button near the top of this pane: click this and it will run your tests and report any differences in the result.  If your tests fail, you'll be able to see what values your function actually returned for those tests, and adjust your code accordingly.  Re-run your tests until they pass!

To get full credit for this part of the assignment, **you must create enough unit tests so that every block of code you write is covered by at least one test**. In other words, every `if` and `else` statement should be tested by at least one of your test cases, so create a test function with sample values that exercise every part of your code.  

If there is a `testMain` test, you can remove that.  It is only necessary to test the `computeAssistance` function, since `main` just obtains user input and then passes them to the `computeAssistance` function.  So these tests automatically run your function for you without asking for input!  That is why we added the `if __name__ == "__main__"` and `def main()` function code snippets to your code earlier: this makes sure that the unit test framework doesn't run this code and ask you to input income and children values manually!

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## References
[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie) and [Prof. Ann Marie Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)

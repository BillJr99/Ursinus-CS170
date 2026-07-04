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
        <a title="P. Kemp, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:If-Then-Else-diagram.svg"><img width="256" alt="If-Then-Else-diagram" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/If-Then-Else-diagram.svg"></a>
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
        <a title="P. Kemp, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:If-Then-Else-diagram.svg"><img width="256" alt="If-Then-Else-diagram" src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/If-Then-Else-diagram.svg"></a>
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

## Notes and Walkthrough

### Programs That Make Decisions
Every program we've written so far runs the same lines, in the same order, every single time.  But think about your own day: *if* it's raining, you grab an umbrella; *otherwise*, you don't.  Real decisions depend on conditions!  A **conditional** is a statement that lets a program choose whether to run some code based on a question with a yes-or-no answer.  Each possible path the program can take is called a **branch** — just like a fork in a hiking trail.

### Boolean Expressions: Questions with Yes/No Answers
Before we can branch, we need a way to ask a question.  A **boolean expression** is an expression whose value is either `True` or `False` — those two values are called **booleans** (named after the mathematician George Boole).  We build boolean expressions with **comparison operators**:

| Operator | Question it asks | Example | Value |
|----------|------------------|---------|-------|
| `==` | Are these equal? | `5 == 5` | `True` |
| `!=` | Are these different? | `5 != 5` | `False` |
| `<`  | Is the left smaller? | `3 < 7` | `True` |
| `>`  | Is the left bigger? | `3 > 7` | `False` |
| `<=` | Smaller or equal? | `18 <= 18` | `True` |
| `>=` | Bigger or equal? | `34 >= 35` | `False` |

Notice that *checking* equality uses **two** equals signs (`==`), while *assignment* (storing a value) uses one (`=`).  This is probably the number one typo in all of programming, so keep an eye out!  You can print a boolean expression just like anything else:

```python
age = 21
print(age >= 18)
print(age >= 35)
print(age == 21)
```

This program prints:

```text
True
False
True
```

### The if Statement: Running Code Only Sometimes
An `if` statement takes a boolean expression (called the **condition**) and a block of code, and runs the block *only* when the condition is `True`.  You've seen the presidential-age example in the model above — here it is again with one extra line, which turns out to be an important experiment:

```python
age = 38

if age >= 35:
    print("You are old enough to run for President of the United States!")
print("Thanks for checking!")
```

This program prints:

```text
You are old enough to run for President of the United States!
Thanks for checking!
```

Three things to notice.  First, the condition ends with a colon (`:`) — that's how Python knows the decision-making block is about to begin.  Second, the line "inside" the `if` is **indented** (pushed to the right, by convention four spaces).  In Python, indentation isn't decoration — it's how Python knows *which lines belong to the `if`*.  Third, the last `print` is *not* indented, so it runs no matter what.  What do you think prints if we change `age` to 21?  Only `Thanks for checking!` — the indented line is skipped, but the unindented line still runs.

### else: What to Do Otherwise
Often we want to do one thing when the condition is `True` and something *different* when it's `False`.  That's the job of `else` — it has no condition of its own, because it simply catches everything the `if` didn't:

```python
age = 21

if age >= 35:
    print("You are old enough to run for President of the United States!")
else:
    print("You're too young to run for President.")
```

This program prints:

```text
You're too young to run for President.
```

Exactly one of the two branches runs — never both, and never neither.  Can you think of decisions in your life that work like this?  "If the dining hall has pizza, I'll get pizza; otherwise, I'll make a sandwich."

### elif: A Waterfall of Possibilities
What if there are more than two possibilities?  Our voting example has *three*: old enough to run for President, old enough only to vote, or too young for both.  We could nest an `if` inside another `if` (as in the model), but Python gives us a tidier tool: `elif`, short for "else if."  Python checks each condition from top to bottom and runs the *first* branch whose condition is `True` — then skips all the rest, like water falling past ledges until it lands:

```python
age = int(input("How old are you? "))

if age >= 35:
    print("You are old enough to run for President of the United States!")
elif age >= 18:
    print("You can't run for President, but you are old enough to vote!")
else:
    print("You're too young to run for President, and too young to vote.")
```

This program prints (if the user types `21`):

```text
How old are you? 21
You can't run for President, but you are old enough to vote!
```

Here's a trace showing which branch fires for several different inputs.  Being able to build a table like this in your head is what "reading" a conditional really means:

| Input `age` | `age >= 35`? | `age >= 18`? | Which branch runs | Output |
|-------------|--------------|--------------|-------------------|--------|
| 40 | `True` | (not even checked!) | the `if` branch | You are old enough to run for President... |
| 35 | `True` | (not checked) | the `if` branch | You are old enough to run for President... |
| 21 | `False` | `True` | the `elif` branch | You can't run for President, but you are old enough to vote! |
| 18 | `False` | `True` | the `elif` branch | You can't run for President, but you are old enough to vote! |
| 12 | `False` | `False` | the `else` branch | You're too young to run for President, and too young to vote. |

Notice something subtle: when `age` is 40, Python never even *looks* at the `elif` condition.  Once one branch fires, the whole chain is done.  That's why the *order* of the checks matters — what would go wrong if we checked `age >= 18` first?  (Try it: a 40-year-old would be told they can only vote, because `40 >= 18` is `True` and fires first!)

### Combining Conditions with and, or, and not
Sometimes one comparison isn't enough.  "You can vote but *not* run for President" needs *two* facts to be true at once.  Python gives us three **boolean operators** for combining conditions:

- `and` — `True` only when *both* sides are `True`
- `or` — `True` when *at least one* side is `True`
- `not` — flips `True` to `False` and vice versa

Let's finish the compound conditional from the model, and add a movie-ticket example.  Many theaters give a discount to children *or* seniors:

```python
age = 25

if age >= 18 and age < 35:
    print("You can vote, but you can't run for President yet.")

if age <= 12 or age >= 65:
    print("You get a discounted movie ticket!")
else:
    print("You pay full price. Sorry!")
```

This program prints:

```text
You can vote, but you can't run for President yet.
You pay full price. Sorry!
```

Why is the first condition `age < 35` and not `age <= 35`?  Because a 35-year-old *can* run for President — so 35 should not be part of the "can't run yet" group.  Getting these boundary values right is a big part of writing correct conditionals.  Here's a trace of the ticket conditional for a few ages:

| Input `age` | `age <= 12`? | `age >= 65`? | `or` result | Which branch | Output |
|-------------|--------------|--------------|-------------|--------------|--------|
| 8 | `True` | `False` | `True` | `if` | You get a discounted movie ticket! |
| 25 | `False` | `False` | `False` | `else` | You pay full price. Sorry! |
| 70 | `False` | `True` | `True` | `if` | You get a discounted movie ticket! |

And `not`?  It's great for readability: `if not raining:` reads almost like English.  Recall the model question about going outside — here's one way to write it:

```python
temperature = 72
raining = False

if temperature >= 60 and not raining:
    print("It's a great day to go outside!")
else:
    print("Maybe stay in with some hot chocolate.")
```

This program prints:

```text
It's a great day to go outside!
```

### Nesting: Decisions Inside Decisions
You saw in the model that an `if` can live *inside* another `if` — that's called **nesting**.  The inner question is only ever asked when the outer answer was "yes."  Nesting is perfect when one decision only makes sense after another.  For example, a theme park ride might require you to be tall enough first, and only *then* check whether you want the front row:

```python
height = int(input("How tall are you (in inches)? "))

if height >= 48:
    seat = input("You can ride! Front row or back row? ")
    if seat == "front":
        print("Brave choice! Enjoy the splash zone.")
    else:
        print("Enjoy the ride from the back!")
else:
    print("Sorry, you must be 48 inches tall to ride.")
```

This program prints (if the user types `60` and then `front`):

```text
How tall are you (in inches)? 60
You can ride! Front row or back row? front
Brave choice! Enjoy the splash zone.
```

Notice how the indentation shows the structure: the inner `if`/`else` is indented *twice*, because it lives inside the outer `if`'s block.  Could you rewrite this with `and` instead of nesting?  Sometimes yes — `if height >= 48 and seat == "front"` — but then where would you ask for the seat?  Nesting lets us wait to ask the second question until we know it matters.

### Common mistakes to avoid
- **Using `=` when you mean `==`.**  `if age = 18:` is a syntax error.  One `=` *stores*, two `==` *compares*.
- **Forgetting the colon** at the end of `if`, `elif`, and `else` lines.  Python will point at the line and complain about syntax.
- **Indentation slips.**  Everything that belongs to a branch must be indented the same amount underneath it.  A line you *meant* to be inside the `if` but forgot to indent will run every time!
- **Comparing a string to a number.**  `input()` gives a string, so `if input("Age? ") >= 18:` fails.  Convert first: `age = int(input("Age? "))`.
- **Conditions in the wrong order in an `elif` chain.**  Put the most specific (largest / strictest) checks first — remember the President-vs-voting example above.
- **Boundary mix-ups between `<` and `<=`.**  Ask yourself: should the boundary value itself (18, 35, 65...) take this branch or the other one?
- **Writing `if age >= 18 and <= 34:`** — Python needs a complete comparison on each side of `and`: `if age >= 18 and age <= 34:`.
- **Case-sensitive string comparisons.**  `"Left" == "left"` is `False`!  A common fix is to lowercase the input first: `choice = input("Left or right? ").lower()`.

## Practice Exercises
Try each one yourself before revealing the solution — struggling a little first is where the learning happens!

### Exercise 1 (warm-up)
Ask the user for their age and print `You can vote!` if they are 18 or older.  (Nothing needs to print otherwise — yet.)

Sample run:

```text
How old are you? 19
You can vote!
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
age = int(input("How old are you? "))  # convert the string from input() to a number
if age >= 18:                          # condition: a boolean expression
    print("You can vote!")             # runs only when the condition is True
```

Remember the conversion with `int()` — comparing the raw string from `input()` against a number is an error.

</details>

### Exercise 2 (if/else)
Extend Exercise 1: if the user is younger than 18, tell them how many years until they can vote.

Sample run:

```text
How old are you? 15
You can vote in 3 years!
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
age = int(input("How old are you? "))
if age >= 18:
    print("You can vote!")
else:
    years = 18 - age                  # arithmetic inside a branch is fine!
    print("You can vote in " + str(years) + " years!")
```

Exactly one branch runs.  Note the `str()` when gluing the number into the message.

</details>

### Exercise 3 (elif chain)
Write a movie ticket pricer: age 12 and under pays $6, age 65 and older pays $8, and everyone else pays $12.  Print the price.

Sample runs:

```text
How old are you? 10
Your ticket costs $6
```

```text
How old are you? 30
Your ticket costs $12
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
age = int(input("How old are you? "))
if age <= 12:
    print("Your ticket costs $6")
elif age >= 65:
    print("Your ticket costs $8")
else:
    print("Your ticket costs $12")     # everyone who isn't a child or senior
```

The `else` needs no condition — it catches every age that fell past the first two checks.  Try tracing ages 12, 13, 64, and 65 to confirm the boundaries.

</details>

### Exercise 4 (challenge: combining conditions)
A local pool has these rules: you can swim in the deep end only if you are at least 13 years old **and** have passed the swim test.  Ask the user for their age and whether they passed the test (have them type `yes` or `no`), and print one of: `Deep end is open to you!`, `Shallow end only — take the swim test!` (right age, no test), or `Shallow end only for now.` (too young).

Sample run:

```text
How old are you? 15
Did you pass the swim test (yes/no)? no
Shallow end only — take the swim test!
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
age = int(input("How old are you? "))
passed = input("Did you pass the swim test (yes/no)? ")

if age >= 13 and passed == "yes":     # both must be True
    print("Deep end is open to you!")
elif age >= 13:                       # old enough, so the test must be the problem
    print("Shallow end only — take the swim test!")
else:
    print("Shallow end only for now.")
```

The `elif age >= 13` branch only runs when the first condition failed — so if we got there and the age was fine, the swim test must be what was missing.  We got that fact "for free" from the waterfall!

</details>

### Exercise 5 (extra challenge: grades)
Using the letter grade idea from the model questions: ask for a numeric grade from 0 to 100 and print the letter grade — A for 90 and above, B for 80 to 89, C for 70 to 79, D for 60 to 69, and F below 60.  Then, make sure a grade like `104` or `-3` prints `That's not a valid grade!` instead.  (Hint: check for invalid input *first* — why?)

Sample run:

```text
What is your grade? 87
You earned a B
```

<details>
<summary>Click to reveal a solution to Exercise 5</summary>

```python
grade = int(input("What is your grade? "))

if grade < 0 or grade > 100:          # catch the impossible values first
    print("That's not a valid grade!")
elif grade >= 90:
    print("You earned an A")
elif grade >= 80:                     # we only get here if grade < 90
    print("You earned a B")
elif grade >= 70:
    print("You earned a C")
elif grade >= 60:
    print("You earned a D")
else:
    print("You earned an F")
```

Two key ideas: the invalid check goes first so that `104` doesn't slip into the A branch, and each `elif` doesn't need an upper bound (like `grade < 90`) because the waterfall guarantees earlier conditions already failed.

</details>

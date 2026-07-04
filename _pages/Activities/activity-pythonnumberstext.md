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

## Notes and Walkthrough

### What is a Variable?
Think about your locker at school.  It has a label on it (your name or a number), and it holds something for you until you need it later.  A **variable** works the same way: it's a named place in the computer's memory where we can store a value, look at it later, and even swap it out for something new.  When we write:

```python
pizzas = 3
```

we're telling Python: "make a locker named `pizzas` and put the value 3 inside."  The `=` sign here doesn't mean "equals" like it does in math class — it means **assignment**: "take whatever is on the right, and store it in the name on the left."  What do you think happens if we assign to the same name twice?  Try it out!

```python
pizzas = 3
print(pizzas)
pizzas = 5
print(pizzas)
```

This program prints:

```text
3
5
```

The second assignment *replaces* the old value — the locker only holds one thing at a time.

### Expressions: Letting Python Do the Math
An **expression** is anything Python can compute down to a single value, like `2 + 3` or `pizzas * 8`.  Python evaluates the right-hand side of an assignment *first*, and only then stores the result.  Remember the operator table in the model above?  Let's put it to work.  Suppose each pizza has 8 slices, and we want to share them among 6 people:

```python
pizzas = 3
slices = pizzas * 8       # multiplication
people = 6
each = slices / people    # division
leftover = slices % people  # modulus: the remainder after dividing
print(slices)
print(each)
print(leftover)
```

This program prints:

```text
24
4.0
0
```

Wait — why did `each` print as `4.0` and not `4`?  This is our first clue that values have **types**.  A **type** is the *kind* of value something is: `24` is an **integer** (`int`, a whole number), while `4.0` is a **floating point number** (`float`, a number that can have a decimal part).  In Python, the `/` division operator *always* produces a `float`, even when the division comes out evenly.  The `%` (modulus) operator gives you the *remainder* after division — super handy for questions like "how many slices are left over?" or "is this number even or odd?"

Here's a trace of exactly what Python does, line by line.  Reading a trace like this is a great habit: it's how you can "be the computer" and predict what a program will do before you run it.

| Step | Line | Variable values after this line | What happens / Output |
|------|------|--------------------------------|------------------------|
| 1 | `pizzas = 3` | `pizzas = 3` | 3 is stored in `pizzas` |
| 2 | `slices = pizzas * 8` | `pizzas = 3`, `slices = 24` | Python looks up `pizzas` (3), computes `3 * 8 = 24`, stores it |
| 3 | `people = 6` | ... `people = 6` | 6 is stored in `people` |
| 4 | `each = slices / people` | ... `each = 4.0` | `24 / 6` is `4.0` — division always gives a `float`! |
| 5 | `leftover = slices % people` | ... `leftover = 0` | `24 % 6` is `0`: no remainder |
| 6-8 | the `print` lines | (unchanged) | Prints `24`, `4.0`, `0` |

What do you think `7 % 2` is?  What about `8 % 2`?  Can you see how `%` could tell you whether a number is even?

### Strings: Storing Text
Numbers are great, but programs also work with text: names, addresses, messages.  A piece of text is called a **string** (think of it as a *string of characters*), and we write it inside quotation marks so Python knows where the text starts and ends:

```python
name = "Grizz"
greeting = "Hello, " + name + "!"
print(greeting)
```

This program prints:

```text
Hello, Grizz!
```

The `+` operator does something different with strings than with numbers: instead of adding, it **concatenates** — a fancy word that just means "glues the strings together end-to-end."  Notice the space inside `"Hello, "` — Python glues *exactly* what you give it, so if you forget the space, you'd get `Hello,Grizz!`.  Try it and see!

Here's a question to ponder: what do you think `"2" + "3"` gives you?  It's not `5` — it's the string `"23"`, because with quotes around them, those are strings being glued together, not numbers being added.  The quotes make all the difference!

### Getting Input from the User
So far, our programs do exactly the same thing every time.  Let's make them interactive!  The `input()` function pauses the program, shows a prompt, and waits for the user to type something and press Enter.  Whatever they type comes back to us so we can store it in a variable:

```python
name = input("What's your name? ")
print("Nice to meet you, " + name + "!")
```

This program prints (if the user types `Bella`):

```text
What's your name? Bella
Nice to meet you, Bella!
```

Here's the catch — and it trips up nearly everyone at first: **`input()` always gives you back a string**, even if the user types a number.  If the user types `19`, you get the *string* `"19"`, not the *number* 19.  Why does that matter?  Because `"19" + 1` is an error (you can't glue a string to a number), and `"19" + "1"` is `"191"` (glue!), not 20.

### Type Conversion: int() and float()
When we want to do math with something the user typed, we have to **convert** it from a string to a number first.  The `int()` function converts to a whole number, and `float()` converts to a decimal number.  Going the other way, `str()` converts a number into a string so we can glue it into a message.  Let's revisit the graduation-year idea from the model:

```python
year = input("What year will you graduate? ")  # year is a string, like "2029"
year = int(year)                               # now year is the number 2029
years_left = year - 2026
print("Only " + str(years_left) + " more years to go!")
```

This program prints (if the user types `2029`):

```text
What year will you graduate? 2029
Only 3 more years to go!
```

Let's trace this carefully, paying attention to the *type* of each value — this is the single most important trace in this whole activity:

| Step | Line | Variable values (and types!) | What happens / Output |
|------|------|------------------------------|------------------------|
| 1 | `year = input(...)` | `year = "2029"` (a `str`) | User types 2029, but it arrives as *text* |
| 2 | `year = int(year)` | `year = 2029` (an `int`) | `int()` converts the string `"2029"` into the number 2029 |
| 3 | `years_left = year - 2026` | `years_left = 3` (an `int`) | Now that `year` is a number, subtraction works: `2029 - 2026 = 3` |
| 4 | `print("Only " + str(years_left) + ...)` | (unchanged) | `str(3)` turns 3 back into `"3"` so it can be glued into the message; prints `Only 3 more years to go!` |

What do you think would happen if we skipped step 2 and tried `"2029" - 2026`?  Try it — reading error messages is a skill, and this one is worth seeing at least once.

### Putting It All Together: A Sales Tax Calculator
Remember the sales tax question from the model?  Let's build the whole thing.  We'll ask for a price, convert it to a `float` (prices have cents, so `int()` won't do!), compute the total with 6% tax, and print it nicely:

```python
price = float(input("What is the price of your item? "))
totalcost = price + price * 0.06     # or: price * 1.06
print("Your total with tax is ${0:,.2f}".format(totalcost))
```

This program prints (if the user types `1250`):

```text
What is the price of your item? 1250
Your total with tax is $1,325.00
```

A couple of things to notice.  First, we nested `input()` *inside* `float()` — Python evaluates the inside first (get the text), then the outside (convert it), all in one line.  Second, that mysterious `{0:,.2f}` is a **format specifier**: the `0` means "insert the first value given to `format()` here," the `,` means "put commas in big numbers," and `.2f` means "show exactly 2 digits after the decimal point."  Perfect for money!  What do you think would print if we left the formatting out and just used `print(totalcost)`?  (Hint: floats sometimes have *lots* of decimal places...)

### Common mistakes to avoid
- **Forgetting that `input()` gives a string.**  `age = input("Age? ")` followed by `age + 1` is an error.  Convert first: `age = int(input("Age? "))`.
- **Gluing numbers into strings without `str()`.**  `print("You are " + age + " years old")` fails when `age` is a number.  Use `print("You are " + str(age) + " years old")`.
- **Mixing up `=` in Python with equals in math.**  In Python, `x = x + 1` is perfectly sensible: "take the current value of `x`, add 1, store it back."
- **Expecting `/` to give a whole number.**  `10 / 2` is `2.0`, a float.  If you truly want whole-number division, Python has `//` (10 // 3 is 3).
- **Missing quotes around text**, or quotes around numbers you want to do math with.  `name = Grizz` is an error (no quotes); `age = "19"` quietly makes a string you can't do math on.
- **Case matters and spelling matters.**  `Print("hi")` and `print(nmae)` are both errors.  Python only knows names *exactly* as you wrote them.

## Practice Exercises
Work through these in order — each one builds on the last.  Write your best attempt *before* peeking at the solution!

### Exercise 1 (warm-up)
Create a variable called `favorite_number` and set it to your favorite number.  Print the number, then print its square (use the `**` operator from the model table).

Sample expected output (if your favorite number is 7):

```text
7
49
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
favorite_number = 7        # store the value in a variable
print(favorite_number)     # print it
print(favorite_number ** 2)  # ** is exponentiation: 7 to the power 2
```

The key idea: a variable stores a value once, and you can use it as many times as you like afterward.

</details>

### Exercise 2 (getting input)
Ask the user for their first name and their favorite food, and print a single sentence that uses both, like `Alex loves tacos!`.

Sample run:

```text
What's your first name? Alex
What's your favorite food? tacos
Alex loves tacos!
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
name = input("What's your first name? ")
food = input("What's your favorite food? ")
print(name + " loves " + food + "!")   # concatenation glues strings together
```

No type conversion needed here — names and foods are text, and `input()` already gives us text.  Watch the spaces inside the quoted pieces!

</details>

### Exercise 3 (numbers from input)
Ask the user how many pizzas they're ordering and how many people are sharing.  Each pizza has 8 slices.  Print how many slices each person gets (it's fine if it's a decimal) and how many slices are left over if everyone takes only whole slices.

Sample run:

```text
How many pizzas? 3
How many people? 5
Each person gets 4.8 slices
Leftover whole slices: 4
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
pizzas = int(input("How many pizzas? "))   # convert: input() gives a string!
people = int(input("How many people? "))
slices = pizzas * 8
print("Each person gets " + str(slices / people) + " slices")
print("Leftover whole slices: " + str(slices % people))
```

Two ideas at work: `int()` converts the typed text into numbers we can do math with, and `%` (modulus) finds the remainder — the slices that can't be split evenly.

</details>

### Exercise 4 (challenge)
Write a tip calculator.  Ask for the bill amount (which may have cents, so use `float()`) and the tip percentage (like `20`).  Print the tip amount and the grand total, each formatted as money with `"{0:,.2f}".format(...)`.

Sample run:

```text
Bill amount? 48.50
Tip percent? 20
Tip: $9.70
Total: $58.20
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
bill = float(input("Bill amount? "))       # float() because bills have cents
percent = float(input("Tip percent? "))
tip = bill * percent / 100                 # 20 percent means multiply by 20/100
total = bill + tip
print("Tip: ${0:,.2f}".format(tip))
print("Total: ${0:,.2f}".format(total))
```

The key idea is converting a percentage into a multiplier by dividing by 100, and using the `.2f` format specifier so money always shows exactly two decimal places.

</details>

### Exercise 5 (extra challenge)
Ask the user for a number of minutes (a whole number), and print it as hours and minutes.  For example, 135 minutes is 2 hours and 15 minutes.  Hint: how could `//` (whole-number division) and `%` (remainder) team up here?

Sample run:

```text
How many minutes? 135
That is 2 hours and 15 minutes.
```

<details>
<summary>Click to reveal a solution to Exercise 5</summary>

```python
minutes = int(input("How many minutes? "))
hours = minutes // 60      # whole-number division: how many full hours fit?
remaining = minutes % 60   # modulus: what's left after taking out the hours?
print("That is " + str(hours) + " hours and " + str(remaining) + " minutes.")
```

This `//` and `%` pairing shows up everywhere in programming: `//` tells you how many whole groups fit, and `%` tells you what's left over.

</details>

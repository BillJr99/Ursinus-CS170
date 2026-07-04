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

## Notes and Walkthrough

Think about a recipe card for chocolate chip cookies.  You write the steps down *once*, give the recipe a name, and from then on you can just say "make the cookie recipe" — you don't re-write the instructions every time you bake.  If the recipe needs details ("make 24 cookies," "use dark chocolate"), you supply those when you use it, and when you're done, you get something back: cookies!

A **function** in Python works exactly the same way.  It's a named chunk of code that you write once and can then run — we say **call** or *invoke* — as many times as you like.  You've already been *calling* functions all semester: `print("hello")`, `input("Your name? ")`, and `random.random()` are all function calls.  Now it's time to write your own.

### Defining a function vs. calling a function

There are two separate moments in a function's life, and keeping them straight is the single most important idea on this page:

1. **Defining** the function — writing the recipe card.  This starts with the keyword `def`, and it does *not* run the code inside.  It just teaches Python the recipe and files it away under a name.
2. **Calling** the function — actually making the cookies.  You write the function's name followed by parentheses `()`, and *that* is when the code inside runs.

```python
def greet():
    print("Hello there!")
    print("Welcome to CS170.")

print("About to greet...")
greet()
greet()
print("Done greeting.")
```

This program prints:

```text
About to greet...
Hello there!
Welcome to CS170.
Hello there!
Welcome to CS170.
Done greeting.
```

Notice the order of the output!  Even though the `def` block appears first in the file, nothing is printed until the *calls* on the later lines.  And because we called `greet()` twice, its two lines printed twice — we wrote the code once and reused it.  Also note the familiar punctuation: a colon `:` after the definition line, and indentation to mark which lines belong to the function (just like `if` and loops).

The parentheses matter more than you'd think.  `greet()` *calls* the function; `greet` without parentheses just *refers to* the recipe card without cooking anything — Python won't complain, but nothing will happen.

### Parameters and arguments: giving a function information

Our `greet` function says the same thing every time.  Recipes get interesting when you can hand them details.  A **parameter** is a variable named in the function definition that acts as a placeholder for information the caller will supply.  An **argument** is the actual value you pass in when you call the function.  (Students mix these up constantly, and honestly, professionals are loose about it too — but here's the memory trick: **p**arameter = **p**laceholder, **a**rgument = **a**ctual value.)

```python
def greet(name):
    print("Hello,", name, "- welcome to CS170!")

greet("Ada")
greet("Grace")
```

This program prints:

```text
Hello, Ada - welcome to CS170!
Hello, Grace - welcome to CS170!
```

When `greet("Ada")` runs, Python copies the argument `"Ada"` into the parameter `name`, and then runs the function body.  It's as if an invisible line `name = "Ada"` ran at the top of the function.  On the second call, `name` is `"Grace"` instead.  Same recipe, different ingredients.

A function can have several parameters, separated by commas — and then the *order* of your arguments matters.  In `triangleArea(base, height)` from the model above, `triangleArea(10, 4)` means `base = 10` and `height = 4`, not the other way around.

### Return values: getting an answer back

Printing is nice, but often you want a function to *compute something and hand the answer back* so the rest of your program can use it.  That's what the **`return`** statement does: it ends the function immediately and sends a value — the **return value** — back to wherever the function was called.  The call itself then *becomes* that value, and you can store it in a variable, print it, or use it in a bigger expression.

This is the difference between a friend who *tells you* the answer to a math problem out loud (`print`) and one who *hands you a slip of paper* with the answer that you can keep using (`return`).

```python
def circleArea(radius):
    area = 3.14159 * radius ** 2
    return area

a = circleArea(10)
print("The area is", a)
print("Twice the area is", circleArea(10) * 2)
```

This program prints:

```text
The area is 314.159
Twice the area is 628.318
```

Let's trace the first call, `a = circleArea(10)`, end to end — watch the value flow *into* the function through the parameter and *back out* through the return:

| Step | Line | Variable values | What happens / Output |
|------|------|------------------|------------------------|
| 1 | `def circleArea(radius):` | — | Python files the recipe away; nothing runs |
| 2 | `a = circleArea(10)` | — | Call begins: the argument `10` is copied into the parameter `radius` |
| 3 | `area = 3.14159 * radius ** 2` | `radius = 10`, `area = 314.159` | The body computes using the parameter |
| 4 | `return area` | `radius = 10`, `area = 314.159` | The function ends; the value `314.159` travels back to the caller |
| 5 | `a = circleArea(10)` (finishing) | `a = 314.159` | The call `circleArea(10)` *became* `314.159`, which is stored in `a` |
| 6 | `print("The area is", a)` | `a = 314.159` | Prints `The area is 314.159` |

One subtle but crucial point: `return` and `print` are *not* the same.  A function that prints its answer but doesn't return it gives you nothing to work with:

```python
def circleAreaPrinter(radius):
    print(3.14159 * radius ** 2)   # prints, but returns nothing

result = circleAreaPrinter(10)
print("result is:", result)
```

This program prints:

```text
314.159
result is: None
```

`None` is Python's way of saying "no value here."  The first line looks fine, but `result` is useless — we couldn't double it, compare it, or use it in a formula.  When in doubt, `return` the answer and let the *caller* decide whether to print it.

### Scope: a function's variables are private

Look back at the trace: `radius` and `area` exist *inside* `circleArea` while it runs.  Once the function returns, those variables vanish.  If you tried to `print(area)` outside the function, Python would report an error that `area` is not defined.  The region of a program where a variable exists is called its **scope**, and variables created inside a function are **local** to it — private scratch paper that gets thrown away when the function finishes.  This is a feature, not a bug!  It means two functions can both use a variable named `area` without stepping on each other, and it's why the only reliable way to get a result out of a function is to `return` it.

### Functions calling functions

Here's where it gets fun: the body of a function can call *other* functions.  Big programs are built exactly this way — small, trustworthy pieces combined into larger ones.

```python
def circleArea(radius):
    return 3.14159 * radius ** 2

def cylinderVolume(radius, height):
    # a cylinder is a circle "stretched" upward, so reuse circleArea!
    return circleArea(radius) * height

def main():
    v = cylinderVolume(10, 2)
    print("The cylinder holds", v, "cubic units")

main()
```

This program prints:

```text
The cylinder holds 628.318 cubic units
```

Follow the chain: `main()` calls `cylinderVolume(10, 2)`, which calls `circleArea(10)`, which returns `314.159` to `cylinderVolume`, which multiplies by 2 and returns `628.318` to `main`, which prints it.  Each function did one small job and trusted the others to do theirs.  Notice we didn't re-derive the circle formula inside `cylinderVolume` — we *reused* it.  If we ever fix or improve `circleArea` (say, using `math.pi` for more precision), every function that calls it improves for free.

This is also why the model above wraps the program's starting point in a `main()` function guarded by `if __name__ == "__main__":` — it keeps the "do things" code in one tidy, named place, separate from the reusable recipes.

### Why bother with functions?

You could write every program as one long list of statements.  Here's why we don't:

* **Reuse:** write the logic once, call it everywhere.  Fix a bug once, and it's fixed everywhere it's used.
* **Naming:** `circleArea(r)` tells a reader *what* is happening without them having to decode the math.  Good function names make programs read almost like sentences.
* **Testing:** you can try a small function by itself — call `circleArea(1)` and check that you get about 3.14 — before trusting it inside a bigger program.  Finding a bug in a 5-line function is much easier than finding one in a 500-line program.
* **Teamwork and thinking:** functions let you split a big problem into pieces you can solve (and think about) one at a time.  Remember our rock-paper-scissors protocol?  Each message type was handled by its own chunk of logic — that's the same instinct.

### Common mistakes to avoid

- **Confusing `return` with `print`.**  `print` shows a value to a human; `return` hands a value back to the program.  If you need the result later, `return` it.  (A function with no `return` gives back `None`.)
- **Forgetting the parentheses when calling.**  `greet` names the function; `greet()` runs it.  If "nothing happened," check for missing `()`.
- **Writing code after `return`.**  `return` exits the function immediately — any lines below it in the function body will never run.
- **Expecting a local variable to exist outside its function.**  Variables created inside a function (including its parameters) disappear when it returns; that's scope.  Get values out with `return`, not by hoping the variable survives.
- **Arguments in the wrong order.**  `triangleArea(4, 10)` and `triangleArea(10, 4)` happen to agree for area, but `range(10, 4)` and `range(4, 10)` certainly don't!  Match your arguments to the parameter list, left to right.
- **Forgetting the `:` after the `def` line, or misindenting the body.**  The rules are the same as `if` and loops: colon at the end, and every line of the body indented consistently.
- **Defining a function but never calling it.**  A `def` block alone produces no output; somewhere, something has to call it.

## Practice Exercises

Try each one before revealing the solution — and when you get stuck, trace the call by hand like the table above.

### Exercise 1 (warm-up)

Define a function `cheer(name)` that prints `Go <name> go!`, then call it three times with three different names.  Sample output:

```text
Go Bears go!
Go Ada go!
Go CS170 go!
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
def cheer(name):
    print("Go", name, "go!")   # name holds whatever argument was passed in

cheer("Bears")   # the argument "Bears" is copied into the parameter name
cheer("Ada")
cheer("CS170")
```

The definition runs zero times on its own; each call runs the body once with a different value in the parameter `name`.

</details>

### Exercise 2

Write a function `rectangleArea(width, height)` that *returns* (not prints!) the area of a rectangle.  Then use it to print the total area of two rooms: one 10 by 12 and one 9 by 11.  Expected output:

```text
Total area: 219
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
def rectangleArea(width, height):
    return width * height        # hand the answer back to the caller

total = rectangleArea(10, 12) + rectangleArea(9, 11)   # 120 + 99
print("Total area:", total)
```

Because the function *returns* a number, each call acts like a number in the expression, and we can add two calls together.  A version that printed instead of returning couldn't do this — that's the whole reason `return` exists.

</details>

### Exercise 3

Write a function `isEven(n)` that returns `True` if `n` is even and `False` otherwise (hint: `n % 2` gives the remainder when dividing by 2).  Then use it in a loop to print which of the numbers 1 through 6 are even.  Expected output:

```text
1 False
2 True
3 False
4 True
5 False
6 True
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
def isEven(n):
    return n % 2 == 0     # this comparison IS a True/False value - return it directly

for i in range(1, 7):     # 1 through 6
    print(i, isEven(i))
```

Two ideas meet here: functions can return booleans (perfect for naming a *question* your program asks), and a returned value can be used immediately inside another call like `print`.  Note there's no need for `if n % 2 == 0: return True` — the comparison already produces `True` or `False`.

</details>

### Exercise 4 (challenge)

Build a tiny temperature toolkit of three functions:

1. `toFahrenheit(celsius)` returns the Fahrenheit equivalent (multiply by 9/5, then add 32).
2. `describe(fahrenheit)` returns the string `"cold"` below 50, `"nice"` from 50 to 80, and `"hot"` above 80.
3. `report(celsius)` uses *both* functions above to return a full sentence.

Calling `print(report(30))` should output:

```text
30 degrees C is 86.0 degrees F - that is hot
```

Try `report(10)` and `report(20)` too — what should they say?

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
def toFahrenheit(celsius):
    return celsius * 9 / 5 + 32

def describe(fahrenheit):
    if fahrenheit < 50:
        return "cold"          # return exits immediately, so no elif is strictly needed
    elif fahrenheit <= 80:
        return "nice"
    else:
        return "hot"

def report(celsius):
    f = toFahrenheit(celsius)              # one function calling another...
    return "{} degrees C is {} degrees F - that is {}".format(celsius, f, describe(f))

print(report(30))    # 30 C -> 86.0 F -> "hot"
print(report(10))    # 10 C -> 50.0 F -> "nice"
print(report(20))    # 20 C -> 68.0 F -> "nice"
```

`report` never does the math or the categorizing itself — it delegates to the two smaller functions and just assembles the sentence.  Each piece can be tested alone (does `toFahrenheit(0)` give 32.0?), which is exactly why we break programs into functions.

</details>

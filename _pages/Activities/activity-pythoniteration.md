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

## Notes and Walkthrough

Have you ever had to do the same thing over and over again?  Maybe you've dealt a deck of cards to four players, or checked your phone every few minutes waiting for a message.  You didn't need new instructions for each repetition — you just kept doing the same steps until you were done.  Computers are exactly the same way, and they're *very* good at repetition.  In programming, we call this repetition a **loop**: a chunk of code that runs over and over.  Each single pass through that chunk is called an **iteration** (so "iterating" just means "repeating").

Python gives us two kinds of loops, and choosing between them is usually easy:

* Use a **`while` loop** when you want to repeat *until something becomes true* (or as long as something stays true), and you don't necessarily know how many times that will take.  "Keep asking the user until they type a valid answer" is a `while` loop.
* Use a **`for` loop** when you know (or can compute) *how many times* you want to repeat.  "Print the numbers 1 through 10" is a `for` loop.

The good news: anything you can do with one, you can do with the other!  They're just more or less convenient for different jobs.

### The `while` loop

A `while` loop looks a lot like the `if` statement you've already seen.  It checks a **condition** (a boolean expression that is either `True` or `False`), and if the condition is `True`, it runs the indented code underneath.  The difference is what happens next: an `if` statement moves on, but a `while` loop jumps *back up* and checks the condition again.  It keeps doing this until the condition becomes `False`.

```python
countdown = 3
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Liftoff!")
```

This program prints:

```text
3
2
1
Liftoff!
```

Notice three things.  First, the colon `:` at the end of the `while` line — just like with `if`, Python requires it.  Second, the two lines inside the loop are indented; that indentation is how Python knows which lines belong to the loop.  Third — and this is the big one — the line `countdown = countdown - 1` *changes* the variable that the condition is checking.  Without it, `countdown` would stay 3 forever, the condition would always be `True`, and the loop would never end.  We call that an **infinite loop**, and it's one of the most common bugs in all of programming!

Let's trace this countdown loop step by step, the way the computer sees it:

| Step | Line | `countdown` | What happens / Output |
|------|------|-------------|------------------------|
| 1 | `countdown = 3` | 3 | Variable created |
| 2 | `while countdown > 0:` | 3 | `3 > 0` is `True`, so enter the loop |
| 3 | `print(countdown)` | 3 | Prints `3` |
| 4 | `countdown = countdown - 1` | 2 | Variable decreases |
| 5 | `while countdown > 0:` | 2 | `2 > 0` is `True`, loop again |
| 6 | `print(countdown)` | 2 | Prints `2` |
| 7 | `countdown = countdown - 1` | 1 | Variable decreases |
| 8 | `while countdown > 0:` | 1 | `1 > 0` is `True`, loop again |
| 9 | `print(countdown)` | 1 | Prints `1` |
| 10 | `countdown = countdown - 1` | 0 | Variable decreases |
| 11 | `while countdown > 0:` | 0 | `0 > 0` is `False`, so *skip past* the loop |
| 12 | `print("Liftoff!")` | 0 | Prints `Liftoff!` |

Try tracing loops like this by hand when a program doesn't do what you expect — it's the single best debugging tool you have.

A `while` loop really shines when you can't predict the number of repetitions.  Here's a loop that keeps asking until the user cooperates (you saw this idea in the first model above):

```python
answer = -1
while answer <= 0:
    answer = int(input("Enter a positive number: "))
print("Thanks! You entered", answer)
```

If the user types `-5`, then `0`, then `42`, this program prints:

```text
Enter a positive number: -5
Enter a positive number: 0
Enter a positive number: 42
Thanks! You entered 42
```

Why did we start `answer` at `-1`?  Because the condition is checked *before* the first iteration — we need the condition to be `True` the first time through so the loop body runs at least once.  This "prime the pump" trick is very common with `while` loops.

### The `for` loop and `range()`

When you know how many times to repeat, Python's `for` loop with the `range()` function is more convenient.  The **`range()`** function generates a sequence of numbers, and the `for` loop visits each one in turn, storing the current number in a **loop variable** that you name:

```python
for i in range(5):
    print("Iteration number", i)
```

This program prints:

```text
Iteration number 0
Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
```

What do you notice?  `range(5)` gives us *five* numbers, but they start at 0 and stop at 4 — the number 5 itself is never included!  This trips up almost everyone at first.  Think of `range(5)` as "give me 5 numbers, starting from 0."  Computer scientists love starting from 0 (you saw this with string indices, too), and stopping just short of the end value makes the count come out right: `range(5)` is exactly 5 iterations.

The `for` loop also quietly does the bookkeeping that we had to do by hand with `while`: it creates `i`, updates it each time, and stops at the right moment.  No infinite loops possible here — that's a real advantage.

`range()` can take up to three values: a **start**, a **stop**, and a **step** (how much to count by):

```python
for i in range(1, 11):      # start at 1, stop before 11
    print(i, end=" ")
print()

for i in range(0, 20, 5):   # start at 0, stop before 20, count by 5
    print(i, end=" ")
print()

for i in range(3, 0, -1):   # count DOWN by using a negative step
    print(i, end=" ")
print("Liftoff!")
```

This program prints:

```text
1 2 3 4 5 6 7 8 9 10
0 5 10 15
3 2 1 Liftoff!
```

(The `end=" "` just tells `print` to put a space after each value instead of moving to a new line.)  Notice the third loop is our countdown again — compare it to the `while` version above.  Same behavior, less code, and no way to forget the update step.

### The accumulator pattern

Loops become truly powerful when they *build up* an answer across iterations.  A variable that collects a result as the loop runs is called an **accumulator**.  The recipe is always the same: (1) create the accumulator *before* the loop, starting it at a sensible empty value (0 for a sum or a count, `""` for text); (2) update it *inside* the loop; (3) use it *after* the loop.

```python
total = 0
for i in range(1, 5):
    total = total + i
    print("Added", i, "- total is now", total)
print("Final total:", total)
```

This program prints:

```text
Added 1 - total is now 1
Added 2 - total is now 3
Added 3 - total is now 6
Added 4 - total is now 10
Final total: 10
```

Here's the iteration-by-iteration trace.  Watch how `total` "remembers" the work of every previous iteration:

| Iteration | `i` | `total` before | `total = total + i` | `total` after |
|-----------|-----|----------------|----------------------|----------------|
| 1st | 1 | 0 | 0 + 1 | 1 |
| 2nd | 2 | 1 | 1 + 2 | 3 |
| 3rd | 3 | 3 | 3 + 3 | 6 |
| 4th | 4 | 6 | 6 + 4 | 10 |

Did you predict `6` as the final total before reading the trace?  It's tempting to see "Added 4" and think the total is whatever we just added — but the accumulator carries *everything* forward: 1 + 2 + 3 + 4 = 10.  When a loop surprises you, build a table like this one and let it settle the argument.

Counting is just accumulating by 1.  The coin-flipping model above uses exactly this pattern: `heads += 1` adds one to the accumulator each time a condition holds.  (`heads += 1` is shorthand for `heads = heads + 1`.)

### Looping over strings

A `for` loop can walk through more than just numbers.  A string is a sequence of characters, and `for letter in text:` visits each character one at a time — no `range()` needed:

```python
text = "micro:bit"
vowels = 0
for letter in text:
    if letter in "aeiou":
        vowels += 1
print("Found", vowels, "vowels")
```

This program prints:

```text
Found 3 vowels
```

Each iteration, `letter` holds the next character: first `'m'`, then `'i'`, then `'c'`, and so on.  Notice the accumulator pattern again — `vowels` starts at 0 before the loop and counts up inside it.  This "loop over a sequence" idea will come back constantly, especially when we meet lists.

### Nested loops (briefly)

You can put a loop inside another loop; we call these **nested loops**.  For each single iteration of the *outer* loop, the *inner* loop runs all of its iterations from the beginning.  Think of a clock: the hour hand (outer loop) moves once for every full trip of the minute hand (inner loop).

```python
for row in range(3):
    for col in range(2):
        print("row", row, "col", col)
```

This program prints:

```text
row 0 col 0
row 0 col 1
row 1 col 0
row 1 col 1
row 2 col 0
row 2 col 1
```

Three outer iterations times two inner iterations gives six lines total.  In the Nested Loops model above, take a careful look at where `j` is set to 0.  It's set *once*, before the outer loop — so after the inner loop finishes the first time, `j` is stuck at 10 forever, and the inner loop never runs again!  To fix it, `j = 0` would need to move *inside* the outer loop, so the inner count restarts on each outer iteration.  What do you think the broken version prints?  Try it out!

### Common mistakes to avoid

- **Forgetting to update the loop variable in a `while` loop.**  If nothing inside the loop can make the condition `False`, the loop runs forever.  If your program seems frozen, this is the first thing to check.
- **Off-by-one errors with `range()`.**  `range(10)` produces 0 through 9 — it stops *before* the stop value.  Want 1 through 10?  Use `range(1, 11)`.
- **Forgetting the colon `:`** at the end of the `while` or `for` line.  Python will complain with a `SyntaxError`.
- **Indentation mistakes.**  Only the indented lines repeat.  A `print` you meant to run once *after* the loop will run every iteration if you accidentally indent it (and vice versa).
- **Initializing the accumulator inside the loop.**  `total = 0` inside the loop body resets your running total every iteration, so you only ever "remember" the last item.  Accumulators are created *before* the loop.
- **Resetting a nested loop's counter in the wrong place** (see the Nested Loops model above) — the inner `while` loop's counter must be reset inside the outer loop, or the inner loop only runs once.

## Practice Exercises

Work through these in order — each builds on the one before.  Write your answer (or at least trace it on paper) before peeking at the solution!

### Exercise 1 (warm-up)

Use a `for` loop with `range()` to print the even numbers from 2 through 20, one per line.  The first lines of output should be:

```text
2
4
6
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
# Start at 2, stop before 22 (so 20 is included), step by 2
for number in range(2, 22, 2):
    print(number)
```

The key idea is the third value to `range()`: the step.  We stop at 22, not 20, because `range()` never includes its stop value — a classic off-by-one to watch for.

</details>

### Exercise 2

Use a loop to compute the sum of the numbers from 1 through 100, then print the result *once* after the loop finishes.  (Legend says the mathematician Gauss did this in his head as a schoolchild.  You get to use a computer!)

Expected output:

```text
5050
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
total = 0                 # accumulator: create it BEFORE the loop
for i in range(1, 101):   # 1 through 100
    total += i            # update it INSIDE the loop
print(total)              # use it AFTER the loop (note the indentation!)
```

This is the accumulator pattern in its purest form.  If your answer printed 100 lines, check the indentation of the `print` — it belongs outside the loop.

</details>

### Exercise 3

Ask the user to enter a password, and keep asking with a `while` loop until they type `open sesame`.  Then print `Welcome!`.  A sample run might look like:

```text
Password? abracadabra
Password? please
Password? open sesame
Welcome!
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
guess = ""                       # prime the pump so the condition starts True
while guess != "open sesame":
    guess = input("Password? ")  # updating guess is what lets the loop end
print("Welcome!")
```

We initialize `guess` to something that cannot match, so the loop body runs at least once.  Because we don't know how many tries the user will need, a `while` loop is the natural choice here — a `for` loop would need a count we don't have.

</details>

### Exercise 4 (challenge)

Write a program that counts how many times the letter `s` appears in the string `"mississippi state"` — but this time, print a running commentary: for each character, print the character, and if it's an `s`, also print how many you've found so far.  Finally, print the total.  The last few lines of output should be:

```text
t
e
Total s count: 5
```

Then, as a bonus, use a *nested* loop to print a small triangle of stars:

```text
*
**
***
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
# Part 1: count the letter s with a running commentary
text = "mississippi state"
count = 0
for letter in text:
    print(letter)
    if letter == "s":
        count += 1
        print("  found an s! count is now", count)
print("Total s count:", count)

# Part 2: a triangle of stars using nested loops
for row in range(1, 4):        # rows 1, 2, 3
    for star in range(row):    # row 1 gets 1 star, row 2 gets 2, ...
        print("*", end="")     # end="" keeps the stars on one line
    print()                    # move to the next line after each row
```

Part 1 combines looping over a string with the accumulator pattern.  In Part 2, notice that the inner loop's `range(row)` depends on the outer loop's variable — that's what makes each row longer than the last.

</details>

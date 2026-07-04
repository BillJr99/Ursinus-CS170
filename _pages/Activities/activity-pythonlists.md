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

## Notes and Walkthrough

So far, every variable we've created has held exactly one thing: one number, one string, one `True` or `False`.  But the world around us rarely comes in ones!  Think about a grade book, a playlist, or a grocery list.  What would it be like to create a separate variable for every single grade in a class -- `grade1`, `grade2`, `grade3`, all the way up to `grade30`?  It would be exhausting, and worse, our program would have to change every time a student joined the class.  There has to be a better way, and there is: the **list**.

A **list** is an ordered collection of data stored under a single variable name.  "Ordered" means the items stay in the order you put them in -- the first item stays first, the second stays second, and so on -- just like the lines on a paper grocery list.  Each item in a list is called an **element**.

### Creating a List

Before we can put anything in a list, we need to create one.  In Python, we write a list using square brackets `[]`, with the elements separated by commas.  We can also start with an empty list -- just the brackets with nothing inside -- and fill it up later.

```python
snacks = ["pretzels", "apples", "popcorn"]
print(snacks)

empty_cart = []
print(empty_cart)
```

This program prints:

```text
['pretzels', 'apples', 'popcorn']
[]
```

Notice that Python prints the whole list back to us, brackets and all.  Try it out!  What happens if you mix types, like `["pretzels", 42, True]`?  Python doesn't mind -- a list can hold any kind of data (though we usually keep one kind of thing per list, so the list has one clear meaning).

### Getting Items Out: Indexing

How do we get just one element back out?  Every element in a list has a position number called its **index**.  Here's the catch that surprises everyone at first: **indices start at 0, not 1**.  The first element is at index 0, the second is at index 1, and so on.  Why?  You can think of the index as "how many steps from the start" -- the first element is zero steps away!

We write the index in square brackets after the list's name.  We can also ask Python how many elements a list has using the `len()` function (short for "length").

```python
snacks = ["pretzels", "apples", "popcorn"]
print(snacks[0])
print(snacks[2])
print(len(snacks))
print(snacks[-1])
```

This program prints:

```text
pretzels
popcorn
3
popcorn
```

Two things to notice here.  First, even though `len(snacks)` is 3, the last valid index is 2 -- always one less than the length, because we started counting at 0.  What do you think happens if you try `snacks[3]`?  Try it!  Python stops your program with an `IndexError: list index out of range`, because there's no fourth element to give you.

Second, that `snacks[-1]` at the end: negative indices count backwards from the end of the list, so `-1` is always the last element, `-2` is second-to-last, and so on.  It's a handy shortcut for "give me the last one" without having to know how long the list is.

### Changing, Adding, and Removing Elements

Lists are not "read-only" -- we can change them as our program runs.  There are three big operations to know:

* **Assigning to an index** replaces one element with a new value, like erasing one line of your grocery list and writing something else there.
* **Appending** adds a new element onto the *end* of the list, making the list one element longer.  The word comes from "append," meaning to attach at the end.
* **Removing** takes an element out of the list, and everything after it slides down to fill the gap.

```python
snacks = ["pretzels", "apples", "popcorn"]
snacks[1] = "grapes"        # replace apples with grapes
snacks.append("cookies")    # add cookies to the end
snacks.remove("pretzels")   # take pretzels out
print(snacks)
print(len(snacks))
```

This program prints:

```text
['grapes', 'popcorn', 'cookies']
3
```

Let's slow down and trace exactly what the list looks like after each line.  Tracing by hand like this is one of the best ways to convince yourself you understand what the computer is doing!

| Step | Line | `snacks` after this line | What happens |
|------|------|--------------------------|--------------|
| 1 | `snacks = ["pretzels", "apples", "popcorn"]` | `["pretzels", "apples", "popcorn"]` | The list is created with 3 elements at indices 0, 1, and 2 |
| 2 | `snacks[1] = "grapes"` | `["pretzels", "grapes", "popcorn"]` | The element at index 1 is replaced; the list is still length 3 |
| 3 | `snacks.append("cookies")` | `["pretzels", "grapes", "popcorn", "cookies"]` | A new element appears at the end (index 3); length grows to 4 |
| 4 | `snacks.remove("pretzels")` | `["grapes", "popcorn", "cookies"]` | The first matching value is removed; everything slides left, so `"grapes"` is now index 0, and length shrinks to 3 |
| 5 | `print(snacks)` | `["grapes", "popcorn", "cookies"]` | Output: `['grapes', 'popcorn', 'cookies']` |
| 6 | `print(len(snacks))` | `["grapes", "popcorn", "cookies"]` | Output: `3` |

Did you catch what happened in step 4?  When an element is removed, the indices of everything after it change.  That's an important detail we'll come back to in the common mistakes below.

### Looping Over a List

Here's where lists really shine.  Because a list keeps its elements in order, we can visit each one in turn with a loop -- this is called **iterating** over the list.  Python gives us two natural ways to do it.

The first way says "for each item in the list, do this."  Python hands us each element, one at a time, in order:

```python
scores = [88, 95, 73]
for score in scores:
    print(score)
```

This program prints:

```text
88
95
73
```

The second way loops over the *indices* using `range(len(scores))`, which counts `0, 1, 2` for a list of length 3.  This is a little wordier, but it's the way to go when you need to know *where* you are in the list, or when you want to change elements as you visit them:

```python
scores = [88, 95, 73]
for i in range(len(scores)):
    print("Score number {} is {}".format(i, scores[i]))
    scores[i] = scores[i] + 5   # everyone gets 5 bonus points!
print(scores)
```

This program prints:

```text
Score number 0 is 88
Score number 1 is 95
Score number 2 is 73
[93, 100, 78]
```

Which style should you use?  If you only need the values, `for score in scores` is cleaner.  If you need the index too (or you're modifying the list), use `for i in range(len(scores))`.

### Accumulating Over a List

One of the most common patterns in all of programming is walking through a list while building up an answer as you go -- a running total, a count, or a "best so far."  The variable that collects the answer is called an **accumulator**.  The recipe is always the same: start the accumulator before the loop, update it inside the loop, and use it after the loop.  Here we compute both the total and the largest value in one pass:

```python
scores = [88, 95, 73]

total = 0            # the accumulator starts at 0
biggest = scores[0]  # "best so far" starts as the first element

for score in scores:
    total = total + score
    if score > biggest:
        biggest = score

print("The total is {}".format(total))
print("The average is {}".format(total / len(scores)))
print("The highest score is {}".format(biggest))
```

This program prints:

```text
The total is 256
The average is 85.33333333333333
The highest score is 95
```

Let's trace the accumulators as the loop runs, one loop pass at a time:

| Step | `score` this pass | `total` after | `biggest` after | What happens |
|------|-------------------|---------------|-----------------|--------------|
| Before loop | - | 0 | 88 | Accumulators are initialized |
| 1 | 88 | 88 | 88 | `0 + 88`; 88 is not greater than 88, so `biggest` stays |
| 2 | 95 | 183 | 95 | `88 + 95`; 95 > 88, so `biggest` updates |
| 3 | 73 | 256 | 95 | `183 + 73`; 73 is not greater than 95, so `biggest` stays |
| After loop | - | 256 | 95 | We print the total, the average (256 / 3), and the biggest |

Why did we start `biggest` at `scores[0]` instead of 0?  What would go wrong if all the scores were negative numbers?  Think it through -- it's a classic trap!

### Common mistakes to avoid

* **Forgetting that indexing starts at 0.**  The first element is `mylist[0]`, and the last is `mylist[len(mylist) - 1]` (or `mylist[-1]`).
* **Index out of range.**  Asking for `mylist[len(mylist)]` (or beyond) crashes with an `IndexError`.  If your loop crashes on its last pass, check your `range` bounds first.
* **Confusing `append` with `+`.**  `mylist.append(5)` adds the number 5 to the end of the list.  `mylist + 5` is an error, and `mylist = mylist + [5]` works but only if you wrap the 5 in brackets.  When in doubt, use `append`.
* **Expecting `append` to return the new list.**  Writing `mylist = mylist.append(5)` actually sets `mylist` to `None`!  Just call `mylist.append(5)` on its own line.
* **Removing elements from a list while looping over it.**  Remember step 4 of our trace: removal shifts every later element's index.  If you delete while iterating, the loop can skip elements.  It's safer to build a new list of the elements you want to keep.
* **Using `=` to copy a list.**  `list2 = list1` doesn't make a copy -- both names now point at the *same* list, so changing one changes "both."  Use `list2 = list(list1)` for a true copy.

## Practice Exercises

Work through these in order -- each one builds on the last.  Try each on your own before peeking at the solution!

### Exercise 1 (warm-up)

Create a list called `days` containing `"Mon"`, `"Wed"`, and `"Fri"`.  Print the first element, the last element (using a negative index), and the length of the list.

Expected output:

```text
Mon
Fri
3
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
days = ["Mon", "Wed", "Fri"]  # create the list with square brackets
print(days[0])    # index 0 is the FIRST element
print(days[-1])   # index -1 counts backwards: the LAST element
print(len(days))  # len() gives the number of elements
```

The key idea: indices start at 0, and negative indices count from the end.

</details>

### Exercise 2 (building and changing a list)

Start with an empty list called `todo`.  Append `"study"`, `"eat"`, and `"sleep"` to it.  Then replace `"eat"` with `"exercise"` using an index assignment, and print the final list.

Expected output:

```text
['study', 'exercise', 'sleep']
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
todo = []                 # start with an empty list
todo.append("study")      # todo is now ['study']
todo.append("eat")        # todo is now ['study', 'eat']
todo.append("sleep")      # todo is now ['study', 'eat', 'sleep']
todo[1] = "exercise"      # replace the element at index 1
print(todo)
```

The key idea: `append` grows the list at the end, while assigning to an index replaces one element without changing the length.

</details>

### Exercise 3 (looping with an accumulator)

Given the list `temps = [68, 72, 75, 71, 69]` (daily temperatures for a week of classes), write a loop that computes and prints the average temperature.

Expected output:

```text
The average temperature is 71.0
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
temps = [68, 72, 75, 71, 69]

total = 0                 # accumulator: the running sum
for temp in temps:
    total = total + temp  # add each temperature to the total

average = total / len(temps)  # divide the sum by how many there are
print("The average temperature is {}".format(average))
```

The key idea: initialize the accumulator *before* the loop, update it *inside* the loop, and use it *after* the loop.

</details>

### Exercise 4 (challenge)

Given `grades = [85, 92, 78, 95, 88]`, write a program that finds and prints both the highest grade *and* the index where it lives, without using Python's built-in `max` function.

Expected output:

```text
The highest grade is 95 at index 3
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
grades = [85, 92, 78, 95, 88]

best = grades[0]       # "best so far" starts as the first element
best_index = 0         # ... which lives at index 0

for i in range(len(grades)):   # loop over INDICES so we know where we are
    if grades[i] > best:
        best = grades[i]       # found a new champion...
        best_index = i         # ...remember where we found it

print("The highest grade is {} at index {}".format(best, best_index))
```

The key idea: because we need to report the *index* of the winner, we loop with `for i in range(len(grades))` instead of `for grade in grades` -- that way, `i` tells us where we are at every step.

</details>

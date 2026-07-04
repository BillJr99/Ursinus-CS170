---
layout: activity
permalink: /Activities/PythonFileIO
title: "CS170: Programming for the World Around Us - File I/O with Python"


info:
  goals: 
    - To read and write files with Python
  models:
    - title: "File I/O in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        file = open("input.txt", "r")
        lines = file.readlines()
        
        for line in lines:
            print(line)
        ]]></script>  
      questions: 
        - "Create a file called <code>input.txt</code> and run this program.  What does it do?"
        - "Modify this program to count the number of words in each line, and print that to the screen."
    - title: "Writing Files in Python"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        file = open("input.txt", "w")
        file.write("High Score: 100")
        file.close()
        ]]></script>  
      questions: 
        - "Run this program, then write a program to read this file, read the line, split it on the <code>:</code> character, and print the high score value (just the 100)."        
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/files/toctree.html
      title: Files
      
tags:
  - python
  - io
  
---

## Notes and Walkthrough

So far, every program we've written has a small problem: the moment the program ends, everything it computed disappears!  Our variables live in the computer's memory, and memory is wiped clean when the program stops.  If we want our data to stick around — a high score, a list of names, a saved game — we need to put it somewhere more permanent.  That's what **files** are for.

### What is a file, anyway?

A **file** is a named collection of data that lives on your computer's storage (a hard drive or SSD) instead of in memory.  Because it's on storage, it survives after your program ends, after you close your laptop, even after you restart the computer.  You've been using files all along: every Python program you've written is a file, and so is every photo, song, and document on your computer.

In this activity, we'll work with **text files**: files that contain ordinary human-readable characters, like the ones you'd type in an editor.  A text file is really just one long sequence of characters, and a special invisible character called a **newline** (written `"\n"` in Python) marks where one line ends and the next begins.  Keep that in mind — it will come back to surprise us later!

### Opening a file: asking the operating system for permission

Before your program can read or write a file, it has to **open** it.  Opening a file is like checking a book out of the library: you tell the librarian (the operating system) which book you want and what you plan to do with it, and you get back a claim ticket that you use for everything afterward.  In Python, that claim ticket is called a **file handle** (or file object), and we get one from the `open` function:

```python
file = open("input.txt", "r")
```

The first argument is the **filename** — the name of the file on disk.  The second argument is the **mode**, which says what you plan to do:

* `"r"` means **read mode**: you want to look at what's in the file.  The file must already exist, or Python will stop with an error.
* `"w"` means **write mode**: you want to create a file and put data into it.  Careful — if the file already exists, `"w"` *erases everything in it* the moment you open it!
* `"a"` means **append mode**: like write mode, but instead of erasing, new data is added to the *end* of whatever is already there.  This is handy for things like log files, where you want to keep adding entries.

What do you think happens if you open a file in `"r"` mode that doesn't exist?  Try it out!  You'll see a `FileNotFoundError` — Python's way of saying the librarian couldn't find your book.

### Reading a file line by line

Once a file is open for reading, the most natural way to read it is one line at a time with a `for` loop — just like looping over a list, except each item is a line of text.  Suppose we have a file called `groceries.txt` that contains:

```text
milk
eggs
bread
```

Here's a program that reads it and prints each item with a number:

```python
file = open("groceries.txt", "r")

count = 1
for line in file:
    print(str(count) + ": " + line)
    count = count + 1

file.close()
```

This program prints:

```text
1: milk

2: eggs

3: bread

```

Wait — why is everything double-spaced?  We didn't ask for blank lines!  Here's the culprit: remember that invisible **newline** character `"\n"` at the end of each line in the file?  When Python reads a line, it keeps that newline attached.  So the string we get is really `"milk\n"`, not `"milk"`.  Then `print` adds its *own* newline, and we end up with two — hence the blank lines.

The fix is the **`strip()`** function, which removes whitespace (spaces, tabs, and newlines) from the beginning and end of a string:

```python
file = open("groceries.txt", "r")

count = 1
for line in file:
    line = line.strip()
    print(str(count) + ": " + line)
    count = count + 1

file.close()
```

This program prints:

```text
1: milk
2: eggs
3: bread
```

Much better!  Stripping each line right after you read it is a great habit — almost every file-reading program you write will want to do it.

### Tracing a file-reading program step by step

Let's slow down and trace exactly what happens as that loop runs.  Here's the file `groceries.txt` again:

```text
milk
eggs
bread
```

And here's the trace of the fixed program above, line by line:

| Step | Line of code | Variable values | What happens / Output |
|------|--------------|-----------------|------------------------|
| 1 | `file = open("groceries.txt", "r")` | `file` = handle to groceries.txt | The file is opened for reading; Python's "bookmark" is at the very beginning. |
| 2 | `count = 1` | `count` = 1 | We start counting at 1. |
| 3 | `for line in file:` | `line` = `"milk\n"` | The first line is read, *including* its newline. |
| 4 | `line = line.strip()` | `line` = `"milk"` | The newline is stripped off. |
| 5 | `print(...)` | `count` = 1 | Prints `1: milk` |
| 6 | `count = count + 1` | `count` = 2 | |
| 7 | `for line in file:` | `line` = `"eggs\n"` | The bookmark has moved; we get the *second* line. |
| 8 | `line = line.strip()` | `line` = `"eggs"` | |
| 9 | `print(...)` | `count` = 2 | Prints `2: eggs` |
| 10 | `count = count + 1` | `count` = 3 | |
| 11 | `for line in file:` | `line` = `"bread\n"` | Third line read. |
| 12 | `line = line.strip()` | `line` = `"bread"` | |
| 13 | `print(...)` | `count` = 3 | Prints `3: bread` |
| 14 | `count = count + 1` | `count` = 4 | |
| 15 | `for line in file:` | (no more lines) | The bookmark is at the end of the file, so the loop stops. |
| 16 | `file.close()` | | The file is returned to the operating system. |

Notice the "bookmark" idea in the trace: a file handle remembers *where you are* in the file, and reading moves the bookmark forward.  That means if you loop over a file twice in a row, the second loop sees *nothing* — the bookmark is already at the end!  If you want to read a file again, close it and open it again.

### Splitting lines into fields

Files often store more than one piece of information per line.  For example, a file of quiz scores called `scores.txt` might look like this, with a name and a score on each line separated by a comma:

```text
Ada,95
Grace,98
Alan,91
```

Each piece on a line is called a **field**.  We can pull the fields apart with the **`split()`** function, which chops a string into a list wherever a separator character appears.  One thing to watch out for: everything read from a file is a *string*, even things that look like numbers.  `"95"` is not the number `95` — so if we want to do math, we need `int()` to convert it:

```python
file = open("scores.txt", "r")

total = 0
count = 0
for line in file:
    fields = line.strip().split(",")
    name = fields[0]
    score = int(fields[1])
    print(name + " scored " + str(score))
    total = total + score
    count = count + 1

file.close()
print("Average: " + str(total / count))
```

This program prints:

```text
Ada scored 95
Grace scored 98
Alan scored 91
Average: 94.66666666666667
```

Notice the pattern on each line: strip first (to get rid of the newline), *then* split.  If you split first, the newline sneaks into the last field — `"95\n"` — and while `int("95\n")` happens to work, comparing or printing that field would carry a surprise newline along with it.  Strip early and you never have to worry.

### Writing files

Writing is the mirror image of reading.  Open the file in `"w"` mode and use the **`write()`** function to send text into it:

```python
file = open("highscore.txt", "w")
file.write("High Score: 100\n")
file.write("Player: Ada\n")
file.close()
```

This program prints nothing to the screen, but afterward the file `highscore.txt` contains:

```text
High Score: 100
Player: Ada
```

Two important things to notice.  First, unlike `print`, the `write()` function does *not* add a newline for you — if you forget the `"\n"`, everything lands on one giant line!  Second, `write()` only accepts strings, so if you want to write a number, wrap it in `str()` first: `file.write(str(score) + "\n")`.

### Closing files, and the tidy habit: `with`

When you're done with a file, call **`close()`**.  This returns your "library book" and — crucially for writing — makes sure everything you wrote is actually saved to disk.  Python sometimes holds written data in a temporary holding area (a **buffer**) for efficiency, and closing the file flushes it out.  Forget to close, and your file might end up empty or incomplete!

Because forgetting `close()` is such a common slip, Python gives us a construct that closes the file for us automatically, no matter what:

```python
with open("groceries.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This program prints:

```text
milk
eggs
bread
```

The `with` statement means: "open this file, call it `file`, run the indented block, and close the file when the block ends — even if something goes wrong in the middle."  It's the tidy habit that professional Python programmers use almost exclusively, and we encourage you to use it too.

### Common mistakes to avoid

* **Forgetting that `"w"` erases the file.**  Opening in write mode wipes the file *immediately*, before you write anything.  If you want to keep what's there and add to it, use `"a"` (append) instead.
* **Leaving the newline on lines you read.**  Every line comes with `"\n"` attached.  If your comparisons mysteriously fail (`line == "milk"` is `False`!) or your output is double-spaced, you probably forgot `strip()`.
* **Forgetting to convert strings to numbers.**  Everything read from a file is a string.  `"95" + "5"` is `"955"`, not `100`!  Use `int()` or `float()` before doing math, and `str()` before writing numbers back out.
* **Trying to read a file twice without reopening it.**  The file handle's bookmark stays at the end after the first read.  Close and reopen (or use `file.seek(0)` once you learn about it) to read again.
* **Wrong filename or wrong folder.**  A `FileNotFoundError` usually means Python is looking in a different folder than you think.  Make sure the file is in the same folder your program runs from, and check the spelling (including the `.txt` extension!).
* **Forgetting to close a file you wrote.**  Your data may sit in the buffer and never reach the disk.  Use `with open(...) as file:` and this can never happen.
* **Forgetting `"\n"` when writing.**  `write()` doesn't add newlines for you, so successive writes run together on one line unless you add them yourself.

## Practice Exercises

Work through these in order — each builds on the one before.  Try each one yourself before peeking at the solution!

### Exercise 1 (warm-up): Print a file with line numbers

Create a file called `poem.txt` with a few lines of your favorite poem or song lyrics.  Write a program that reads the file and prints each line preceded by its line number and a colon.

Sample `poem.txt`:

```text
Roses are red
Violets are blue
```

Expected output:

```text
1: Roses are red
2: Violets are blue
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
# Open the file for reading; "with" closes it for us automatically
with open("poem.txt", "r") as file:
    count = 1
    for line in file:
        # strip() removes the invisible newline at the end of each line
        print(str(count) + ": " + line.strip())
        count = count + 1
```

The key idea is stripping each line before printing so that `print`'s own newline is the only one — otherwise the output would be double-spaced.

</details>

### Exercise 2: Save a shopping list

Write a program that asks the user for three items (using `input()`) and writes them to a file called `shopping.txt`, one item per line.  Then open the file in your editor to check that all three items are there, each on its own line.

Sample run:

```text
Item 1: milk
Item 2: eggs
Item 3: bread
```

Expected contents of `shopping.txt`:

```text
milk
eggs
bread
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
# "w" mode creates the file (or erases it if it already exists)
with open("shopping.txt", "w") as file:
    for i in range(3):
        item = input("Item " + str(i + 1) + ": ")
        # write() does not add a newline, so we add "\n" ourselves
        file.write(item + "\n")
```

Remember that `write()` never adds a newline for you — without the `+ "\n"`, all three items would run together on a single line.

</details>

### Exercise 3: Total up a numbers file

Create a file called `numbers.txt` containing one number per line.  Write a program that reads the file, adds up all the numbers, and prints the total.

Sample `numbers.txt`:

```text
10
25
7
```

Expected output:

```text
Total: 42
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        # Everything read from a file is a string, so convert with int()
        total = total + int(line.strip())

print("Total: " + str(total))
```

The two conversions are the heart of this one: `int()` turns the string `"10"` into the number `10` so we can add it, and `str()` turns the numeric total back into a string so we can glue it onto the message.

</details>

### Exercise 4 (challenge): Grade book with fields

Create a file called `grades.txt` where each line has a student's name and two quiz scores, separated by commas.  Write a program that reads the file and writes a *new* file called `averages.txt` containing each student's name and their average score.

Sample `grades.txt`:

```text
Ada,90,100
Grace,85,95
Alan,70,80
```

Expected contents of `averages.txt`:

```text
Ada,95.0
Grace,90.0
Alan,75.0
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
# Open both files at once: one to read from, one to write to
with open("grades.txt", "r") as infile:
    with open("averages.txt", "w") as outfile:
        for line in infile:
            # strip first (remove the newline), then split into fields
            fields = line.strip().split(",")
            name = fields[0]
            score1 = int(fields[1])
            score2 = int(fields[2])
            average = (score1 + score2) / 2
            # convert the number back to a string before writing
            outfile.write(name + "," + str(average) + "\n")
```

This exercise combines everything: reading line by line, `strip()` then `split()`, converting fields with `int()`, computing, and writing back out with `str()` and an explicit `"\n"`.

</details>

### Exercise 5 (challenge): A persistent high score

Write a program for a (pretend) game: it asks the user for their score, reads the current high score from `highscore.txt` (if the file exists), and — if the new score is higher — writes the new score back to the file and congratulates the player.  Hint: the very first time, the file won't exist, so use `try`/`except FileNotFoundError` (or just create the file with a `0` in it first) to handle that case.

Sample run (when `highscore.txt` contains `100`):

```text
Enter your score: 150
New high score: 150!
```

<details>
<summary>Click to reveal a solution to Exercise 5</summary>

```python
score = int(input("Enter your score: "))

# Read the old high score; if the file doesn't exist yet, treat it as 0
try:
    with open("highscore.txt", "r") as file:
        highscore = int(file.read().strip())
except FileNotFoundError:
    highscore = 0

if score > highscore:
    # "w" erases the old contents, which is exactly what we want here
    with open("highscore.txt", "w") as file:
        file.write(str(score) + "\n")
    print("New high score: " + str(score) + "!")
else:
    print("The high score is still " + str(highscore) + ".")
```

Notice that this is one of the rare times we *want* `"w"` mode's erasing behavior — the old high score should be replaced, not appended to.  This is also why files matter in the first place: the high score survives after the program ends, so next time you play, it's still there.

</details>

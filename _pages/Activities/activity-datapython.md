---
layout: activity
permalink: /Activities/DataPython
title: "CS170: Programming for the World Around Us - Hands-On Data Analysis with Python"


info:
  goals: 
    - To read a small CSV data file using plain Python
    - To store data in lists and dictionaries for analysis
    - To compute summary statistics (count, total, average, minimum, and maximum) with loops
    - To group and count data by category with a dictionary
    - To produce a simple, readable text report from data
  models:
    - title: "Reading a CSV File into Parallel Lists"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        # snacks.csv contains lines like:
        # name,category,price
        # Pretzels,salty,2.50
        # Apple,fruit,0.75
        
        names = []
        categories = []
        prices = []
        
        f = open("snacks.csv")
        rownum = 0
        for line in f:
            if rownum > 0:  # skip the header line
                parts = line.strip().split(",")
                names.append(parts[0])
                categories.append(parts[1])
                prices.append(float(parts[2]))
            rownum = rownum + 1
        f.close()
        
        print(names)
        print(prices)
        ]]></script>     
      questions:
        - "Why do we skip the first row of the file?  What would happen to <code>float(parts[2])</code> if we didn't?"
        - "What does <code>line.strip()</code> remove, and what could go wrong without it?"
        - "These three lists are called <em>parallel lists</em>: <code>names[2]</code>, <code>categories[2]</code>, and <code>prices[2]</code> all describe the same snack.  What is at index 1 of each list?"
    - title: "Computing Statistics with a Loop"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        prices = [2.50, 0.75, 3.25, 1.00, 2.00]
        
        total = 0
        for price in prices:
            total = total + price
        
        average = total / len(prices)
        print("Average price:", average)
        ]]></script>     
      questions:
        - "Trace this loop by hand: what is <code>total</code> after each of the five iterations?"
        - "Modify the loop to also find the largest price, and use parallel lists to print the <em>name</em> of that most expensive snack."
    - title: "Grouping and Counting with a Dictionary"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        categories = ["salty", "fruit", "salty", "candy", "fruit"]
        
        counts = {}
        for category in categories:
            if category in counts:
                counts[category] = counts[category] + 1
            else:
                counts[category] = 1
        
        print(counts)
        ]]></script>     
      questions:
        - "What does this program print?  Trace the dictionary's contents after each loop iteration to check yourself."
        - "Why do we need the <code>if category in counts</code> check?  What error do you get without it?"
  additional_reading:
    - link: https://runestone.academy/ns/books/published/py4e-int/files/toctree.html
      title: Files
    - link: https://runestone.academy/ns/books/published/py4e-int/dictionaries/toctree.html
      title: Dictionaries
      
tags:
  - python
  - lists
  - dictionaries
  - io
  - data
  
---

## Notes and Walkthrough

You have learned about variables, conditionals, loops, functions, lists, and dictionaries — today they all come together to do the single most common thing people use Python for in the real world: **answering questions about data**.  Biologists tally species observations, athletic trainers summarize workout logs, businesses total their sales, and journalists fact-check claims — all with programs shaped exactly like the one you'll build in this activity.  No new language features are required; the skill we're practicing is *composing* the pieces you already know.

### The Shape of Every Data Analysis Program

Nearly every small data analysis program has the same three-part shape:

1. **Read**: open the file and load its values into lists (converting text to numbers as needed).
2. **Compute**: loop over the lists to count, total, average, find the biggest and smallest, or group by category.
3. **Report**: print the answers in a way a human can read.

Keep this shape in mind and even a blank editor won't feel intimidating: you always know what the first section of your program will do.

### Our Dataset

We'll analyze a tiny snack bar sales file, `snacks.csv`.  Create it in your editor by making a new file with exactly these lines (or invent your own snacks — the program won't mind!):

```
name,category,price
Pretzels,salty,2.50
Apple,fruit,0.75
Trail Mix,salty,3.25
Banana,fruit,1.00
Chocolate Bar,candy,2.00
```

The first line is the **header**: it names the columns for humans.  Every other line is one **record**: a snack's name, its category, and its price, separated by commas.  This is a *CSV* ("comma separated values") file — the humble format behind an enormous amount of the world's data, and one you can open in any spreadsheet program too.

### Step 1: Read — From Text File to Lists

The first model above reads the file into three *parallel lists*.  Two conversions happen along the way, and they trip up everyone at first:

- Each `line` arrives as a **string** ending in an invisible newline character; `line.strip()` removes it.  Without it, the last column of every row would be `"2.50\n"` — and printing your data would look mysteriously double-spaced.
- Everything read from a file is text, even the numbers!  `"2.50" + "0.75"` is `"2.500.75"` (string gluing), not `3.25`.  That's why we convert with `float(parts[2])` *before* appending.

Here is a trace of the reading loop for the first three lines of the file:

| Iteration | `line` (after strip) | `rownum` at loop top | What happens | `prices` afterward |
|-----------|----------------------|------|--------------|--------------------|
| 1 | `name,category,price` | 0 | Header: the `if` is False, nothing appended | `[]` |
| 2 | `Pretzels,salty,2.50` | 1 | Split into 3 parts; `2.50` becomes the float `2.5` | `[2.5]` |
| 3 | `Apple,fruit,0.75` | 2 | Split; `0.75` becomes `0.75` | `[2.5, 0.75]` |

After the whole file, `names` has 5 strings, `categories` has 5 strings, and `prices` has 5 floats — and index `i` of each list describes the same snack.

### Step 2: Compute — Asking the Data Questions

**How many snacks?**  That's just `len(names)`.

**What do they cost on average?**  Total them with the *accumulator pattern* — start a running total at 0 and add each value:

```python
total = 0
for price in prices:
    total = total + price
average = total / len(prices)
```

This program prints (given our file):

```
Average price: 1.9
```

**What's the most expensive snack?**  Track the best-so-far *index*, so the parallel lists can tell you its name:

```python
biggest = 0  # index of the priciest snack seen so far
for i in range(len(prices)):
    if prices[i] > prices[biggest]:
        biggest = i
print("Most expensive:", names[biggest], "at $" + str(prices[biggest]))
```

Trace it against our data — `prices` is `[2.5, 0.75, 3.25, 1.0, 2.0]`:

| `i` | `prices[i]` | `prices[biggest]` before | Is it bigger? | `biggest` after |
|-----|-------------|--------------------------|---------------|-----------------|
| 0 | 2.5  | 2.5  | no (tie with itself) | 0 |
| 1 | 0.75 | 2.5  | no  | 0 |
| 2 | 3.25 | 2.5  | yes | 2 |
| 3 | 1.0  | 3.25 | no  | 2 |
| 4 | 2.0  | 3.25 | no  | 2 |

The loop ends with `biggest = 2`, so it prints `Most expensive: Trail Mix at $3.25`.

**How many snacks per category?**  Categories are *labels*, so counting them calls for a dictionary mapping each label to its count — the third model above.  Trace its loop over `["salty", "fruit", "salty", "candy", "fruit"]`:

| Iteration | `category` | Already in `counts`? | `counts` afterward |
|-----------|------------|----------------------|--------------------|
| 1 | `salty` | no  | `{'salty': 1}` |
| 2 | `fruit` | no  | `{'salty': 1, 'fruit': 1}` |
| 3 | `salty` | yes | `{'salty': 2, 'fruit': 1}` |
| 4 | `candy` | no  | `{'salty': 2, 'fruit': 1, 'candy': 1}` |
| 5 | `fruit` | yes | `{'salty': 2, 'fruit': 2, 'candy': 1}` |

### Step 3: Report — Presenting the Answers

Raw numbers dumped to the screen make readers work too hard.  A few `print` calls turn your analysis into a report:

```python
print("SNACK BAR SALES REPORT")
print("======================")
print("Snacks on the menu:", len(names))
print("Average price: $" + str(round(average, 2)))
print("Most expensive:", names[biggest])
print()
print("By category:")
for category in counts:
    print("  " + category + ": " + str(counts[category]))
```

This program prints:

```
SNACK BAR SALES REPORT
======================
Snacks on the menu: 5
Average price: $1.9
Most expensive: Trail Mix

By category:
  salty: 2
  fruit: 2
  candy: 1
```

Notice the loop at the bottom: looping over a dictionary visits its *keys*, and `counts[category]` looks up each one's value.

### Common Mistakes to Avoid

- **Forgetting to skip the header** — your program crashes with `ValueError: could not convert string to float: 'price'`.  Now you know exactly what that message means!
- **Forgetting `float(...)`** — no crash, but totals come out as strangely glued-together text, or you get a `TypeError` when dividing.
- **Dividing by `len(...)` of an empty list** — if your file path is wrong or the file is empty, you'll divide by zero.  Print `len(names)` early to confirm the data actually loaded.
- **Using a new dictionary key without creating it** — `counts[category] = counts[category] + 1` on a first-time key raises a `KeyError`; that's what the `if category in counts` check prevents.
- **Mixing up index and value** — `prices[biggest]` (with `biggest` an index) versus `biggest` itself.  If your "maximum price" prints as `2`, you printed the index!

## Practice Exercises

Work through these in order — each builds on the last.  **Choose your own dataset if you like**: instead of snacks, make a CSV of your music library (title, genre, minutes), a sports team (player, position, points), books you've read (title, genre, pages) — anything with one text column, one category column, and one numeric column will work with exactly the same code.

### Exercise 1 (warm-up): Count and Total

Read `snacks.csv` (or your own file) into parallel lists and print how many records it contains and the total of the numeric column.  Expected output for the snack data: `5 snacks totaling $9.5`.

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
names = []
prices = []

f = open("snacks.csv")
rownum = 0
for line in f:
    if rownum > 0:
        parts = line.strip().split(",")
        names.append(parts[0])
        prices.append(float(parts[2]))
    rownum = rownum + 1
f.close()

total = 0
for price in prices:
    total = total + price

print(str(len(names)) + " snacks totaling $" + str(total))
```

The reading loop is the same pattern as the model; the totaling loop is the accumulator pattern.

</details>

### Exercise 2: Minimum and Maximum

Print the name of the cheapest *and* most expensive snack.  Expected output: `Cheapest: Apple` and `Most expensive: Trail Mix`.

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
# (read the file into names and prices as in Exercise 1 first)

cheapest = 0
biggest = 0
for i in range(len(prices)):
    if prices[i] < prices[cheapest]:
        cheapest = i
    if prices[i] > prices[biggest]:
        biggest = i

print("Cheapest:", names[cheapest])
print("Most expensive:", names[biggest])
```

Both searches track an *index* so the parallel `names` list can supply the answer's name.

</details>

### Exercise 3: Group Averages

Using a dictionary, compute the *average price per category*.  Hint: you'll need two dictionaries (or a dictionary whose values are lists): one accumulating each category's total, one counting its members.  Expected output includes `fruit: 0.875`.

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
# (read the file into categories and prices first)

totals = {}
counts = {}
for i in range(len(prices)):
    category = categories[i]
    if category in totals:
        totals[category] = totals[category] + prices[i]
        counts[category] = counts[category] + 1
    else:
        totals[category] = prices[i]
        counts[category] = 1

for category in totals:
    print(category + ": " + str(totals[category] / counts[category]))
```

Two parallel dictionaries share the same keys, just as parallel lists share the same indices.

</details>

### Exercise 4: Filter and Report

Ask the user for a price limit with `input()`, then print a formatted report of only the snacks at or under that limit, followed by how many matched.  Remember that `input()` gives you a string!

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
# (read the file into names and prices first)

limit = float(input("Price limit: $"))

print("Snacks within your budget:")
matches = 0
for i in range(len(prices)):
    if prices[i] <= limit:
        print("  " + names[i] + " ($" + str(prices[i]) + ")")
        matches = matches + 1
print(str(matches) + " snack(s) found.")
```

The `float(...)` around `input()` matters: comparing a string to a float raises a `TypeError`.

</details>

### Exercise 5 (challenge): Write the Report to a File

Combine everything into a full report — count, average, cheapest, most expensive, and per-category counts — and *write* it to `report.txt` instead of the screen, using `open("report.txt", "w")` and `file.write(...)`.  Open the result in your editor to admire it.  (Remember: `write` does not add newlines for you — end each line with `"\n"`.)

<details>
<summary>Click to reveal a solution to Exercise 5</summary>

```python
# (read the file and compute total, average, biggest, counts as above)

report = open("report.txt", "w")
report.write("SNACK BAR SALES REPORT\n")
report.write("======================\n")
report.write("Snacks on the menu: " + str(len(names)) + "\n")
report.write("Average price: $" + str(round(average, 2)) + "\n")
report.write("Most expensive: " + names[biggest] + "\n")
report.write("By category:\n")
for category in counts:
    report.write("  " + category + ": " + str(counts[category]) + "\n")
report.close()

print("Report written to report.txt")
```

Forgetting `report.close()` can leave the file empty — Python may not flush your writes to disk until the file is closed.

</details>

### Where You'll Use This Next

This read-compute-report shape is exactly the skeleton of the [Respiratory Tracker assignment](../Assignments/RespiratoryTracker) (reading sensor data and computing breathing rates), and it's a natural backbone for many final projects.  If today's activity clicked, you already know how to start both.

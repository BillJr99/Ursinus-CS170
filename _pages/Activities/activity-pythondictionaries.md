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

## Notes and Walkthrough

Suppose you want to look up a friend's phone number.  You wouldn't want to read every entry in the phone book from the top until you happened upon their name!  Instead, you use what you *know* (their name) to jump straight to what you *want* (their number).  That act of using one piece of data to find another is called a **lookup**, and it's such a common need in programming that Python gives us a whole data structure for it: the **dictionary**.

A **dictionary** is a collection of pairs.  Each pair has a **key** (the thing you look things up *by*, like a name in the phone book) and a **value** (the thing you're looking *for*, like the phone number).  We say a dictionary **maps** keys to values.  Every key in a dictionary must be unique -- just like a phone book would be pretty confusing if the same exact name appeared twice with different numbers -- but many keys are allowed to have the same value.

How is this different from a list?  A list numbers its elements for you (index 0, 1, 2, ...), so the only way to find something is by its position.  A dictionary lets *you* choose the labels.  Instead of remembering "the phone number is at index 7," you just ask for `phonebook["Taylor"]`.

### Creating a Dictionary and Adding Pairs

We write a dictionary with curly braces `{}` (notice: *curly* braces, not the square brackets we used for lists).  We can start with an empty dictionary and add pairs one at a time, or write the pairs right inside the braces using a colon between each key and its value.

To add a pair, we write the key in square brackets after the dictionary's name and assign it a value -- it looks just like assigning to a list index, except the "index" is a key we made up ourselves:

```python
phonebook = {}                     # an empty dictionary
phonebook["Taylor"] = "555-1234"   # add a key-value pair
phonebook["Jordan"] = "555-9876"   # add another
print(phonebook)

# or, all at once:
menu = {"coffee": 3, "bagel": 2, "muffin": 4}
print(menu)
```

This program prints:

```text
{'Taylor': '555-1234', 'Jordan': '555-9876'}
{'coffee': 3, 'bagel': 2, 'muffin': 4}
```

Try it out!  What do you think happens if you assign to a key that's *already* in the dictionary?

### Looking Up and Updating Values

To look up a value, we write the key in square brackets -- and to update a value, we just assign to that key again.  Because keys are unique, assigning to an existing key *replaces* the old value rather than adding a second copy:

```python
menu = {"coffee": 3, "bagel": 2, "muffin": 4}

print("A bagel costs ${}".format(menu["bagel"]))

menu["coffee"] = 4          # the price of coffee went up!
menu["tea"] = 2             # a brand new key: this ADDS a pair

print(menu)
```

This program prints:

```text
A bagel costs $2
{'coffee': 4, 'bagel': 2, 'muffin': 4, 'tea': 2}
```

Notice the two assignments do different things: `menu["coffee"] = 4` found an existing key and *updated* its value, while `menu["tea"] = 2` used a new key and *added* a pair.  Same syntax, and the dictionary figures out which one you meant by checking whether the key already exists.

Here's a trace of the dictionary changing over time:

| Step | Line | `menu` after this line | What happens |
|------|------|------------------------|--------------|
| 1 | `menu = {"coffee": 3, "bagel": 2, "muffin": 4}` | `{'coffee': 3, 'bagel': 2, 'muffin': 4}` | The dictionary is created with 3 key-value pairs |
| 2 | `print(menu["bagel"])` | (unchanged) | Lookup by key: output is `2`.  Nothing is modified |
| 3 | `menu["coffee"] = 4` | `{'coffee': 4, 'bagel': 2, 'muffin': 4}` | `"coffee"` already exists, so its value is *updated* from 3 to 4 |
| 4 | `menu["tea"] = 2` | `{'coffee': 4, 'bagel': 2, 'muffin': 4, 'tea': 2}` | `"tea"` is a new key, so a new pair is *added* |

But what if you look up a key that isn't there, like `menu["pizza"]`?  Python stops your program with a `KeyError`, the dictionary cousin of the list's `IndexError`.  How can we avoid that?  Read on!

### Checking Membership with `in`

Before looking up a key you're not sure about, you can ask whether it exists using the `in` keyword.  The expression `key in dictionary` is `True` if the key is present and `False` if it isn't -- perfect for an `if` statement:

```python
menu = {"coffee": 3, "bagel": 2, "muffin": 4}

if "pizza" in menu:
    print("Pizza costs ${}".format(menu["pizza"]))
else:
    print("Sorry, we don't sell pizza.")

print("coffee" in menu)
```

This program prints:

```text
Sorry, we don't sell pizza.
True
```

One subtlety: `in` checks the *keys*, not the values.  `3 in menu` is `False` here even though 3 is one of the values, because 3 is not a key.

### Looping Over a Dictionary

Just like a list, we can visit everything in a dictionary with a loop.  If you loop over a dictionary directly, Python hands you each *key*, and you can look up its value inside the loop.  Or, you can use the dictionary's `.items()` method to get each key *and* value together in one step -- you saw this in the model at the top of the page:

```python
menu = {"coffee": 3, "bagel": 2, "muffin": 4}

for item in menu:                  # loops over the KEYS
    print("{} costs ${}".format(item, menu[item]))

for item, price in menu.items():   # keys AND values together
    print("{}: ${}".format(item, price))
```

This program prints:

```text
coffee costs $3
bagel costs $2
muffin costs $4
coffee: $3
bagel: $2
muffin: $4
```

Both loops visit the same pairs -- `.items()` just saves you the lookup step inside the loop.  Use whichever reads more clearly to you.

### Counting Things with a Dictionary

Here's one of the most useful patterns in all of programming.  Suppose we want to count how many times each word appears in a sentence.  With a dictionary, the plan is simple: the keys are the words we've seen, and the values are the counts.  For each word, if we've seen it before, add one to its count; if it's brand new, start its count at 1.  Notice how `in` protects us from a `KeyError`:

```python
words = ["duck", "duck", "goose", "duck"]
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1   # seen it before: add one
    else:
        counts[word] = 1                  # first sighting: start at 1

print(counts)
```

This program prints:

```text
{'duck': 3, 'goose': 1}
```

Let's trace it carefully, one loop pass at a time, and watch the dictionary grow and change:

| Step | `word` this pass | Is `word in counts`? | `counts` after this pass | What happens |
|------|------------------|----------------------|--------------------------|--------------|
| Before loop | - | - | `{}` | We start with an empty dictionary |
| 1 | `"duck"` | No | `{'duck': 1}` | New key: `"duck"` is added with value 1 |
| 2 | `"duck"` | Yes | `{'duck': 2}` | Existing key: its value is updated from 1 to 2 |
| 3 | `"goose"` | No | `{'duck': 2, 'goose': 1}` | New key: `"goose"` is added with value 1 |
| 4 | `"duck"` | Yes | `{'duck': 3, 'goose': 1}` | Existing key: its value is updated from 2 to 3 |
| After loop | - | - | `{'duck': 3, 'goose': 1}` | Output: `{'duck': 3, 'goose': 1}` |

This little pattern -- check with `in`, then add or update -- shows up everywhere: counting votes, tallying grades, tracking how many times each micro:bit ID has sent you a radio message.  Once you can trace this table on your own, you've really got dictionaries!

### When Should You Use a Dictionary Instead of a List?

Both structures hold collections of data, so how do you choose?  Ask yourself: *how will I look things up?*

* If your data is naturally a numbered sequence -- the 1st, 2nd, 3rd reading from a sensor, where order matters and positions are meaningful -- use a **list**.
* If you look things up by a meaningful label -- a name, a course number like `"CS170"`, a word -- use a **dictionary**.  `courses["CS170"]` says exactly what you mean; scanning a list for the entry whose first item is `"CS170"` makes the computer (and the reader of your code) do extra work.
* If you don't know ahead of time *what* items will show up (like the words in a sentence), a dictionary lets you add keys as you discover them -- that's exactly what made the counting example so tidy.

### Common mistakes to avoid

* **`KeyError` on a missing key.**  Looking up `menu["pizza"]` when `"pizza"` isn't a key crashes your program.  Check with `if "pizza" in menu:` first (or remember this is exactly what the counting pattern's `if`/`else` is for).
* **Confusing keys and values.**  You look up *by key* to get a *value*.  There's no direct `menu[3]` to ask "which item costs 3?" -- if you need to search by value, you have to loop over `.items()` and check each one.
* **Using `[]` when you mean `{}`.**  Square brackets `[]` create a *list*; curly braces `{}` create a *dictionary*.  If you write `menu = []` and then try `menu["coffee"] = 3`, Python complains that list indices must be integers.
* **Expecting duplicate keys.**  Assigning to an existing key replaces its value -- it never creates a second pair.  If you need several values under one key, store a *list* as the value (like the `students` list inside the complex dictionary model above).
* **Assuming a position/order like a list.**  There's no `menu[0]` "first pair" -- dictionaries are looked up by key, not by position.
* **Forgetting that `in` checks keys, not values.**  `"coffee" in menu` is `True`; `3 in menu` is `False` even if some value is 3.

## Practice Exercises

Try each one before revealing the solution -- tracing on paper counts as trying!

### Exercise 1 (warm-up)

Create a dictionary called `ages` that maps `"Alex"` to 19 and `"Lee"` to 20.  Then print Lee's age by looking it up.

Expected output:

```text
20
```

<details>
<summary>Click to reveal a solution to Exercise 1</summary>

```python
ages = {}          # start with an empty dictionary (curly braces!)
ages["Alex"] = 19  # add a pair: key "Alex", value 19
ages["Lee"] = 20   # add another pair
print(ages["Lee"]) # look up the value by its key
```

You could also create it all at once with `ages = {"Alex": 19, "Lee": 20}` -- both are correct.

</details>

### Exercise 2 (updating and adding)

Start with `stock = {"apples": 5, "bananas": 2}`.  Someone buys a banana (subtract 1 from its count), and a shipment of 10 oranges arrives (a new key).  Print the final dictionary.

Expected output:

```text
{'apples': 5, 'bananas': 1, 'oranges': 10}
```

<details>
<summary>Click to reveal a solution to Exercise 2</summary>

```python
stock = {"apples": 5, "bananas": 2}
stock["bananas"] = stock["bananas"] - 1  # look up the old value, subtract, store it back
stock["oranges"] = 10                    # new key, so this ADDS a pair
print(stock)
```

The key idea: the same square-bracket assignment either updates an existing key or adds a new one, depending on whether the key is already there.

</details>

### Exercise 3 (membership and looping)

Given `birthdays = {"Alex": "May 4", "Lee": "Oct 31", "Sam": "Feb 29"}`, first check whether `"Jordan"` is in the dictionary and print `"No birthday on file for Jordan"` if not.  Then loop over the dictionary and print each person's birthday, one per line, in the form `Alex: May 4`.

Expected output:

```text
No birthday on file for Jordan
Alex: May 4
Lee: Oct 31
Sam: Feb 29
```

<details>
<summary>Click to reveal a solution to Exercise 3</summary>

```python
birthdays = {"Alex": "May 4", "Lee": "Oct 31", "Sam": "Feb 29"}

if "Jordan" not in birthdays:            # 'in' checks the KEYS
    print("No birthday on file for Jordan")

for name, day in birthdays.items():      # keys and values together
    print("{}: {}".format(name, day))
```

The key idea: checking with `in` before looking up avoids a `KeyError`, and `.items()` hands you each key and value as a pair.

</details>

### Exercise 4 (challenge)

Write a program that counts how many times each letter grade appears in the list `grades = ["A", "B", "A", "C", "B", "A"]`, using a dictionary.  Then print each grade and its count.

Expected output:

```text
A: 3
B: 2
C: 1
```

<details>
<summary>Click to reveal a solution to Exercise 4</summary>

```python
grades = ["A", "B", "A", "C", "B", "A"]
counts = {}                            # keys will be grades, values will be counts

for grade in grades:
    if grade in counts:
        counts[grade] = counts[grade] + 1  # seen before: add one
    else:
        counts[grade] = 1                  # first time: start the count at 1

for grade, count in counts.items():
    print("{}: {}".format(grade, count))
```

This is the counting pattern from the notes: check membership with `in`, then either update or add.  Try tracing `counts` after each loop pass, just like the duck-duck-goose table above!

</details>

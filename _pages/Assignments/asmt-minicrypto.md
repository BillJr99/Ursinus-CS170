---
layout: assignment
permalink: /Assignments/MiniCrypto
title: "CS170: Programming for the World Around Us - Mini RSA Cryptography"


info:
  coursenum: CS170
  points: 100
  goals:
    - To implement mathematical theory in the Python programming language
    - "To implement algorithms that iterate over characters in a text variables"
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
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
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, descriptive comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, descriptive comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions    
      
tags:
  - python
  - math
  - cryptography
  
---

This assignment is adapted from Prof. Mongan's assignments in communications and introductory cryptography \[[^1], [^2], [^3]\], and from the CS Unplugged Public Key Encryption lesson module \[[^4]\].

[^1]: William M. Mongan. 2012. An integrated introduction to network protocols and cryptography to high school students (abstract only). In Proceedings of the 43rd ACM technical symposium on Computer Science Education (SIGCSE ’12). Association for Computing Machinery, New York, NY, USA, 664. DOI:[https://doi.org/10.1145/2157136.2157364](https://doi.org/10.1145/2157136.2157364)
[^2]: William M. Mongan. 2011. Networking Applications, Protocols, and Cryptography with Java. Google CS4HS Workshop at the University of Pennsylvania, Philadelphia, PA.
[^3]: William M. Mongan. 2012. Networking Applications, Protocols, and Cryptography with Java. Tapia Workshop at the University of Pennsylvania, Philadelphia, PA.
[^4]: Bell, Witten, and Fellows. 1998. Computer Science Unplugged - Public Key Encryption. Available at [https://classic.csunplugged.org/public-key-encryption/](https://classic.csunplugged.org/public-key-encryption/)

## Step 1: Encrypting Characters Using A Public/Private Key that We Create

### Identify Two Prime Numbers from which to Calculate our Public and Private Key
Write a function to generate a public and private key pair and print these to the screen.  

A number N is prime if no number from 2 to N-1 divides evenly into it.  In mathematical terms, we write: <span>\\((N (mod \; k)) \ne 0\\)</span> for all <span>\\(k \in [2, N-1]\\)</span>, but we just mean that no number has a remainder when divided into N (that is, the modulus is never 0), and thus N is prime.  We need two prime numbers to form our keys.

The larger the prime numbers, the harder it is to break your key.  We'll explore this later, but the idea is that it is very easy to figure out that 21 has two prime factors (7 and 3), but much harder to factor larger numbers because you basically have to try every possibility.  In practice, prime numbers that are hundreds of digits long are not uncommon!  The community is actively searching for larger prime numbers to improve the secrecy of the key.   For our program, prime numbers between about 17 and 997 are sufficient.  We want to be able to encrypt every character in the standard western keyboard set, and the [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html) provides for 127 such characters.  Extensions to the ASCII table support additional characters and character sets, so really we should plan on much larger keys, but this is usually not a concern since we want to use large prime numbers to form our keys, anyway.  Go ahead and choose two prime values from [this list](https://en.wikipedia.org/wiki/List_of_prime_numbers).

Once you generate those prime numbers (let's call them A and B), you can generate your public key (E, C) and private key (D, C).  Recall that the value C is shared between the public and private key, and that E and C are made available to others so that they can encrypt data to you.  Your private key (D, C) is needed to decrypt those values, so you must keep the value D a secret!

### Generate a Public/Private Key Pair
These prime numbers are not actually your keys, but rather, we will use these prime numbers to generate a public and private key value that are inverses of each other.

To generate your public key:

1. Choose two prime numbers A and B.  Make these prime numbers at least 2 digits in length, but no more than 3 digits.  In practice, the values are much larger, but this is a demonstration.  You've done this already!  Ask the user to input these values from the keyboard and assign them to variables called `A` and `B`.
2. Compute <span>\\(C = AB\\)</span>.  Since the ASCII table contains 128 entries (numbered 0 through 127), C should be larger than 127, so that all these characters can be represented.  If you send messages with characters from the extended ASCII table, C should be greater than 255.
3. Compute <span>\\(M = \phi(C)\\)</span> by computing `(A-1)*(B-1)`.  <span>\\(\phi\\)</span> is known as [Euler's Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function), a mathematical function with properties that enable us to ensure that the public and private key are inverses of one another.  When `C` is the product of two prime numbers (as ours is), you can simply calculate `(A-1)*(B-1)`, which is much faster than computing it manually as we would for other values.  
 
However, you can compute it by calling `totient(C)` from a Python program, assuming you have imported this library: `from sympy.ntheory.factor_ import totient`.  Additionally, you could write your own totient function using a loop:
```python
def totient(n):
  answer = 1

  for i in range(2, n):
    if math.gcd(n, i) == 1:
      answer = answer + 1

  return answer
```

Verify that your totient of `C` is equal to `(A-1)*(B-1)` by printing both values to the screen!
4. Compute E, a value co-prime to M.  The `coprime(X)` function can help you do this, and you can copy it into your program.
5. Compute D, the modular inverse of <span>\\(E (mod \; M)\\)</span>.  The formula to compute the modular inverse uses the Euler's Totient function that we saw earlier, and is: <span>\\(E^{\phi(M)-1} (mod M)\\)</span>.  Recall that the `**` operator will raise to an exponent, and the `%` operator will compute the modulus.

Here is a `coprime` function that you can paste into your program and use:
```python
def coprime(M):
  result = 2 * M + 1001 # int(random.uniform(M, 2*M))

  while math.gcd(M, result) != 1:
    result = result + 1

  return result
```

Print `E`, `D`, and `C` to the screen.  All the other variables are no longer needed!  

`E` and `C` make up your public key.  You can share these values with the world.  `D` is your private key, and will be used to invert the values people encrypt to you back to their original message.  Share `E` and `C` on the discussion board for others to see!

## Step 2: Communicating Secret Messages to a Classmate Using Only Their Public Key
Now, create a new file, and write a program to input your classmate's public key.  You can exchange keys via the discussion board.  Ask the user to enter a character on the keyboard.  To convert this to its ASCII numeric value, you can create a variable whose value is `ord(x)`, where `x` is the character variable value you just obtained from the user.  Run your program and enter characters, one by one, to obtain their encrypted values.  

The formula to encrypt a value is:

<span>\\(x^{E} (mod C)\\)</span>

Post those encrypted values on the board to your classmate so they can decrypt your message.  The idea is that no one can decrypt these values unless they know the value of `D`, which only your buddy knows!  

## Step 3: Receiving and Decrypting a Message from Your Partner Using Your D and C Key Values

Similarly, create another program, and this time, accept your own private key (D and C) as parameters.  Input a numeric value (that you received from a classmate).  You can use the `int()` function to convert the input to a numeric value, and then use `chr()` to convert it from its ASCII value to the corresponding letter.  

The formula to decrypt is:

<span>\\(x^{D} (mod C)\\)</span>

Print that to the screen.  It should be the message intended for you!  Post the result to the message board, and when someone posts your message, let them know if they decrypted it correctly!

**Notice that you always encrypt with the public key, and always decrypt with the private key.  But notice that the formulas are symmetrical, and invert one another!  What do you think would happen if you encrypt something with your own private key.  Who could decrypt it?  Why might you ever want to do this (hint - what information do you know if you are able to decrypt something that was encrypted with a particular person's public key)?**

## Step 4: Cracking a Public Key to Calculate the Private Key
Because we used small key values, it is actually possible to recover someone's private key from their public key.  It is important to choose a key that is so large that this is computationally infeasible!  In our example, the keys were small, and so it is rather easy to do.

To compute the private key that goes with a public key, recall the formula:

<span>\\(E^{\phi(M)-1} (mod M)\\)</span>

You know `E`, but you don't know `M`.  What is the formula for `M`?  It is the Euler's Totient of `C`.  You do know the value of `C`, so using Part 1 as a guide, compute the Totient of `C`, call that value `M`, and use that to compute `D` using the formula above.  The larger the key, the longer this will take, but the code and the math are the same regardless.  

Display on the screen, and then post, the private key of your buddies to the discussion board too - and confirm with one another if you got it right!

## Summary

As a summary, here is what to do.  You might want to write separate programs (projects) for each of these, and export and submit each of them.  It's up to you!

* Generate a key to share with the class.  Share your `E` and `C` public key with the class, but keep your `D` private key value a secret that you will use later!
* Use someone else's public key (`E` and `C`) to encrypt a secret message to them, one character at a time.  Share your encrypted numeric values with that person.
* When someone shares a message with you, use your own private key (`D` and `C`) to decrypt them to characters, one by one, and print them to the screen.  What message did you get?  Note that this `C` is different than the one you used to encrypt something to your classmate in the prior step: you used their `C` value instead!  Here, you are using your own value of `C`.
* Take someone's public key (`E` and `C`) and compute `M` and `D` from it.  Did it match their private key?  Why is this hard to do with actual public keys on the internet?

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## A Note About Export Controls

Some governments, including the United States, have [export controls on cryptographic technologies](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States). 

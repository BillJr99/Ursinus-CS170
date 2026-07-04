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
      preemerging: "The programs do not run, or key generation does not produce and print values for E, D, and C"
      beginning: "Key generation runs but produces an invalid key pair - for example, C = A*B is not larger than 127, M is not computed as (A-1)*(B-1), or D is not the modular inverse of E - so characters encrypted with the public key do not decrypt back to the original message"
      progressing: "Key generation, encryption (applying x**E % C to the ord() value of each typed character), and decryption (applying x**D % C and converting back with chr()) all work on tested characters, but one component has a minor issue: for example, the Step 4 cracking program does not recover a classmate's D from their public key, or the totient of C is not verified against (A-1)*(B-1)"
      proficient: "All four programs work end-to-end: key generation reads two primes A and B from the keyboard and prints a valid E, D, and C (with the totient of C verified against (A-1)*(B-1)); encryption converts a typed character with ord() and computes x**E % C; decryption computes x**D % C and converts back with chr() to recover the original character; and the Step 4 cracking program recovers a private key D from a public key E and C"
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: "Indentation and spacing are inconsistent enough to make the programs hard to follow, or indentation errors (for example, inside the totient or coprime loops) prevent the programs from running"
      beginning: "Indentation and spacing are mostly consistent, with a few isolated issues such as uneven spacing around the ** and % operators"
      progressing: "Indentation and spacing are consistent across the key-generation, encryption, decryption, and cracking files, with only a minor adjustment needed"
      proficient: "Indentation and spacing are consistent throughout every file: loop and function bodies are indented one level, operators are consistently spaced, and blank lines separate the input, computation, and output steps of each program"
    - weight: 10
      description: Code Quality
      preemerging: "The code has not been run through pylint, and there are widespread style issues such as unclear one-letter names (beyond the documented key variables A, B, C, D, E, and M) or large copy-pasted blocks shared across the programs"
      beginning: "pylint reports several warnings that were not addressed (for example, unused imports or variables left over from experimenting), or logic like the totient computation is copy-pasted where a function would do"
      progressing: "The code runs nearly clean through pylint with only one or two unaddressed warnings; helper functions like totient and coprime are used rather than duplicating their logic, with a few isolated style issues remaining"
      proficient: "The code follows the course style guide and runs cleanly through pylint (no warnings other than those the instructor has designated as acceptable): descriptive snake_case names for everything beyond the mathematical key variables A, B, C, D, E, and M; no unused variables or imports; and shared logic like totient lives in a function rather than duplicated blocks"
    - weight: 10
      description: Code Documentation
      preemerging: "The code contains no comments, or comments are so sparse that a reader cannot tell which program generates keys, which encrypts, and which decrypts"
      beginning: "Some sections are commented, but key steps such as computing M = (A-1)*(B-1) or the modular inverse that produces D are unexplained"
      progressing: "Comments are present at each major step, but they mostly restate the code rather than explaining why (for example, why C must be larger than 127, or why D must be kept secret)"
      proficient: "Every function (including totient and coprime) has a comment or docstring stating its purpose, inputs, and output; non-obvious steps such as why C must exceed 127, why encryption computes x**E % C, and why D must stay secret are explained; comments explain why, not just what"
    - weight: 10
      description: Writeup and Submission
      preemerging: "No README.md is committed to the repository, or the repository is missing one or more of the key-generation, encryption, decryption, or cracking programs"
      beginning: "A README.md is committed, but it does not answer the bolded question (what happens if you encrypt with your own private key, and who could decrypt it), or the final version of the code was not pushed to GitHub before the deadline"
      progressing: "The README.md answers the bolded question and describes how to run the programs, with a minor omission such as not saying which program to run first or what to type at a prompt"
      proficient: "The README.md answers the bolded question about encrypting with your own private key, explains how to run the key-generation, encryption, decryption, and cracking programs and what to type at each prompt, describes the message exchange with your classmate, and the final version of all files is committed and pushed to GitHub"
      
tags:
  - python
  - math
  - cryptography
  
---

## Purpose

Every time you shop online, send a private message, or log into a website, cryptography like the RSA algorithm you'll build here keeps your information safe from eavesdroppers.  In this assignment, you will implement a miniature version of that real-world system in Python: you'll generate your own public and private keys, exchange secret messages with your classmates, and even see for yourself why small keys can be cracked - and why real keys are hundreds of digits long.  Along the way, you'll practice translating mathematical formulas into code and iterating over the characters of a text message.

This assignment is adapted from Prof. Mongan's assignments in communications and introductory cryptography \[[^1], [^2], [^3]\], and from the CS Unplugged Public Key Encryption lesson module \[[^4]\].

[^1]: William M. Mongan. 2012. An integrated introduction to network protocols and cryptography to high school students (abstract only). In Proceedings of the 43rd ACM technical symposium on Computer Science Education (SIGCSE ’12). Association for Computing Machinery, New York, NY, USA, 664. DOI:[https://doi.org/10.1145/2157136.2157364](https://doi.org/10.1145/2157136.2157364)
[^2]: William M. Mongan. 2011. Networking Applications, Protocols, and Cryptography with Java. Google CS4HS Workshop at the University of Pennsylvania, Philadelphia, PA.
[^3]: William M. Mongan. 2012. Networking Applications, Protocols, and Cryptography with Java. Tapia Workshop at the University of Pennsylvania, Philadelphia, PA.
[^4]: Bell, Witten, and Fellows. 1998. Computer Science Unplugged - Public Key Encryption. Available at [https://classic.csunplugged.org/public-key-encryption/](https://classic.csunplugged.org/public-key-encryption/)

## Getting Started with GitHub

Accept the assignment invitation using the GitHub Classroom link, and clone your repository to your computer to get started.  As you work, commit your changes early and often with meaningful messages, and push them before the deadline: your latest pushed commit is what is graded.  If this is new to you, the [Using Git and GitHub](../Modules/Github/Module) and [Cloning an Assignment with GitHub Classroom](../Modules/GithubClassroom/Module) modules walk you through it step-by-step.

Your Code Quality score is informed by pylint: see the [Code Quality and Linting module](../Modules/Pylint/Module) for how to run it and read its output.

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

As a summary, here is what to do.  You might want to write a separate program (file) for each of these steps, all committed to the same GitHub repository.  It's up to you!

* Generate a key to share with the class.  Share your `E` and `C` public key with the class, but keep your `D` private key value a secret that you will use later!
* Use someone else's public key (`E` and `C`) to encrypt a secret message to them, one character at a time.  Share your encrypted numeric values with that person.
* When someone shares a message with you, use your own private key (`D` and `C`) to decrypt them to characters, one by one, and print them to the screen.  What message did you get?  Note that this `C` is different than the one you used to encrypt something to your classmate in the prior step: you used their `C` value instead!  Here, you are using your own value of `C`.
* Take someone's public key (`E` and `C`) and compute `M` and `D` from it.  Did it match their private key?  Why is this hard to do with actual public keys on the internet?

## What to Turn In

When you're done, write a `README.md` file in your repository, save all your files, and commit and push everything (all of your Python programs and your README) to GitHub.  There is no need to export your project to ZIP: your pushed repository is your submission, and your latest pushed commit before the deadline is what will be graded.  If a Canvas submission link is posted, you may also paste your repository's URL there as a secondary confirmation.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## Before You Submit: Self-Check

Before you submit, walk through this checklist - if you can check every box, you're in great shape!

- [ ] Each program runs from top to bottom without errors when I run it fresh.
- [ ] My key-generation program reads two primes and prints `E`, `D`, and `C`, and it verifies that the totient of `C` equals `(A-1)*(B-1)`.
- [ ] My encryption program converts a typed character with `ord()` and prints its encrypted value using my classmate's public key.
- [ ] My decryption program takes an encrypted number, applies my private key, and prints the original character with `chr()` - I tested that a character I encrypt decrypts back to itself.
- [ ] My Step 4 cracking program recovers a private key `D` from a public key `E` and `C`.
- [ ] I ran my code through pylint and addressed the warnings (see the [Code Quality and Linting module](../Modules/Pylint/Module)).
- [ ] Every function (including `totient` and `coprime`) has a comment or docstring explaining its purpose, inputs, and output.
- [ ] My `README.md` answers the bolded question and explains how to run each program.
- [ ] I committed AND pushed my work to GitHub, and I can see my final version on github.com in my browser.

## A Note About Export Controls

Some governments, including the United States, have [export controls on cryptographic technologies](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States). 

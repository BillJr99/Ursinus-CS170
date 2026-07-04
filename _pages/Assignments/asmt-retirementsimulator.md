---
layout: assignment
permalink: /Assignments/RetirementSimulator
title: "CS170: Programming for the World Around Us - Retirement Simulator"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use randomness to simulate natural phenomena
    - To use iteration to repeat long-running simulations
    - To visualize simulations
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: "The programs do not run, or neither the pi estimation nor the retirement simulation produces output"
      beginning: "The programs run but a core calculation has a logic slip, such as forgetting to multiply the inside-circle ratio by 4, testing the dart condition x**2 + y**2 <= 1 incorrectly, or failing to subtract the annual spending S at the start of each simulated year"
      progressing: "The pi estimation and the single retirement simulation both produce correct results for the required inputs, but one component has a minor issue: for example, the multi-trial version does not re-initialize the starting balance for each new trial, the run-out-of-money case does not exit both the day and year loops, or portfolio_history is not built correctly so the plot is empty or wrong"
      proficient: "The pi estimator approximates pi for N = 100 through 1,000,000 dart throws and prints the approximation, absolute error, and percentage error; the retirement simulation subtracts annual spending, applies a random daily change between -P_down and P_up, and stops correctly (reporting the day and year) when money runs out; and the k-trial version re-initializes its variables each trial, reports the percentage of successful trials, and builds portfolio_history for the matplotlib plot"
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: "Indentation and spacing are inconsistent enough to make the programs hard to follow, or indentation errors in the nested year and day loops prevent the programs from running"
      beginning: "Indentation and spacing are mostly consistent, with a few isolated issues such as uneven indentation inside the nested trial, year, and day loops"
      progressing: "Indentation and spacing are consistent, with only a minor adjustment needed (for example, missing blank lines between the initialization and simulation sections)"
      proficient: "Indentation and spacing are consistent throughout: each level of the trial, year, and day loops is indented one level deeper than the last, operators are consistently spaced, and blank lines separate the initialization, simulation, and output sections"
    - weight: 10
      description: Code Quality
      preemerging: "The code has not been run through pylint, and there are widespread style issues such as unclear names or the simulation logic copy-pasted between the single-trial and multi-trial versions"
      beginning: "pylint reports several warnings that were not addressed (for example, unused variables or imports left over from experimenting)"
      progressing: "The code runs nearly clean through pylint with only one or two unaddressed warnings; names like count_inside, percent_error, and portfolio_history are descriptive snake_case, with a few isolated style issues remaining"
      proficient: "The code follows the course style guide and runs cleanly through pylint (no warnings other than those the instructor has designated as acceptable): descriptive snake_case names such as count_inside and portfolio_history, no unused variables, and the simulation logic written once rather than copy-pasted between the single-trial and multi-trial versions"
    - weight: 10
      description: Code Documentation
      preemerging: "The code contains no comments, or comments are so sparse that a reader cannot follow the simulation logic"
      beginning: "Some sections are commented, but key steps such as the dart-inside-the-circle test or the yearly spending subtraction are unexplained"
      progressing: "Comments are present at each major step, but they mostly restate the code rather than explaining why (for example, why the ratio is multiplied by 4, or why variables are re-initialized each trial)"
      proficient: "Every function has a comment or docstring stating its purpose, inputs, and output; non-obvious steps such as why the inside-circle ratio approximates pi/4 and why the balance variables must be re-initialized at the start of each trial are explained; comments explain why, not just what"
    - weight: 10
      description: Writeup and Submission
      preemerging: "No README.md is committed to the repository, or the repository is missing the simulation programs or the required plots"
      beginning: "A README.md is committed, but it is missing the output table, one of the plots, or the answers to the bolded questions (the areas of the square and circle, and how accuracy improves as N increases), or the final version was not pushed to GitHub before the deadline"
      progressing: "The README.md includes the output table, both plots, and answers to the bolded questions, with a minor omission such as a missing row of the table or a brief discussion paragraph"
      proficient: "The README.md includes the output table for all five values of N, the percentage-error plot, the portfolio balance plot with a paragraph discussing the patterns you observe, answers to both bolded questions, a description of how to run the programs, and the final version of all files is committed and pushed to GitHub"
      
tags:
  - python
  - numeric
  - scientific
  - functions
  - iteration
  
---

## Purpose

How do scientists and financial planners answer questions that are too complicated to solve with a single formula - like "will my retirement savings last 30 years in an unpredictable market?"  One powerful answer is simulation: use a computer to run an experiment with random chance thousands of times, and study the pattern of outcomes.  In this assignment, you will use that technique (called a Monte Carlo simulation) first to estimate the value of pi by "throwing darts," and then to model a retirement portfolio through decades of random market ups and downs - the same kind of analysis real financial planning tools perform.

## Getting Started with GitHub

Accept the assignment invitation using the GitHub Classroom link, and clone your repository to your computer to get started.  As you work, commit your changes early and often with meaningful messages, and push them before the deadline: your latest pushed commit is what is graded.  If this is new to you, the [Using Git and GitHub](../Modules/Github/Module) and [Cloning an Assignment with GitHub Classroom](../Modules/GithubClassroom/Module) modules walk you through it step-by-step.

Your Code Quality score is informed by pylint: see the [Code Quality and Linting module](../Modules/Pylint/Module) for how to run it and read its output.

## Part 1: Simulating Pi with a Monte Carlo Simulation

For this experiment, you will simulate "dart throwing" using a Monte Carlo simulation to approximate the value of <span>\\(\pi\\)</span>. Imagine a unit square with a circle inscribed.  The diameter of the circle is `1`, since the length of a side of the unit square (in which the circle is inscribed) is `1`. When throwing darts randomly at the board, the proportion of darts that land inside the circle compared to the total number of darts thrown can be used to approximate <span>\\(\pi\\)</span>!

**Question: what is the area of the square, and what is the area of the circle?**

See [this article](https://academo.org/demos/estimating-pi-monte-carlo/) for an animation showing the estimation of the value of <span>\\(\pi\\)</span> as the ratio of the number of points that fall inside of the area of the circle to the number of points that fall inside the area of the square.  This will be approximately equal to the area of the circle you identified above!

## Task Instructions

1. **Generate Random Dart Throws**:
   - For each dart (iteration), generate two random numbers `x` and `y` between 0 and 1. These represent the coordinates of the dart.
   - Use the Python `random` module to generate these random values.

2. **Simulate N Dart Throws**:
   - Ask the user to input the number of darts to throw, `N`.
   - Simulate `N` dart throws, and for each dart, calculate whether it lands inside the circle. A dart lands inside the circle if <span>\\(x^{2} + y^{2} \leq 1\\)</span>.

3. **Calculate Approximation of Pi**:
   - Count the number of darts that land inside the circle (a variable called `count_insde`).
   - Compute the ratio of darts inside the circle to the total darts thrown: <span>\\(\text{ratio} = \frac{\text{count\_inside}}{N}\\)</span>
   - This ratio corresponds to <span>\\(\frac{\pi}{4}\\)</span> because the area of the circle is <span>\\(\pi r^2 = \pi \left(\frac{1}{2}\right)^2 = \frac{\pi}{4}\\), and the area of the square is 1.
   - Multiply the result by 4 to approximate <span>\\(\pi\\)</span>.

4. **Calculate Error**:
   - Print the approximate value of <span>\\(\pi\\)</span>, the absolute error (`abs_error`): <span>\\(\text{abs\_error} = \left| \text{approximation} - \pi \right|\\)</span>
   - To get the value of <span>\\(\pi\\)</span>, you can `import math` and use `math.pi`
   - To calculate the absolute value of `abs_error`, you can execute `abs_error = abs(abs_error)`
   - Calculate and print the percentage error (`percent_error`): <span>\\(\text{percent\_error} = \frac{\text{abs\_error}}{\pi} \times 100\\)</span>

5. **Run the Experiment**:
   - Perform the simulation for `N` = 100, 1000, 10000, 100000 and 1000000.
   - Record the percentage error for each `N`.

6. **Plot the Results**:
   - Using Microsoft Excel or another graphing tool, manually create a plot of `percent_error` on the y-axis versus `N` on the x-axis). Use a logarithmic scale for `N` if available.
   - Include your plot as part of your submission.

## Submission Requirements

1. **Output Table**:
   - Record the results for `N` = 100, 1000, 10000, 100000, and 1000000 in a table, including:
     - The value of `N`
     - The approximated value of <span>\\(\pi\\)</span>
     - The absolute error
     - The percentage error

2. **Graph**:
   - Include a plot of percentage error versus `N`.

**Question: How does the accuracy of the approximation improves as `N` increases? Discuss why this happens and how the percentage error changes with larger `N`.**
   
## Part 2: Simulating a Retirement Scenario

In this experiment, you will simulate the effect of daily market fluctuations on an individual’s finances over a number of years. This simulation will incorporate random market gains and losses, annual spending, and the possibility of running out of money. You will then expand this simulation to analyze the probability of financial success over many iterations, express the results as a percentage, and visualize the portfolio balance for all trials.

---

### Step 1: Single Simulation

1. **Initialize Starting Conditions**:
   - Create and initialize the following variables:
     - Starting amount of money (`M`).
     - Number of years to simulate (`N`).
     - Annual spending amount (`S`).
     - Maximum daily percentage market gain (`P_up`), i.e. `0.01` for one percent.
     - Maximum daily percentage market loss (`P_down`), i.e. `0.01` for one percent.

2. **Simulate Over Years**:
   - Simulate `N` years, with each year containing 365 days.
   - At the beginning of each year:
     - Subtract `S` (annual spending) from the total amount of money.
     - If the amount becomes negative, print that the individual has run out of money and exit both loops.

3. **Simulate Daily Market Fluctuations**:
   - For each day of the year:
     - Generate a random percentage between `-P_down` and `P_up`.
     - Apply this percentage change to the current amount of money.
     - If the total amount of money becomes negative on any day, print that the individual has run out of money and exit both loops.

4. **Output Results**:
   - At the end of each year, print the total amount of money remaining.
   - If the simulation ends early due to running out of money, print the day and year when it occurred.
   - If the simulation completes all `N` years, print the final total amount of money.

### Step 2: Multiple Simulations

1. **Extend the Program**:
   - Modify your program to simulate this process `k` times, where `k` is another variable provided by the user.  Put a loop around your double loop code, and be sure to re-initialize your variables above in this outer loop, so that you start fresh for each trial.

2. **Track Outcomes**:
   - Track the portfolio balances for each trial using an array of arrays:
     - Create an empty list called `portfolio_history`.
     - During each trial, create an empty list `daily_balances` to store the portfolio balance for each day.
     - Append `daily_balances` to `portfolio_history` after each trial.

3. **Count Outcomes**:
   - Track how many simulations result in a positive amount of money at the end of `N` years.
   - Track how many simulations result in the individual running out of money.
   - Calculate and print the percentage of successful trials: <span>\\(\text{Percentage Positive} = \frac{\text{Positive Outcomes}}{k} \times 100\\)</span>.

4. **Output Statistics**:
   - Print the number of successful trials (positive outcomes).
   - Print the percentage of successful trials.

---

### Part 3: Visualizing Results

1. **Plot Portfolio Balances**:
   - Use the provided function below to plot the portfolio balance for all trials:
     ```python
     import matplotlib.pyplot as plt

     def plot_portfolio_balances(portfolio_history):
         """
         Plots portfolio balances for all trials.

         Parameters:
         - portfolio_history: List of lists, where each sublist contains daily balances for a single trial.
         """
         for trial in portfolio_history:
             plt.plot(trial, alpha=0.5, linewidth=0.8)  # Plot each trial's daily balances
         plt.xlabel('Day')
         plt.ylabel('Portfolio Balance')
         plt.title('Portfolio Balances Across All Trials')
         plt.grid(True)
         plt.show()
     ```
   - After building your `portfolio_history` list, pass it as an argument to this function to create the plot.

To install `matplotlib`, you can execute:

```
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/python3 -m pip install matplotlib
```

On some computers, the last command will be:

```
.venv/Scripts/python -m pip install matplotlib
```

### Example Steps for Tracking Portfolio History

1. **Inside the Loop for Each Trial**:
   - Initialize `daily_balances = []`.
   - For each day, calculate the new portfolio balance and append it to `daily_balances` using `daily_balances.append(balance)`.
   - If the portfolio goes negative, stop adding to `daily_balances`, or stop looping the daily and yearly trials (i.e., move on to the next trial iteration).

2. **At the End of Each Trial**:
   - Append `daily_balances` to `portfolio_history` using `portfolio_history.append(daily_balances)`.

3. **After All Trials**:
   - Pass `portfolio_history` to the `plot_portfolio_balances` function to visualize the results.

---

## Submission Requirements

### Step 1: Single Simulation
- Record the results of the simulation for `M = 100,000`, `N = 30`, `S = 10,000`, `P_up = 0.5%`, `P_down = 0.5%`.

### Step 2: Multiple Simulations
- Run `k = 100,000` simulations with the same conditions.
- Print the total number of successful trials and express it as a percentage of the total trials.

### Step 3: Visualization
- Submit the portfolio balance plot for all trials.
- Include a brief paragraph discussing the patterns you observe in the plot and how frequently portfolios dip into negative territory.

## What to Turn In

When you're done, write a `README.md` file in your repository, save all your files, and commit and push everything (your Python files, your plots, and your README) to GitHub.  There is no need to export your project to ZIP: your pushed repository is your submission, and your latest pushed commit before the deadline is what will be graded.  If a Canvas submission link is posted, you may also paste your repository's URL there as a secondary confirmation.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## Before You Submit: Self-Check

Before you submit, walk through this checklist - if you can check every box, you're in great shape!

- [ ] Each program runs from top to bottom without errors when I run it fresh (after installing `matplotlib`).
- [ ] My pi estimator asks the user for `N`, and I recorded results for N = 100, 1,000, 10,000, 100,000, and 1,000,000 in my output table (approximation, absolute error, and percentage error).
- [ ] My single retirement simulation subtracts spending each year, applies a random daily change, and correctly reports the day and year if the money runs out.
- [ ] My multi-trial version re-initializes the balance variables at the start of each trial and prints the number and percentage of successful trials.
- [ ] My `portfolio_history` plot displays, and my README includes it plus the percentage-error plot for Part 1.
- [ ] I ran my code through pylint and addressed the warnings (see the [Code Quality and Linting module](../Modules/Pylint/Module)).
- [ ] Every function has a comment or docstring explaining its purpose, inputs, and output.
- [ ] My `README.md` answers every bolded question and includes the discussion paragraph about the portfolio plot patterns.
- [ ] I committed AND pushed my work to GitHub, and I can see my final version on github.com in my browser.

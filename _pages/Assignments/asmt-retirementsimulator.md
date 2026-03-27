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
  - numeric
  - scientific
  - functions
  - iteration
  
---

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

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

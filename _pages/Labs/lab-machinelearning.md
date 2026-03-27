---
layout: assignment
permalink: /Labs/MachineLearning
title: "CS170: Programming for the World Around Us - Machine Learning"


info:
  coursenum: CS170
  points: 100
  goals:
    - To use Python scientific computing and statistical libraries to perform machine learning classifications on data
    - To explore the automatic separability of data for making predictions
    - To visualize data
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
    
tags:
  - python
  - machinelearning
  - visualization
  
---

In this lab, we will explore the capabilities of Machine Learning, which allow us to make observations about data and then make predictions about new observations.  For example, if you think about your classes and the grades you're getting, you might imagine that your grades are higher in the classes that you're putting more time into.  You might even be able to go so far as to predict how many hours of practice or study you need in a certain class to earn a particular grade.  This is far from perfect, because other variables impact the result you might observe, but it turns out that we can model information about historical data and use it to make predictions about the future.

In general, many machine learning approaches involve **training** a model on historical observations, and then using that model to **predict** outcomes on new observations.  Often, we measure the effectiveness of a machine learning algorithm by **testing** it on predictions whose answers we already know (so that we can compare its answers against the answer key).

We will expore two datasets: one for classifying flower species by measuring its petal and sepal portions, and one for making observations about breast tumors for possible malignancy.  In each example, we will train the model, test it, give it an accuracy score (out of 100%), and peek "under the hood" by visualizing the model that the machine learning algorithm created.

## What to Do

### Part 1: The Iris Dataset
We will begin by exploring the Iris Dataset using the scikit-learn package \[[^1]\].  

#### Exploring the Data
Take a look at the dataset itself.  You'll notice four columns (called "features") and the species (called the "label" that we eventually want to predict without knowing it).

**With your partner, pretend you are playing a game of "guess who" in which you can ask up to four questions about the lengths and widths below to figure out the variety of the flower.  One partner can pick one row from the table, and without revealing anything about it, the other partner can ask four questions (for example, "is the sepal length at least 5?") before trying to guess the species.  What questions did you come up with?  Write these down in your readme in the form of Python `if` statements**

| "sepal.length" | "sepal.width" | "petal.length" | "petal.width" | "variety"    |
|----------------|---------------|----------------|---------------|--------------|
| 5.1            | 3.5           | 1.4            | .2            | "Setosa"     |
| 4.9            | 3             | 1.4            | .2            | "Setosa"     |
| 4.7            | 3.2           | 1.3            | .2            | "Setosa"     |
| 4.6            | 3.1           | 1.5            | .2            | "Setosa"     |
| 5              | 3.6           | 1.4            | .2            | "Setosa"     |
| 5.4            | 3.9           | 1.7            | .4            | "Setosa"     |
| 4.6            | 3.4           | 1.4            | .3            | "Setosa"     |
| 5              | 3.4           | 1.5            | .2            | "Setosa"     |
| 4.4            | 2.9           | 1.4            | .2            | "Setosa"     |
| 4.9            | 3.1           | 1.5            | .1            | "Setosa"     |
| 5.4            | 3.7           | 1.5            | .2            | "Setosa"     |
| 4.8            | 3.4           | 1.6            | .2            | "Setosa"     |
| 4.8            | 3             | 1.4            | .1            | "Setosa"     |
| 4.3            | 3             | 1.1            | .1            | "Setosa"     |
| 5.8            | 4             | 1.2            | .2            | "Setosa"     |
| 5.7            | 4.4           | 1.5            | .4            | "Setosa"     |
| 5.4            | 3.9           | 1.3            | .4            | "Setosa"     |
| 5.1            | 3.5           | 1.4            | .3            | "Setosa"     |
| 5.7            | 3.8           | 1.7            | .3            | "Setosa"     |
| 5.1            | 3.8           | 1.5            | .3            | "Setosa"     |
| 5.4            | 3.4           | 1.7            | .2            | "Setosa"     |
| 5.1            | 3.7           | 1.5            | .4            | "Setosa"     |
| 4.6            | 3.6           | 1              | .2            | "Setosa"     |
| 5.1            | 3.3           | 1.7            | .5            | "Setosa"     |
| 4.8            | 3.4           | 1.9            | .2            | "Setosa"     |
| 5              | 3             | 1.6            | .2            | "Setosa"     |
| 5              | 3.4           | 1.6            | .4            | "Setosa"     |
| 5.2            | 3.5           | 1.5            | .2            | "Setosa"     |
| 5.2            | 3.4           | 1.4            | .2            | "Setosa"     |
| 4.7            | 3.2           | 1.6            | .2            | "Setosa"     |
| 4.8            | 3.1           | 1.6            | .2            | "Setosa"     |
| 5.4            | 3.4           | 1.5            | .4            | "Setosa"     |
| 5.2            | 4.1           | 1.5            | .1            | "Setosa"     |
| 5.5            | 4.2           | 1.4            | .2            | "Setosa"     |
| 4.9            | 3.1           | 1.5            | .2            | "Setosa"     |
| 5              | 3.2           | 1.2            | .2            | "Setosa"     |
| 5.5            | 3.5           | 1.3            | .2            | "Setosa"     |
| 4.9            | 3.6           | 1.4            | .1            | "Setosa"     |
| 4.4            | 3             | 1.3            | .2            | "Setosa"     |
| 5.1            | 3.4           | 1.5            | .2            | "Setosa"     |
| 5              | 3.5           | 1.3            | .3            | "Setosa"     |
| 4.5            | 2.3           | 1.3            | .3            | "Setosa"     |
| 4.4            | 3.2           | 1.3            | .2            | "Setosa"     |
| 5              | 3.5           | 1.6            | .6            | "Setosa"     |
| 5.1            | 3.8           | 1.9            | .4            | "Setosa"     |
| 4.8            | 3             | 1.4            | .3            | "Setosa"     |
| 5.1            | 3.8           | 1.6            | .2            | "Setosa"     |
| 4.6            | 3.2           | 1.4            | .2            | "Setosa"     |
| 5.3            | 3.7           | 1.5            | .2            | "Setosa"     |
| 5              | 3.3           | 1.4            | .2            | "Setosa"     |
| 7              | 3.2           | 4.7            | 1.4           | "Versicolor" |
| 6.4            | 3.2           | 4.5            | 1.5           | "Versicolor" |
| 6.9            | 3.1           | 4.9            | 1.5           | "Versicolor" |
| 5.5            | 2.3           | 4              | 1.3           | "Versicolor" |
| 6.5            | 2.8           | 4.6            | 1.5           | "Versicolor" |
| 5.7            | 2.8           | 4.5            | 1.3           | "Versicolor" |
| 6.3            | 3.3           | 4.7            | 1.6           | "Versicolor" |
| 4.9            | 2.4           | 3.3            | 1             | "Versicolor" |
| 6.6            | 2.9           | 4.6            | 1.3           | "Versicolor" |
| 5.2            | 2.7           | 3.9            | 1.4           | "Versicolor" |
| 5              | 2             | 3.5            | 1             | "Versicolor" |
| 5.9            | 3             | 4.2            | 1.5           | "Versicolor" |
| 6              | 2.2           | 4              | 1             | "Versicolor" |
| 6.1            | 2.9           | 4.7            | 1.4           | "Versicolor" |
| 5.6            | 2.9           | 3.6            | 1.3           | "Versicolor" |
| 6.7            | 3.1           | 4.4            | 1.4           | "Versicolor" |
| 5.6            | 3             | 4.5            | 1.5           | "Versicolor" |
| 5.8            | 2.7           | 4.1            | 1             | "Versicolor" |
| 6.2            | 2.2           | 4.5            | 1.5           | "Versicolor" |
| 5.6            | 2.5           | 3.9            | 1.1           | "Versicolor" |
| 5.9            | 3.2           | 4.8            | 1.8           | "Versicolor" |
| 6.1            | 2.8           | 4              | 1.3           | "Versicolor" |
| 6.3            | 2.5           | 4.9            | 1.5           | "Versicolor" |
| 6.1            | 2.8           | 4.7            | 1.2           | "Versicolor" |
| 6.4            | 2.9           | 4.3            | 1.3           | "Versicolor" |
| 6.6            | 3             | 4.4            | 1.4           | "Versicolor" |
| 6.8            | 2.8           | 4.8            | 1.4           | "Versicolor" |
| 6.7            | 3             | 5              | 1.7           | "Versicolor" |
| 6              | 2.9           | 4.5            | 1.5           | "Versicolor" |
| 5.7            | 2.6           | 3.5            | 1             | "Versicolor" |
| 5.5            | 2.4           | 3.8            | 1.1           | "Versicolor" |
| 5.5            | 2.4           | 3.7            | 1             | "Versicolor" |
| 5.8            | 2.7           | 3.9            | 1.2           | "Versicolor" |
| 6              | 2.7           | 5.1            | 1.6           | "Versicolor" |
| 5.4            | 3             | 4.5            | 1.5           | "Versicolor" |
| 6              | 3.4           | 4.5            | 1.6           | "Versicolor" |
| 6.7            | 3.1           | 4.7            | 1.5           | "Versicolor" |
| 6.3            | 2.3           | 4.4            | 1.3           | "Versicolor" |
| 5.6            | 3             | 4.1            | 1.3           | "Versicolor" |
| 5.5            | 2.5           | 4              | 1.3           | "Versicolor" |
| 5.5            | 2.6           | 4.4            | 1.2           | "Versicolor" |
| 6.1            | 3             | 4.6            | 1.4           | "Versicolor" |
| 5.8            | 2.6           | 4              | 1.2           | "Versicolor" |
| 5              | 2.3           | 3.3            | 1             | "Versicolor" |
| 5.6            | 2.7           | 4.2            | 1.3           | "Versicolor" |
| 5.7            | 3             | 4.2            | 1.2           | "Versicolor" |
| 5.7            | 2.9           | 4.2            | 1.3           | "Versicolor" |
| 6.2            | 2.9           | 4.3            | 1.3           | "Versicolor" |
| 5.1            | 2.5           | 3              | 1.1           | "Versicolor" |
| 5.7            | 2.8           | 4.1            | 1.3           | "Versicolor" |
| 6.3            | 3.3           | 6              | 2.5           | "Virginica"  |
| 5.8            | 2.7           | 5.1            | 1.9           | "Virginica"  |
| 7.1            | 3             | 5.9            | 2.1           | "Virginica"  |
| 6.3            | 2.9           | 5.6            | 1.8           | "Virginica"  |
| 6.5            | 3             | 5.8            | 2.2           | "Virginica"  |
| 7.6            | 3             | 6.6            | 2.1           | "Virginica"  |
| 4.9            | 2.5           | 4.5            | 1.7           | "Virginica"  |
| 7.3            | 2.9           | 6.3            | 1.8           | "Virginica"  |
| 6.7            | 2.5           | 5.8            | 1.8           | "Virginica"  |
| 7.2            | 3.6           | 6.1            | 2.5           | "Virginica"  |
| 6.5            | 3.2           | 5.1            | 2             | "Virginica"  |
| 6.4            | 2.7           | 5.3            | 1.9           | "Virginica"  |
| 6.8            | 3             | 5.5            | 2.1           | "Virginica"  |
| 5.7            | 2.5           | 5              | 2             | "Virginica"  |
| 5.8            | 2.8           | 5.1            | 2.4           | "Virginica"  |
| 6.4            | 3.2           | 5.3            | 2.3           | "Virginica"  |
| 6.5            | 3             | 5.5            | 1.8           | "Virginica"  |
| 7.7            | 3.8           | 6.7            | 2.2           | "Virginica"  |
| 7.7            | 2.6           | 6.9            | 2.3           | "Virginica"  |
| 6              | 2.2           | 5              | 1.5           | "Virginica"  |
| 6.9            | 3.2           | 5.7            | 2.3           | "Virginica"  |
| 5.6            | 2.8           | 4.9            | 2             | "Virginica"  |
| 7.7            | 2.8           | 6.7            | 2             | "Virginica"  |
| 6.3            | 2.7           | 4.9            | 1.8           | "Virginica"  |
| 6.7            | 3.3           | 5.7            | 2.1           | "Virginica"  |
| 7.2            | 3.2           | 6              | 1.8           | "Virginica"  |
| 6.2            | 2.8           | 4.8            | 1.8           | "Virginica"  |
| 6.1            | 3             | 4.9            | 1.8           | "Virginica"  |
| 6.4            | 2.8           | 5.6            | 2.1           | "Virginica"  |
| 7.2            | 3             | 5.8            | 1.6           | "Virginica"  |
| 7.4            | 2.8           | 6.1            | 1.9           | "Virginica"  |
| 7.9            | 3.8           | 6.4            | 2             | "Virginica"  |
| 6.4            | 2.8           | 5.6            | 2.2           | "Virginica"  |
| 6.3            | 2.8           | 5.1            | 1.5           | "Virginica"  |
| 6.1            | 2.6           | 5.6            | 1.4           | "Virginica"  |
| 7.7            | 3             | 6.1            | 2.3           | "Virginica"  |
| 6.3            | 3.4           | 5.6            | 2.4           | "Virginica"  |
| 6.4            | 3.1           | 5.5            | 1.8           | "Virginica"  |
| 6              | 3             | 4.8            | 1.8           | "Virginica"  |
| 6.9            | 3.1           | 5.4            | 2.1           | "Virginica"  |
| 6.7            | 3.1           | 5.6            | 2.4           | "Virginica"  |
| 6.9            | 3.1           | 5.1            | 2.3           | "Virginica"  |
| 5.8            | 2.7           | 5.1            | 1.9           | "Virginica"  |
| 6.8            | 3.2           | 5.9            | 2.3           | "Virginica"  |
| 6.7            | 3.3           | 5.7            | 2.5           | "Virginica"  |
| 6.7            | 3             | 5.2            | 2.3           | "Virginica"  |
| 6.3            | 2.5           | 5              | 1.9           | "Virginica"  |
| 6.5            | 3             | 5.2            | 2             | "Virginica"  |
| 6.2            | 3.4           | 5.4            | 2.3           | "Virginica"  |
| 5.9            | 3             | 5.1            | 1.8           | "Virginica"  |

These questions actually form the basis of a machine learning model called a **Decision Tree**.  You could create one using `if` statements, but the challenge is figuring out which specific questions will give you the best chance of predicting the species of all the flowers.  Fortunately, there is a well-known algorithm that analyzes the set of training data and decides how best to create the decisions within the tree, and what values to set as the boundaries for its `if` statements that separate them.  

The algorithm itself is beyond the scope of this class, but the **scikit-learn** Python library includes it for us to use.  We just have to pass it the example training data and it will return the tree for us to use to make predictions.

#### Training the Decision Tree Classifier
We will begin by importing the libraries that we will need to perform the classification.  In your project shell, you may need to type `pip install scikit-learn matplotlib` to install these two packages, in case they're not already installed.

```python
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay
import sklearn.metrics
```

Normally, we'd have to save the table above as a text file and then read it in with a loop in Python.  This only requires a few lines of code, but the scikit-learn library actually downloads the data for us and loads it.  How nice!

```python
iris = datasets.load_iris()
```

Now, the `iris` variable contains the table of data you saw above.  Although computers can classify on any number of columns, our eyes can see things most easily in two dimensions, so we'll arbitrarily choose two columns from the data to classify on.  We'll use the sepal length, and the petal length, which are columns 0 and 2 of the input data.  The following line of code takes the first and third feature columns, which are the sepal length and petal length in cm ([0, 2]), and all rows (:).  We'll call this variable `X`:

```python
X = iris.data[:, [0, 2]] 
```

We'll also store the answers (the species) in a target variable called `y`:

```python
y = iris.target # the "answer key" we will train on
```

Optionally, you can print some of the data to see what it looks like.  The `target names` shows the list of targets (the species that we're classifying).  We'll also print features 0 and 2, the sepal length and the petal length, by extracting columns 0 through 3 of the `feature_names` set, counting by 2 (hence, 0 and 2):

```python
print(X)
print(iris.target_names)
print(iris.feature_names[0:3:2])
```

Now for the real work: let's create the decision tree classifier and pick out our questions.  Like our class exercise, we'll limit the classifier to 4 questions, by specifying a `max_depth` of 4:

```python
clf1 = DecisionTreeClassifier(max_depth=4)
clf1.fit(X, y)
```

That's it!  The `fit` function tells the model to pick out its 4 questions by looking at the petal length and sepal length (in the `X` variable), and by looking at the target species answers in the `y` variable.

#### Making Predictions
You can predict by passing a list of sepal lengths and petal lengths, like this:

```python
new_flowers = [[5, 1.4], [6, 5]]
predictions = clf1.predict(new_flowers)
print(predictions) # setosa is 0, versicolor is 1, virginica is 2
```

One way you can evaluate a machine learning algorithm is by cutting out some of the training data and using it to make the predictions.  This way, it wasn't used to train the model (no cheating!), but we still know the right answers.  We'll explore this in Part 2, but for now, we can run the predictions against the original testing set.  It should do pretty well, since we used it to train the model in the first place!

```python
predictions = clf1.predict(X)
print(predictions)
```

### Evaluating Model Accuracy
You can score an algorithm's accuracy out of 100% as follows, by passing the correct answers and the predictions to the `accuracy_score` function of scikit-learn.  If you predicted on the original training set `X`, then the answers are the original target list which we called `y`.  Otherwise, you can create a new list `y` that contains a list of the right answers (0, 1, or 2 for setosa, versicolor, or virginica).

```python
print(sklearn.metrics.accuracy_score(y, predictions))
```

### Visualizing the Results
You can see a graph plotting the cutoff points of the decision tree by using the `matplotlib` library and the scikit-learn `DecisionBoundaryDisplay` library:

```python
# X[:, 0] means the first column of the X training set, and X[:, 1] means the second column - this ensures we only plot two things, which is convenient for your eyes to see in 2D
fig, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(clf1, X, alpha=0.4, ax=ax, response_method="predict")
ax.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
ax.set_title("Decision Boundary (max depth 4)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.savefig("output.png")
plt.show()
plt.clf()
```

Here is the result:

<p align="center">
<img src="../files/lab-machinelearning/flowerboundary.png" alt="The decision tree cutoff boundaries for the sepal length and petal length" style="max-width: 100%">
</p>

**Looking at the graph, guess which four questions the algorithm is asking as part of its decision tree.  Don't worry if it's right or wrong, just take your best guess to get some intuition about what you're seeing!**

### Visualizing the Decision Tree

Similarly, you can display the decision tree itself, and see exactly what questions are being asked.  The `plot_tree` function takes the classifier, the names of the features (the sepal length and petal length), and the targets (0 for setosa, 1 for versicolor, and 2 for virginica).  You can print `iris.feature_names` and `iris.target_names` to see what they look like.

```python
# Display the decision tree
fig = plt.figure(figsize=(25,20))
sklearn.tree.plot_tree(clf1, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
fig.savefig("tree.png")
plt.show()
```

Here is the result:

<p align="center">
<img src="../files/lab-machinelearning/flowertree.png" alt="The decision tree with a max depth of 4" style="max-width: 100%">
</p>

At the top of the tree, you can see the first question being asked.  It asks if the sepal width is less than or equal to 2.45.  This evaluated 150 samples, of which 50 are setosa, 50 are versicolor, and 50 are virginica (see the `samples` and `value` entries in the top node of the tree).  If so, the flower is predicted right off the bat to be a setosa flower (see the `class` entry).  Looking to the left, we see that all 50 flowers were classified as setosa, with no probability of a misprediction (that's what a `gini` value of 0% means).  To the right, we see that we still have 100 samples, and some are versicolor and some are virginica.  It will continue to ask more questions about them.  **Look at the rest of the nodes and write down the questions being asked, and what predictions are being made.  Play your own game of "guess who" again - pick a flower from the original list, ask these questions, and see if you get it right now!  Write down which flower you chose and whether it was correctly predicted or not.**

**Notice the number of samples in the tree, and how it gets smaller with each level of depth.  What would happen to this number if you added more depth to the tree (in other words, asked more questions), and what would that mean?  Would it be better or worse if all the leaves at the bottom of the tree had a sample size of 1, and why?**

**Look at the bottom of the tree.  Is it still possible to mispredict a flower?  How could you change the code to avoid this?  Try changing the `max_depth` of the tree and re-running the program.  Try several different values, some large, and some small: how do your results change?**

### Part 2: Tumor Classification
Now, we'll repeat this process using the Breast Cancer dataset \[[^2]\].  This time, we'll use a different machine learning algorithm known as Naive Bayes, which is a statistical model, but this is an arbitrary decision and the library functions are nearly exactly the same!  This is a convenient feature of scikit-learn; you can introduce different algorithms to ask different kinds of questions, but the code is pretty much identical no matter what you choose.  This is called "providing a consistent interface" to the programmer: the operations remain the same even if the underlying algorithm changes.  Think of this like driving a car: most cars have a steering wheel, gear shift, and turn signals in roughly the same places, even though the engine and transmissions might be different between the different makes ans models.

#### Training the Model
Like before, we'll import the libraries and load the dataset:

```python
import matplotlib.pyplot as plt

import sklearn 
import sklearn.datasets
import sklearn.model_selection
import sklearn.naive_bayes 
import sklearn.metrics
import sklearn.inspection

data = sklearn.datasets.load_breast_cancer()
```

The labels and features are stored in the data as a dictionary, and we can extract them into variables like so:

```python
# Organize our data
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Look at our data
print(label_names)
print(labels)
print(feature_names)
print(features)
```

Recall in our prior example that we tested the accuracy of the model against the training data.  This is a bit like cheating, since the algorithm had access to the whole answer key up front.  The solution is to split the features and labels into a training set and a testing set, and only train on the training rows.  You could do this with array indexing to take a subset of the list, but scikit-learn provides a function for doing this because it is such a common machine learning operation.  The `train_test_split` function returns the training set, the testing set, the answers ("labels") for the training set, and the labels for the testing set.  We'll ask it to remove 33% of the features and labels from the training set and use it as the testing set.  It uses a random number generator to decide which rows to remove, and we can optionally seed the random number generator using the `random_state` parameter.

```python
# Split our data
train, test, train_labels, test_labels = sklearn.model_selection.train_test_split(features, labels,test_size=0.33,random_state=42)
```

**Write a function to perform the operation of `train_test_split`.  In your version, it's fine to simply remove the first 33% of the rows of the list, rather than use a random number generator to pick the rows.**

**Why might it be better to use a random number generator to split the set instead of picking the first or last third of the data?**

Now, we'll train the classifier, just like before:

```python
# Initialize our classifier
gnb = sklearn.naive_bayes.GaussianNB()

# Train our classifier
gnb.fit(train, train_labels)
```

### Predicting and Scoring Accuracy

This time, we'll test on the testing set, which the model has never seen before during testing.  This gives results that we can expect to be a bit more authentic:

```python
# Make predictions
preds = gnb.predict(test)
print(preds)

# Evaluate accuracy
print(sklearn.metrics.accuracy_score(test_labels, preds))
```

### Visualizing the Decision Boundary
Like before, let's see how the algorithm made its decisions.  For convenience, we'll just look at two features, but this will give us a representative idea of what's going on:

```python
# Visualize the results
# There are 30 features, but we will visualize in 2 dimensions by choosing the first two ([:, 0] and [:, 1]), which are the radius and texture
malignant = test[test_labels==0] # select those rows from test where the label is 0 for malignant
benign = test[test_labels==1] # and same for benign
fig, ax = plt.subplots()
ax.scatter(malignant[:, 0], malignant[:, 1], color='r', label="Malignant Tumors")
ax.scatter(benign[:, 0], benign[:, 1], color='b', label="Benign Tumors")
plt.title("Tumor Classification")
plt.xlabel("Mean Radius")
plt.ylabel("Mean Texture")
plt.savefig("output.png")
plt.show()
```

Here is the result:

<p align="center">
<img src="../files/lab-machinelearning/tumorclassification.png" alt="The breast cancer dataset classification on the radius and texture features" style="max-width: 100%">
</p>

**Around where is the algorithm cutting off between the malignant and benign classes on the x and y axes?**

**Modify this program to visualize two different features of the dataset instead, and label the graph accordingly.**

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

## References
[^1]: [https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html#sphx-glr-auto-examples-ensemble-plot-voting-decision-regions-py](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html#sphx-glr-auto-examples-ensemble-plot-voting-decision-regions-py), BSD License
[^2]: [https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn](https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn), [CC Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

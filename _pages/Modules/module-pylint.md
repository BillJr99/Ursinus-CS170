---
layout: module
permalink: /Modules/Pylint/Module

title: "CS170: Programming for the World Around Us - Code Quality and Linting with Pylint"

info:
  prev: "../GithubClassroom/Module"
  
---

## Code Quality and Linting with Pylint

Have you ever had a teacher proofread an essay draft and hand it back with the spelling mistakes circled, before you turned in the final version?  A **linter** does the same thing for code.  It reads your program *without running it* and points out things like misspelled variable names, variables you created but never used, confusing names, and inconsistent formatting.  In this course we use a popular Python linter called **pylint**, and your Code Quality rubric score on programming assignments is informed by how cleanly your code passes it.

The best part: the linter is not a gotcha — you get to run it yourself, as many times as you like, *before* you submit.  Think of it as unlimited free proofreading.

### Installing Pylint

You only need to do this once.  Open a terminal (on Windows, the Command Prompt or the terminal inside your editor) and run:

```
pip install pylint
```

If `pip` isn't found, try `pip3 install pylint` or `python -m pip install pylint`.

### Running Pylint

From the folder that contains your program (your cloned assignment repository), run:

```
pylint yourprogram.py
```

You'll see output like this:

```
************* Module respiratory
respiratory.py:12:0: C0103: Constant name "sampleRate" doesn't conform to UPPER_CASE naming style (invalid-name)
respiratory.py:27:4: W0612: Unused variable 'total' (unused-variable)
respiratory.py:1:0: C0114: Missing module docstring (missing-module-docstring)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 6.88/10, +0.62)
```

### Reading the Output

Each line tells you four things: the **file and line number** where the issue is (`respiratory.py:12`), a **code** for the type of issue (`C0103`), a **plain-English description**, and a short **name** in parentheses (`invalid-name`).  The letter at the front of the code tells you how serious it is:

| Letter | Meaning | Should I fix it? |
|--------|---------|------------------|
| `E` (Error) | Probably a real bug — the code may crash here | Yes, right away! |
| `W` (Warning) | Suspicious code, like an unused variable | Yes |
| `C` (Convention) | A style issue, like a poorly formatted name | Yes — these are most of your Code Quality score |
| `R` (Refactor) | The code works but could be structured better | When you can |

At the bottom, pylint gives your code a score out of 10.  Fix an issue, re-run pylint, and watch the score climb — it is strangely satisfying.

### Fixing the Most Common Findings

- **`invalid-name` (C0103)**: Python variable and function names should be lowercase `snake_case` (like `respiratory_rate`, not `RespiratoryRate` or `x2`), and names of constants that never change should be `UPPER_CASE` (like `SAMPLE_RATE`).  Descriptive names also make your code easier for *you* to debug!
- **`unused-variable` (W0612)**: you assigned a variable but never used it.  Either you meant to use it (a possible bug!), or it is leftover scaffolding you can delete.
- **`missing-module-docstring` / `missing-function-docstring` (C0114/C0116)**: add a short `"""description"""` as the first line of your file and of each function saying what it does — this doubles as your code documentation.
- **`trailing-whitespace` / `line-too-long` (C0303/C0301)**: invisible spaces at the ends of lines, or lines over 100 characters.  Most editors can show and trim these automatically.
- **`redefined-outer-name`, `global-statement`**: usually a sign that a function should take a parameter and return a value instead of reaching for an outside variable — exactly the habit we practice in the Functions activity.

It is okay if you can't get to a perfect 10/10 on every assignment — but you should *read* every message, fix the ones you understand, and ask about the ones you don't.  "I didn't understand this warning" is a great office-hours question.

### Automatic Lint Checks on GitHub (GitHub Actions)

Because you submit your work by pushing to GitHub, we can have GitHub run pylint for you automatically on every push, using a tool called [autograding-pylint-grader](https://github.com/rlalik/autograding-pylint-grader).  If your assignment repository includes this, you'll see a green check mark (or a red X) next to each commit on github.com — click "Details" to read the same pylint report you'd get locally.

Instructors (or curious students) can enable this in any assignment repository by adding a file named `.github/workflows/lint.yml` with the following contents, committing, and pushing:

{% raw %}
```yaml
name: Lint

on:
  - push
  - workflow_dispatch

permissions:
  checks: write
  actions: read
  contents: read

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repository
        uses: actions/checkout@v4
      - name: Run the pylint autograder
        id: pylint
        uses: rlalik/autograding-pylint-grader@v1
        with:
          max-score: 10
          files: FINDALL
      - name: Report the result
        run: 'echo "${{ steps.pylint.outputs.result }}"'
```
{% endraw %}

What this does, line by line: on every `push`, GitHub starts a fresh little Linux machine (`runs-on: ubuntu-latest`), checks out your repository, and runs the grader action, which runs pylint over every `.py` file it finds (`files: FINDALL`), and converts the pylint rating into a score.  In GitHub Classroom, this score can feed directly into the autograding results the instructor sees — the same rubric row you see as "Code Quality."

**A note on honesty**: the linter checks style, not correctness.  A program can score 10/10 on pylint and still compute the wrong answer — so run your *program* on the sample inputs too, not just the linter.  The "Before You Submit" self-check on each assignment page walks you through both.

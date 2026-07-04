---
layout: module
permalink: /Modules/Github/Module

title: "CS170: Programming for the World Around Us - Using Git and GitHub"

info:
  next: "./Module2"
  video: "https://www.youtube.com/embed/zl7fgkRjG_c"
  
---

## Why Git and GitHub?

Throughout this course, you will write programs that grow and change over many work sessions.  **Git** is a tool called a *version control system*: it keeps a running history of your work, so you can save a snapshot (called a **commit**) every time you make progress, and rewind if something breaks.  **GitHub** is a website that stores a copy of your git history in the cloud, which is how you will submit your assignments in this course — and how software teams all over the world share their work every day.

Here is the whole workflow in one picture:

| Step | Command | What it does |
|------|---------|--------------|
| 1 | `git clone <url>` | Downloads your assignment repository to your computer (you only do this once per assignment) |
| 2 | *(edit your files)* | Write some code! |
| 3 | `git add .` | Stages your changed files, telling git "include these in my next snapshot" |
| 4 | `git commit -m "describe what you did"` | Saves a snapshot of your staged work, with a message describing it |
| 5 | `git push` | Uploads your commits to GitHub, where the instructor can see them |
| 6 | Repeat steps 2-5 early and often! | Each commit is a safety checkpoint — and your latest *pushed* commit is what is graded |

A good habit: **commit every time you get one piece working** (for example, "reads the file correctly," or "first loop working").  If you commit early and often, you will never lose more than a few minutes of work, and you will always have a working version you can go back to.

Please watch the video above for a walkthrough, and when you're finished, continue to the next module to practice working with a repository.

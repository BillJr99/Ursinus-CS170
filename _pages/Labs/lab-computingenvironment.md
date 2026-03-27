---
layout: assignment
permalink: /Labs/ComputingEnvironment
title: "CS170: Programming for the World Around Us - Setting up Your Computing Environment"


instructorgithub: BillJr99

info:
  coursenum: CS170
  points: 50
  goals:
    - To set up the computing tools needed for CS170
  rubric:
    - weight: 100
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
    
tags:
  - computing
  
---

## What to Do

### GitHub
Go to [GitHub](https://www.github.com) and create an account.  GitHub provides a platform for saving your work to the cloud, which provides a backup as well as a mechanism to share your work with your peers and instructors.  We will integrate this into the micro:bit and Visual Studio Code environments that we'll use throughout the semester.

### Visual Studio Code
First, download and install [Visual Studio Code](https://code.visualstudio.com/download) for your operating system.  

#### Extensions
Within Visual Studio Code, click the **Extensions** icon or press Control-Shift-X to bring up the set of extensions.  There are a few that you'll want to install:

* Python
* Live Share
* Archiver

#### Trying out Visual Studio Code
Create a folder on your desktop by right clicking on your desktop and choosing `New Folder`.  You can give it any name you like.

Create a new project in Visual Studio Code by going to `File - Open Folder`.  Pick the folder you just created.

Go to `File - New Text File` and paste the following:

```python
print("Hello World!")
```

Go to `File - Save` or hit Control-S to save the file into your folder.  Call it `main.py`. Click the run button at the top right (it looks like a triangle pointing to the right) of your screen to run it.

#### Trying out Live Share
At the bottom left of your screen, click `Live Share`.  Select `Allow Access` if you're asked to let this through your computer's firewall, so that it can be accessed from the Internet.  This puts a link on your clipboard.  E-mail this link to your partner and join each other's project.  Paste this link into a web browser to load it.  Click to `Continue in Visual Studio Code` when you paste the link into the browser, and have your partner click to `Accept Read-Write` so that you can access and edit the project.  Add a print statement of your own to your partner's project and run it.

#### Trying out GitHub
Click the `Source Control` icon on the left toolbar or press Control-Shift-G to open the source control tab.  Click `Publish to GitHub` and log into your GitHub account to save the project there.  If prompted, enter a message (for example "My first commit upload") and click `Commit` and, if prompted, `Push`, to upload your work to the cloud.

##### Sharing your GitHub Repository
Go to [https://www.github.com](https://www.github.com) on your web browser, and click on the repository that was just created when you saved your project.  Click the `Settings` menu item in the browser, followed by `Collaborators` on the left.  Click the `Add People` button in the middle and add me ({{ page.instructorgithub }}) as a collaborator.

#### Creating a README
Go to the `File - New Text File` menu, and type your name and a README describing what you've done.  Save this file as `README`.

#### Exporting a Project
Go to the `View - Command Palette` menu.  Type `Archive Folder` into the menu at the top to export your project.  It will be saved as a zip file just outside of the folder you created (i.e., on your desktop).

## What to Turn In

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.** 

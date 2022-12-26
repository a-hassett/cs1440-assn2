# CS 1440 Assignment 2: Big Data Processing 

* [Instructions](./instructions/README.md)
* [Hints](./instructions/Hints.md)
* [Rubric](./instructions/Rubric.md)
* [Installing the Text Tools](./instructions/Installing_Text_Tools.md)

Clone this repository and use it as a basis for your work.  Run each of these
commands one-at-a-time, without the '$' (that represents your shell's prompt).
Be sure to replace the words `LAST`, `FIRST`, and `USERNAME` with your own
names.

```
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn2 cs1440-LAST-FIRST-assn2
$ cd cs1440-LAST-FIRST-assn2
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn2.git
$ git push -u origin --all
```

## Overview

Your last project was a great success! The customer was very pleased with their
new TextTools and so impressed with the quality of your work that they have
decided to contract you to finish the entire project for them.

Your task is to analyze a large body of data and produce a report of the
findings.  This program summarizes national employment data collected by the
U.S. Bureau of Labor Statistics in 2020.  The report consists of two sections,
a summary across all industries and a summary across the software publishing
industry.  I worked with the customer far enough to develop the format of the
report.  It is your task to analyze a 493MB CSV file to pull out the data
needed by the report.


## Objectives

-   Learn how to process a large body of data
-   Using Python's built-in string operations
-   Research programming documentation
-   Reading, understanding, and following instructions
-   Using advanced data structures (list, dictionary, set)
-   Apply problem solving strategies
    -   Divide the problem
    -   Reduce the problem
    -   Don't get frustrated
-   Exercise debugging techniques
    -   Direct debugging with the IDE
    -   Indirect debugging
    -   Wolf-Fence debugging


## Expected Behavior

Each subfolder of [data/](data) contains a file named `output.txt`.
Your program's output for that data set should match that file exactly.

Instructions for creating the testing data sets using the Text Tools from
Assignment #1 are provided.  These crafted input files should form the basis of
your verification procedure.

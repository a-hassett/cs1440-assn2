# CS 1440 Assignment 2 Instructions

## Description

Write a Python program that summarizes the Bureau of Labor Statistics'
employment data for 2020.  This data is available in a text file.  Leverage
techniques learned in the previous assignment to achieve your goal.


## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 9.4
Average Score % (Grade)          | 92.33% (A-)
% students thought this was Easy | 27.01%
... Medium                       | 58.39%
... Hard                         | 11.68%
... Too Hard/Did not complete    | 2.92%



## Preparation

The starter code includes a selection of output examples.  The corresponding
data files can be created from the provided instructions by using your Text
Tools (or the "real" text tools provided with your shell).  These data sets are
for your use as you test and debug your program.  Reduced data sets that are
especially good for interactive debugging are Washington D.C., Delaware and
Rhode Island.  Your submission will be graded by running it against the full
BLS data set for the year 2020, as well as a **special, crafted data set** that
you will not have access to.  To ensure that your program will get full marks,
test it thoroughly by running it against the **full** data set.

*   The complete CSV file is too big to include in the git repository, and so
    you won't get it by cloning this project.
*   Instead, download it from this link: [2020.annual.singlefile.zip](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn2/uploads/4eb861c60490487135f56365b9397c48/2020.annual.singlefile.zip)
    *   Unzip it into your repository's `data/USA_full/` directory
    *   **Use only the copy of this file provided here!** Don't download the
        file directly from the BLS website as there is a possibility that they
        will change its contents without warning, rendering your output
        different from the provided examples.
*   Once the file is downloaded, follow the instructions in each sub-directory
    under `data/` to create smaller data sets for testing
    *   Use the smaller data sets while you are developing the program, and
        test against larger data sets as your project nears completion
    *   Use the `wc` tool to see which data sets are the small ones
    *   The data sets with `_reversed` names are identical to their
        corresponding `_combined` data sets save for one difference - they are
        created with `tac` instead of `cat`.  This reversal of their contents
        should make no difference to your program.  Use these data sets to
        ensure this is the case.


### Don't commit huge files to git!

I have crafted a special `.gitignore` file to prevent the inclusion of huge CSV
files into your git repository.  Don't do anything that defeats these
safeguards!

*   Don't rename or remove this `.gitignore` file.
*   Do not rename the CSV data file in any way. This includes changing its name
    from lower to upper case, changing punctuation, etc.
*   Before you do a `git commit`, first run `git status` and carefully examine
    the list of files to be added.  **STOP** if any CSV file besides
    `area_titles.csv` is about to be committed!


## Requirements

### Command Line Interface

To ensure that the graders are able to run your program, all submissions must
implement this command-line interface.

Your program accepts a single mandatory argument: the name of a directory
containing CSV files.

For example, to compute statistics for the complete Washington D.C. data set,
run this command from the repository's top directory:

```
$ python src/bigData.py data/DC_combined
```

To generate the report against the entire national database, use this command:

```
$ python src/bigData.py data/USA_full
```

When the data directory argument is omitted a message is printed and the
program exits:

```
$ python src/bigData.py
Usage: src/bigData.py DATA_DIRECTORY
```

When the specified directory is non-existent or inaccessible, simply let Python's `open()` function fail:

```
$ python src/bigData.py data/DERP
Traceback (most recent call last):
  File "src/bigData.py", line 220, in <module>
    fips = get_fips_areas(sys.argv[1])
  File "src/bigData.py", line 9, in get_fips_areas
    with open(f'{datadir}/area_titles.csv') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/DERP/area_titles.csv'
```

#### Important notes regarding this program's user interface

*   Unlike the previous assignment, this program takes exactly one argument,
    which is the name of a *directory*, not a *file*.
*   This program is an exception to our general rule about hard-coding file
    names into programs.
    *   For this assignment you *must* hard-code the names of the input files
        `area_titles.csv` and `2020.annual.singlefile.csv` into your program,
        but *not* the name of the directory containing them.
*   Do not make any assumptions about the current directory your program runs
    from.  It must be able to run from any working directory.
*   Do not read too much into the naming convention I used for the data
    directories supplied in this repository.
    *   The names of the directories should not make any difference to your
        program; your program should not employ an `if` statement to run
        different code when the directory name contains "_software" versus
        "_combined".
    *   Your program must be able to work with *any* directory name that can be
        supplied on the command line, even directories not included with the
        starter code.
    *   Just take the data as it comes and fill out the report *based on what
        is seen in the file*.


### Filling in the report

*   The starter code provides a module called `Report.py`
    *   Do not modify `Report.py`. Treat it as read-only.
    *   You may create new modules and classes if desired.
*   Study the starter code to learn how to use the Report object named `rpt`
    *   You can avoid a lot of extra variables if you use `rpt` for storage
    *   Some fields within `rpt` hold integers, others hold lists



### Running the program and checking your output

This repository contains many sample input directories under the `data/`
directory, each of which contains three files.

*   `README.md`
    -   Instructions for trimming the full data set down using command line text tools
*   `area_titles.csv`
    -   The database of FIPS area codes
*   `output.txt`
    -   The correct output for this data set

Unlike other assignments, this program's output must *exactly* match that of
the provided examples down to the smallest detail.

*   Except for the final `print(rpt)` line provided in the starter code, your final submission *must
not* write any other data to `sys.stdout`.
*   Before you turn in your finished program, delete all of the `print()`s that output **TODO** messages
    *   The `print()`s which report the time used to load the CSV files are okay to leave as-is because they write to the error stream `sys.stderr` instead of `sys.stdout`.


### Processing `area_titles.csv`

While the file name `area_titles.csv` is hard-coded into your program, the name
of the directory containing it is specified by the user.

This CSV file contains two columns of data, `area_fips` and `area_title`.
These columns map a FIPS area code into a familiar place name.


#### FIPS Codes

A FIPS code is a 5 character alphanumeric code similar to a ZIP code.  A FIPS
area can be a county, an entire state, or a metropolitan area.  There are even
FIPS codes which represent the nation as a whole.  The area designated by a FIPS
area code is much larger than a ZIP code, and one place may be represented by
many overlapping FIPS areas. It is important for the accuracy of the report
that overlapping areas excluded so as to not double-count statistics.

The format of FIPS area codes are described in the [QCEW Area Code
Guide](https://data.bls.gov/cew/doc/titles/area/area_guide.htm).  Part of the
assignment is to read and thoroughly understand this document.


#### How to use the information from `area_titles.csv`

*   Do not modify the file `area_titles.csv`; your program accepts this file as-is
*   Read this file one line at a time
    *   Decide whether or not to include this FIPS area in the final report by looking at the FIPS area code
    *   Your program can make this determination *solely* from the `area_fips` field; do not consider the `area_title`
*   Keep track of FIPS areas that may be included in the report by using one of Python's built-in *data structures*
    *   I recommend using a **dictionary** (it is much faster), but you could use a **list**
*   The report *must* consider data from all 50 states, the District of Columbia, and territories of the United States of America.
    *   This means that your report *must* include
        *   "Overseas Locations"
        *   "Multicounty, Not Statewide"
        *   "Out-of-State"
        *   and "Unknown Or Undefined" areas
    *   *All of these are easily identified by looking only at their FIPS codes*
    *   The report considers data only from counties and county-equivalent divisions
        *   For example, Louisiana has *parishes*, Alaska has *boroughs* and *census areas*, and Puerto Rico has *municipios*
*   Your report *must not* include US aggregate data, per-state aggregate data, nor should it consider metropolitan areas
    *   Inclusion of these areas will result in an incorrect report
    *   *Again, all of these are easily identified by the form of their FIPS codes*


#### Exclude these areas

*   "U.S. combined" and "TOTAL" FIPS areas
*   All areas labeled "statewide"
*   MicroSAs
*   MSAs
*   CSAs
*   Federal Bureau of Investigation – undesignated


#### Do *not* exclude these areas

*   Puerto Rico
*   Washington, D.C.
*   Virgin Islands


### Processing `2020.annual.singlefile.csv`

As with the file `area_titles.csv`, the file name `2020.annual.singlefile.csv` shall be hard-coded into your program.  The name of the directory in which this file is found is supplied by the user.

Each line of this file captures employment statistics such as total wages paid, the number of people employed and the number of establishments in each FIPS area for the year 2020.  The layout of this CSV file is described by [this document](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm).  Bear in mind as you read this document that we are working with the **singlefile**.

The fields in this file that are significant for our report are:

*   `area_fips`
*   `industry_code`
*   `own_code`
*   `total_annual_wages`
*   `annual_avg_emplvl`
*   `annual_avg_estabs`


#### How to use the information from `2020.annual.singlefile.csv`

*   Only one line of this file may be stored in memory at a time
    *   Avoid slurping the entire file into memory either as one giant string, or as an array
        *   To be crystal clear: it is not a good idea to use `.read()` or `.readlines()`
        *   Slurping works just fine on small input files, but is a big problem with large ones
        *   You are allowed to make temporary copies of the *current* line, and keep copies in different forms (i.e. you can have temporary variables holding strings, a list of sub strings, a dictionary, etc.)
        *   Once you've finished with the current line of input there is no need to keep it
        *   In Python this means you should overwrite any temporary variables, or just let them go out of scope
*   Not all lines of this file have information that will be included in the report
    *   In fact, your program will skip over the vast majority of the data it sees as it seeks the few data points our customer is interested in
    *   In addition to skipping over lines about excluded FIPS areas, you must also skip lines that don't belong to the sectors of the economy our customer is interested in
*   Any line of this file with the desired values for `area_fips`, `industry_code`, and `own_code` *must* be included in the report
    *   The name of the directory containing this file **does not matter** to your program
    *   For example, if a copy of `2020.annual.singlefile.csv` contains data about Washington State but is in a directory named "`South_Dakota`", then your program had better output something about Washington
*   Numeric data must be converted from a string through an appropriate function
    *   `eval()` is **inappropriate**


#### Excluded FIPS areas

Some lines contain data for areas that do not belong in the report.   Identify which lines your program should skip over by inspecting the `area_fips` column.  See the section above titled *How to use the information from `area_titles.csv`*.


#### All Industries

If a line of the file pertains to a reportable FIPS area and `industry_code` is equal to `"10"` and `own_code` is equal to `"0"`, then its data is added to the "all industries" portion of the report.


#### Software Publishing Industry

If a line of the file pertains to a reportable FIPS area and `industry_code` is equal to `"5112"` and `own_code` is equal to `"5"`, then its data is added to the "software publishing industry" portion of the report.


**No other industry codes or ownership codes have a place in the report.**

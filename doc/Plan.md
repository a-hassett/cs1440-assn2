# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

I have to figure out what FIPS codes correspond to what locations. I should include
overseas locations (_ _ 996), multicounty not statewide locations (_ _ 997), 
out-of-state locations (_ _ 998), and unknown or undefined areas(_ _ 999).\
\
So it will exclude US aggregate data, per-state aggregate data, and 
metropolitan areas ("U.S. Combined (US _ _ _)(3 letters), TOTAL (US000), statewide
( _ _ 000), MicroSAs or MSAs (C _ _ _ _)(4-digit number), CSAs (CS _ _ _), 
FBI - undesignated"(57000)). It will also include Puerto Rico, Washington D.C.,
and the Virgin Islands. There will be 3,643 out of 4,726 FIPS codes left after
doing this. Under 6 seconds is a very fast run time.\
\
There are many fields in the 2020.annual.singlefile.csv file. The only ones that
are relevant to us are area_fips (1) in the form of a 5-character string, 
industry_code (3) in the form of a 6-character string, own_code (2) in the form
of a 1-character string, total_annual_wages (16) in the form of a 15-digit integer,
annual_avg_emplvl (15) in the form of a 9-digit integer, and annual_avg_estabs (14)
in the form of an 8-digit integer.\
\
We're going to want to check that the FIPS code exists in the area_titles.csv file
and that it isn't one of the bad ones. We can do this through binary search, since
the file is already sorted. We can load the file into a dictionary linking the FIPS
code with its area title. This will make it easier to find the area's name later on
when we make the report. I'm not sure how dictionaries work, because I've never used
them before, but I think they're the kind that has a key that leads to an item. This
should be faster and easier than moving between indices in a list.\
\
After looking over the example sets again, it appears that the annual average
establishments is section 9, so index 8. Annual average employment is section 10, so
index 9. Total annual wages is section 11, so index 10. In the output, we will be
adding all the section 9's and searching for the largest. To save space, I will
make a totalEstablishments variable that I will keep adding to and a maxEstablishments
variable that I will compare to the current number of establishments. If it is greater
than the current max, I'll replace it. I'll also have to keep track of its index,
so I will also make a maxEstablishmentsFIPS to hold onto the right code that will
be linked through a dictionary to the right county name. I'll also have a line counter
so I can print the right number of counties. I'll do this same thing for section 10
and 11 with the employment level and total wages.\
\
The catch with the system outlined above is that it doesn't include every county
in the file. It only includes the software industry counties and the "all industries"
counties. Software industry counties are the ones whose industry codes are 5112 with
an ownership code of 5. "All industry" counties are ones where the ownership code 
is 0 and the industry code is 10.


## Phase 1: System Analysis *(10%)*

We will take input from the command line of the shell. This will be in the form of
a list of strings. We only care about sys.argv[1] which will contain the name of
the directory we will be using. Don't forget to open and close the files we're going
to be using! We will turn the data from directory/area_titles.csv
into a dictionary linking the FIPS code with the county name. Then we will read
through 2020.annual.singlefile.csv one line at a time. As we read the line, we will
line.split() it into a list, and then we will use list[0:3] and list[8:11] which
will keep only the parts of the file we care about. We will then check if the FIPS
code isn't one of the invalid ones outlined in Phase 0. (I think when I first start
programming this, I will test this to make sure it only runs through 3,643 lines.)
Then I will test if it's a software industry county. If yes, its data will be added
to the total, and I will store the FIPS code and max of the max county for each of
the three statistics. After running through the whole file, I will use the
dictionary we made earlier to find the matching county names for the record counties
that we only know the FIPS codes for. Then the Report class's variables will be
updated so I can print them. We also need to make sure to skip the first line of
every file.


## Phase 2: Design *(30%)*

```python
def isValidFips(fips):
    # the fips code will be the first item in the line: line[0]
    if fips == U.S. combined:  # US_ _ _
        return False
    elif fips == TOTAL:  # US000
        return False
    elif fips == statewide:  # _ _000
        return False
    elif fips == microSAs or MSAs:  # C _ _ _ _
        return False
    elif fips == CSAs:  # CS_ _ _
        return False
    elif fips == FBI - undesignated:  # 57000
        return False
    else:
        return True
```
```python
def isSoftwareIndustry(ownershipCode, industryCode):
    # ownership code will be line[1] and industry code will be line[2]
    if industryCode == 5112 and ownershipCode == 5:
        return True
    else:
        return False
```
```python
def isAllIndustries(ownershipCode, industryCode):
    # ownership code will be line[1] and industry code will be line[2]
    if industryCode == 10 and ownershipCode == 0:
        return True
    else:
        return False
```
```python
def makeAreaTitleDictionary(directory):
    # sys.argv[1] will provide the directory we're working with
    file = openFile(directory/area_titles.csv)
    fipsToAreaTitle = emptyDictionary  # I'll have to figure out how to make a dictionary
    for every line in file:
        add the data to emptyDictionary
    file.close()
```
```python
def findMaxAmounts(fips, annualAvgEst, annualAvgEmpLvl, totalAnnualWages):
    # fips is line[0], annualAvgEst is line[8], annualAvgEmpLvl is line[9], totalAnnualWages is line[10]
    totalWages = 0
    totalWages += annualAnnualWages
    totalEst = 0
    totalEst += annualAvgEst
    totalEmpLvl = 0
    totalEmpLvl += annualAvgEmpLvl
    maxWagesCode = ""
    if maxWages < totalAnnualWages:
        maxWages = totalAnnualWages
        # maxWages will be a list, so make sure to use the proper index
        maxWagesCode = fips
    if maxEst < annualAvgEst:
        maxEst = annualAvgEst
        # maxEst will be a list, so make sure to use the proper index
        maxEstCode = fips
    if maxEmpLvl < annualAvgEmpLvl:
        maxEmpLvl = annualAvgEmpLvl
        # maxEmpLvl will be a list, so make sure to use the proper index
        maxEmpLvlCode = fips
```
```python
def fipsToAreaTitle(maxFips, dictionary):
    print(dictionary[maxFips])
```


## Phase 3: Implementation *(15%)*

I struggled with making the dictionary, because it kept reading in the last line
of the area_titles.csv file which is blank, so I had an out of range area for a
while. Then I fixed the out of range error, but my while loop just kept going.
I fixed this by specifying a different between the line that was read in and the
split line. I couldn't figure out how to get the line to be read and split into
the correct type of variables. I had to turn the words with quotation marks around
them into a string type without extra quotes, and I turned the words with numbers
into float-type variables. I had to strip the extra quotes and type-cast to achieve
this. Then I had to double back and fix the variable types. Then it was working
fine, but it printed out extra lines. Then Professor Falor sent out an announcement
on Canvas, so I pulled from Gitlab and it fixed my problem! Then I just went back
and added some functions for readability and redid some variable types. I deleted
excess comments. I left the timing comments in just in case anyone wanted to use
them. I also tried to write a function that would simplify the updating of max values
and total values for each type of data, but the totals wouldn't update through
the function, so I had to do those separately. I ended up writing a function to
update the maximum value, and it made my code a lot more readable.


## Phase 4: Testing & Debugging *(30%)*

The biggest bug I ran into was when the 2020.annual.singlefile.csv file had an extra
line at the end, which it often did. I had to figure out how to exclude from the 
data reading to prevent index-out-of-range errors. I did this by counting the length
of the line. I also couldn't figure out, for the life of me, how to get rid of the
extra lines that were printing when I ran my code. It turned out not being my error,
but that stressed me out for a while. 


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

* I think when I split the lines from the 2020.annual.singlefile.csv it was pretty
messy. I had to mess with a lot of stuff to get it to turn out the way I wanted.
I had to split by comma, then remove extra quotation marks. If there weren't extra
quotation marks, I turned the value into an integer. I also think my technique for 
excluding the last line of the file was a bit messy, but now any empty lines in
the middle of the file won't be included either.
* I'm not sure how the class variables from Report.py get imported and used in
bigData.py. I kinda just hoped for the best and got it.
* I think it wouldn't take me long to find any bugs in my program. All the bugs I
worked with got identified pretty quickly. I knew where the problem lied; I just
had to figure out _how_ to fix it.
* I think my documentation will mostly make sense to other people. Phase 0 is written
a bit confusingly, because I wrote into it as I was understanding what was going on
during the first little bit. My future self might take a second look but it won't
be too bad.
* It will make sense to other people as well. I think I'm clear about what variables
and situations I'm talking about.
* Adding new features shouldn't be too hard. I can probably just make a new function
checking for some other kind of industry and add that to the Report.py file. It'll
be incorporated right along the others.
* I don't think my computer's hardware will affect the ability of my program. It might
speed it up or slow it down, but that's it.
* The operating system shouldn't matter, because I used forward slashes when I hard
coded the file names into my program. Forward slashes work for pretty much every
OS, but back slashes don't, which is why I avoided them.
* I think the riskiest things that will probably get updated in future versions of
Python are the string methods. The _string_.split() could get a little bit switched
up and the mutability of lists might change as well, which would just slow down
the program.

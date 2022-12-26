import time
import sys                                                          	         	  
from Report import Report                                           	         	  


rpt = Report(year=2020)
areaTitles = {}

def makeAreaTitleDictionary(directory):
    file = open(directory + "/area_titles.csv")

    while True:
        line = file.readline()
        splitLine = line.split("\"")
        if len(splitLine) > 1:  # exclude empty lines in file
            areaTitles[splitLine[1]] = splitLine[3]

        if not line:
            break
    file.close()


def isValidFips(fips):
    if fips[:2] == "US" or fips[2:] == "000" or fips[0] == "C" or fips == "57000":
        return False
    else:
        return True


# made these two separate functions instead of one function with more parameters for readability in the main function
def isAllIndustries(ownershipCode, industryCode):
    if ownershipCode == "0" and industryCode == "10":
        return True
    else:
        return False


def isSoftwareIndustry(ownershipCode, industryCode):
    if ownershipCode == "5" and industryCode == "5112":
        return True
    else:
        return False


def updateMax(max, fips, newAmount):
    if newAmount >= max[1]:
        max[0] = areaTitles[fips]
        max[1] = newAmount


if __name__ == '__main__':
    # number of arguments error
    if len(sys.argv) != 2:
        print("Usage: src/bigData.py DATA_DIRECTORY")
        exit(1)

    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    makeAreaTitleDictionary(sys.argv[1])

    file = open(sys.argv[1] + "/2020.annual.singlefile.csv")

    while True:  # for each line in file
        line = file.readline()
        splitLine = line.split(",")
        stripLine = []

        # exclude the last empty line
        if len(splitLine) == 1:
            break

        # fixing variable types
        for i in range(3):
            stripLine.append(splitLine[i].strip("\""))
        for i in range(3):
            if splitLine[i + 8].isnumeric():
                stripLine.append(int(splitLine[i + 8]))
            else:
                stripLine.append(0)


        if isValidFips(stripLine[0]):
            if isAllIndustries(stripLine[1], stripLine[2]):
                rpt.all.num_areas += 1

                # update maxes
                updateMax(rpt.all.max_annual_wage, stripLine[0], stripLine[5])
                updateMax(rpt.all.max_estab, stripLine[0], stripLine[3])
                updateMax(rpt.all.max_empl, stripLine[0], stripLine[4])

                # update totals
                rpt.all.total_annual_wages += stripLine[5]
                rpt.all.total_estab += stripLine[3]
                rpt.all.total_empl += stripLine[4]

            if isSoftwareIndustry(stripLine[1], stripLine[2]):
                rpt.soft.num_areas += 1

                # update maxes
                updateMax(rpt.soft.max_annual_wage, stripLine[0], stripLine[5])
                updateMax(rpt.soft.max_estab, stripLine[0], stripLine[3])
                updateMax(rpt.soft.max_empl, stripLine[0], stripLine[4])

                # update totals
                rpt.soft.total_annual_wages += stripLine[5]
                rpt.soft.total_estab += stripLine[3]
                rpt.soft.total_empl += stripLine[4]

        if not line:
            break

    file.close()

    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    print(rpt)

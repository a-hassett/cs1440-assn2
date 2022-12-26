This data set can be generated from a full copy of the data file `../USA_full/2020.annual.singlefile.csv`.  Navigate to this directory in your shell and run these commands:

    head -n 1 ../USA_full/2020.annual.singlefile.csv > header.csv
    grep '^"38' ../USA_full/2020.annual.singlefile.csv > dat.csv
    grep '"0","10"' dat.csv > trimmed.csv
    cat header.csv trimmed.csv > 2020.annual.singlefile.csv
    rm header.csv dat.csv trimmed.csv

*Note: You may use your own implementation of `tt.py` if it has been **installed**. See [Installing_Text_Tools.md](../../instructions/Installing_Text_Tools.md) for details and the modifications needed to the above sequence of commands.*

 # highestprofit

**Summary:** Read a CSV file containing corporate profits over the years and create JSON format data and look for highest profit values in the data.

Full instructions found [here.](https://github.com/bobbae/gcp/tree/main/challenges/highest-profit) 

## Requirements

 - Download the data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as "raw" and read the file into a program memory.
 - Print out how many rows of the data is in the CSV data. This is your first printed answer.
 - Remove all rows with 'profit' that is not numerical value. Then print out how many rows of data are left, after removing all the rows with invalid non-numeric profit column data. This is your second printed answer.
 - Convert the content you read into memory in your program in Part 1 into JSON format and write it out to another file called data2.json which should only contain rows of data that have the valid numeric profit values. Each row in the Array should contain data columns like year, rank, company, revenue, and profit.
 - Order the data based on the profit value. Print the top 20 rows with the highest profit values. This is your third printed answer.

## Instructions to run the program
This was tested on a Windows machine and as such, will be using the included run.bat script


1. Download the repository to your local machine

  ` git clone https://github.com/zimindkp/highestprofit workingdirectory`
  
2. Execute the run.bat script 

```bash
cd workingdirectory
run.bat
```

3. (Optional) Delete the local repository if no longer needer

```bash
cd workingdirectory
del .git
cd ..
del workingdirectory /s /q
```

**What the run.bat script does:**
- Navigates to the working directory for the standalone executable (dist/highest_profit)
- Downloads the data.csv file as raw format
- Executes the standalone executable highest_profit.exe
- Verifies a data2.json file was created in the current directory

## Verification
Check and make sure your solution produces three answers as printed output. And a file called data2.json is produced.

## Design

The main script run is highest_profit.py, included in this repository. I used the pandas library as I am familiar with it and suitable for the data analysis and manipulation required. I also use the json and numpy libraries for generating the JSON file and validating numerical data respectively. Since there are a number of dependencies, I packaged the whole program including the libraries needed into a standalone executable using [Pyinstaller.]((https://pyinstaller.readthedocs.io/en/stable/). 

I did my testing on a Windows machine and have included a run.bat script, as well as some output from my testing to show the results (testrun.log). The instructions above and run.bat script should guide you to the working directory and location of the packaged solution to run with no issues. 

If you have Python 3.6+ installed, you are welcome to run the highest_profit.py on your machine for further testing. The script successfully outputs the number of rows, then purges any rows with non-numerical values for "profit". It then converts the remaining rows with profit values to a signed datatype, then writes it to the json file in the same working directory. Lastly, the remaining data is sorted by profits in ascending order, and the top 20 highest profits are displayed.


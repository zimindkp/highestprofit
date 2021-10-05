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

## Verification
Check and make sure your solution produces three answers as printed output. And a file called data2.json is produced.

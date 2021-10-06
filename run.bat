@echo off
REM Go to working directory
cd dist/highest_profit

REM Verify a highest_profit.exe file exists
if not exist highest_profit.exe goto failure

REM  obtain file
curl -O -s https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv
dir | findstr "data.csv"
@echo:
REM run the standalone file
highest_profit.exe

REM verify the data2.json file was created
if not exist data2.json goto failure
@echo:
REM successful completion here
:failure
pause

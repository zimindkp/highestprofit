@echo off
REM Go to working directory
cd dist/highest_profit

REM Verify a highest_profit.exe file exists
if not exist highest_profit.exe goto failure

@echo:
REM run the standalone file
highest_profit.exe

REM verify the data2.json file was created
if not exist data2.json goto failure
@echo:
REM successful completion here
:failure
pause

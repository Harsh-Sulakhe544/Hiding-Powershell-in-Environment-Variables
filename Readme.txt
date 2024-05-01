THIS PROJECT ALSO FAILS , CUZ MY POWERSHELL RECOGNIZES THE SCRIPT WITH AI 
Commands in Powershell 

ls Env:  ==> to get all the "environment variables" 
Get-ChildItem ==> list all items under the directory ==> similar to "dir" or "ls" command 

project begins 
# GET ALL THESE list of ENV VARIABLES FROM  : https://www.computerhope.com/issues/ch000088.html

to test ==> 
Powershell  ==> echo $env:COMSPEC  ==> C:\WINDOWS\system32\cmd.ex  ==> we found cmd.exe location
also "echo $env:COMSPEC[18]" ==> gives answer 
if i paste "echo $env:COMSPEC" in file-explorer ==> we redirect to BING ==> means we are running a microsoft Server 

"REMEMBER WE ARE RUNNING 'FILE EXPLORER'  ON A MICROSOFT SERVER "

powershell ==> [char]65 ==>  A ==> testing part ==> we can do type-conversions in Powershell itself

Invoke expressions ==> iex in POWERSHELLL

we can hide in ex : 
PS C:\Users\itzha\Desktop\hidingPowerShell IN ENVIRONMENT> iex ($env:PATHTEXT[45], $env:ProgramW6432[10] -Join $env:PATHTEXT[1000])  

this command is not allowed , so we write 1 more function 

PROJECT CONFIGURATION 
"run envhide.py from path"  ==> u get a big ENVIRONMENT-VARIABLES-PASSKEY ==> 1  
"open POWERSHELL , then redirect to the path where we have this project"
"paste the PASSKEY IN POWERSHELL , AND CHECK WHETHER O/P IS 420"

"NOTE THIS PROJECT IS RANDOMISED DUE TO WHICH , RUN IT MULTIPLE TIMES TO OBTAIN PASSSKEY EACH 
TIME , PASTE IT IN POWERSHELL , UNTILL U GET A CORRECT ATTEMPT AND O/P AS 420 "

"IT MAY NOT WORK IN SOME OF THE SYSTEMS , BCUZ ADVANCEMENT OF POWERSHELL WITH AI FEATURE AND 
OTHER SECURITY UPDATES "
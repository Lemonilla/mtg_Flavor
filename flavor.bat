@echo off
setlocal EnableDelayedExpansion

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::
::: SCRIPT.........: flavor.bat
::: VERSION........: 3.0
::: DATE...........: 12/18/2014
::: AUTHOR.........: Neal Troscinski
::: REQUIRMENTS....: flavor.py
::: DESCRIPTION....: Downloads the flavor text from 
:::                  Magic: The Gathering cards.
:::
:::      flavor [threads]
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Check to see if arg[1] is defined.
:: If so, this instance is a thread with ID = arg[2]
if not "%~2"=="" goto :run

:: Setup threads and run them.
:: Split total number of cards by the number of threads
:: and start a thread for each segment.
:: If arg[0] is not defined, assign the
:: number of threads to 250.
set "threads=%~1"
if not defined total set total=100000
if not defined threads set threads=250
set /a add=%total%/%threads%
set lower=1
set upper=%add%
set t_ID=1
:thread
	start /b "" "cmd /c Python flavor.py %cd%\save_%t_ID%.txt %lower% %upper%"
	set /a lower+=%add%
	set /a upper+=%add%
	set /a t_ID+=1
if %lower% LSS %total% goto :thread
@echo off

cd C:\Users\Andrew\Andrew\Documents\CSC499HW1

@py.exe C:\Users\Andrew\Andrew\Documents\CSC499HW1\sort.py %*

fc /b Output SortedFile > nul
if errorlevel 1 goto files_differ
echo Test Passed

:files_differ
echo Test Failed

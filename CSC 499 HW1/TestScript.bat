@echo off

fc /b Output SortedFile > nul
if errorlevel 1 goto files_differ
echo Test Passed

:files_differ
echo Test Failed

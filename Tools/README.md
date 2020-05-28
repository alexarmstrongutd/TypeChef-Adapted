# About Each Tool

## extractScript

extractScript.sh takes 1 parameter a directory to insert the VAA result files into
the files are zipped and placed with the source code so this program takes those files and compiles them all in a readable
format

## cleanVAA

cleans out the VAA files to prepare for another run so that bad files may be cleaned out to avoid being parsed again

## extractLocations

deduplicates the header locations obtained in findCFiles.py and names the result headerSet.txt

## findCFiles

produces the list of files and list of headers (with dupes) that are used in the program

## HeaderCreater

This file was used to generate the correct config.h file for axtls by parsing the Config.in file.
If you are following the guide this should be unncessary.

## parser & test_parser

test_parser.py is a wrapper around parser.py which parses all the report files and compiles the results.

## ResultStats

This file produces the stats of the errors reported in the files. It does need an argument which is the Json file produces by the output of test_parser.py

## CompareResults

This file takes 2 arguments to json formatted files to compare errors based on line and filename and reports the number of differences in them

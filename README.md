# Name:
Yangbo Liu
# Stevens ID: 
yliu8
# URL: 
[https://github.com/Tythla/TestHarness](https://github.com/Tythla/TestHarness)
# Estimated time spent:
About 12 hour
# How I tested my codes:
I tested the code using a custom Python script named 'test.py'. This script automates the process of testing the three programs in the project. For each program, it reads input data from 'in' files, runs the program with this input, and then compares the program's output to the expected output stored in 'out' files. After that, it print's 'Pass' or 'Failed' on console with each programe's name.
# Bugs or Issues Encountered
One big issue encountered was related to how the 'test.py' script executed the programs. Initially, the script was designed to pass input data to the programs through STDIN. However, the programs were expecting file arguments instead. This mismatch led to all tests failing because the programs weren't receiving the expected input format.
# How to Resolve
I modified the 'test.py' script to run `subprocess.run` command for each program with its corresponding '.in' file as a command-line argument. This adjustment aligned with the expected usage of the programs and resolved the failures. 
# List of extension
1. wc with multiple files: There are two tests for wc.py. Input both of them as argument and the console should show both file's result and their sum.
2. wc with flags to control output: Using `-l`, `-w` or `-c` as argument after file name. The program will only display numbers for lines, words or characters. Combination like '-lw' will also work.
3. gron.py with control the base-object name: Add argument `--obj` and the name you like before the file name. The program with replace the base-object name. For example `gron --obj example test.json`.
# UiT [Bio-3027 / Bio-8027](https://uit.no/utdanning/emner/emne?p_document_id=785588&ar=2023&semester=V) 
## Introduction to Python in the Life Sciences Course 
### [Schedule Spring 2023](https://timeplan.uit.no/emne_timeplan.php?sem=23v&module=BIO-3027-1#week=1-25 "Timeplan")
---
This repository contains all course material, including lectures, sample code, and exercises.

The files are organised per day and will be updated accordingly.

Course description: [MSc](courseinfo/python_course_msc.pdf) [PhD](python_course_phd.pdf)  
Description of [final assignment](courseinfo/final_assignment_guidelines.pdf)

### Schedule Overview
_week 1_  
**[Day 1](basics_day1)**: Course intro, using Python, Strings, Numbers  
**[Day 2](datastructures_day2)**: Booleans, Data structures (dictionaries, lists), Loops & Control flow (for, while, if/else)  
**[Day 3](functions_day3)**: Functions, Sets, Tuples, Code structure, Practice with loops and data types learned so far  
**[Day 4](fileIO_day4)**: File handling, file parsing, practice day with recap exercises    
**[Day 5](modules_day5)**: Modules, advanced functions, error handling, more practice   

_week 2_  
**Day 6**: Object-oriented programming, basics of data science: Jupyter, Pandas, Scipy  
**Day 7**: Plotting: Matplotlib, Seaborn  
**Day 8**: Biology: BLAST, Biopython  
**Day 9**: Coding Practice, pathlib and argparse, start to work on assignments   
**Day 10**: Best practices, Good code, Work on assignments 

### Breakdown of Content per Day
_week 1_
1. [Day 1](basics_day1)
	* [introductory lecture](basics_day1/0_introduction.pdf)
		* brief overview of the course and expectations, practical info
	* [introductory lecture 2](basics_day1/1_1_basics.pdf)
		* what is inside your computer and how this relates to programming
		* operating systems, intro to the terminal
		* 3 ways of writing and running Python: interactive shell, script, IDE, [-->](basics_day1/script.py)
	* [variables, strings, numbers lecture](basics_day1/1_2_variables.pdf)
		* use of variables as placeholders for objects
		* Strings in python and their behaviour [-->](basics_day1/playing_with_strings.py)
		* basic number operations [-->](basics_day1/number_operations.py)
		* avoid whitespace at beginning of lines
		* how to comment in the script with hashtags and multiple line comments
		* general functions vs. methods
	* [exercise list](basics_day1/day1_exercises.pdf)
		* [greeter exercise](basics_day1/greeter.py)
		* [pizza volume calculator](basics_day1/pizza_area.py)
		* [string replacement exercises](basics_day1/replace_in_str.py)
2. [Day 2](datastructures_day2)
	* [data structures lecture](datastructures_day2/2_1_data_structures.pdf)
		* booleans don't behave as you would expect in Python, a lot more map to True [-->](datastructures_day2/practice_with_booleans.py)
		* if statements structured by indentation, meaning of if, elif, and else [-->](datastructures_day2/practice_with_booleans.py)
		* mutable types 1: lists can contain anything, and are readily changeable [-->](datastructures_day2/demo_with_lists.py)
		* mutable types 2: dictionaries are a key to value mapping sequence, even better than lists [-->](datastructures_day2/demo_with_dict.py)
		* for loops: use when you know how many times or what you want to loop over [-->](demo_for_loop.py)
		* while loops: use when you want to stop only if condition is met or don't know how many times you want to loop [-->](demo_while_loop.py)
	* [exercise list](datastructures_day2/day2_exercises.pdf)
		* [test number even odd exercise](datastructures_day2/test_number_odd_even.py)
		* [print number in loop exercise](datastructures_day2/print_number_in_loop.py)
		* [guess the number exercise basic](datastructures_day2/guess_the_number.py)
			* [Gaute game with hints](datastructures_day2/gaute_guess_the_number.py)
			* [Marja game that counts attempts](datastructures_day2/marja_guess_the_number.py)
	
		


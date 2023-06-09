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
**[Day 3](functions_day3)**: Functions, Code structure, Practice with loops and data types learned so far  
**[Day 4](fileIO_day4)**: Sets, Tuples, File handling, file parsing, list comprehension, practice day with recap exercises    
**[Day 5](review_day5)**: Review day with focus on File IO, Rosalind exercises   

_week 2_  
**[Day 6](modules_day6)**: Modules, error handling, numpy  
**[Day 7](pandas_day7)**: Jupyter, intro to data science with Pandas  
**[Day 8](plotting_day8)**: Plotting with Matplotlib and Seaborn    
**[Day 9](numpy_scipy_day9)**: brief intro to git, more pandas (biodiversity assignment), numpy, scipy    
**[Day 10](final_day10)**: biopython, best coding practices, start work on assignments    

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
		* [guess the number exercise advanced with numeric checker](datastructures_day2/number_guesser_checks_numeric.py)
3. [Day 3](functions_day3)
	* [functions lecture](functions_day3/functions_control_flow_day3.pdf): only covered functions and scope in this lecture
		* recap of day 2 while loop guessing game [-->](datastructures_day2/number_guesser_checks_numeric.py)
		* recap of day 2 with gc content script [-->](functions_day3/get_gc_content.py)
		* [introduction to functions](functions_day3/demo_with_functions.py)
	* [exercise list](functions_day3/day3_exercises.pdf)
		* [function to calculate mean](functions_day3/calculate_mean.py)
		* [function to calculate gc content](functions_day3/gc_calculator_function.py)
		* [function to invert a string, or swap its case](functions_day3/inverse_string.py)
		* [function to calculate factorial](functions_day3/calculate_factorial)
4. [Day 4](fileIO_day4)
	* [demo with list comprehension](fileIO_day4/demo_list_comprehension.py)
		* [even odd list comprehension exercise](fileIO_day4/even_odd_list_comprehension.py)
	* [demo sets tuples](fileIO_day4/demo_sets_tuples.py)
	* [exercise list](fileIO_day4/mean_file_reading_exercise.py)
		* [mean file reading exercise](fileIO_day4/mean_file_reading_exercise.py)
5. [Day 5](review_day5): Today is a review day, focusing on all we have learned so far.  
	* [exercise list](review_day5/exercise_outline_wk1_day5.pdf)
	* [rainfall exercise](review_day5/average_rainfall.py)
		* use the [rainfall data](review_day5/rainfall.txt)
	* [rosalind count nucleotides exercise](review_day5/rosalind_count_nucleotides.py)
	* [rosalind transcribe dna to rna exercise](review_day5/rosalind_transcribe_dna_to_rna.py)
	* [rosalind reverse complement exercise](review_day5/rosalind_reverse_complement_dna.py)


_week 2_

6. [Day 6](modules_day6)
	* [demo with modules](modules_day6/demo_modules.py)
		* use the [greeter functions](modules_day6/greeter.py) in the demo
	* [brief introduction to lambda](modules_day6/lambda_exercise.py)
	* [exercise list](modules_day6/exercise_list_day6.pdf)
	* [building a module out of rosalind](modules_day6/rosalind_utils.py)
		* import the rosalind module in [sequence analysis script](modules_day6/sequence_analysis.py)
	* [rosalind GC content exercise](modules_day6/rosalind_gc_content_full.py): very good exercise to practice!
	* practice with [regular expressions](https://regexone.com/)
7. [Day 7](pandas_day7): We only cover jupyter and pandas today! Numpy and Scipy we will get more into on Thursday
	* [introduction to jupyter notebook](pandas_day7/intro_jupy_pandas.ipynb)
	* [introduction to pandas](pandas_day7/presentation_pandas.ipynb)
		* use the [tips dataset](pandas_day7/tips.csv), [iris dataset](numpy_scipy_pandas_day7/iris.csv), and [gene mapping dataset](numpy_scipy_pandas_day7/gene_mapping.tsv)
	* our main exercise today is the [biodiversity](pandas_day7/biodiversity) exercise
		* you need the [species](pandas_day7/biodiversity/species_info.csv) and [observation](pandas_day7/biodiversity/observations.csv) datasets
		* we skip the plotting and statistics parts (chi squared test)
		* use pandas for this exercise
8. [Day 8](plotting_day8)
	* zoom link for exercise sharing: https://uit.zoom.us/j/62796373530?pwd=MFJoZGg3NWNnMEFuc3RaNTZTS3Rodz09
    * We start and work in the Jupyter notebook
    * Introduction to Matplotlib
	* From a simple plot towards plot customization
    * From Matplotlib towards other plotting libraries
    * Learning how to re-use and adapt a gallery example
    * Learning how to re-use an example with own data
9. [Day 9](numpy_scipy_day9)
	* [introduction to Git](https://rogerdudler.github.io/git-guide/)
	* [numpy exercise worksheet](numpy_scipy_day9/presentation_numpy.ipynb) as jupyter notebook
	* [finish biodiversity exercise](numpy_scipy_day9/biodiversity_key.ipynb)
		* **skip** chi squared test and the last minimum detectable size part (last two lines of code)
10. [Day 10](final_day10)


# Exercise I - PYTHON DATA STRUCTURES AND CONTROL FLOW

<footnote>

#### I. [Data Analysis and Processing](#data-analysis-and-processing)

#### II. [Mechanical Data Analysis](#mechanical-data-analysis)

#### III. [Beam Analysis](#beam-analysis)

#### IV. [Evaluation Criteria](#evaluation-criteria)

#### V. [Submission Instructions](#submission-instructions)
</footnote>

**NOTE:** We did not cover error handling in the class but I will cover that in our next class.

## Data Analysis and Processing 

You are given a CSV file containing information about various books. Your task is to read this data, process it, perform calculations, and output the results. You will implement several functions to handle different aspects of the data analysis. You need to use code template provided for this  part of the assignment and complete the functions. See the "Code Template" section for this part of the assignment.

### Data Loading and Initial Processing

1. Implement a function `load_book_data(filename)` that reads the CSV file and returns a list of dictionaries, where each dictionary represents a book with properties like 'title', 'author', 'year', 'genre', and 'price'.

2. Create a function `calculate_discount_price(books, discount_rate)` that takes the list of book dictionaries and a discount rate, and adds a new key-value pair for the discounted price to each book dictionary.

3. Implement a function `find_unique_genres(books)` that returns a set of unique genres from the data.

### Data Analysis and Filtering

4. Create a function `filter_books_by_year(books, start_year, end_year)` that returns a list of books published within the given year range.

5. Implement a function `sort_books(books, sort_by, reverse=False)` that sorts the list of books based on a specified property.

6. Create a function `find_most_prolific_author(books)` that returns the author with the most books in the dataset.

### Analysis and Reporting

7. Implement a function `calculate_average_price_by_genre(books)` that calculates and returns a dictionary of average book prices for each genre.

8. Create a function `generate_book_report(books, output_filename)` that writes a formatted report of the books and their properties to a text file.

### Data Manipulation 

9. Implement a function `update_book_properties(books, updates)` that takes a dictionary of updates (book title as key, dictionary of property updates as value) and modifies the books list accordingly. 

10. Create a function `convert_currency(books, exchange_rate)` that converts the prices of books to a different currency based on the given exchange rate. Use exception handling to manage potential conversion errors.

### Code Template
Use the code template provided [here](./Exercise/0_template.py) and replace `TODO` and `pass` parts with the code lines required to perform the task. DO NOT CHANGE THE FUNCTION NAME.


### Input Data
The input file `books.csv` can be found [here](./Exercise/books.csv).

### Expected Output
The program should generate an output file `book_analysis_report.txt` containing a formatted report of the books, their properties, and the results of various analyses performed. See the `main()` function in the template.

### Hints
- Use appropriate data structures (lists, dictionaries, sets) for different parts of the exercise.
- Implement error handling to deal with potential issues in data processing and file operations.
- Consider using list comprehension for more concise code where appropriate.
- Pay attention to the types of values you're working with (strings vs. numbers) and convert as necessary. See [this page](https://www.geeksforgeeks.org/type-conversion-in-python/) for help if you are not familiar with type conversion.


## Mechanical Data Analysis

You are given a CSV file containing time, position, and force data from a simple mechanical experiment. Your task is to analyze this data, calculate velocity and acceleration, determine the maximum force applied, and compute the work done on the system. You need to use code template provided for this  part of the assignment and complete the functions. See the "Code Template" section for this part of the assignment.

### Tasks

1. Implement the following functions in the [template file](./Exercise/1_template.py)

   a. `read_mechanical_data(filename)`  
   b. `calculate_velocity(position_data, time_step)`  
   c. `calculate_acceleration(velocity_data, time_step)`  
   d. `find_max_force(force_data)`  
   e. `calculate_work_done(force_data, position_data)`  
   f. `write_results(filename, results_data)`  

2. Use these functions in the `main()` function to process the data and generate results.

3. Handle potential exceptions that may occur during file operations or calculations.

### Code Template
See the code template [here](./Exercise/1_template.py) and replace `TODO` and `pass` parts with the code lines required to perform the task. DO NOT CHANGE THE FUNCTION NAME.

### Input Data

The input file `mechanical_data.csv` contains time, position, and force data in the following format:
```sh
time,position,force
0.00,0.0000,10.0000
0.10,0.0314,9.5106
0.20,0.0628,8.0902
0.30,0.0941,5.8779
0.40,0.1253,3.0902
```
See the input data file [here](./Exercise/mechanical_data.csv).

### Expected Output

The program should generate an output file `analysis_results.csv` containing the calculated velocity, acceleration, maximum force, and total work done. The exact format of this file is up to you to decide as part of the exercise.

### Hints

- Use the `csv` module for reading and writing CSV files. 
    ```python 
    import csv
    ```
- For velocity and acceleration calculations, use simple difference formulas: v ≈ Δx/Δt, a ≈ Δv/Δt.
- Work done can be approximated as the sum of force times displacement for each time step.
- Handle potential exceptions, especially during file operations.

## Beam Analysis

You are given a CSV file containing data about a beam, including its length, cross-sectional properties, and applied loads at different points. Your task is to analyze this data, calculate maximum bending stress, maximum shear stress, and maximum deflection of the beam. You need to use code template provided for this  part of the assignment and complete the functions. See the "Code Template" section for this part of the assignment.

### Tasks

1. Implement the following functions:

    a. `read_beam_data(filename)`  
    b. `calculate_bending_moment(length, loads)`  
    c. `calculate_shear_force(loads)`  
    d. `calculate_max_bending_stress(max_moment, moment_of_inertia, y_max)`  
    e. `calculate_max_shear_stress(max_shear, first_moment, moment_of_inertia, width)`  
    f. `calculate_max_deflection(length, loads, elastic_modulus, moment_of_inertia)`  
    g. `write_results(filename, results_data)`  

2. Use these functions in the main() function to process the data and generate results.

3. Handle potential exceptions that may occur during file operations or calculations.

### Code Template
See the code template [here](./Exercise/2_template.py) and replace `TODO` and `pass` parts with the code lines required to perform the task. DO NOT CHANGE THE FUNCTION NAME.

### Input Data
The input file `beam_data.csv` contains the following data: 
```
length, width, height, elastic_modulus
load_position_1, load_magnitude_1
load_position_2, load_magnitude_2
...
```
See the input data file [here](./Exercise/beam_data.csv).

### Expected Output
The program should generate an output file `beam_analysis_results.csv` containing the calculated maximum bending stress, maximum shear stress, and maximum deflection.

### Hints
- Use the csv module for reading and writing CSV files.
    ```python
    import csv
    ```
- For beam calculations, you may assume a [simply supported beam](https://calcresource.com/statics-simple-beam-diagrams.html).
- Handle potential exceptions, especially during file operations and calculations.

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

1. Correctness of implementation for each function
2. Proper use of Python data structures (lists, tuples, dictionaries)
3. Effective use of file I/O operations.
4. Proper error handling.
5. Code readability.

## Submission Instructions

1. Complete the implementation of all functions in the provided template. DO NOT CHANGE THE FUNCTION NAMES.
2. Ensure your code runs without errors and produces the expected output.
3. Make sure not to change the name of the functions in the code.
4. You are NOT allowed to use any special Python library except the ones mentioned in the code template and in this guide.
5. Submit your Python scripts and the output data for each part as the final submission on MS Teams.
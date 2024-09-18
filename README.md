# PA 3 - Python Data Analysis (PANDAS)

To create a Python script/code in the Jupyter Notebook to do the given problems.

## Description/Given Problems

### 1. **PROBLEM 1:** Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:
  - a) Load the corresponding .csv file into a data frame named cars using pandas
  - b) Display the first five and last five rows of the resulting cars.

### **PROBLEM 2:** Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
    - a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
    - b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
    - c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
    - d) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

## Getting Started

### Dependencies

* Anaconda Navigator
* Jupyter Notebook
* Optional : Microsoft Excel
* Any updated version of Windows, Mac, or Linux that is capable of running the programs above.

### Executing program

* How to run the program
* In order to run each cell, please remember to press Shift + Enter.
```
import pandas as pd
```
* It is crucial to include "import pandas as pd" as the entire Python script relies on this specific code.
```
# Read cars data from CSV file into dataframe
cars=pd.read_csv("cars.csv")
```
* The code block above is also important as this loads the .csv file. Without it, the entire script won't run.

## Author

Sherwin Miguel C. Mapaye

## Version History
* 0.1
    * Initial Release

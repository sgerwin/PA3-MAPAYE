# PA 3 - Python Data Analysis (PANDAS)

## :bulb: Intended Learning Outcomes
- To identify the codes and functions incorporated in the Pandas library<br>
- To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

### :hammer: Instructions
- To create a Python script/code in the Jupyter Notebook to do the given problems

## :ledger: Index

- [Description/Given Problems](#beginner-descriptiongiven-problems)
- [Getting Started](#green_circle-getting-started)
   - [Dependencies](#electric_plug-dependencies)
   - [Executing Program](#wrench-executing-prorgram)
- [Author](#writing_hand-author)
  - [Acknowledgements](#star2-acknowledgements)
- [Version History](#scroll-version-history)

## :beginner: Description/Given Problems

**PROBLEM 1:** Save your file as Surname_Pandas-P1.py

- Using knowledge obtained from the experiment and demonstrations:
   - a) Load the corresponding .csv file into a data frame named cars using pandas
   - b) Display the first five and last five rows of the resulting cars.

**PROBLEM 2:** Save your file as Surname_Pandas-P2.py

- Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
   - a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
   - b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
   - c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
   - d) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

## :green_circle: Getting Started

### :electric_plug: Dependencies

* Anaconda Navigator
* Jupyter Notebook / Visual Studio Code
* _**[cars.csv](http://bit.ly/Cars_file)**_
* _Optional: Microsoft Excel_
* Any updated version of Windows, Mac, or Linux that is capable of running the programs above.

### :wrench: Executing Program

* How to run the program
* Make sure to have downloaded the _**[cars.csv](http://bit.ly/Cars_file)**_
* In order to run each cell, please remember to press **_Shift + Enter_**
```
import pandas as pd
```
* It is **_crucial_** to include __"import pandas as pd"__ as the entire Python script relies on this specific code.
```
# Read cars data from CSV file into dataframe
cars=pd.read_csv("cars.csv")
```
* The code block above is also important as this loads the .csv file. Without it, the entire script won't run.

## :writing_hand: Author
* Sherwin Miguel C. Mapaye

### :star2: Acknowledgements
* [Engr. Ma. Madecheen S. Pangaliman, MSc](https://www.ust.edu.ph/profile/pangaliman-ma-madecheen-s)<br>
* Engr. Nico John Leo S. Lobos

## :scroll: Version History
* 0.1
   * Initial Release


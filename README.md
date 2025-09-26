# maximielfrancisco-pixel_Francisco-Maximiel-Anton-V.--PA-3
------
### 1)  Problem 1: It is Displaying Data from CSV 
The program reads a dataset (cars-PA3.csv) and displays its contents, including the first and last 5 rows. This helps to preview and verify the dataset.

```python
 import pandas as pd

# READ THE CSV FILE
CARS = pd.read_csv('cars-PA3.csv')
CARS

# BY THE FUNCTION .HEAD AUTOMATICALLY DISLAY THE FIRST 5 ROWS OF DATA
CARS.head()

# BY THE FUNCTION .TAIL AUTOMATICALLY DISLAY THE LAST 5 ROWS OF DATA
CARS.tail()

```
##### Step-by-Step Procedure of Functions:
- `import pandas as pd` → imports the pandas library, which is used for handling tabular data.
- `pd.read_csv('cars-PA3.csv')` → This Code reads the CSV file and will be able load into PANDAS Data Frame
- `_head()` → Shows the First 5 rows of the Data Frame by default output of its code
- `_.tail()` → Shows the Last 5 rows of the Data Frame by default output of its code

Outcome:
- The complete car dataset is loaded and displayed.
- The first 5 rows and the last 5 rows are shown to give a quick view of the dataset’s structure.
------
### 2) Problem 2: It Filters and Selects Data
 The program performs different operations on the car dataset using pandas indexing and filtering techniques, such as .iloc, .loc, and .isin.

```python
import pandas as pd

# READ CSV FILE AND SHOW DATA
CARS = pd.read_csv('cars-PA3.csv')
CARS

# DO THE CONDITION FOR .ILOC
CARS.iloc[:5, 1::2]

# WILL USE BOOLEAN INDEXING TO FILTER ROWS
CARS[CARS['Model'] == 'Mazda RX4']

# LOCATE SPECIFIC MODEL AND SPECIFIC CYL
CARS.loc[CARS['Model'] == 'Camaro Z28', ['Model','cyl']]

# USE .ISIN TO FILTER MULTIPLE MODELS, THEN SELECT SPECIFIC COLUMNS TO SHOW
CARS.loc[CARS['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear']]


```

##### Step-by-Step Procedure of Functions:
- `pd.read_csv('cars-PA3.csv')` → This Code reads the CSV file and will be able load into PANDAS Data Frame
- `CARS.iloc[:5, 1::2]` → This selects the first 5 rows and every other column starting at index 1, showing the odd format of using index collumns
- `CARS[CARS['Model'] == 'Mazda RX4']` → This is a Function uses boolean indexing to be able to filter specific rows. Hence, this display only the row where the car model is "Mazda RX4"
- `CARS.loc[CARS['Model'] == 'Camaro Z28', ['Model','cyl']]` → This Code I used shows the row for Camaro Z28 and shows only its Model and cyl columns
- `CARS.loc[CARS['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear']]` → Using the .isin() built in code gives us flexibility to filter multiple rows at once. Therefore, (Mazda RX4, Ford Pantera L, Honda Civic) and only display the "cyl" and "gear" columns for those cars.

Outcome:
- A subset of rows and columns is displayed using .iloc.
- The "Mazda RX4" row is displayed separately.
- The "Camaro Z28" model’s cylinder count is shown.
- The cylinder and gear values for multiple models (Mazda RX4, Ford Pantera L, --Honda Civic) are displayed.


------
VER 2 README

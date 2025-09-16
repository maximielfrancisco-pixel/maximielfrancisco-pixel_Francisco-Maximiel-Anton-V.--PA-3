# maximielfrancisco-pixel_Francisco-Maximiel-Anton-V.--PA-3
------
### 1)  Problem 1:
```python
  CARS = pd.read_csv('cars-PA3.csv')
  CARS
```
##### Step-by-Step Procedure of Functions:
- `pd.read_csv('cars-PA3.csv')` → This Code reads the CSV file and will be able load into PANDAS Data Frame
- `_head()` → Shows the First 5 rows of the Data Frame by default output of its code
- `_.tail()` → Shows the Last 5 rows of the Data Frame by default output of its code
------
### 2) Problem 2:

##### Step-by-Step Procedure of Functions:
- `pd.read_csv('cars-PA3.csv')` → This Code reads the CSV file and will be able load into PANDAS Data Frame 
- `_.iloc[:5, 1::2]` → This selects the first 5 rows and every other column starting at index 1, showing the odd format of using index collumns
- `[0:1]` → This is a Function that uses row slicing using on the DataFrame.
- `CARS.loc[CARS['Model']=='Camaro Z28',` → This Code I used shows the row for Camaro Z28 and shows only its Model and cyl columns
- `_.loc[[1,28,18],['Model','cyl','gear']]` → Retrieves the rows at indices 1, 28, and 18 (Mazda RX4 Wag, Ford Pantera L, Honda Civic) and as stated form the problem will displays their Model, cyl, and gear values.
------

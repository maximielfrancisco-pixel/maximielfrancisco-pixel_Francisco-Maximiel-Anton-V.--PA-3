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
```python
  CARS.iloc[:5, 1::2]
```
- `[[''] == '']` → This is a Function uses boolean indexing to be able to filter specific rows
```python
  CARS[CARS['Model'] == 'Mazda RX4']
```
- `.loc[CARS['']=='',[]]` → This Code I used shows the row for Camaro Z28 and shows only its Model and cyl columns
```python
  CARS.loc[CARS['Model'] == 'Camaro Z28',
        ['Model','cyl']]
```
- `CARS.loc[CARS['Model'].isin(['','']), ['','']]` → Using the .isin() built in code gives us flexibility to filter multiple rows at once
  ```python
  CARS.loc[CARS['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear']]
```
------

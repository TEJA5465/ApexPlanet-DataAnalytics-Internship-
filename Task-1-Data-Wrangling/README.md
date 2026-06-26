# Task 1 - Data Immersion and Wrangling

## Internship

ApexPlanet Data Analytics Internship

## Objective

The objective of this task is to understand the dataset, perform data cleaning operations, remove inconsistencies, handle missing values, standardize column names, and prepare the dataset for analysis.

---

## Dataset Information

Dataset Name: Superstore Sales Dataset

Number of Records: 10

Number of Columns: 9

Columns:

1. Order_ID
2. Order_Date
3. Customer_Name
4. Region
5. Category
6. Sub_Category
7. Sales
8. Profit
9. Quantity

---

## Tools Used

* Python 3.12
* Pandas
* Microsoft Excel
* Visual Studio Code
* Command Prompt

---

## Folder Structure

Task-1-Data-Wrangling

data/

* raw_dataset.csv
* cleaned_dataset.csv

reports/

* data_dictionary.xlsx

screenshots/

* raw_dataset.png
* cleaned_dataset.png
* python_code.png
* cmd_output.png
* data_dictionary.png

scripts/

* data_cleaning.py

README.md

---

## Data Cleaning Process

### Step 1: Load Dataset

The dataset was loaded using Pandas.

### Step 2: Data Inspection

Checked:

* Number of rows
* Number of columns
* Data types
* Sample records

### Step 3: Remove Duplicates

Duplicate records were removed using:

drop_duplicates()

### Step 4: Handle Missing Values

Missing values were replaced with:

Unknown

### Step 5: Standardize Column Names

Column names were converted into lowercase format and spaces were replaced with underscores.

Example:

Order Date → order_date

Customer Name → customer_name

### Step 6: Save Cleaned Dataset

The cleaned dataset was exported as:

cleaned_dataset.csv

---

## Python Script

File:

data_cleaning.py

Main Functions Used:

* read_csv()
* drop_duplicates()
* fillna()
* to_csv()

---

## Results

Successfully loaded the dataset.

Successfully cleaned the data.

Successfully generated cleaned_dataset.csv.

Successfully prepared the dataset for Exploratory Data Analysis (EDA).

---

## Output Files

1. raw_dataset.csv
2. cleaned_dataset.csv
3. data_dictionary.xlsx
4. data_cleaning.py

---

## Conclusion

The dataset was successfully cleaned and transformed into a structured format suitable for further analysis, visualization, dashboard development, and business intelligence reporting.

# 🐼 Pandas Cheat Sheet:
This guide covers the essential Pandas operations required for Data Analysis and Science. 

---

## 🏗️ 1. Getting Started & Data Loading
Before any analysis, we need to bring data into our environment.
```python
import pandas as pd
import numpy as np

# Loading different file formats
df = pd.read_csv('data.csv')          # CSV
df = pd.read_excel('data.xlsx')      # Excel
df = pd.read_json('data.json')        # JSON


2. Data Inspection (First Look)

df.head(10) : Pehli 10 rows dekhne ke liye.

df.info() : Data types aur memory usage check karne ke liye.

df.describe() : Statistical summary (Mean, Median, Std Dev) ke liye.

df.shape : Rows aur columns ka count (Dimensions) janne ke liye.

df.columns : Saare column names ki list.



3. Selection & Filtering (The Core)
Data manipulation ka sabse zaruri hissa.

Using .loc and .iloc
.loc : label based -> Index names ya Column names se select karta hai.
.iloc : Integer -  based -> Row/Column ke position (0, 1, 2) se select karta hai.

Advanced Filtering
# Multiple conditions: Use & (AND) and | (OR)
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'Delhi')]

# Selecting specific columns
subset = df[['Name', 'Salary', 'Designation']]



4. Data Cleaning
Real-world data messy hota hai.
# Checking for missing values
df.isnull().sum()

# Dropping missing values
df.dropna(inplace=True)

# Filling missing values (Mean Imputation)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Renaming Columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Changing Data Types
df['Date'] = pd.to_datetime(df['Date'])



5. Data Aggregation & Grouping
nsights nikalne ke liye grouping zaruri hai.

# Grouping by Category and finding Mean
category_avg = df.groupby('Category')['Price'].mean()

# Pivot Tables (Like Excel)
pivot = df.pivot_table(index='City', columns='Year', values='Sales', aggfunc='sum')

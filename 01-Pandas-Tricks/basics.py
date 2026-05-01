import pandas as pd

# Loading different file formats
df = pd.read_csv('data.csv')          # CSV
df = pd.read_excel('data.xlsx')      # Excel
df = pd.read_json('data.json')        # JSON

# 1. Loading Data 
df = pd.read_csv('your_data.csv')

# 2. Quick Inspection
print(df.head()) # Top 5 rows
print(df.info()) # Data types aur missing values ki summary

# 3. Filtering 
# Sirf wo rows jahan 'Sales' 1000 se zyada ho
high_sales = df[df['Sales'] > 1000]

# 4. Handling Missing Values 
# Missing values ko column ke mean se bhar dena
df['Age'] = df['Age'].fillna(df['Age'].mean())

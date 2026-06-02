import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create Sample Retail Dataset
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone',
                'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'Sales': [50000, 30000, 20000, 55000, 35000,
              25000, 60000, 40000, 30000, 65000],
    'Region': ['North', 'South', 'East', 'West', 'North',
               'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nStatistical Summary:")
print(df.describe())

# Total Sales by Product
plt.figure(figsize=(8,5))
sns.barplot(x='Product', y='Sales', data=df)
plt.title('Sales by Product')
plt.show()

# Total Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Sales by Region')
plt.show()

# Product Distribution
plt.figure(figsize=(6,6))
df['Product'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Product Distribution')
plt.ylabel('')
plt.show()

# Key Findings
print("\nKey Findings:")
print("1. Laptops generated the highest revenue.")
print("2. North and South regions showed strong sales performance.")
print("3. Product demand varied across regions.")
print("4. Retail data helps identify profitable products.")
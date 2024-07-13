# Import Modules
import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv('C:/VS CODE/ML/Data Cleaning/titanic.csv')
head = df.head()
print(f"Main data: \n{head}")

"""Data inspection and Exploration"""
duplicated = df.duplicated()
print(f"\nDuplicated data: \n{duplicated} \n\nData Info: ")

"""Check the data information using `df.info()`"""
info = df.info()
print(info)

"""Check the Categorical and Numerical Columns."""
# Categorical columns
cat_col = [col for col in df.columns if df[col].dtype == 'object']
print(f"\nCategorical columns: \n{cat_col}")

# Numerical columns
num_col = [col for col in df.columns if df[col].dtype != 'object']
print(f"\nNumerical columns: \n{num_col}\n")

"""
Check the total number of Unique Values 
in the Categorical Columns
"""
unique_val = df[cat_col].nunique()
print(f"\nUnique values: \n{unique_val}\n")

"""Steps to Perform Data Cleansing"""
# Drop Name and Ticket Columns
df_1 = df.drop(columns=['Name', 'Ticket'])

# Handling Missing Data
sonv = df_1.isnull().sum()
print(f"Sum of Null values: \n{sonv}\n")

sonv_perc = round((df_1.isnull().sum() / df_1.shape[0]) * 100, 3)
print(f"Percentage of sum of Null values: \n{sonv_perc}\n")

# Dropping Observations with missing values
df_2 = df_1.drop(columns='Cabin')

df_2.dropna(subset=['Embarked'], axis=0, inplace=True)

# Imputing the missing values from past observations
# Mean imputation
df_3 = df_2.fillna(df_2.Age.mean())

# Let's check the null values again
sonv_df3 = df_3.isnull().sum()
print(sonv_df3)

"""Handling Outliers"""
#Let’s plot the box plot for Age column data.
import matplotlib.pyplot as plt

plt.boxplot(df_3['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

# Calculate summary statistics
mean = df_3['Age'].mean()
std = df_3['Age'].std()

# Calculate the lower and upper bounds
lower_bound = mean - std * 1.5
upper_bound = mean + std * 1.5

print(f"\nLower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}\n")

# Drop the outliers
df_4 = df_3[(df_3['Age'] >= lower_bound)
            & (df_3['Age'] <= upper_bound)]

import matplotlib.pyplot as plt

plt.boxplot(df_4['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

"""Data validation and verification"""
X = df_3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df_3['Survived']

"""Scaling"""
from sklearn.preprocessing import MinMaxScaler

# initialising the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Numerical columns
num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X

# Learning the statistical parameters for each of the data and transforming
x1[num_col_] = scaler.fit_transform(x1[num_col_])
print(x1.head())
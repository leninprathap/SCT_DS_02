#Data Cleaning 

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

np.random.seed(0)

data = pd.DataFrame({
    'Age': np.random.randint(18, 80, size=200),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], size=200, p=[0.45, 0.45, 0.1])
})

print("=== Missing Values ===")
print(data.isnull().sum())
print("\n=== Data Types ===")
print(data.dtypes)
print("\n=== Unique Genders ===")
print(data['Gender'].unique())

print("\n=== Descriptive Statistics ===")
print(data.describe(include='all'))

plt.figure(figsize=(10, 5))
plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Age in Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


gender_counts = data['Gender'].value_counts()

plt.figure(figsize=(7, 5))
gender_counts.plot(kind='bar', color=['lightcoral', 'lightblue', 'lightgreen'], edgecolor='black')
plt.title('Distribution of Gender in Population')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x='Gender', y='Age', palette='Set3')
plt.title('Age Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.tight_layout()
plt.show()

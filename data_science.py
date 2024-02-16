import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Define file path
file_path = "/home/w091h948/FunDataScience/sample_data.csv"

# Read the CSV file without specifying data types
df = pd.read_csv(file_path)

# Visualize the distribution of the 'age' numerical feature using a histogram
df['age'].hist(bins=30, figsize=(10, 6))
"""plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()"""

# Visualize the relationship between 'salary' and 'age' using a scatter plot
fig = px.scatter(df, x='age', y='salary', title='Scatter Plot of Age vs Salary')
fig.show()

# Visualize the distribution of the 'gender' categorical feature using a bar plot
df['gender'].value_counts().plot(kind='bar', figsize=(10, 6))
plt.title('Count of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Calculate the average salary for males and females separately
average_salary_male = df[df['gender'] == 'Male']['salary'].mean()
average_salary_female = df[df['gender'] == 'Female']['salary'].mean()

print("Average salary for males:", average_salary_male)
print("Average salary for females:", average_salary_female)

# Visualize the average salary by gender using a bar plot
plt.figure(figsize=(8, 6))
plt.bar(['Male', 'Female'], [average_salary_male, average_salary_female], color=['blue', 'pink'])
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.show()

# Visualize the relationship between 'city' and 'salary' using box plots
fig = px.box(df, x='city', y='salary', title='Box Plot of Salary by City')
fig.show()

import pandas as pd

# Sample data
data = {
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [60000, 50000, 70000, 65000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV in the same directory as this Python script
df.to_csv("employees.csv", index=False)

print("CSV file 'employees.csv' created successfully!")
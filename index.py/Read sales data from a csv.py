# Program to read sales data from CSV file
# and plot a bar chart using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Creating sample sales data
sales_data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Printer", "Camera"],
    "Sales": [50000, 70000, 30000, 20000, 45000]
}

# Creating DataFrame
df = pd.DataFrame(sales_data)

# Saving to CSV file
df.to_csv("sales_data.csv", index=False)

# Reading CSV file
sales_df = pd.read_csv("sales_data.csv")

# Displaying data
print("Sales Data:\n")
print(sales_df)

# Creating bar chart
plt.bar(sales_df["Product"], sales_df["Sales"])

# Adding title and labels
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales Amount")

# Displaying chart
plt.show()

# Expected Output
"""
A bar chart displaying product-wise sales.
"""
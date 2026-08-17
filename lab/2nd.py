import numpy as np

sales_data = np.array([
    [100, 120, 150],
    [200, 180, 220],
    [50, 75, 80]
])

# Calculate average price of all products sold
average_price = np.mean(sales_data)

print("Average price of all products sold:", average_price)
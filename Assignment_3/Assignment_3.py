# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file (make sure the file path is correct)
file_path = 'linear_regression_data.csv'
data = pd.read_csv(file_path, header=None, names=['x', 'y'])

# Extract the independent (x) and dependent (y) variables
x = data['x']
y = data['y']

# Calculate the mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate the covariance and variance
cov_xy = np.sum((x - x_mean) * (y - y_mean))
var_x = np.sum((x - x_mean) ** 2)

# Compute the slope (m) and intercept (b) of the linear model
m = cov_xy / var_x
b = y_mean - m * x_mean

# Define the linear model
def linear_model(x):
    return m * x + b

# Generate predictions
y_pred = linear_model(x)

# Plot the data points and the regression line
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label=f'Linear Fit: y = {m:.2f}x + {b:.2f}')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.legend()
plt.title('Linear Regression using Covariance Approach')
plt.grid(True)
plt.show()

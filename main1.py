import pandas as pd

# Define two Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([5, 10, 15, 20, 25])

print("Series 1:")
print(series1)

print("\nSeries 2:")
print(series2)

# Perform addition
addition = series1 + series2
print("\nAddition of Series 1 and Series 2:")
print(addition)

# Perform subtraction
subtraction = series1 - series2
print("\nSubtraction of Series 1 and Series 2:")
print(subtraction)

# Perform multiplication
multiplication = series1 * series2
print("\nMultiplication of Series 1 and Series 2:")
print(multiplication)

# Perform division
division = series1 / series2
print("\nDivision of Series 1 and Series 2:")
print(division)

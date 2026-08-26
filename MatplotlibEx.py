# WAP for Data Visualization using Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# Bar Plot
plt.figure()
plt.bar(x, y)
plt.title("Bar Plot")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Histogram
plt.figure()
plt.hist(y)
plt.title("Histogram")
plt.show()
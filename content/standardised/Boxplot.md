---
type: term
tags:
  - "#statistics"
  - data_cleaning
  - data_visualization
---
A boxplot, also known as a whisker plot, is a standardized way of displaying the distribution of data based on a five-number summary: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. It can also highlight outliers in the dataset.
## Key Components

Uses:
- Identifying [[standardised/Outliers]].
- Understanding the spread and skewness of the data [[Distributions]].
- Comparing distributions across different categories.
- Need to remove then in order to do [[Data Cleansing]].

Components:
- **Minimum:** The smallest data point excluding outliers.
- **First Quartile (Q1):** The median of the lower half of the dataset.
- **Median (Q2):** The middle value of the dataset.
- **Third Quartile (Q3):** The median of the upper half of the dataset.
- **Maximum:** The largest data point excluding outliers.
- **Outliers:** Data points that fall outside 1.5 times the interquartile range (IQR) above Q3 or below Q1.

## Implementing Boxplot in Python

You can create a boxplot in Python using libraries like Matplotlib and Seaborn. Here's how you can do it:

## Implementation

```python
import matplotlib.pyplot as plt

# Sample data
data = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# Create a boxplot
plt.boxplot(data)

# Add title and labels
plt.title('Boxplot Example')
plt.ylabel('Values')

# Show plot
plt.show()
```
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# Create a boxplot
sns.boxplot(data=data)

# Add title and labels
plt.title('Boxplot Example')
plt.ylabel('Values')

# Show plot
plt.show()
```
[[outliers]]

[[Distributions]]

[[Feature Scaling]]

[[Encoding Categorical Variables]]

[[Correlation]]

# plotting

```python
sns.pairplot(
    penguins,
    x_vars=["bill_length_mm"],
    y_vars=["bill_depth_mm"],hue="species")
```
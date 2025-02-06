Standard deviation is a statistical measure that quantifies the amount of variation or dispersion in a set of data values. It indicates how much individual data points deviate from the mean (average) of the dataset.

## Formula

For a dataset with $n$ observations $X_1, X_2, \ldots, X_n$, the standard deviation $\sigma$ is calculated using the formula:

$$
\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (X_i - \mu)^2}
$$

Where:
- $\sigma$ = standard deviation
- $n$ = number of observations
- $X_i$ = each individual observation
- $\mu$ = mean of the dataset, calculated as:  
$$
\mu = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

## Why Standard Deviation is Preferred Over [[Variance]]

1. **Same Units as Data**  
   Standard deviation is expressed in the same units as the original data, making it more [[interpretability|interpretable]].  
   - **Example:** If you measure height in centimeters, the standard deviation will also be in centimeters.  
   - **Contrast:** Variance is expressed in squared units (e.g., square centimeters), which can be less intuitive to understand.

2. **Direct Interpretation**  
   Standard deviation provides a direct measure of the average distance of data points from the mean.  
   - A **small standard deviation** indicates that the data points are close to the mean.  
   - A **large standard deviation** suggests that the data points are more spread out.

3. **Normal [[Distributions|Distribution]] Context**  
   In the context of a normal distribution, standard deviation helps in understanding the spread of data:  
   - Approximately **68%** of the data falls within **one standard deviation** of the mean.  
   - About **95%** falls within **two standard deviations**.  
   - About **99.7%** falls within **three standard deviations** (known as the empirical rule).  
   This property is particularly useful for identifying [[outliers]].

4. **Ease of Communication**  
   Standard deviation is more intuitive and easier to communicate to a broader audience, including those without a strong statistical background. Its direct relation to the data makes it a preferred choice for explaining variability.

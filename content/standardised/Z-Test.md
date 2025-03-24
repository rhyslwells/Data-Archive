The Z-test is a statistical method used to determine if there is a ==significant difference between the means of two groups or to compare a sample mean to a known population mean when the population [[standard deviation]] is known==. 

It is typically applied when the sample size is large (usually n > 30).

## Types of Z-tests

1. **One-Sample Z-test**: This test compares the mean of a single sample to a known population mean. It assesses whether the sample mean significantly differs from the population mean.

2. **Two-Sample Z-test**: This test compares the means of two independent samples. It is used when both sample sizes are large and the population variances are known or can be assumed to be equal.

## Characteristics of the Z-distribution

The Z-distribution is a normal distribution with a mean of 0 and a standard deviation of 1. It is symmetric and bell-shaped, which allows for the application of the [[Central Limit Theorem]]. As sample sizes increase, the distribution of sample means approaches a normal distribution, making the Z-test applicable.

## Assumptions

For the Z-test to be valid, certain assumptions must be met:
- The data should be normally distributed, especially for smaller sample sizes. However, with large samples, the Central Limit Theorem allows for the Z-test to be used even if the data is not perfectly normal.
- The samples should be independent of each other.
- The population standard deviation should be known.

## Test Statistic

The test statistic for the Z-test is calculated using the formula:

$$ Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} $$

where:
- $\bar{X}$ = sample mean
- $\mu$ = population mean (or mean of the second sample in the two-sample test)
- $\sigma$ = population standard deviation
- $n$ = sample size

This formula allows for the comparison of the sample mean to the population mean, standardizing the difference in terms of standard deviations.
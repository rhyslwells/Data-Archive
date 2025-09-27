---
aliases: []
category: STATISTICS
date modified: 27-09-2025
tags:
- statistics
---
The T-test is a statistical method ==used to determine if there is a significant difference between the means of two groups, especially when the population [[Standard deviation]] is unknown.== It is particularly useful when dealing with small sample sizes.

## Types of T-tests

1. **One-Sample T-test**: This test compares the mean of a single sample to a known value (often the population mean). It helps determine if the sample mean significantly differs from the population mean.

2. **Two-Sample T-test**: This test compares the means of two independent samples. It can be further categorized into:
   - **Two-Sample T-test with Known [[Variance]]**: Used when the variances of the two groups are known and assumed to be equal.
   - **Two-Sample T-test with Unknown Variance**: Used when the variances are unknown and may differ between the two groups. This version is more common in practice.

## Characteristics of the T-distribution

The T-distribution resembles the normal [[Distributions|distribution]] but has fatter tails. This characteristic accounts for the increased variability expected with smaller sample sizes. As the sample size increases, the T-distribution approaches the normal distribution.

## Assumptions

For the T-test to be valid, certain assumptions must be met:
- The data should be approximately normally distributed, especially for small sample sizes.
- The samples should be independent of each other.
- For the two-sample T-test, the variances of the two groups should be equal (for the equal variance version).

## Estimation of Standard Deviation

Since the population standard deviation is unknown, the sample standard deviation is used to estimate it. This estimation is crucial for calculating the test statistic.

## Test Statistic

The test statistic for the T-test is calculated using the formula:

$$ T = \frac{\bar{X} - \mu}{s / \sqrt{n}} $$

where:
- $\bar{X}$ = sample mean
- $\mu$ = population mean (or mean of the second sample in the two-sample test)
- $s$ = sample standard deviation
- $n$ = sample size

This formulation condenses all the data into a single variable, allowing for [[Hypothesis testing]].
## Importance of the T-test

The T-test is a Uniformly Most Powerful Unbiased (UMPU) test, meaning it is optimal for detecting differences in means under the specified conditions.

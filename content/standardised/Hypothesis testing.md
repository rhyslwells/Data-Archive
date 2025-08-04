---
aliases: []
category: 
date modified: 27-07-2025
tags: [statistics]
---
Used to draw inferences about population parameters based on sample data. The process involves the formulation of two competing hypotheses: the null hypothesis ($H_0$) and the alternative hypothesis ($H_1$). 

### Key Concepts
- Null Hypothesis ($H_0$): The hypothesis that there is no effect or no difference, which we seek to test.
- Alternative Hypothesis ($H_1$): The hypothesis that indicates the presence of an effect or a difference.
- P-value: A measure that helps determine the strength of the evidence against $H_0$. A small p-value (typically $< 0.05$) suggests that we reject $H_0$, indicating that the observed effect is statistically significant.
### Decision Making
- Accepting $H_0$: This means there is insufficient evidence to support the alternative hypothesis, suggesting that any observed effect could be due to random chance.
- Rejecting $H_0$: This indicates that there is enough statistical evidence to conclude that the status quo does not represent the truth.
### Limitations
Hypothesis testing is subject to Type I errors (false positives) and Type II errors (false negatives). A small p-value does not guarantee practical significance or causation, and results can be influenced by sample variability.

### Example
An example of hypothesis testing is conducting a [[t-test]] to compare the means of two groups. The null hypothesis states that the means are equal ($H_0: \mu_1 = \mu_2$), while the alternative hypothesis states they are not equal ($H_1: \mu_1 \neq \mu_2$).

### Important Notes
- Hypothesis testing relies on the formulation of $H_0$ and $H_1$, and the decision to accept or reject $H_0$ is based on the [[p values]].
- A small p-value indicates statistical significance but does not imply practical relevance or causation.

### Follow-up Questions and Answers

##### In hypothesis testing, why might a very small p-value still lead to incorrect conclusions?  

A very small p-value might lead to incorrect conclusions due to several factors, including:
   - Sample Size: With large sample sizes, even trivial effects can yield small p-values, leading to the rejection of $H_0$ for effects that are not practically significant.
   - Multiple Comparisons: Conducting multiple tests increases the risk of Type I errors, where we incorrectly reject $H_0$.
   - Misinterpretation: A small p-value does not imply that the effect is large or important; it merely ==indicates that the observed data is unlikely under $H_0$.==

##### How does the inclusion of effect size metrics improve the interpretation of hypothesis testing results?  

Including ==effect size metrics== provides a quantitative measure of the magnitude of the observed effect, allowing researchers to assess the practical significance of their findings. While p-values indicate whether an effect exists, ==effect sizes help determine how meaningful that effect is== in real-world terms.

##### What are the implications of multiple testing on the validity of p-values in hypothesis testing?  

Multiple testing increases the likelihood of encountering false positives (Type I errors). When multiple hypotheses are tested simultaneously, the probability of incorrectly rejecting at least one true null hypothesis rises. This necessitates adjustments to p-values (e.g., Bonferroni correction) to maintain the overall error rate.

### Related Topics
- Bayesian statistics and its approach to hypothesis testing
- The role of confidence intervals in statistical [[inference]]
- [[Statistics]]
- [[Testing]]

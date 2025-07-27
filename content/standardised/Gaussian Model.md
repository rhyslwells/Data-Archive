---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
### Gaussian Model 

(Univariate)

- **Formula:**  
    $p(x; \mu, \sigma^2) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right)$
- **Steps:**
    - Estimate $\mu$ and $\sigma^2$ from the data.
    - Compute the probability density for each data point.
    - Points with low probabilities (below a threshold $\epsilon$) are considered anomalies.

![[Pasted image 20241230202826.png|500]]

### **5. Multivariate Gaussian Distribution**

- **Steps:**
    - Extend the Gaussian model to include covariance across features.
    - Fit the multivariate Gaussian model:  
        $p(x; \mu, \Sigma) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x - \mu)^T \Sigma^{-1} (x - \mu)\right)$
        - $\mu$: Mean vector
        - $\Sigma$: Covariance matrix
    - Threshold low-probability examples to identify anomalies.
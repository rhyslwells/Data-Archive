---
aliases:
- null
category: ML
date modified: 27-09-2025
tags:
- evaluation
- modeling
- statistics
---
See https://youtu.be/StSAJIZuqws?t=655

```R
)

# [[Monte Carlo Simulation]]: Multicollinearity & Harm
results = expand_grid(
rho = seq(0, 0.95, 0.05),
rep = 1:1000
) %>%
mutate(
sim = map(rho, function(p) {

set.seed(runif(1, 1, 10000) %>% ceiling)
R = matrix(c(1, p, p, 1), nrow = 2, ncol = 2, byrow = TRUE)
Sigma = cor2cov(R, c(1, 1))

data = MASS :: mvrnorm(n= 30, mu = c(0, 0), Sigma = Sigma) %>%
as_tibble %>%
mutate( Y=1+0.5*V1+0.5*V2+ rnorm(30) )

model = 1m(Y ~ V1 + V2, data = data)

summary(model) $coefficients %>% as_tibble
})
```


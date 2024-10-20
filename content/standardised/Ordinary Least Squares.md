**Derivation of Coefficients**:
    - OLS derives the coefficients by setting the partial derivatives of the SSE with respect to each coefficient to zero. This results in a set of normal equations that can be solved to find the optimal coefficients.
    - In matrix form, the solution can be expressed as:  
$$b=(X^{T}X)^{-1} X^{T}y$$
    - Here, $X$ is the matrix of input features (including a column of ones for the intercept),  is the vector of observed values, and  is the vector of coefficients.
**Derivation of Coefficients**:
    - OLS derives the coefficients by setting the partial derivatives of the SSE with respect to each coefficient to zero. This results in a set of normal equations that can be solved to find the optimal coefficients.
    - In matrix form, the solution can be expressed as:  
$$b=(X^{T}X)^{-1} X^{T}y$$
    - Here, $X$ is the matrix of input features (including a column of ones for the intercept),  is the vector of observed values, and  is the vector of coefficients.



### [[Ordinary Least Squares]]

The Ordinary Least Squares method is used to minimize SSE. It achieves this by finding the values of  that minimize the sum of squared differences between the observed and predicted values. The formulas for  are derived by setting partial derivatives of SSE with respect to each coefficient to zero.

OLS is an analytical method



[[Ordinary Least Squares]]

![[Pasted image 20240117145455 1.png|500]] ![[Pasted image 20240124135607.png|500]]
# Simple Linear Regression

This repo. consists of a very basic implementation of linear regression from scratch using the least squares estimation. The purpose is to show the process of building a model and the type of visuals which can add value and understanding.
The code consists of the following steps
  1. Load data (read directly from a .csv file)
  2. Build regression model built by writing a function to calculate the least squares expressions for the coefficients
     $$\beta_1= \dfrac{\sum{(x- \overline{x})(y- \overline{y})}}{\sum{(x- \overline{x})^2}}$$
     
     $$\beta_0 = \overline{y} - \beta_1 \overline{x} $$
  4. Evaluate model - here we have chosen the basic correlation coefficient (and consequently the coefficient of determination, which measures the amount of variance for which the model can account for)
   $$R^2 = \dfrac{N \sum{xy} - \sum{x}(\sum{y})}
{N \sum{x^2}-(\sum{x})^2}$$

  6. Plot data and line of best fit
  
  <p align="center">
  <img src = "https://github.com/RobSLong/Data-Science/blob/main/Regression/linear_regression/figures/regression_line.png" width="350" />
  </p>
 
  6. Plot residuals and a histogram of residuals to check there is no pattern in the residual spread
  7. 
  <p align="center">
  <img src = "https://github.com/RobSLong/Data-Science/blob/main/Regression/linear_regression/figures/residuals.png" width="350" />
  </p>


 num = (N * (x * y).sum()) - (x.sum() * y.sum()) # define numerator
    den = np.sqrt((N * (x**2.).sum() - x.sum()**2.) * (N * (y**2.).sum() - y.sum()**2.)) # define denominator

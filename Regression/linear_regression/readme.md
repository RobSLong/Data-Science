# Simple Linear Regression

This repo. consists of a very basic implementation of linear regression from scratch using the least squares estimation. The purpose is to show the process of building a model and the type of visuals which can add value and understanding.
The code consists of the following steps
  1. Load data (read directly from a .csv file)
  2. Build regression model built by writing a function to calculate the least squares expressions for the coefficients
     $$\beta_1=$$
  4. Evaluate model
  5. Plot data and line of best fit
  6. Plot residuals and a histogram of residuals to check there is no pattern in the residual spread

beta1 = (((x - xmean)*(y - ymean)).sum()) / (((x - xmean)**2.).sum())
    beta0 = ymean - (beta1 * xmean)

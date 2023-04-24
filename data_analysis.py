import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_loading import load_data, preprocess_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from stargazer.stargazer import Stargazer

# Load preprocessed data
# data = preprocess_data()

# # Descriptive statistics
# print(data.describe())

# # Correlation analysis
# correlation_matrix = data.corr()
# plt.figure(figsize=(12, 9))
# sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')

# # EDA: Create visualizations
# # Example: Bar chart for the relationship between gender and investment satisfaction
# sns.barplot(x="What is your gender?", y="How satisfied are you with your investment performance?", data=data)

# Hypothesis testing, feature selection, and modeling
# ...
def fit_linear_regression(data, target, features):
    # Select the target variable and features
    X = data[features]
    y = data[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict the target variable for the test set
    y_pred = model.predict(X_test)

    # Evaluate the model performance
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    return model


import statsmodels.api as sm


def run_linear_regression(data, target_column='How satisfied are you with your investment performance?'):
    # Select only numerical columns
    numerical_data = data.select_dtypes(include=['float64', 'int64', 'bool'])

    # Remove target column from features
    X = numerical_data.drop(target_column, axis=1)
    
    # Add a constant term to the features
    X = sm.add_constant(X)
    
    # Define target variable (y)
    y = numerical_data[target_column]

    # Fit the linear regression model
    model = sm.OLS(y, X).fit()

    # Print the summary of the regression model
    # print(model.summary())

    return model



def run_multiple_linear_regressions(data, dependent_var, independent_vars_list):
    fitted_models = []
    for independent_vars in independent_vars_list:
        X = data[independent_vars]
        X = sm.add_constant(X)
        y = data[dependent_var]
        model = sm.OLS(y, X).fit()
        fitted_models.append(model)
    return fitted_models

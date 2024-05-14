# analysis_engine.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class AnalysisEngine:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        # Generate summary statistics
        summary = self.df.describe(include='all')
        return summary

    def correlation_matrix(self):
        # Generate a correlation matrix
        correlation = self.df.corr()
        return correlation

    def linear_regression_analysis(self, target_column, feature_columns):
        # Prepare the data for linear regression
        X = self.df[feature_columns]
        y = self.df[target_column]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        # Evaluate the model
        train_mse = mean_squared_error(y_train, y_pred_train)
        test_mse = mean_squared_error(y_test, y_pred_test)

        results = {
            'model': model,
            'train_mse': train_mse,
            'test_mse': test_mse,
            'coefficients': model.coef_,
            'intercept': model.intercept_
        }

        return results

    def perform_analysis(self):
        pass

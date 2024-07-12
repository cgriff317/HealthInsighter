# analysis_engine.py

import pandas as pd


class AnalysisEngine:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        # Generate summary statistics
        summary = self.df.describe(include='all')
        return summary

    def correlation_matrix(self):
        # Select only numeric columns for correlation matrix
        numeric_df = self.df.select_dtypes(include=['number'])
        correlation = numeric_df.corr()
        return correlation


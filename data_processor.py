# data_processor.py

import pandas as pd


def preprocess_data(df):
    # Convert categorical data to ordered categorical types
    category_columns = {
        'Asset Wealth': ['Lowest', '2nd', '3rd', 'Highest'],
        'Self-rated Health': ['Poor', 'Good', 'Very Good', 'Excellent']
    }
    for col, categories in category_columns.items():
        df[col] = pd.Categorical(df[col], categories=categories, ordered=True)

    # Encoding all other categorical columns as category datatypes
    categorical_cols = df.select_dtypes(include=['object']).columns.difference(category_columns.keys())
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    # Ensure there are no NaN values in important columns
    important_cols = ['Asset Wealth', 'Self-rated Health', 'Disability Level', 'Health Insurance Status', 'Household Type', 'Employment Status']
    for col in important_cols:
        if df[col].isnull().any():
            if df[col].dtype.name == 'category':
                df[col] = df[col].cat.add_categories(['Unknown'])
            df[col].fillna('Unknown', inplace=True)  # Fill with a placeholder or a suitable default value

    return df


class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        # Load the data from a local CSV file
        data = pd.read_csv(self.file_path)
        return data

    def preprocess_data(self, df):
        pass

import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            # Load the data from a local CSV file
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def preprocess_data(self, df):
        if df is None:
            print("Data is None, cannot preprocess.")
            return None

        try:
            # Map ordinal categories to numeric values
            category_mappings = {
                'Asset Wealth': {'Lowest': 1, '2nd': 2, '3rd': 3, 'Highest': 4},
                'Self-rated Health': {'Poor': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4},
                'Disability Level': {'Not disabled': 0, 'IADL limitation only': 1, 'ADL limitation only': 2, 'Both IADL and ADL': 3},
                'Health Insurance Status': {'Not covered': 0, 'Medical card only': 1, 'Health insurance only': 2, 'Dual coverage': 3, 'All medical cards': 4, 'All health insurance': 5},
                'Education': {'Primary': 1, 'Secondary': 2, 'Tertiary or higher': 3},
                'Household Type': {'Living alone': 1, 'Living with others': 2, 'Living with spouse': 3},
                'Employment Status': {'Other': 0, 'Retired': 1, 'Working': 2}
            }

            for col, mapping in category_mappings.items():
                df[col] = df[col].map(mapping)
                print(f"Processed column: {col} with mapping: {mapping}")

            # Encoding all other categorical columns as category datatypes
            categorical_cols = df.select_dtypes(include=['object']).columns.difference(category_mappings.keys())
            for col in categorical_cols:
                df[col] = df[col].astype('category').cat.codes
                print(f"Encoded column: {col}")

            # Ensure there are no NaN values in important columns
            important_cols = list(category_mappings.keys()) + list(categorical_cols)
            for col in important_cols:
                if df[col].isnull().any():
                    df[col].fillna(df[col].mode()[0], inplace=True)  # Fill with the mode (most common value)
                    print(f"Filled NaN values in column: {col}")

            return df
        except Exception as e:
            print(f"Error during preprocessing: {e}")
            return None

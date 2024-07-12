import pandas as pd


class DataProcessor:

    # Initialize the DataProcessor with the given file path. :param file_path: Path to the CSV file containing health
    # data.
    def __init__(self, file_path):
        self.file_path = file_path

    # Load data from the CSV file specified by the file path. :return: DataFrame containing the loaded data,
    # or None if loading fails.
    def load_data(self):
        try:
            # Load the data from a local CSV file
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    # Preprocess the data by mapping ordinal categories to numeric values, encoding other categorical columns,
    # and handling missing values. :param df: DataFrame to preprocess. :return: Preprocessed DataFrame, or None if
    # preprocessing fails.

    def preprocess_data(self, df):
        if df is None:
            print("Data is None, cannot preprocess.")
            return None

        try:
            # Map ordinal categories to numeric values
            category_mappings = {
                'Asset Wealth': {'Lowest': 1, '2nd': 2, '3rd': 3, 'Highest': 4},
                'Self-rated Health': {'Poor': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4},
                'Disability Level': {'Not Disabled': 0, 'IADL Limitation Only': 1, 'ADL Limitation Only': 2,
                                     'Both IADL and ADL': 3},
                'Health Insurance Status': {'Not Covered': 0, 'Medical Cards': 1, 'Health Insurance': 2,
                                            'Dual Coverage': 3},
                'Education': {'Primary': 1, 'Secondary': 2, 'Tertiary or higher': 3},
                'Household Type': {'Living Alone': 1, 'Living with Others': 2, 'Living with Spouse': 3},
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

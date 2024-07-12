# test_data_preprocessing.py
from data_processor import DataProcessor


def test_data_preprocessing():
    data_processor = DataProcessor(file_path='Health Status Study.csv')
    df = data_processor.load_data()
    preprocessed_df = data_processor.preprocess_data(df)
    assert 'Health Insurance Status' in preprocessed_df.columns, "Preprocessing did not work as expected"
    assert not preprocessed_df.isnull().sum().sum(), "There are still missing values after preprocessing"
    print("Data preprocessing test passed.")


test_data_preprocessing()

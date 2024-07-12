# test_data_loading.py
import pandas as pd
from data_processor import DataProcessor


def test_data_loading():
    data_processor = DataProcessor(file_path='Health Status Study.csv')
    df = data_processor.load_data()
    assert isinstance(df, pd.DataFrame), "Data did not load correctly"
    assert not df.empty, "DataFrame is empty"
    print("Data loading test passed.")


test_data_loading()

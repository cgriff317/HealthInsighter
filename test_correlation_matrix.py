# test_correlation_matrix.py
import pandas as pd
from data_processor import DataProcessor
from analysis_engine import AnalysisEngine


def test_correlation_matrix():
    data_processor = DataProcessor(file_path='Health Status Study.csv')
    df = data_processor.load_data()
    df = data_processor.preprocess_data(df)
    analysis_engine = AnalysisEngine(df)
    correlation_matrix = analysis_engine.correlation_matrix()

    print(correlation_matrix)

    assert isinstance(correlation_matrix, pd.DataFrame), "Correlation matrix not calculated correctly"
    assert not correlation_matrix.empty, "Correlation matrix DataFrame is empty"
    assert all(correlation_matrix.columns == correlation_matrix.index), "Correlation matrix is not square"

    print("Correlation matrix test passed.")


test_correlation_matrix()

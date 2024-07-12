# test_summary_statistics.py
import pandas as pd
from data_processor import DataProcessor
from analysis_engine import AnalysisEngine


def test_summary_statistics():
    data_processor = DataProcessor(file_path='Health Status Study.csv')
    df = data_processor.load_data()
    df = data_processor.preprocess_data(df)
    analysis_engine = AnalysisEngine(df)
    summary_stats = analysis_engine.summary_statistics()  # Correct method name

    print(type(summary_stats))
    print(summary_stats)

    assert isinstance(summary_stats, pd.DataFrame), "Summary statistics not calculated correctly"
    assert not summary_stats.empty, "Summary statistics DataFrame is empty"

    print("Data summary statistics test passed.")


test_summary_statistics()

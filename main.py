from data_processor import DataProcessor
from analysis_engine import AnalysisEngine
from dashboard import Dashboard


def main():
    # Initialize DataProcessor with the correct file path
    data_processor = DataProcessor(file_path='Health Status Study.csv')

    # Load and preprocess data
    df = data_processor.load_data()

    if df is None:
        print("Failed to load data. Exiting...")
        return

    df = data_processor.preprocess_data(df)

    if df is None:
        print("Failed to preprocess data. Exiting...")
        return

    # Verify the data
    print("Data Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())

    # Initialize AnalysisEngine and perform analysis
    analysis_engine = AnalysisEngine(df)

    # Summary statistics
    summary = analysis_engine.summary_statistics()
    print("\nSummary Statistics:\n", summary)

    # Correlation matrix
    correlation = analysis_engine.correlation_matrix()
    print("\nCorrelation Matrix:\n", correlation)

    # Initialize and run the dashboard
    dashboard = Dashboard(df)
    dashboard.setup_layout()
    dashboard.register_callbacks()
    return dashboard.app


if __name__ == "__main__":
    app = main()
    app.run_server(debug=True)

# Expose the server variable for Gunicorn
server = main().server

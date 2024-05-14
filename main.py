# main.py

from data_processor import DataProcessor
from analysis_engine import AnalysisEngine
from dashboard import Dashboard


def main():
    # Initialize DataProcessor
    data_processor = DataProcessor(file_path='Health_Status_Study.csv')

    # Load and preprocess data
    df = data_processor.load_data()
    df = data_processor.preprocess_data(df)

    # Verify the data
    print(df.dtypes)
    print(df.isnull().sum())

    # Initialize AnalysisEngine and perform analysis
    analysis_engine = AnalysisEngine(df)

    # Summary statistics
    summary = analysis_engine.summary_statistics()
    print("\nSummary Statistics:\n", summary)

    # Correlation matrix
    correlation = analysis_engine.correlation_matrix()
    print("\nCorrelation Matrix:\n", correlation)

    # Linear regression analysis
    target_column = 'Self-rated Health'  # Example target column
    feature_columns = ['Age', 'Asset Wealth', 'Disability Level']  # Example feature columns
    regression_results = analysis_engine.linear_regression_analysis(target_column, feature_columns)

    print("\nLinear Regression Results:")
    print("Train MSE:", regression_results['train_mse'])
    print("Test MSE:", regression_results['test_mse'])
    print("Coefficients:", regression_results['coefficients'])
    print("Intercept:", regression_results['intercept'])

    # Initialize and setup Dashboard
    dashboard = Dashboard(df)
    dashboard.setup_layout()
    dashboard.app.run_server(debug=True)


if __name__ == '__main__':
    main()
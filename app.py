# app.py

from data_processor import DataProcessor, preprocess_data
from analysis_engine import AnalysisEngine
from dashboard import Dashboard

# Initialize DataProcessor with the correct file path
data_processor = DataProcessor(file_path='Health_Status_Study.csv')

# Load and preprocess data
df = data_processor.load_data()
df = preprocess_data(df)

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

# Expose the server variable to be used by Gunicorn
server = dashboard.app.server
app = dashboard.app

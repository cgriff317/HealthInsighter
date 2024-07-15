# Health Insighter Project

## Background
The Health Insighter project aims to provide comprehensive insights into health data using advanced data processing, statistical analysis, and machine learning techniques. The primary objective is to analyze and visualize health-related data to understand health insurance coverage, overall self-rated health status, and their correlations with factors such as wealth, employment status, and living arrangements. This project leverages the power of data integration and analytics to transform healthcare services and inform policy-making.

## Approach to Implementation

### Data Acquisition and Preprocessing
- **Data Sources:** Public health datasets covering demographics, insurance coverage, and health outcomes.
- **Data Ingestion:** Data is loaded from CSV files using custom-built functions in the `DataProcessor` class.
- **Data Cleaning:** Handling missing values, encoding categorical variables, and normalizing data to ensure consistency and reliability.
- **Data Preprocessing:** Further processing of data to make it analysis-ready, including mapping ordinal categories to numeric values.

### Data Analysis and Modeling
- **Exploratory Data Analysis (EDA):** Conducted to understand the data distribution, identify patterns, and generate initial insights using statistical summaries and visualizations.
- **Predictive Modeling:** Developed multiple machine learning models (e.g., logistic regression, random forests) to assess health risks based on the available data.
- **Model Evaluation:** Evaluated models using accuracy, precision, recall, and AUC-ROC metrics to ensure robustness and reliability.

### Dashboard Development
- **Tools Used:** Python for data processing, analysis, and visualization; Dash and Plotly for creating interactive dashboards.
- **Dashboard Layout:** Defined in the `dashboard.py` class, which sets up the layout and visualization components.
- **Visualization:** Various charts and graphs to present data insights interactively.
- **Deployment:** Hosted on Heroku for easy accessibility and scalability.

### Error-Handling Mechanisms
- Implemented robust error-handling mechanisms to ensure the application’s reliability.

## User Guide to Run the Application

### Prerequisites
- **Python 3.8+**
- **Libraries:** Install the required libraries using the command: `pip install -r requirements.txt`

### Running the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/health-insighter.git
   cd health-insighter
2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the Application**
   ```bash
   python main.py
5. **Access the Dashboard**
Open your web browser and navigate to http://127.0.0.1:8050/ to view the interactive dashboard.

### Project Structure
- **data_processor.py:** Manages data ingestion, cleaning, and preprocessing.
- **analysis_engine.py:** Handles statistical analysis and predictive modeling.
- **dashboard.py:** Manages the creation and display of interactive visualizations using Plotly Dash.
- **main.py:** Entry point of the application, orchestrating data flow through the modules.

### Additional Information
- **Integration with GitHub:** The project integrates well with GitHub for version control and collaboration.
- **Deployment on Heroku:** Heroku is used for deployment, ensuring easy access and scalability. Environment variables and add-ons are configured in the Heroku Dashboard.

### Future Work
- **Enhance Visualization Layout:** Further refine the layout and design of the visualizations.
- **Explore Additional Data Sources:** Integrate more data sources to enrich analysis.
- **Incorporate Performance Metrics:** Add performance metrics to evaluate the efficiency of data processing and analysis components.

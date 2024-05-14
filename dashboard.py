# dashboard.py

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


class Dashboard:
    def __init__(self, dataframe):
        dataframe['Asset Wealth'] = pd.Categorical(
            dataframe['Asset Wealth'],
            categories=['Lowest', '2nd', '3rd', 'Highest'],
            ordered=True
        )
        dataframe['Asset Wealth'] = dataframe['Asset Wealth'].cat.codes
        dataframe['Asset Wealth'] = pd.to_numeric(dataframe['Asset Wealth'], errors='coerce')
        dataframe['Asset Wealth'].fillna(dataframe['Asset Wealth'].mean(), inplace=True)
        assert not dataframe['Asset Wealth'].isnull().any(), "There are still NaN values in 'Asset Wealth'"
        self.data = dataframe
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = dbc.Container([
            dbc.Row(html.H1("Health Insighter Dashboards")),
            dbc.Tabs([
                dbc.Tab(self.insurance_distribution_dashboard(), label="Insurance Coverage Distribution"),
                dbc.Tab(self.mortality_rate_dashboard(), label="Mortality Rate Comparison"),
                dbc.Tab(self.risk_factors_dashboard(), label="Risk Factors Analysis"),
                dbc.Tab(self.predictive_analytics_dashboard(), label="Predictive Analytics"),
            ])
        ])

    def insurance_distribution_dashboard(self):
        fig = px.pie(self.data, names='Health Insurance Status', title='Distribution of Health Insurance Coverage')
        return dcc.Graph(figure=fig)

    def mortality_rate_dashboard(self):
        fig = px.line(self.data, x='Age', y='Self-rated Health', color='Health Insurance Status',
                      title='Health Outcomes by Insurance Status')
        return dcc.Graph(figure=fig)

    def risk_factors_dashboard(self):
        fig = px.scatter(self.data, x='Disability Level', y='Self-rated Health', size='Asset Wealth',
                         color='Health Insurance Status',
                         title='Impact of Disability and Wealth on Health')
        return dcc.Graph(figure=fig)

    def predictive_analytics_dashboard(self):
        if 'Predicted Health Outcomes' not in self.data.columns:
            self.data['Predicted Health Outcomes'] = self.data['Self-rated Health']
        fig = px.line(self.data, x='Age', y='Predicted Health Outcomes', title='Future Predictions of Health Outcomes')
        return dcc.Graph(figure=fig)

    # def comparative_analytics_dashboard(self):
    # fig = px.bar(self.data, x='Region', y='Self-rated Health', color='Region', barmode='group',
    # title='Health Outcomes: Local vs National')
    # return dcc.Graph(figure=fig)

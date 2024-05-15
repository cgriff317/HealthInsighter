from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px


def mortality_rate_dashboard():
    return dbc.Container([
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='self-rated-health-dropdown',
                options=[
                    {'label': 'Poor', 'value': 1},
                    {'label': 'Good', 'value': 2},
                    {'label': 'Very Good', 'value': 3},
                    {'label': 'Excellent', 'value': 4},
                ],
                placeholder="Select Self-rated Health",
            ), width=6),
            dbc.Col(dcc.Checklist(
                id='health-insurance-status-checklist',
                options=[
                    {'label': 'Not Covered', 'value': 0},
                    {'label': 'Medical Card Only', 'value': 1},
                    {'label': 'Health Insurance Only', 'value': 2},
                    {'label': 'Dual Coverage', 'value': 3},
                    {'label': 'All Medical Cards', 'value': 4},
                    {'label': 'All Health Insurance', 'value': 5},
                ],
                value=[0, 1, 2, 3, 4, 5]  # default to show all
            ), width=6)
        ]),
        dbc.Row(dcc.Graph(id='mortality-rate-graph'))
    ])


class Dashboard:
    def __init__(self, dataframe):
        self.data = dataframe
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.setup_layout()
        self.register_callbacks()

    def setup_layout(self):
        legend_health_insurance_status = """
        **Health Insurance Status:**
        - 0: Not Covered
        - 1: Medical Card Only
        - 2: Health Insurance Only
        - 3: Dual Coverage
        - 4: All Medical Cards
        - 5: All Health Insurance
        """

        legend_disability_level = """
        **Disability Level:**
        - 0: Not Disabled
        - 1: IADL Limitation Only
        - 2: ADL Limitation Only
        - 3: Both IADL and ADL
        """

        legend_education = """
        **Education:**
        - 1: Primary
        - 2: Secondary
        - 3: Tertiary or Higher
        """

        legend_household_type = """
        **Household Type:**
        - 1: Living Alone
        - 2: Living with Others
        - 3: Living with Spouse
        """

        legend_employment_status = """
        **Employment Status:**
        - 0: Other
        - 1: Retired
        - 2: Working
        """

        legend_self_rated_health = """
        **Self-rated Health:**
        - 1: Poor
        - 2: Good
        - 3: Very Good
        - 4: Excellent
        """

        self.app.layout = dbc.Container([
            dbc.Row(html.H1("Health Insighter Dashboards")),
            dbc.Row([
                dbc.Col(dcc.Markdown(legend_health_insurance_status), width=4),
                dbc.Col(dcc.Markdown(legend_disability_level), width=4),
                dbc.Col(dcc.Markdown(legend_education), width=4)
            ]),
            dbc.Row([
                dbc.Col(dcc.Markdown(legend_household_type), width=4),
                dbc.Col(dcc.Markdown(legend_employment_status), width=4),
                dbc.Col(dcc.Markdown(legend_self_rated_health), width=4)
            ]),
            dbc.Tabs([
                dbc.Tab(self.insurance_distribution_dashboard(), label="Insurance Coverage Distribution"),
                dbc.Tab(mortality_rate_dashboard(), label="Mortality Rate Comparison"),
                dbc.Tab(self.risk_factors_dashboard(), label="Risk Factors Analysis"),
                dbc.Tab(self.predictive_analytics_dashboard(), label="Predictive Analytics"),
                ])
        ])

    def insurance_distribution_dashboard(self):
        fig = px.pie(self.data, names='Health Insurance Status', title='Distribution of Health Insurance Coverage')
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

    def register_callbacks(self):
        @self.app.callback(
            Output('mortality-rate-graph', 'figure'),
            Input('self-rated-health-dropdown', 'value'),
            Input('health-insurance-status-checklist', 'value')
        )
        def update_mortality_rate_graph(selected_health, selected_insurance):
            filtered_data = self.data
            if selected_health:
                filtered_data = filtered_data[filtered_data['Self-rated Health'] == selected_health]
            if selected_insurance:
                filtered_data = filtered_data[filtered_data['Health Insurance Status'].isin(selected_insurance)]
            if filtered_data.empty:
                return {
                    'data': [],
                    'layout': {
                        'title': 'No data available for the selected filters.'
                    }
                }
            fig = px.line(filtered_data, x='Age', y='Self-rated Health', color='Health Insurance Status',
                          title='Health Outcomes by Insurance Status',
                          facet_col='Health Insurance Status', facet_col_wrap=3)  # Use facets for better comparison
            fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  # Clean up facet labels
            return fig

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


class Dashboard:
    def __init__(self, dataframe):
        self.data = dataframe
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.setup_layout()
        self.register_callbacks()

    def setup_layout(self):
        self.app.layout = dbc.Container([
            dbc.Row(html.H1("Health Insighter Dashboards")),
            dbc.Row([
                dbc.Col(self.insurance_distribution_dashboard(), width=6),
                dbc.Col(self.risk_factors_dashboard(), width=6)
            ]),
            dbc.Row([
                dbc.Col(self.predictive_analytics_dashboard(), width=10),
            ]),
            dbc.Row([
                dbc.Col(self.health_status_by_living_arrangement_dashboard(), width=10),
            ]),
            dbc.Row([
                dbc.Col(self.employment_status_health_coverage_dashboard(), width=10)
            ]),
            dbc.Row([
                dbc.Col(self.correlation_matrix_dashboard(), width=6),
            ]),
            dbc.Row([
                dbc.Col(self.self_rated_health_by_age_sex_education_dashboard(), width=12)
            ]),
            dbc.Row([
                dbc.Col(self.insurance_status_by_wealth_dashboard(), width=10),
            ])
        ], fluid=True)

    def insurance_distribution_dashboard(self):
        fig = px.pie(self.data, names='Health Insurance Status', title='Distribution of Health Insurance Coverage',
                     color='Health Insurance Status',
                     labels={'Health Insurance Status': 'Health Insurance Status'})

        percentages = (self.data['Health Insurance Status'].value_counts(normalize=True) * 100).round(2).astype(
            str) + '%'
        fig.update_traces(
            text=[f"{name}<br>{percent}" for name, percent in zip(self.data['Health Insurance Status'], percentages)],
            textinfo='percent+label')

        fig.update_layout(showlegend=True, legend_title_text='Health Insurance Status',
                          legend=dict(
                              orientation="h",
                              yanchor="bottom",
                              y=-1.02,
                              xanchor="right",
                              x=1,

                          ))

        return html.Div([
            dcc.Graph(figure=fig),
            dcc.Markdown("""
                **Health Insurance Status Key:**
                - 0: Not Covered
                - 1: Medical Cards
                - 2: Health Insurance
                - 3: Dual Coverage
            """)
        ])

    def risk_factors_dashboard(self):
        # Update the scatter plot with more descriptive labels and a wealth description key
        fig = px.scatter(self.data, x='Disability Level', y='Self-rated Health', size='Asset Wealth',
                         color='Health Insurance Status', title='Impact of Disability and Wealth on Health',
                         labels={
                             'Disability Level': 'Disability Level',
                             'Self-rated Health': 'Self-rated Health',
                             'Asset Wealth': 'Wealth Level',
                             'Health Insurance Status': 'Health Insurance Status'
                         })

        fig.update_layout(
            coloraxis_colorbar=dict(
                title='Health Insurance Status',
                tickvals=[0, 1, 2, 3],
                ticktext=['Not Covered', 'Medical Cards', 'Health Insurance', 'Dual Coverage']
            )
        )

        return html.Div([
            dcc.Graph(figure=fig),
            html.Div([
                dcc.Markdown("""
                    **Disability Level Key:**
                    - 0: Not Disabled
                    - 1: IADL Limitation Only
                    - 2: ADL Limitation Only
                    - 3: Both IADL and ADL
                """),
                dcc.Markdown("""
                    **Self-rated Health Key:**
                    - 1: Poor
                    - 2: Good
                    - 3: Very Good
                    - 4: Excellent
                """),
                dcc.Markdown("""
                    **Wealth Level Key:**
                    - 1: Lowest
                    - 2: 2nd
                    - 3: 3rd
                    - 4: Highest
                """)
            ], style={'display': 'flex', 'justify-content': 'left', 'gap': '200px', 'width': '100%',
                      'font-size': '14px'})
        ])

    def predictive_analytics_dashboard(self):
        # Assuming 'Predicted Health Outcomes' is already in the dataframe
        if 'Predicted Health Outcomes' not in self.data.columns:
            self.data['Predicted Health Outcomes'] = self.data['Self-rated Health']

        # Aggregate data to show average predicted health outcomes at different ages
        age_groups = pd.cut(self.data['Age'], bins=[20, 30, 40, 50, 60, 70, 80, 90, 100],
                            labels=['20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'])
        aggregated_data = self.data.groupby(age_groups)['Predicted Health Outcomes'].mean().reset_index()

        fig = px.line(aggregated_data, x='Age', y='Predicted Health Outcomes',
                      title='Future Predictions of Health Outcomes',
                      labels={
                          'Age': 'Age Group',
                          'Predicted Health Outcomes': 'Average Predicted Health Outcomes'
                      })

        # Update the layout for clarity
        fig.update_layout(
            xaxis_title='Age Group',
            yaxis_title='Average Predicted Health Outcomes',
            title={
                'text': "Future Predictions of Health Outcomes",
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        # Add a key to explain the predicted health outcomes
        return html.Div([
            dcc.Graph(figure=fig),
            dcc.Markdown("""
                **Predicted Health Outcomes Key:**
                - 1: Poor
                - 2: Good
                - 3: Very Good
                - 4: Excellent
            """)
        ])

    def health_status_by_living_arrangement_dashboard(self):
        # Group by Household Type and Self-rated Health to get accurate counts
        grouped_data = self.data.groupby(['Household Type', 'Self-rated Health']).size().reset_index(name='counts')

        fig = px.bar(grouped_data, x='Household Type', y='counts', color='Self-rated Health', barmode='stack',
                     title='Comparison of Health Status Across Different Living Arrangements',
                     labels={'Household Type': 'Household Type', 'counts': 'Count',
                             'Self-rated Health': 'Self-rated Health'},
                     text='counts')

        fig.update_layout(
            xaxis_title='Household Type',
            yaxis_title='Count of Self-rated Health',
            coloraxis_colorbar=dict(
                title='Self-rated Health',
                tickvals=[1, 2, 3, 4],
                ticktext=['Poor', 'Good', 'Very Good', 'Excellent']
            )
        )

        return html.Div([
            dcc.Graph(figure=fig),
            html.Div([
                dcc.Markdown("""
                    **Household Type Key:**
                    - 1: Living Alone
                    - 2: Living with Others
                    - 3: Living with Spouse

                """)
            ], style={'display': 'flex', 'justify-content': 'left', 'gap': '400px', 'width': '100%',
                      'font-size': '14px'})
        ])

    def correlation_matrix_dashboard(self):
        # Select only numeric columns for correlation matrix
        numeric_cols = self.data.select_dtypes(include='number').columns
        fig = px.imshow(self.data[numeric_cols].corr(), text_auto=True,
                        title="Correlation Matrix of Health Data")
        return html.Div([
            dcc.Graph(figure=fig),
            dcc.Markdown("""
                **Variable Key:**
                - Age: The age of the individual.
                - Sex: The gender of the individual (0 = Female, 1 = Male).
                - Education: The highest level of education attained (1 = Primary, 2 = Secondary, 3 = Tertiary or Higher).
                - Asset Wealth: The wealth status based on assets (1 = Lowest, 2 = 2nd, 3 = 3rd, 4 = Highest).
                - Disability Level: The level of disability (0 = Not Disabled, 1 = IADL Limitation Only, 2 = ADL Limitation Only, 3 = Both IADL and ADL).
                - Self-rated Health: The self-rated health status (1 = Poor, 2 = Good, 3 = Very Good, 4 = Excellent).
                - Health Insurance Status: The type of health insurance coverage (0 = Not Covered, 1 = Medical Cards, 2 = Health Insurance, 3 = Dual Coverage).
                - Household Type: The type of household the individual lives in (1 = Living Alone, 2 = Living with Others, 3 = Living with Spouse).
                - Employment Status: The current employment status (0 = Other, 1 = Retired, 2 = Working).
                - Predicted Health Outcomes: The predicted health outcomes based on the model.
        """, style={'text-align': 'left', 'font-size': '14px'})
        ])

    def employment_status_health_coverage_dashboard(self):
        # Group by Employment Status and Health Insurance Status to get accurate counts
        grouped_data = self.data.groupby(['Employment Status', 'Health Insurance Status']).size().reset_index(
            name='counts')

        fig = px.bar(grouped_data, x='Employment Status', y='counts', color='Health Insurance Status', barmode='stack',
                     title='Employment Status and Health Insurance Coverage',
                     labels={'Employment Status': 'Employment Status', 'counts': 'Count',
                             'Health Insurance Status': 'Health Insurance Status'},
                     text='counts')

        fig.update_layout(
            xaxis_title='Employment Status',
            yaxis_title='Count of Health Insurance Status',
            coloraxis_colorbar=dict(
                title='Health Insurance Status',
                tickvals=[0, 1, 2, 3],
                ticktext=['Not Covered', 'Medical Cards', 'Health Insurance', 'Dual Coverage']
            )
        )

        return html.Div([
            dcc.Graph(figure=fig),
            html.Div([
                dcc.Markdown("""
                    **Employment Status Key:**
                    - 0: Other
                    - 1: Retired
                    - 2: Working

                """)
            ], style={'display': 'flex', 'justify-content': 'left', 'gap': '400px', 'width': '100%',
                      'font-size': '14px'})
        ])

    def self_rated_health_by_age_sex_education_dashboard(self):
        self.data['Age Group'] = pd.cut(self.data['Age'], bins=[0, 64, 74, 100], labels=['50-64', '65-74', '>=75'])
        fig = px.histogram(self.data, x='Age Group', color='Self-rated Health',
                           facet_col='Sex', facet_row='Education', barmode='group',
                           title='Self-rated health by age, sex, and education')
        fig.update_layout(barmode='stack',
                          xaxis_title='Age Group',
                          yaxis_title='Sum - Self-rated Health',
                          margin=dict(l=0, r=0, t=50, b=0))
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
        return html.Div([
            dcc.Graph(figure=fig),
            dcc.Markdown("""
                **Variable Key:**
                - Sex: The gender of the individual (0 = Female, 1 = Male).
                - Education: The highest level of education attained (1 = Primary, 2 = Secondary, 3 = Tertiary or Higher).
                - Self-rated Health: The self-rated health status (1 = Poor, 2 = Good, 3 = Very Good, 4 = Excellent).
                
            """)
        ])

    def insurance_status_by_wealth_dashboard(self):
        # Group data by 'Asset Wealth' and 'Health Insurance Status' and count the occurrences
        grouped_data = self.data.groupby(['Asset Wealth', 'Health Insurance Status']).size().reset_index(name='Count')

        # Create a stacked bar chart
        fig = px.bar(grouped_data, x='Asset Wealth', y='Count', color='Health Insurance Status',
                     title='Health Insurance Status by Wealth',
                     labels={'Asset Wealth': 'Asset Wealth', 'Health Insurance Status': 'Health Insurance Status'},
                     barmode='stack')

        # Update layout
        fig.update_layout(showlegend=True, legend_title_text='Health Insurance Status',
                          legend=dict(
                              orientation="h",  # Horizontal layout for legend items
                              yanchor="bottom",
                              y=1.02,  # Position the legend just above the chart
                              xanchor="right",
                              x=1  # Position the legend to the right of the chart
                          ))

        return html.Div([
            dcc.Graph(figure=fig),
            html.Div([
                dcc.Markdown("""
                    **Wealth Level Key:**
                    - 1: Lowest
                    - 2: 2nd
                    - 3: 3rd
                    - 4: Highest
                """),
                dcc.Markdown("""
                    **Health Insurance Status Key:**
                    - 0: Not Covered
                    - 1: Medical Cards
                    - 2: Health Insurance
                    - 3: Dual Coverage
                """)
            ], style={'display': 'flex', 'justify-content': 'left', 'gap': '400px', 'width': '100%',
                      'font-size': '14px'})
        ])

    def register_callbacks(self):
        pass

import pandas as pd
import random
import plotly.express as px
from dash import Dash, dcc, html
import os

# Step 1: Generate a detailed dataset and save it as CSV
data = {
    "Month": pd.date_range(start="2024-01-01", periods=12, freq="M").strftime("%b-%Y"),
    "Expense Category": random.choices(["Operations", "Marketing", "Research", "IT"], k=12),
    "Amount": [random.randint(10000, 50000) for _ in range(12)],
    "Region": random.choices(["North", "South", "East", "West"], k=12),
    "Sales": [random.randint(50000, 150000) for _ in range(12)],
    "Type": random.choices(["AP", "AR"], k=12),
    "Aging Bucket": random.choices(["0-30 days", "31-60 days", "61-90 days", "90+ days"], k=12),
}

# Save the data to a CSV file
csv_file = "financial_data.csv"
df = pd.DataFrame(data)
df.to_csv(csv_file, index=False)
print(f"CSV file '{csv_file}' created successfully!")

# Step 2: Load the dataset from CSV
df = pd.read_csv(csv_file)

# Step 3: Create detailed and visually appealing graphs

# Expense Summary
expense_summary = df.groupby("Expense Category")["Amount"].sum().reset_index()
expense_chart = px.bar(
    expense_summary,
    x="Expense Category",
    y="Amount",
    title="Expense Summary",
    color="Expense Category",
    text="Amount",
    template="plotly_dark",
)
expense_chart.update_traces(texttemplate='%{text:.2s}', textposition='outside')
expense_chart.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
expense_image = "expense_summary.png"
expense_chart.write_image(expense_image, width=800, height=600)

# Sales by Region
sales_summary = df.groupby("Region")["Sales"].sum().reset_index()
sales_chart = px.pie(
    sales_summary,
    names="Region",
    values="Sales",
    title="Sales by Region",
    hole=0.3,
    template="plotly_dark",
)
sales_image = "sales_by_region.png"
sales_chart.write_image(sales_image, width=800, height=600)

# AP and AR Aging Summary
ap_ar_summary = df.groupby(["Type", "Aging Bucket"])["Amount"].sum().reset_index()
aging_chart = px.bar(
    ap_ar_summary,
    x="Aging Bucket",
    y="Amount",
    color="Type",
    barmode="group",
    title="AP and AR Aging Summary",
    text="Amount",
    template="plotly_dark",
)
aging_chart.update_traces(texttemplate='%{text:.2s}', textposition='outside')
aging_image = "ap_ar_aging_summary.png"
aging_chart.write_image(aging_image, width=800, height=600)

# Step 4: Set up the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("CFO Dashboard", style={"textAlign": "center", "color": "white"}),

    html.Div([
        html.H2("Expense Summary", style={"color": "white"}),
        dcc.Graph(figure=expense_chart)
    ], style={"marginBottom": "30px"}),

    html.Div([
        html.H2("Sales by Region", style={"color": "white"}),
        dcc.Graph(figure=sales_chart)
    ], style={"marginBottom": "30px"}),

    html.Div([
        html.H2("AP and AR Aging Summary", style={"color": "white"}),
        dcc.Graph(figure=aging_chart)
    ], style={"marginBottom": "30px"})
], style={"backgroundColor": "#111111", "padding": "20px"})

# Step 5: Run the Dash server
if __name__ == "__main__":
    print("Starting Dash server at http://127.0.0.1:8050/")
    app.run_server(debug=True, port=8050)

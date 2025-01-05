# Cretum Advisory - Assignment

## Deployed Version

The CFO Dashboard has been deployed and can be accessed via the following ngrok link:

- **Deployed CFO Dashboard**: [https://fd44-34-48-18-108.ngrok-free.app/](https://fd44-34-48-18-108.ngrok-free.app/)

## What is Happening?

This dashboard visualizes financial data using **interactive charts** built with **Dash** and **Plotly**. The main features are:
- **Expense Summary**: Displays a bar chart of expenses by category.
- **Sales by Region**: Displays a pie chart of sales distribution across different regions.
- **AP and AR Aging Summary**: Shows a bar chart for accounts payable and receivable aging.

The **ngrok** service is being used to expose the local development server to the internet. This allows you to access the dashboard remotely through the ngrok-generated link, which serves the locally running Dash app.

## How It Works:

- **ngrok** creates a secure tunnel from the public internet to your local machine.
- When you run the application on your local server, ngrok provides a public URL (like the one above) that points to your local app.
- This URL can be shared with others for remote access to the application.

Feel free to explore the dashboard via the provided link and check out the financial insights it provides.

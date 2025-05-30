import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Load data
file_path = "/mnt/data/epa-sea-level.csv"
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    df = None

# Proceed only if data is loaded
if df is not None:
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    # First line of best fit (all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = np.arange(1880, 2051)
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    plt.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (1880–2050)')

    # Second line of best fit (from 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit Line (2000–2050)')

    # Finalizing plot
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid(True)

    # Save and return figure
    output_path = "/mnt/data/sea_level_plot.png"
    plt.savefig(output_path)
    plt.close()
    output_path
else:
    "Dataset not found. Please upload epa-sea-level.csv."


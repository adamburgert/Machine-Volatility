import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dataset recreation
data_reformatted = {
    "Configuration": [
        "Without Volatility Input", "Without Volatility Input", "Without Volatility Input",
        "3-Day Volatility Input", "3-Day Volatility Input", "3-Day Volatility Input",
        "9-Day Volatility Input", "9-Day Volatility Input", "9-Day Volatility Input",
        "21-Day Volatility Input", "21-Day Volatility Input", "21-Day Volatility Input",
        "30-Day Volatility Input", "30-Day Volatility Input", "30-Day Volatility Input",
        "60-Day Volatility Input", "60-Day Volatility Input", "60-Day Volatility Input",
        "90-Day Volatility Input", "90-Day Volatility Input", "90-Day Volatility Input",
    ],
    "Dataset": [
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
        "Training", "Validation", "Testing",
    ],
    "MSE": np.round([
        1.10888, 0.64484, 0.23075,
        0.17777, 0.08987, 0.09839,
        0.17922, 0.07221, 0.12490,
        0.17820, 0.11669, 0.15419,
        0.05956, 0.05001, 0.06768,
        0.03296, 0.03337, 0.05435,
        0.17046, 0.08365, 0.12078,
    ], 5),
    "MAE": np.round([
        0.56737, 0.46712, 0.33405,
        0.31991, 0.21953, 0.22597,
        0.28810, 0.19643, 0.25280,
        0.33583, 0.27054, 0.28253,
        0.18562, 0.17461, 0.19698,
        0.13794, 0.13773, 0.14466,
        0.32339, 0.22257, 0.24130,
    ], 5),
    "MAPE": np.round([
        3.30890, 3.56365, 4.20611,
        1.27186, 1.36212, 3.26164,
        1.33550, 1.28366, 3.79487,
        1.34740, 1.47506, 3.02902,
        0.84266, 0.99121, 2.30152,
        0.55818, 0.67478, 1.42557,
        1.08077, 1.02609, 2.43608,
    ], 5),
    "Average Price Prediction Difference (Nominal in USD$)": np.round([
        0.26700, 0.23199, 0.05488,
        -0.01756, 0.02085, -0.09037,
        -0.23298, -0.12208, -0.21981,
        -0.06671, -0.02194, -0.04278,
        0.02897, -0.03939, -0.16261,
        0.06687, 0.05257, -0.05889,
        -0.06896, -0.04325, -0.19649,
    ], 5),
    "Average Price Prediction Difference (%)": np.round([
        0.66158, 0.58172, -0.56514,
        -0.29485, -0.45501, -2.38550,
        -1.13427, -0.98053, -3.65575,
        0.39907, 0.46929, 0.50563,
        -0.20710, -0.54434, -2.14954,
        0.19731, 0.16701, -0.75347,
        -0.67913, -0.55736, -2.17543,
    ], 5),
}

df_reformatted = pd.DataFrame(data_reformatted)

# Metrics and configurations
metrics = ["MSE", "MAE", "MAPE",
           "Average Price Prediction Difference (Nominal in USD$)",
           "Average Price Prediction Difference (%)"]
configurations = df_reformatted["Configuration"].unique()
datasets = ["Training", "Validation", "Testing"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Colors for datasets

# Plotting
for metric in metrics:
    plt.figure(figsize=(14, 8))
    
    # Bar positions for configurations
    x_positions = np.arange(len(configurations))
    bar_width = 0.2  # Width of each bar
    
    # Plot each dataset as a separate group of bars
    for i, dataset in enumerate(datasets):
        dataset_values = df_reformatted[df_reformatted["Dataset"] == dataset][metric].values
        plt.bar(
            x_positions + i * bar_width,
            dataset_values,
            width=bar_width,
            label=f"{dataset} Dataset",
            color=colors[i]
        )
    
    plt.title(f"{metric} Across Configurations and Datasets Call options", fontsize=16, fontweight="bold")
    plt.xlabel("Configuration", fontsize=14)
    plt.ylabel(metric, fontsize=14)
    plt.xticks(x_positions + bar_width, configurations, rotation=45, ha="right", fontsize=12)
    plt.legend(title="Dataset", fontsize=12)
    plt.tight_layout()
    plt.show()







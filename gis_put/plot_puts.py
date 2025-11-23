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
        1.5183, 0.8666, 0.309,
        0.5492, 0.1704, 0.1808,
        0.7483, 0.2938, 0.1785,
        1.1578, 0.2511, 0.1443,
        0.0726, 0.0619, 0.0519,
        1.675, 0.4785, 0.2437,
        0.1541, 0.0769, 0.1189,
    ], 5),
    "MAE": np.round([
         0.7435, 0.5859, 0.4202,
        0.4501, 0.2913, 0.3239,
        0.6006, 0.4064, 0.3456,
        0.7466, 0.3672, 0.3243,
        0.2126, 0.1946, 0.1719,
        0.9056, 0.4975, 0.4075,
        0.2887, 0.2082, 0.2346,
    ], 5),
    "MAPE": np.round([
         5.1128, 5.3318, 6.3299,
        2.3086, 1.8767, 3.4033,
        2.6772, 2.1384, 2.6717,
        2.2976, 1.7041, 4.1,
        0.91, 1.1155, 1.9789,
        2.0879, 1.8784, 3.5271,
        1.3493, 1.3385, 3.838,
    ], 5),
    "Average Price Prediction Difference (Nominal in USD$)": np.round([
         -0.0147, 0.1005, 0.0123,
        -0.1341, -0.0634, -0.0756,
        -0.4527, -0.2196, 0.244,
        -0.0179, 0.0525, 0.0769,
        -0.0527, -0.0401, -0.111,
        0.1868, 0.0997, 0.1651,
        -0.0263, 0.0002, -0.1575,
    ], 5),
    "Average Price Prediction Difference (%)": np.round([
      -1.7119, -1.2842, -2.8281,
        -1.0824, -0.3231, 0.7699,
        -2.0539, -1.3358, 0.7807,
        -0.8719, -0.365, -2.3222,
        -0.4407, -0.5504, -1.5818,
        1.0957, 1.0207, 0.6847,
        0.0631, -0.1352, -3.3826,
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
    
    plt.title(f"{metric} Across Configurations and Datasets Put Options", fontsize=16, fontweight="bold")
    plt.xlabel("Configuration", fontsize=14)
    plt.ylabel(metric, fontsize=14)
    plt.xticks(x_positions + bar_width, configurations, rotation=45, ha="right", fontsize=12)
    plt.legend(title="Dataset", fontsize=12)
    plt.tight_layout()
    plt.show()






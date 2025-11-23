import pandas as pd
import matplotlib.pyplot as plt




# Load the provided Excel file
file_path = "./validation_data_synthetic_4.xlsx"
calls_df = pd.read_excel(file_path, sheet_name="Calls")
puts_df = pd.read_excel(file_path, sheet_name="Puts")

# Extract relevant columns for plotting
calls_plot_data = calls_df[["Date", "Call Price_ITM_1", "Call Price_ITM_2", "Call Price_OTM_1", "Call Price_OTM_2"]]
puts_plot_data = puts_df[["Date", "Put Price_ITM_1", "Put Price_ITM_2", "Put Price_OTM_1", "Put Price_OTM_2"]]

# Convert 'Date' columns to datetime for better plotting
calls_plot_data["Date"] = pd.to_datetime(calls_plot_data["Date"])
puts_plot_data["Date"] = pd.to_datetime(puts_plot_data["Date"])

# Plot Call Option Prices over Time
plt.figure(figsize=(12, 6))
plt.plot(calls_plot_data["Date"], calls_plot_data["Call Price_ITM_1"], label="ITM Call 1")
plt.plot(calls_plot_data["Date"], calls_plot_data["Call Price_ITM_2"], label="ITM Call 2")
plt.plot(calls_plot_data["Date"], calls_plot_data["Call Price_OTM_1"], label="OTM Call 1")
plt.plot(calls_plot_data["Date"], calls_plot_data["Call Price_OTM_2"], label="OTM Call 2")
plt.title("Call Option Prices Over Time Validation Dataset")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# Plot Put Option Prices over Time
plt.figure(figsize=(12, 6))
plt.plot(puts_plot_data["Date"], puts_plot_data["Put Price_ITM_1"], label="ITM Put 1")
plt.plot(puts_plot_data["Date"], puts_plot_data["Put Price_ITM_2"], label="ITM Put 2")
plt.plot(puts_plot_data["Date"], puts_plot_data["Put Price_OTM_1"], label="OTM Put 1")
plt.plot(puts_plot_data["Date"], puts_plot_data["Put Price_OTM_2"], label="OTM Put 2")
plt.title("Put Option Prices Over Time Validation Dataset")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()


# Extract rolling volatility columns for plotting
volatility_plot_data = calls_df[["Date", "3_Day_Volatility", "9_Day_Volatility", "21_Day_Volatility",
                                 "30_Day_Volatility", "60_Day_Volatility", "90_Day_Volatility","3_Day_Percent_Volatility", "9_Day_Percent_Volatility", "21_Day_Percent_Volatility", "30_Day_Percent_Volatility", "60_Day_Percent_Volatility", "90_Day_Percent_Volatility" ]]

# Convert 'Date' column to datetime
volatility_plot_data["Date"] = pd.to_datetime(volatility_plot_data["Date"])
# Plot Rolling Volatility Trends
plt.figure(figsize=(12, 6))
plt.plot(volatility_plot_data["Date"], volatility_plot_data["3_Day_Volatility"], label="3-Day Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["9_Day_Volatility"], label="9-Day Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["21_Day_Volatility"], label="21-Day Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["30_Day_Volatility"], label="30-Day Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["60_Day_Volatility"], label="60-Day Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["90_Day_Volatility"], label="90-Day Volatility")
plt.title("Rolling Volatility (Nominal in USD$) Trends Over Time Validation Dataset")
plt.xlabel("Date")
plt.ylabel("Volatility (Nominal in USD$)")
plt.legend()
plt.grid(True)
plt.show()


# Convert 'Date' column to datetime
volatility_plot_data["Date"] = pd.to_datetime(volatility_plot_data["Date"])
# Plot Rolling Volatility Trends
plt.figure(figsize=(12, 6))
plt.plot(volatility_plot_data["Date"], volatility_plot_data["3_Day_Percent_Volatility"], label="3_Day_Percent_Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["9_Day_Percent_Volatility"], label="9_Day_Percent_Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["21_Day_Percent_Volatility"], label="21_Day_Percent_Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["30_Day_Percent_Volatility"], label="30_Day_Percent_Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["60_Day_Percent_Volatility"], label="60_Day_Percent_Volatility")
plt.plot(volatility_plot_data["Date"], volatility_plot_data["90_Day_Percent_Volatility"], label="90_Day_Percent_Volatility")
plt.title("Rolling Volatility (%)) Trends Over Time Validation Dataset")
plt.xlabel("Date")
plt.ylabel("Volatility (%))")
plt.legend()
plt.grid(True)
plt.show()




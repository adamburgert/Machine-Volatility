import numpy as np
import pandas as pd
from scipy.stats import norm

# Set random seed for reproducibility
np.random.seed(100)

# Parameters for synthetic price generation
n_days = 5090  # Number of days (approximately 8 years)
initial_price = 349.759615445901  # Initial price of the asset (e.g., GLD)
mu = 0.0005  # Drift factor (average daily return)
dt = 1 / 252  # Daily time step (assuming 252 trading days in a year)

# Volatility range (annualized)
min_annual_volatility = 0.01  # 0.5% minimum annualized volatility
max_annual_volatility = 0.4  # 30% maximum annualized volatility

# Define random volatility generator (uses annual volatility)
def get_random_volatility():
    return np.random.uniform(min_annual_volatility, max_annual_volatility)

# Risk-free interest rate
r = 0.05  # Annualized risk-free rate (5%)


# Generate random annualized volatilities
annual_volatilities = np.random.uniform(min_annual_volatility, max_annual_volatility, n_days)

# Convert to daily volatilities
daily_volatilities = annual_volatilities / np.sqrt(252)


# Generate synthetic price data starting from the initial price
price_data = np.zeros(n_days)
price_data[0] = initial_price

# Generate synthetic price data using Geometric Brownian Motion
daily_returns = np.random.normal(mu * dt, daily_volatilities, n_days)
price_data = initial_price * np.exp(np.cumsum(daily_returns))

# Create DataFrame with synthetic data
dates = pd.date_range(start="1987-11-04", periods=n_days, freq="B")  # Business days
synthetic_data = pd.DataFrame({"Date": dates, "Close": price_data})

# Calculate log returns
synthetic_data["Log_Returns"] = np.log(synthetic_data["Close"] / synthetic_data["Close"].shift(1))

# Rolling standard deviations (volatility) for different windows
rolling_std_3 = synthetic_data["Log_Returns"].rolling(window=3).std().fillna(0)
rolling_std_9 = synthetic_data["Log_Returns"].rolling(window=9).std().fillna(0)
rolling_std_21 = synthetic_data["Log_Returns"].rolling(window=21).std().fillna(0)
rolling_std_30 = synthetic_data["Log_Returns"].rolling(window=30).std().fillna(0)
rolling_std_60 = synthetic_data["Log_Returns"].rolling(window=60).std().fillna(0)
rolling_std_90 = synthetic_data["Log_Returns"].rolling(window=90).std().fillna(0)

# Annualize rolling standard deviations
annualized_std_3 = rolling_std_3 * np.sqrt(252)
annualized_std_9 = rolling_std_9 * np.sqrt(252)
annualized_std_21 = rolling_std_21 * np.sqrt(252)
annualized_std_30 = rolling_std_30 * np.sqrt(252)
annualized_std_60 = rolling_std_60 * np.sqrt(252)
annualized_std_90 = rolling_std_90 * np.sqrt(252)

# Calculate percentage volatilities
percentage_volatility_3 = annualized_std_3 * 100 * np.sqrt(3 / 252)
percentage_volatility_9 = annualized_std_9 * 100 * np.sqrt(9 / 252)
percentage_volatility_21 = annualized_std_21 * 100 * np.sqrt(21 / 252)
percentage_volatility_30 = annualized_std_30 * 100 * np.sqrt(30 / 252)
percentage_volatility_60 = annualized_std_60 * 100 * np.sqrt(60 / 252)
percentage_volatility_90 = annualized_std_90 * 100 * np.sqrt(90 / 252)

# Define a function to calculate Black-Scholes option prices
def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    S: Stock price (current price of synthetic asset)
    K: Strike price
    T: Time to expiration (in years)
    r: Risk-free interest rate (annualized)
    sigma: Volatility (annualized)
    option_type: 'call' for call option, 'put' for put option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


# Option pricing parameters
expiration_days = 30  # Time to expiration (30 days)
T = expiration_days / 365  # Convert days to years

itm_call_factors_1 = np.random.uniform(0.90, 0.99, n_days)  # ITM Call - 1-10% below current price
itm_call_factors_2 = np.random.uniform(0.80, 0.90, n_days)  # ITM Call - 10-20% below current price

otm_call_factors_1 = np.random.uniform(0.70, 0.80, n_days)  # OTM Call - 20-30% below current price
otm_call_factors_2 = np.random.uniform(0.60, 0.70, n_days)  # OTM Call - 30-40% below current price

itm_put_factors_1 = np.random.uniform(1.01, 1.10, n_days)   # ITM Put - 1-10% above current price
itm_put_factors_2 = np.random.uniform(1.10, 1.20, n_days)   # ITM Put - 10-20% above current price

otm_put_factors_1 = np.random.uniform(1.20, 1.30, n_days)   # OTM Put - 20-30% above current price
otm_put_factors_2 = np.random.uniform(1.30, 1.40, n_days)   # OTM Put - 30-40% above current price



# Lists to store option data
calls_data = []
puts_data = []

# Loop through each day and calculate option prices
for i in range(len(synthetic_data)):
    current_price = synthetic_data["Close"].iloc[i]
    last_date = synthetic_data["Date"].iloc[i]
    volatility = get_random_volatility()

    # Call options: ITM and OTM
    itm_strike_call_1 = current_price * itm_call_factors_1[i]
    itm_strike_call_2 = current_price * itm_call_factors_2[i]
    otm_strike_call_1 = current_price * otm_call_factors_1[i]
    otm_strike_call_2 = current_price * otm_call_factors_2[i]


    calls_data.append({
        "Date": last_date,
        "Underlying Price": current_price,
        "Expiration Days": expiration_days,
        "3_Day_Volatility": annualized_std_3.iloc[i] * current_price * volatility,
        "9_Day_Volatility": annualized_std_9.iloc[i] * current_price * volatility,
        "21_Day_Volatility": annualized_std_21.iloc[i] * current_price * volatility,
        "30_Day_Volatility": annualized_std_30.iloc[i] * current_price * volatility,
        "60_Day_Volatility": annualized_std_60.iloc[i] * current_price * volatility,
        "90_Day_Volatility": annualized_std_90.iloc[i] * current_price * volatility,
        "3_Day_Percent_Volatility": percentage_volatility_3.iloc[i],
        "9_Day_Percent_Volatility": percentage_volatility_9.iloc[i],
        "21_Day_Percent_Volatility": percentage_volatility_21.iloc[i],
        "30_Day_Percent_Volatility": percentage_volatility_30.iloc[i],
        "60_Day_Percent_Volatility": percentage_volatility_60.iloc[i],
        "90_Day_Percent_Volatility": percentage_volatility_90.iloc[i],
        "Strike_ITM_1": otm_strike_call_1,
        "Call Price_ITM_1": black_scholes(current_price, otm_strike_call_1, T, r, volatility, "call"),
        "Strike_ITM_2": otm_strike_call_2,
        "Call Price_ITM_2": black_scholes(current_price, otm_strike_call_2, T, r, volatility, "call"),
        "Strike_OTM_1": itm_strike_call_1,
        "Call Price_OTM_1": black_scholes(current_price, itm_strike_call_1, T, r, volatility, "call"),
        "Strike_OTM_2": itm_strike_call_2,
        "Call Price_OTM_2": black_scholes(current_price, itm_strike_call_2, T, r, volatility, "call"),

    })

    # Put options: ITM and OTM
    itm_strike_put_1 = current_price * itm_put_factors_1[i]
    itm_strike_put_2 = current_price * itm_put_factors_2[i]

    otm_strike_put_1 = current_price * otm_put_factors_1[i]
    otm_strike_put_2 = current_price * otm_put_factors_2[i]


    puts_data.append({
        "Date": last_date,
        "Underlying Price": current_price,
        "Expiration Days": expiration_days,
        "3_Day_Volatility": annualized_std_3.iloc[i] * current_price * volatility,
        "9_Day_Volatility": annualized_std_9.iloc[i] * current_price * volatility,
        "21_Day_Volatility": annualized_std_21.iloc[i] * current_price * volatility,
        "30_Day_Volatility": annualized_std_30.iloc[i] * current_price * volatility,
        "60_Day_Volatility": annualized_std_60.iloc[i] * current_price * volatility,
        "90_Day_Volatility": annualized_std_90.iloc[i] * current_price * volatility,
        "3_Day_Percent_Volatility": percentage_volatility_3.iloc[i],
        "9_Day_Percent_Volatility": percentage_volatility_9.iloc[i],
        "21_Day_Percent_Volatility": percentage_volatility_21.iloc[i],
        "30_Day_Percent_Volatility": percentage_volatility_30.iloc[i],
        "60_Day_Percent_Volatility": percentage_volatility_60.iloc[i],
        "90_Day_Percent_Volatility": percentage_volatility_90.iloc[i],
        "Strike_ITM_1": itm_strike_put_1,
        "Put Price_ITM_1": black_scholes(current_price, itm_strike_put_1, T, r, volatility, "put"),
        "Strike_ITM_2": itm_strike_put_2,
        "Put Price_ITM_2": black_scholes(current_price, itm_strike_put_2, T, r, volatility, "put"),
        "Strike_OTM_1": otm_strike_put_1,
        "Put Price_OTM_1": black_scholes(current_price, otm_strike_put_1, T, r, volatility, "put"),
        "Strike_OTM_2": otm_strike_put_2,
        "Put Price_OTM_2": black_scholes(current_price, otm_strike_put_2, T, r, volatility, "put"),

    })




# Convert to DataFrames
calls_df = pd.DataFrame(calls_data)
puts_df = pd.DataFrame(puts_data)

# Drop first 30 rows and reset index
calls_df = calls_df.iloc[90:].reset_index(drop=True)
puts_df = puts_df.iloc[90:].reset_index(drop=True)

# Save to Excel in separate sheets
with pd.ExcelWriter("validation_data_synthetic_4.xlsx") as writer:
    calls_df.to_excel(writer, sheet_name="Calls", index=False)
    puts_df.to_excel(writer, sheet_name="Puts", index=False)

# Print verification
print("Sample Calls Data:")
print(calls_df.head())  # Display the first few rows of the calls DataFrame

print("\nSample Puts Data:")
print(puts_df.head())  # Display the first few rows of the puts DataFrame
# Smart Inventory Forecasting for reducing food wastage.
# Author: Jeevika Bhat
# Tools: Python, Prophet, Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import plotly.express as px

# Step-1 : Load the Data
data = pd.read_csv("data/train.csv")
data["date"] = pd.to_datetime(data["date"])

#Step-2 : Prepare the Data (1 Store only)
store_df = data[data["store"] == 1].groupby("date")["sales"].sum().reset_index()
store_df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)
print(f"Loaded {len(store_df)} daily records for Store 1")

#Step-3 : Visualize all the trends
plt.figure(figsize=(10, 4))
plt.plot(store_df["ds"], store_df["y"], color="teal")
plt.title("Daily Sales Trend - Store 1")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("data/historical_sales.png", dpi=300)
plt.show()

#Step-4 : Train Prophet Model 
print("Training Prophet model.")
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
model.fit(store_df)
print("Model training completed.")

#Step-5 :  Forecast next 60 days
future = model.make_future_dataframe(periods=60)
forecast = model.predict(future)

#Step-6 : Visualize full Prophet Forecast
fig1 = model.plot(forecast, xlabel="Date", ylabel="Sales")
plt.title("Sales Forecast - Full Timeline")
plt.tight_layout()
plt.savefig("data/full_forecast.png", dpi=300)
plt.show()

#Step-7 : Plot for next 60 days only
plt.figure(figsize=(10, 5))
plt.plot(forecast["ds"], forecast["yhat"], label="Forecast", color="darkorange")
plt.plot(store_df["ds"], store_df["y"], label="Actual", color="steelblue")
plt.title("Next 60 Days Forecast for Store 1")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("data/next_60_days_forecast.png", dpi=300)
plt.show()

#Step-8 : Interactive visualization
print("Generating interactive forecast...")
future_only = forecast[forecast["ds"] > store_df["ds"].max()]
fig = px.line(future_only, x="ds", y="yhat", title="Interactive Sales Forecast (Next 60 Days)", labels={"ds": "Date", "yhat": "Predicted Sales"})
fig.show()
fig.write_html("data/interactive_forecast.html")
print("Interactive chart saved as data/interactive_forecast.html")

#Step-9 : Save the forecast results
forecast.to_excel("data/sales_forecast.xlsx", index=False)
print("Forecast results saved to data/sales_forecast.xlsx")

#Step-10 : Business insights
top_days = forecast.nlargest(5, "yhat")[["ds", "yhat"]]
print("\nTop 5 predicted high-demand days:")
print(top_days.to_string(index=False))

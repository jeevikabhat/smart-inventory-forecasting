## 🧠 Smart Inventory Forecasting System
This project predicts product demand using past sales data so that retail or food businesses can plan inventory better and reduce food waste.

## 📊 What It Does
It uses Meta’s Prophet model to analyze historical sales and forecast demand for the next 60 days.  
You can view:
1. Sales trends over time  
2. Predicted demand for upcoming weeks  
3. Top 5 highest-demand days

## 💻 Tech Used
1. Python 3
2. Libraries: pandas, matplotlib, prophet, openpyxl
3. Dataset: Store Item Demand Forecasting Challenge from Kaggle

## 🚀 Steps to Run

1. Install dependencies
   pip3 install pandas matplotlib prophet openpyxl
2. Place your train.csv inside a folder named data
3. Run the script:
   python3 forecast.py
4. Output files will be generated in the data/ folder:
   
**Forecast Excel:** [sales_forecast.xlsx](data/sales_forecast.xlsx)  
**Full forecast chart:** [full_forecast.png](data/full_forecast.png)  
**Next 60 days chart:** [next_60_days_forecast.png](data/next_60_days_forecast.png)

## ⚠️ Learnings & Challenges
1. Initially, the Prophet forecast plotted all available data (2013–2018) instead of just the upcoming 60 days. This was resolved by filtering the forecast output before plotting.
2. While setting up Prophet on Python 14.0.0, I faced an environment management issue due to system-protected Python (PEP 668). This can be resolved by creating a virtual environment (venv).
3. Learned how to structure, clean and visualize data to interpret predictions effectively.

## 💡 Improvements
1. Add an interactive Streamlit or Plotly dashboard
2. Include accuracy metrics (MAPE, RMSE) for evaluation

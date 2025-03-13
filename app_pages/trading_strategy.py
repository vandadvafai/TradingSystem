import streamlit as st
import pandas as pd
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Import necessary modules
from trading_strat import TradingStrategy
from api_wrapper import api_wrapper

def trading_strategy_page():
    st.title("📈 Trading Strategy Simulation")

    st.header("How It Works")
    st.write(
        "This page allows you to test an **automated trading strategy** based on AI-powered market predictions. "
        "The system fetches stock market data, applies a **machine learning model**, and executes **Buy/Sell/Hold** decisions."
    )

    st.subheader("Trading Strategy Rules")
    st.markdown(
        """
        - 📈 **Buy**: If the model predicts a price increase, the system buys shares.
        - 📉 **Sell**: If the model predicts a price decrease, the system sells shares.
        - ⏳ **Hold**: If no clear signal is given, the system holds the current position.
        """
    )

    st.header("Run the Strategy")
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
    start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("2023-12-31"))

    if st.button("Run Trading Strategy"):
        api = api_wrapper()
        stock_data = api.get_share_prices(ticker, str(start_date), str(end_date))

        if stock_data is not None and not stock_data.empty:
            strategy = TradingStrategy()
            final_cash, final_shares = strategy.apply_strategy(stock_data)

            # Display trade log
            st.subheader("📜 Trade Log")
            for trade in strategy.trade_log:
                st.write(trade)

            # Display final portfolio value
            final_portfolio_value = final_cash + final_shares * stock_data.iloc[-1]['Close']
            st.subheader("💰 Final Portfolio Value")
            st.write(f"**${final_portfolio_value:,.2f}**")

            # Show price trends
            st.subheader("📊 Stock Price Movements")
            st.line_chart(stock_data.set_index("Date")["Close"])

        else:
            st.error("⚠️ No stock data available for the given ticker and date range.")

    st.write("🚀 Developed as part of a group project in **Automated Daily Trading Systems**.")

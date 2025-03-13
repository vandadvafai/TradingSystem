import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import datetime

def go_live_page():
    st.title("📊 Live Trading Dashboard")
    st.write("Powered by Machine Learning & SimFin API")

    # Load Merged Data from ETL Output
    etl_output_path = "data/processed/output.csv"  # Adjust path if necessary
    df_merged = pd.read_csv(etl_output_path)

    # Ensure the Date column is in datetime format
    df_merged['Date'] = pd.to_datetime(df_merged['Date'])

    # Get the list of unique tickers from the merged data
    unique_tickers = sorted(df_merged['Ticker'].unique())

    # Sidebar Controls: select ticker
    st.sidebar.header("Select a Stock from ETL")
    ticker = st.sidebar.selectbox("Ticker:", unique_tickers)

    # Define allowed date range: start date cannot be before Jan 1, 2020,
    # and end date cannot be after today's date.
    today = datetime.date.today()
    min_allowed_date = datetime.date(2020, 1, 1)

    # Date inputs with built-in restrictions
    start_date = st.sidebar.date_input(
        "Start Date", value=min_allowed_date,
        min_value=min_allowed_date, max_value=today
    )
    end_date = st.sidebar.date_input(
        "End Date", value=today,
        min_value=min_allowed_date, max_value=today
    )

    # Check if start_date is later than end_date
    if start_date > end_date:
        st.error("Start date cannot be after end date.")
        return

    # (Optional) Extra warning messages if needed (the widget restrictions prevent invalid choices)
    if start_date < min_allowed_date:
        st.warning("Start date cannot be before January 1, 2020.")
    if end_date > today:
        st.warning("End date cannot be after today's date.")

    # When the user clicks "Load Data", filter the data accordingly
    if st.sidebar.button("Load Data"):
        mask = (
            (df_merged['Ticker'] == ticker) &
            (df_merged['Date'] >= pd.to_datetime(start_date)) &
            (df_merged['Date'] <= pd.to_datetime(end_date))
        )
        df_filtered = df_merged.loc[mask].sort_values('Date')

        if df_filtered.empty:
            st.error("No data available for this ticker and date range.")
            return

        # Show a quick data preview
        st.subheader(f"Data Preview for {ticker}")

        # Plot the Stock Price
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df_filtered['Date'], df_filtered['Close'], color='blue', label='Close Price')
        ax.set_xlabel("Date")
        ax.set_ylabel("Stock Price ($)")
        ax.set_title(f"{ticker} Closing Price Over Time")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Run a Model for Predictions
        st.subheader("Model Predictions")

        # Define the required features for the model (adjust if needed)
        required_features = ['Open', 'High', 'Low', 'Close', 'Volume']

        try:
            # Load your pre-trained model (ensure the path is correct)
            model = joblib.load("/Users/vandad/Desktop/TradingSystem/stock_price_predictor.pkl")

            # Check if required feature columns exist in the filtered data
            if all(col in df_filtered.columns for col in required_features):
                # Use the most recent row for prediction as an example
                latest_row = df_filtered.iloc[-1][required_features].values.reshape(1, -1)
                prediction = model.predict(latest_row)

                # Display the prediction result (assuming binary classification: 1=rise, 0=fall)
                if prediction[0] == 1:
                    st.success("Model Prediction: Price is likely to RISE. (Signal: BUY)")
                else:
                    st.warning("Model Prediction: Price is likely to FALL. (Signal: SELL)")
            else:
                st.error("Required feature columns not found in the filtered data. Please adjust your ETL or model feature list.")

        except FileNotFoundError:
            st.error("Model file not found. Please ensure 'stock_price_predictor.pkl' is in the correct path.")

        except Exception as e:
            st.error(f"An error occurred while loading or running the model: {e}")

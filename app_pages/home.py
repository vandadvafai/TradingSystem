import streamlit as st

def home_page():
    st.title("📈 Automated Trading System")
    
    st.header("About the System")
    st.write(
        "This automated trading system leverages **machine learning models** "
        "to analyze historical stock prices and predict market movements. "
        "Users can interact with the system, view insights, and make informed trading decisions."
    )

    st.subheader("Core Functionalities")
    st.markdown(
        """
        - 📊 **Stock Market Analysis**: View historical and real-time stock data.
        - 🤖 **AI-Powered Predictions**: Get next-day market movement forecasts.
        - 🔄 **Automated Trading Decisions**: Buy, sell, or hold suggestions based on predictions.
        - 🌎 **Multi-Company Support**: Works with at least 5 US companies.
        """
    )

    st.header("Meet the Team")
    st.write("Our development team consists of:")
    st.markdown(
        """
        - **Clara Sobejano**
        - **Adam Kassab**
        - **Vandad Vafai Tabrizi**
        - **Juan Echeverri**
        - **Adrian Soto**
        """
    )

    st.header("System Purpose & Objectives")
    st.write(
        "The goal of this system is to **help traders make data-driven decisions** "
        "by providing real-time analysis and AI-powered insights into market trends."
    )

    st.write("🚀 Developed as part of a group project in **Automated Daily Trading Systems**.")

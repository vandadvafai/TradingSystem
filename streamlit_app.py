import streamlit as st

# Import your page functions directly (adjust the import paths as needed)
from app_pages.home import home_page
from app_pages.go_live import go_live_page
from app_pages.trading_strategy import trading_strategy_page

# Set the page title and layout
st.set_page_config(page_title="Automated Trading System", page_icon="📈", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📊 Go Live", "🪙 Trading Strategy"])

# Load the appropriate page
if page == "🏠 Home":
    home_page()
elif page == "📊 Go Live":
    go_live_page()
elif page == "🪙 Trading Strategy":
    trading_strategy_page()
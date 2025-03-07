# Automated Daily Trading System

This repository contains a **multi-page Streamlit application** and accompanying Python scripts to automate daily stock trading predictions. The project is divided into:

1. **Data Analytics Module**  
   - ETL scripts (`etl.py`) to process historical stock price data from SimFin.  
   - ML scripts (`model.py`) to train and predict next-day market movements.  
   - (Optional) Trading strategy logic (`trading_strategy.py`) for buy/sell/hold decisions.

2. **Web-Based Application**  
   - A Streamlit multi-page app (`streamlit_app.py` and `pages/` directory) that allows real-time data retrieval (via `api_wrapper.py`), displays predictive analytics, and shows trading signals.  

## Project Structure

```
your_project/
├── streamlit_app.py         # Main entry point for the Streamlit web app
├── pages/
│   ├── 1_Home.py
│   ├── 2_Go_Live.py
│   ├── 3_ML_Process.py
│   └── 4_About_Trading_Strategy.py (optional)
├── src/
│   ├── etl.py               # ETL code
│   ├── model.py             # ML model code
│   ├── trading_strategy.py  # Trading strategy logic (optional)
│   └── api_wrapper.py       # PySimFin API wrapper
├── data/
│   ├── raw/                 # Bulk download from SimFin
│   └── processed/           # Cleaned/processed data
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/vandadvafai/TradingSystem.git
   cd TradingSystem
   ```

2. **Run the Streamlit Application**  
   ```bash
   streamlit run streamlit_app.py
   ```
   - This command opens a local URL in your browser (usually http://localhost:8501).
   - Explore the pages (Home, Go Live, ML Process, etc.) from the left sidebar.

3. **Project Usage**  
   - **Data ETL**: Download data from SimFin (bulk downloads). Place raw files in `data/raw/`. Run or modify `src/etl.py` to preprocess.  
   - **Model Training**: Adjust and run `src/model.py` to train or update the machine learning model.  
   - **API Wrapper**: Configure `src/api_wrapper.py` with your SimFin API key.  
   - **Trading Strategy (Optional)**: Implement custom buy/sell logic in `src/trading_strategy.py`.  

## Notes

- **SimFin API Key**: Make sure to add your SimFin API key in your environment or directly in `api_wrapper.py` headers (take care not to commit secrets to public repos).
- **Rate Limits**: The free tier of the SimFin API only allows up to 2 requests per second. Built-in delays or caching are recommended if you experience throttling.
- **Further Improvements**: 
  - Deploy the app to Streamlit Cloud or a cloud service if you need to share it publicly.  
  - Add caching to reduce repeated data fetches or large computations.

---

# streamlit_app.py

import streamlit as st
from backend.main import hello_backend

def main():
    st.title("Trading System Web App")
    st.write("This is a minimal Streamlit app connected to a simple Python backend.")
    
    # Display the greeting from the backend
    backend_message = hello_backend()
    st.write(backend_message)

if __name__ == "__main__":
    main()

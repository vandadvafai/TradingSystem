import streamlit as st

def app():
    st.title("Automated Daily Trading System")
    st.subheader("Home")
    st.markdown("""
    **Welcome!** This system forecasts daily stock movements for selected US companies 
    and suggests trading actions. Explore the other pages to see live data, model 
    predictions, and more.
    """)
    
    st.markdown("### Meet the Team")
    st.write(" - Person A: ML Engineer")
    st.write(" - Person B: Data Engineer")
    st.write(" - Person C: Web App Developer")
    # etc.

# This is the code that Streamlit will run if this file is directly opened,
# but typically the multipage system handles navigation.
if __name__ == "__main__":
    app()

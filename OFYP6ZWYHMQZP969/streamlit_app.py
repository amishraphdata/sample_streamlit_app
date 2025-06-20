import streamlit as st
from utils.data_utils import get_sample_data

st.title("🚀 Streamlit Git Integration Test App")

st.markdown("""
Welcome to the **main page** of your Streamlit app!
- Navigate to the sidebar for more.
""")

df = get_sample_data()
st.subheader("Sample Data")
st.dataframe(df, use_container_width=True)

if st.button("Click me!"):
    st.success("You clicked the button! 🎉")

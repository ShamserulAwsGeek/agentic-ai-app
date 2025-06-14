import streamlit as st
import pandas as pd

st.write("""
# My first app 
Hello "Agentic AI"!
""")

df = pd.read_csv(my_data.csv)
st.line_chart(df)

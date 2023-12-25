import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')

df
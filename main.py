import streamlit as st
import pandas as pd
from PIL import Image
import yfinance as yf

st.write("""
#Stock Market Web Application
Visually show data on a stock! Date range Jan 1,2010 to Dec 31,2022
""")

start = '2010-01-01'
end = '2022-12-31'

image = Image.open('C:/Users/91886/PycharmProjects/stockPredictor/venv/image1.jpg')
st.image(image, use_column_width = True)

st.sidebar.header('User Input')
def get_input():
    start_date = st.sidebar.text_input("Start Date", start)
    end_date = st.sidebar.text_input("End Date", end)
    stock_symbol = st.sidebar.text_input("stock_symbol")
    return start_date, end_date, stock_symbol

start1, end1, tick = get_input()

df = yf.download(tick, start1, end1)

st.header("Close Price\n")
st.line_chart(df['Close'])

st.header("Volume\n")
st.line_chart(df['Volume'])

st.header("Data Statistics\n")
st.write(df.describe())




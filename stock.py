import yfinance as yf
import streamlit as st

st.write("""
# Doosan Closing price and Days Volume

Shown are the stock **closing price** and ***volume*** of Doosan Corporation

""")


tickerSymbol = '000150.KS'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-8-01', end='2023-8-24')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
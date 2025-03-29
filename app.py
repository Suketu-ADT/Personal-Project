import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL", "GOOG", "MSFT", "GME", "TSLA", "AMZN", "META", "NFLX", "NVDA", "PYPL", "ADBE")
selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1, 4)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stock)
data_load_state.text("Loading data... done!")

st.subheader("Raw data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    
    # 1) Stock Open line
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Open'],
        name='stock_open',
        line=dict(color='blue', width=2)
    ))
    
    # 2) Stock Close line
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        name='stock_close',
        line=dict(color='red', width=2)
    ))
    
    # 3) Update layout to use default Plotly styling
    fig.update_layout(
        title_text=f"{selected_stock} Stock Price Over Time",
        xaxis_rangeslider_visible=True,   # Show the bottom rangeslider
        hovermode='x unified'            # Combine hover labels if desired
        # No 'template', 'plot_bgcolor', or extra styling so we get the default look
    )
    
    st.plotly_chart(fig, use_container_width=True)

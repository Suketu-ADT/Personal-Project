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
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Open'],
        name='Stock Open',
        line=dict(color='blue', width=2),
        hovertemplate='<b>Date</b>: %{x}<br><b>Price</b>: $%{y:.2f}'
    ))
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        name='Stock Close',
        line=dict(color='red', width=2),
        hovertemplate='<b>Date</b>: %{x}<br><b>Price</b>: $%{y:.2f}'
    ))
    fig.layout.update(
        title=dict(
            text=f"{selected_stock} Stock Price Over Time",
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title='Date',
            gridcolor='lightgrey',
            showgrid=True,
            showline=True,
            linewidth=1,
            linecolor='lightgrey'
        ),
        yaxis=dict(
            title='Price (USD)',
            gridcolor='lightgrey',
            showgrid=True,
            showline=True,
            linewidth=1,
            linecolor='lightgrey',
            tickformat='$,.2f'
        ),
        xaxis_rangeslider_visible=True,
        template="plotly_white",
        hovermode='x unified',
        plot_bgcolor='aliceblue',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

plot_raw_data()

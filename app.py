import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")
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
    # Add candlestick
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick',
        increasing_line_width=2,
        decreasing_line_width=2,
        increasing_line_color='#26a69a',
        decreasing_line_color='#ef5350',
        hovertext=[f'Open: ${o:,.2f}<br>High: ${h:,.2f}<br>Low: ${l:,.2f}<br>Close: ${c:,.2f}' 
                  for o, h, l, c in zip(data['Open'], data['High'], data['Low'], data['Close'])]
    ))
    # Add closing price line
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        name='Closing Price',
        line=dict(color='red', width=1.5),
        hovertemplate='%{y:$.2f}'
    ))
    # Calculate y-axis range with padding
    y_min = data[['Low']].min().min() * 0.95
    y_max = data[['High']].max().max() * 1.05
    
    fig.update_layout(
        title=dict(
            text=f'{selected_stock} Share Price',
            x=0.5,
            xanchor='center',
            font=dict(size=24)
        ),
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=True,
        template='plotly_white',
        height=600,
        margin=dict(l=50, r=50, t=100, b=50, autoexpand=True),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)',
            tickformat='$,.2f',
            title_standoff=25,
            range=[y_min, y_max],
            automargin=True
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)',
            rangeslider=dict(visible=True, thickness=0.05),
            automargin=True
        ),
        hoverlabel=dict(
            bgcolor='rgba(0,0,0,0.8)',
            font_size=12
        )
    )
    st.plotly_chart(fig, use_container_width=True)

plot_raw_data()
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
    # Add candlestick
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick',
        increasing_line_width=2,
        decreasing_line_width=2,
        increasing_line_color='#26a69a',
        decreasing_line_color='#ef5350',
        hovertext=[f'Open: ${o:.2f}<br>High: ${h:.2f}<br>Low: ${l:.2f}<br>Close: ${c:.2f}' 
                  for o, h, l, c in zip(data['Open'], data['High'], data['Low'], data['Close'])]
    ))
    # Add closing price line
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        name='Closing Price',
        line=dict(color='red', width=1.5),
        hovertemplate='%{y:$.2f}'
    ))
    # Calculate y-axis range with padding
    y_min = data[['Low']].min().min() * 0.95
    y_max = data[['High']].max().max() * 1.05
    
    fig.update_layout(
        title=dict(
            text=f'{selected_stock} Share Price',
            x=0.5,
            xanchor='center',
            font=dict(size=24)
        ),
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=True,
        template='plotly_white',
        height=600,
        margin=dict(l=50, r=50, t=100, b=50, autoexpand=True),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)',
            tickformat='$,.2f',
            title_standoff=25,
            range=[y_min, y_max],
            automargin=True
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)',
            rangeslider=dict(visible=True, thickness=0.05),
            automargin=True
        ),
        hoverlabel=dict(
            bgcolor='rgba(0,0,0,0.8)',
            font_size=12
        )
    )
    st.plotly_chart(fig, use_container_width=True)

plot_raw_data()

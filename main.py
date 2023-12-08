import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather forecast for the next 5 days')

place = st.text_input('Place')
days = st.slider('Forecast days', min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select dada to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


# def get_data(days):
#     dates = ['2023-12-01', '2023-12-02', '2023-12-03']
#     temperatures = [10, 24, 16]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={'x': 'Days', 'y': 'Temperature'})
st.plotly_chart(figure)

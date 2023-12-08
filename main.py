import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather forecast for the next 5 days')

place = st.text_input('Place')
days = st.slider('Forecast days', min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select dada to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

try:
    if place:
        # Temp and sky data
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            days = [dict['dt_txt'] for dict in filtered_data]
            # Temp plot
            figure = px.line(x=days, y=temperatures, labels={'x': 'Days', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {'Clear': 'images/sun.png', 'Clouds': 'images/rain.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}

            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]

            # Sky images
            st.image(image_path, width=70)
except KeyError:
    st.error('Please enter correct city name')

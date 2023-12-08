import requests


APIkey = 'df69f6304cc4abcc200484e809eb62f8'


def get_data(city_name, forecast_days=None, kind=None):

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={APIkey}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    number_values = 8*forecast_days
    filtered_data = filtered_data[:number_values]

    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__=='__main__':
    print(get_data(city_name='Buford'))

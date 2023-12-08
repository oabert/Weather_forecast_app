import requests

APIkey = 'df69f6304cc4abcc200484e809eb62f8'


def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    number_values = 8 * forecast_days
    filtered_data = filtered_data[:number_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Buford'))

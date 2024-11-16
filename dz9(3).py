import requests
from bs4 import BeautifulSoup
import sqlite3

def get_weather_data():
    url = 'https://pogoda.meta.ua/ua/Ternopilska/Ternopilskyi/Ternopil/tomorrow/'

    response = requests.get(url)
    response.raise_for_status()


    soup = BeautifulSoup(response.text, 'html.parser')
    forecast_items = soup.find_all('div', class_='city__forecast-col')

    weather_data = []
    for item in forecast_items:
        time_element = item.find('div', class_='city__forecast-time')
        temp_element = item.find('span', class_='graph-data__value')

        if time_element and temp_element:
            time = time_element.text.strip()
            temp = temp_element.text.strip().replace('°', '')
            try:
                weather_data.append((time, float(temp)))  # Додаємо дані в список
            except ValueError:
                print(f"Помилка перетворення температури для часу {time}")
                continue

    print(f"Отримані дані: {weather_data}")
    return weather_data

def save_to_dataBase(weather_data):

    conn = sqlite3.connect('HM9.sl3')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    datetime TEXT,
                    temperature REAL  
                    )''')

    for time, temperature in weather_data:
        c.execute('INSERT INTO weather (datetime, temperature) VALUES (?, ?)', (time, temperature))

    conn.commit()
    conn.close()




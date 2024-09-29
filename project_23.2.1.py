import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_user_rates(user_login):
    page_num = 1
    data = []
    while True:
        url = (f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}/')
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        entries = soup.find_all('div', class_='item')

        if len(entries) == 0:  # Признак остановки
            break
        for entry in entries:
            div_film_name = entry.find('div', class_='nameRus')
            film_name = div_film_name.find('a').text
            vote = entry.find('div', class_='vote').text
            data.append({'film_name': film_name, 'vote': vote})

        page_num += 1  # Переходим на следующую страницу
    return data

user_rates = collect_user_rates(input("Введите данные пользователя: "))
print(len(user_rates))

df = pd.DataFrame(user_rates)
df.to_excel('user_rates1.xlsx')

def get_rated_films(user_rates):
    rated_films = []
    while True:
        for item in user_rates:
            vote = float(item['vote'])  # Преобразуем строку в число с плавающей точкой
            if vote >= 7:
                rated_films.append(item)
        return rated_films

user_rates = get_rated_films(user_rates)
print(len(user_rates))

df = pd.DataFrame(user_rates)
df.to_excel('user_rates2.xlsx')
import requests
from bs4 import BeautifulSoup as bs
import csv


r = requests.get("https://avtomir.ru/new-cars/")
html = bs(r.content, 'html.parser')

cars = html.find_all('div', class_='card')

with open("auto.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Год', 'Цена', 'Кузов'])
    for car in cars:
        name = car.find('a', 'card__name').text.strip()
        date = car.find('div', 'card__date').text.strip().split()[2]
        price = car.find('span', 'card__price-num').text.strip()
        text = car.find('div', 'card__text').text.strip().split()[1]
        writer.writerow([name, date, price, text])
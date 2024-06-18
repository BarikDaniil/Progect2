import requests
import pprint


URL = "https://fakestoreapi.com/carts"
user_ID_input = int(input("Введите свой userID: "))

response = requests.get(URL).json()

for items in response:
    if items['userId'] == user_ID_input:
        print("Продукты в корзине:", items['products'])
        print("ID корзины:", items['id'])
        break
else:
    print("Такого пользователя нет")
import requests
import pprint


URL = "https://fakestoreapi.com/products"
user_prod_input = input("Введите ваш продукт, который желаете посмотреть: ")
response = requests.get(URL).json()
pprint.pp(response)
one_var = False
for product in response:
    if product['category'] == user_prod_input:
        pprint.pprint(f"Информация о вашем продукте - {product}")
        one_var = True
if one_var == False:
    print("ТАкого продукта нет в каталоге!")


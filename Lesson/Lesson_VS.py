import requests
import pprint
#DJm1rxJ27VWw3ApEsoeU
#ID: 51948975
access_token = 'vk1.a.57WYDmRmgpH3ZlsoZzp4L1Vvg88YQOHR2oVYAr7xL4RTKui3Dp_ueK7Z2NEYnWo6c_3K7XUiyvf8Ug-3MQJSCEkozEEuID5FdnZg0LiE2YrsNDwh7lFZuVJRvcYBWgn_ExAjVXlFfzYF6c_aHBeoYKnNrEOqYauA1Zf3OGOhSx9Z76ZxWDs8afUZ8y1raO--'
user_input = input("Введите ID или Ник VK")
URL = 'https://api.vk.com/method/users.get'
params = {
    "users_ids": user_input,
    #"flields": "city, career",
    "access_token": access_token,
    "v": "5.131"
}
response = requests.get(URL, params=params)
users_info = response.json()["response"][0]
print(users_info)
print("Имя- ",{users_info["first_name"]})
print("Фамилия-", {users_info["last_name"]})
#print("Город-", {users_info["city"]["title"]})
#print("Карьера",- {users_info["career"]})
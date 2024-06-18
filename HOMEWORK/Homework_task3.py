import requests
import pprint


#DJm1rxJ27VWw3ApEsoeU
#ID: 51948975
access_token = 'vk1.a.cDLhgp-jPBdDxGzTRCmHOaKm5W7LkX7ZZcHCL1zGNCQs6-hCma4kWYpaK0C8q9tMgiOGHL0_I2-i3l9pQ_hiqgnW1EZtLFnp1UpzVRJIOGuFJEeJm8XhEKr68ZMdl_wdbbBWXMPH88ctXH5p2w-Sb4Gbw4FgNXakhPXscBvL6zYinMGWgnjuFVkwz1z8FHsA'
user_input = input("Введите ID или Ник VK")
URL = 'https://api.vk.com/method/friends.get'
params = {
    "users_ids": user_input,
    "access_token": access_token,
    'fields': 'status', 
    'fields':'online',
    "v": "5.131"

}
response = requests.get(URL, params=params)
user_info = response.json()["response"]

for item in user_info:
    if item == user_info['count']:
        print("Кол-во", user_info['count'])
    else:
        for user in user_info['items']:
            print("Имя -", user['first_name'])
            print("Фамилия -", user['last_name'])
            print("ID-", user['id'])
            print("online -", user['online'])
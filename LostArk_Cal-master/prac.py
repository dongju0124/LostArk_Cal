import requests
import json
from lostark_api_token import Token

headers = {
    'accept': 'application/json',
    'authorization': Token,
    'Content-Type': 'application/json',
}

data = {
    "CategoryCode": 50010
}

url = 'https://developer-lostark.game.onstove.com/markets/items'
response = requests.post(url, headers=headers, json=data)

jsonObject = response.json()

print(jsonObject)

#90200 채집
#90300 벌목
#90400 채광
#90500 수렵
#90600 낚시
#90700 고고학
#{'Code': 60200, 'CodeName': '배틀 아이템 -회복형'},
# {'Code': 60300, 'CodeName': '배틀 아이템 -공격형'},
# {'Code': 60400, 'CodeName': '배틀 아이템 -기능성'},
# {'Code': 60500, 'CodeName': '배틀 아이템 -버프형'}],
# 'Code': 60000, 'CodeName': '전투 용품'},
# {'Subs': [], 'Code': 70000, 'CodeName': '요리'}
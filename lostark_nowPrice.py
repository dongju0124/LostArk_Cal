import requests
import json
from lostark_api_token import Token

headers = {
    'accept': 'application/json',
    'authorization': Token,
    'Content-Type': 'application/json',
}

data = {
    "CategoryCode": 90700
}

url = 'https://developer-lostark.game.onstove.com/markets/items'
response = requests.post(url, headers=headers, json=data)

jsonObject = response.json()

# 정보를 저장할 파일명
output_file = 'item_info.json'

print(response)
count = 0  # 출력할 아이템 개수를 정하는 변수
items_info = []  # 정보를 저장할 리스트
for item in jsonObject['Items']:
    item_info = {
        'Name': item['Name'],
        'Id': item['Id'],
        'RecentPrice': item['RecentPrice'],
        'BundleCount': item['BundleCount'],  # BundleCount 추가
        'AvgPrice': None,  # 일단 None으로 초기화
    }
    items_info.append(item_info)

    print(f"{item_info['Name']} : {item_info['Id']} 현재 금액:{item_info['RecentPrice']} BundleCount: {item_info['BundleCount']}")
    count += 1
    if count == 3:  # 출력할 아이템 개수를 3으로 설정
        break

# 특정 아이템 ID 리스트
item_ids = [6861011]

# 각 아이템 ID에 대한 정보 요청 및 출력
for item_id in item_ids:
    url = f'https://developer-lostark.game.onstove.com/markets/items/{item_id}'
    response = requests.get(url, headers=headers)
    jsonObject = response.json()

    # 해당 아이템에 대한 정보 출력
    for item in jsonObject:
        print(f"{item['Name']} : {item_id} 평균 금액: {item['Stats'][0]['AvgPrice']} BundleCount: {item['BundleCount']}")
        # items_info에 정보 추가
        found = False
        for info in items_info:
            if info['Id'] == item_id:
                info['AvgPrice'] = item['Stats'][0]['AvgPrice']
                info['BundleCount'] = item['BundleCount']  # BundleCount 추가
                found = True
                break
        if not found:
            # items_info에 해당 아이템이 없으면 추가
            item_info = {
                'Name': item['Name'],
                'Id': item_id,
                'RecentPrice': None,  # 아이템 목록에 없는 경우 RecentPrice는 None으로 남김
                'AvgPrice': item['Stats'][0]['AvgPrice'],
                'BundleCount': item['BundleCount'],  # BundleCount 추가
            }
            items_info.append(item_info)

# 정보를 파일에 저장
with open(output_file, 'w') as file:
    json.dump(items_info, file)

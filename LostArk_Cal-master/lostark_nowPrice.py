import requests
import json
from lostark_api_token import Token

headers = {
    'accept': 'application/json',
    'authorization': Token,
    'Content-Type': 'application/json',
}

# 채집, 벌목, 채광, 수렵, 낚시, 고고학에 해당하는 카테고리 코드들
category_codes = [90200, 90300, 90400, 90500, 90600, 90700]

items_info = {}  # 모든 정보를 저장할 딕셔너리

# 각 카테고리 코드에 대해 순회하며 요청
for category_code in category_codes:
    data = {
        "CategoryCode": category_code
    }

    url = 'https://developer-lostark.game.onstove.com/markets/items'
    response = requests.post(url, headers=headers, json=data)

    jsonObject = response.json()

    print(f"Response for category code {category_code}: {response}")

    for item in jsonObject['Items']:
        item_info = {
            'Name': item['Name'],
            'RecentPrice': item['RecentPrice'],
            'BundleCount': item['BundleCount'],  # BundleCount 추가
            'AvgPrice': None,  # 일단 None으로 초기화
        }
        items_info[item['Id']] = item_info  # Id를 키로 사용하여 저장

        print(f"{item_info['Name']} : {item['Id']} 현재 금액: {item_info['RecentPrice']} BundleCount: {item_info['BundleCount']}")

# 특정 아이템 ID 리스트
item_ids = [6861008, 6861009, 6861011, 6861012]

# 각 아이템 ID에 대한 정보 요청 및 출력
for item_id in item_ids:
    url = f'https://developer-lostark.game.onstove.com/markets/items/{item_id}'
    response = requests.get(url, headers=headers)
    jsonObject = response.json()

    # 해당 아이템에 대한 정보 출력 및 업데이트
    for item in jsonObject:
        print(f"{item['Name']} : {item_id} 평균 금액: {item['Stats'][0]['AvgPrice']} BundleCount: {item['BundleCount']}")

        if item_id in items_info:
            items_info[item_id]['AvgPrice'] = item['Stats'][0]['AvgPrice']
            items_info[item_id]['BundleCount'] = item['BundleCount']  # BundleCount 업데이트
        else:
            # items_info에 해당 아이템이 없으면 추가
            item_info = {
                'Name': item['Name'],
                'RecentPrice': None,  # 아이템 목록에 없는 경우 RecentPrice는 None으로 남김
                'AvgPrice': item['Stats'][0]['AvgPrice'],
                'BundleCount': item['BundleCount'],  # BundleCount 추가
            }
            items_info[item_id] = item_info

# 정보를 저장할 파일명
output_file = 'nowPrice.json'

# 모든 정보를 파일에 저장
with open(output_file, 'w') as file:
    json.dump(items_info, file, ensure_ascii=False, indent=4)

print(f"JSON 데이터가 '{output_file}' 파일에 저장되었습니다.")

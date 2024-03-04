import json
import subprocess


# 저장된 정보를 불러오기
output_file = 'item_info.json'
with open(output_file, 'r') as file:
    items_info = json.load(file)

# Each_Price를 저장할 리스트
each_prices = []

# 불러온 정보 출력 및 Each_Price에 추가
for item_info in items_info:
    print(f"Name: {item_info['Name']}")
    print(f"Id: {item_info['Id']}")
    print(f"RecentPrice: {item_info.get('RecentPrice', None)}")
    print(f"AvgPrice: {item_info.get('AvgPrice', None)}")
    print(f"BundleCount: {item_info.get('BundleCount', None)}")
    print()

    # 각각의 Price/BundleCount의 값을 Each_Price에 추가
    each_price = {
        'Name': item_info['Name'],
        'Id': item_info['Id'],
        'Each_Price': (
            item_info['RecentPrice'] / item_info['BundleCount']
            if item_info['RecentPrice'] is not None and item_info['BundleCount'] is not None
            else item_info['AvgPrice'] / item_info['BundleCount']
            if item_info['AvgPrice'] is not None and item_info['BundleCount'] is not None
            else None
        ),
    }
    each_prices.append(each_price)

# Each_Price 출력
for each_price in each_prices:
    print(f"Name: {each_price['Name']}")
    print(f"Id: {each_price['Id']}")
    print(f"Each_Price: {each_price['Each_Price']}")
    print()

# Each_Price를 파일에 저장
output_each_price_file = 'each_price_info.json'
with open(output_each_price_file, 'w') as each_price_file:
    json.dump(each_prices, each_price_file)

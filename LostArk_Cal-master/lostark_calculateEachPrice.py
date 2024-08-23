import json

# 저장된 정보를 불러오기
output_file = 'nowPrice.json'
with open(output_file, 'r') as file:
    items_info = json.load(file)

# Each_Price를 저장할 딕셔너리 (Id를 키로 사용)
each_prices = {}

# 불러온 정보 출력 및 Each_Price에 추가
for item_id, item_info in items_info.items():  # 딕셔너리의 키와 값을 각각 item_id, item_info로 받음
    print(f"Name: {item_info['Name']}")
    print(f"Id: {item_id}")
    print(f"RecentPrice: {item_info.get('RecentPrice', None)}")
    print(f"AvgPrice: {item_info.get('AvgPrice', None)}")
    print(f"BundleCount: {item_info.get('BundleCount', None)}")
    print()

    # 각각의 Price/BundleCount의 값을 Each_Price에 추가
    each_price = {
        'Name': item_info['Name'],
        'Each_Price': (
            item_info['RecentPrice'] / item_info['BundleCount']
            if item_info['RecentPrice'] is not None and item_info['BundleCount'] is not None
            else item_info['AvgPrice'] / item_info['BundleCount']
            if item_info['AvgPrice'] is not None and item_info['BundleCount'] is not None
            else None
        ),
    }
    each_prices[int(item_id)] = each_price  # Id를 키로 사용하여 딕셔너리에 추가

# Each_Price 출력
for item_id, each_price in each_prices.items():
    print(f"Id: {item_id}")
    print(f"Name: {each_price['Name']}")
    print(f"Each_Price: {each_price['Each_Price']}")
    print()

# Each_Price를 파일에 저장
output_each_price_file = 'each_price_info.json'
with open(output_each_price_file, 'w') as each_price_file:
    json.dump(each_prices, each_price_file, ensure_ascii=False, indent=4)

print(f"Each_Price 데이터가 '{output_each_price_file}' 파일에 저장되었습니다.")

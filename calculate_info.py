import json
import math
import subprocess
import os

# lostark_nowPrice.py 실행
subprocess.run(["python", "lostark_nowPrice.py"])

# lostark_calculate.py 실행
subprocess.run(["python", "lostark_calculate.py"])

n = input('수수료 감소')

# Each_Price 정보를 불러오기
output_each_price_file = 'each_price_info.json'
with open(output_each_price_file, 'r') as each_price_file:
    each_prices = json.load(each_price_file)

def calculate_and_compare(items_info):
    for item_info in items_info:
        print(f"Name: {item_info['Name']}")
        print(f"Id: {item_info['Id']}")
        print(f"Each_Price: {item_info['Each_Price']}")
        print()

    # 비교할 가격 계산
    compare_price = (
        items_info[0]['Each_Price'] * 107
        + items_info[1]['Each_Price'] * 51
        + items_info[2]['Each_Price'] * 52
        + 300 * ((100-int(n))/100)
    )

    # 최상급 융화재료의 초기 가격 계산 (내림해서 양의 정수로)
    top_grade_material_price = math.floor(items_info[3]['Each_Price']) * 15 * 0.95

    # 결과 출력
    if top_grade_material_price > compare_price:
        print(f"제작 비용은 {compare_price}, 총 판매 비용은 {top_grade_material_price}")
        print(f"최상급 융화재료의 가격이 {math.floor(items_info[3]['Each_Price'])}로 이득입니다.")
    else:
        # 최상급 융화재료의 가격이 언제 더 큰지 출력
        while top_grade_material_price <= compare_price:
            items_info[3]['Each_Price'] = math.floor(items_info[3]['Each_Price']) +1
            top_grade_material_price = math.floor(items_info[3]['Each_Price']) * 15 * 0.95
        print(f"제작 비용은 {compare_price}, 총 판매 비용은 {top_grade_material_price}")
        print(f"최상급 융화재료의 가격이 {items_info[3]['Each_Price']} 골드일 때 이득입니다.")

# Each_Price 정보를 불러오기
output_each_price_file = 'each_price_info.json'
with open(output_each_price_file, 'r') as each_price_file:
    each_prices = json.load(each_price_file)

# 계산 및 비교 함수 호출
calculate_and_compare(each_prices)

os.system("pause")

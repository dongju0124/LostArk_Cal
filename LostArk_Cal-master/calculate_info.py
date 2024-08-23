import json
import math
import subprocess
import os

# lostark_nowPrice.py 실행
subprocess.run(["python", "lostark_nowPrice.py"])

# lostark_calculateEachPrice.py 실행
subprocess.run(["python", "lostark_calculateEachPrice.py"])

n = input('수수료 감소: ')

# Each_Price 정보를 불러오기
output_each_price_file = 'each_price_info.json'
with open(output_each_price_file, 'r') as each_price_file:
    each_prices = json.load(each_price_file)

def calculate_and_compare(items_info):
    results = []

    def add_result(category, price, total, gap, item_price):
        results.append({
            'Category': category,
            'ProductionCost': price,
            'TotalSales': total,
            'Gap': gap,
            'ItemPrice': item_price
        })

    # 필요한 아이템의 ID 값을 설정
    archId_0 = "6882701"  # 고대유물
    archId_1 = "6882704"  # 희귀한 유물
    archId_2 = "6885705"  # 진귀한 유물
    archId_3 = "6885709"  # 아비도스 유물
    archId_4 = "6885708"  # 오레하 유물
    archId_5 = "6882708"  # 고고학의 결정

    herbId_0 = "6882101" # 들꽃
    herbId_1 = "6882104" # 수줍은 들꽃
    herbId_2 = "6882107" # 화사한 들꽃
    herbId_3 = "6882109" # 아비도스 들꽃

    lumbId_0 = "6882301" # 목재
    lumbId_1 = "6882304" # 부드러운 목재
    lumbId_2 = "6884307" # 튼튼한 목재
    lumbId_3 = "6884308" # 아비도스 목재

    mineId_0 = "6882401" # 철광석
    mineId_1 = "6882404" # 묵직한 철광석
    mineId_2 = "6884407" # 단단한 철광석
    mineId_3 = "6884408" # 아비도스 철광석

    huntId_0 = "6882501" # 두툼한 생고기
    huntId_1 = "6882504" # 다듬은 생고기
    huntId_2 = "6885505" # 진귀한 가죽
    huntId_3 = "6885508" # 오레하 두툼한 생고기
    huntId_4 = "6885509" # 아비도스 두툼한 생고기

    fishId_0 = "6882601" # 생선
    fishId_1 = "6882604" # 붉은 살 생선
    fishId_2 = "6885608" # 오레하 태양 잉어
    fishId_3 = "6885609" # 아비도스 태양 잉어
    fishId_4 = "6882608" # 낚시의 결정


    id_low = "6861008"  # 오레하
    id_mid = "6861009"  # 상레하
    id_high = "6861011"  # 최상레하
    id_t4 = "6861012" # 아비도스

    for item_id, item_info in items_info.items():
        print(f"Name: {item_info['Name']}")
        print(f"Id: {item_id}")
        print(f"Each_Price: {item_info['Each_Price']}")
        print()


    # 비교할 가격 계산 오레하
    archLowPrice = (
        items_info[archId_0]['Each_Price'] * 64
        + items_info[archId_1]['Each_Price'] * 26
        + items_info[archId_4]['Each_Price'] * 8
        + 205 * ((100 - int(n)) / 100)
    )

    # 오레하 융화재료의 초기 가격 계산 (내림 적용)
    archLow = math.floor(items_info[id_low]['Each_Price']) * 30 * 0.95
    archLowGap = archLow - archLowPrice
    add_result('오레하 (고고학)', archLowPrice, archLow, archLowGap, math.floor(items_info[id_low]['Each_Price']))

    # 비교할 가격 계산 상급 오레하
    archmidPrice = (
        items_info[archId_0]['Each_Price'] * 94
        + items_info[archId_1]['Each_Price'] * 29
        + items_info[archId_4]['Each_Price'] * 16
        + 250 * ((100 - int(n)) / 100)
    )

    # 상급 오레하 융화재료의 초기 가격 계산 (내림 적용)
    archMid = math.floor(items_info[id_mid]['Each_Price']) * 20 * 0.95
    archMidGap = archMid - archmidPrice
    add_result('상급 오레하 (고고학)', archmidPrice, archMid, archMidGap, math.floor(items_info[id_mid]['Each_Price']))

    # 비교할 가격 계산 최상레하
    archHighPrice = (
        items_info[archId_0]['Each_Price'] * 107
        + items_info[archId_1]['Each_Price'] * 51
        + items_info[archId_4]['Each_Price'] * 52
        + 300 * ((100 - int(n)) / 100)
    )

    # 최상급 융화재료의 초기 가격 계산 (내림 적용)
    archHigh = math.floor(items_info[id_high]['Each_Price']) * 15 * 0.95
    archHighGap = archHigh - archHighPrice
    add_result('최상급 오레하 (고고학)', archHighPrice, archHigh, archHighGap, math.floor(items_info[id_high]['Each_Price']))


    # 비교할 가격 계산 아비도스
    archT4Price = (
        items_info[archId_0]['Each_Price'] * 86
        + items_info[archId_1]['Each_Price'] * 45
        + items_info[archId_3]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    archT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    archT4Gap = archT4 - archT4Price
    add_result('아비도스 (고고학)', archT4Price, archT4, archT4Gap, math.floor(items_info[id_t4]['Each_Price']))

    # 비교할 가격 계산 오레하
    fishLowPrice = (
        items_info[fishId_0]['Each_Price'] * 80
        + items_info[fishId_1]['Each_Price'] * 40
        + items_info[fishId_2]['Each_Price'] * 10
        + 205 * ((100 - int(n)) / 100)
    )

    # 오레하 융화재료의 초기 가격 계산 (내림 적용)
    fishLow = math.floor(items_info[id_low]['Each_Price']) * 30 * 0.95
    fishLowGap = fishLow - fishLowPrice
    add_result('오레하 (낚시)', fishLowPrice, fishLow, fishLowGap, math.floor(items_info[id_low]['Each_Price']))

    # 비교할 가격 계산 상급 오레하
    fishMidPrice = (
        items_info[fishId_0]['Each_Price'] * 128
        + items_info[fishId_1]['Each_Price'] * 64
        + items_info[fishId_2]['Each_Price'] * 16
        + 250 * ((100 - int(n)) / 100)
    )

    # 상급 오레하 융화재료의 초기 가격 계산 (내림 적용)
    fishMid = math.floor(items_info[id_mid]['Each_Price']) * 20 * 0.95
    fishMidGap = fishMid - fishMidPrice
    add_result('상급 오레하 (낚시)', fishMidPrice, fishMid, fishMidGap, math.floor(items_info[id_mid]['Each_Price']))

    # 비교할 가격 계산 최상레하
    fishHighPrice = (
        items_info[fishId_0]['Each_Price'] * 142
        + items_info[fishId_1]['Each_Price'] * 69
        + items_info[fishId_2]['Each_Price'] * 52
        + 300 * ((100 - int(n)) / 100)
    )

    # 최상급 융화재료의 초기 가격 계산 (내림 적용)
    fishHigh = math.floor(items_info[id_high]['Each_Price']) * 15 * 0.95
    fishHighGap = fishHigh - fishHighPrice
    add_result('최상급 오레하 (낚시)', fishHighPrice, fishHigh, fishHighGap, math.floor(items_info[id_high]['Each_Price']))


    # 비교할 가격 계산 아비도스
    fishT4Price = (
        items_info[fishId_0]['Each_Price'] * 86
        + items_info[fishId_1]['Each_Price'] * 45
        + items_info[fishId_3]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    fishT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    fishT4Gap = fishT4 - fishT4Price
    add_result('아비도스 (낚시)', fishT4Price, fishT4, fishT4Gap, math.floor(items_info[id_t4]['Each_Price']))

    #
    # 수렵
    #

    # 비교할 가격 계산 오레하
    huntLowPrice = (
        items_info[huntId_0]['Each_Price'] * 80
        + items_info[huntId_1]['Each_Price'] * 40
        + items_info[huntId_3]['Each_Price'] * 10
        + 205 * ((100 - int(n)) / 100)
    )

    # 오레하 융화재료의 초기 가격 계산 (내림 적용)
    huntLow = math.floor(items_info[id_low]['Each_Price']) * 30 * 0.95
    huntLowGap = huntLow - huntLowPrice
    add_result('오레하 (수렵)', huntLowPrice, huntLow, huntLowGap, math.floor(items_info[id_low]['Each_Price']))

    # 비교할 가격 계산 상급 오레하
    huntMidPrice = (
        items_info[huntId_0]['Each_Price'] * 128
        + items_info[huntId_1]['Each_Price'] * 64
        + items_info[huntId_3]['Each_Price'] * 16
        + 250 * ((100 - int(n)) / 100)
    )

    # 상급 오레하 융화재료의 초기 가격 계산 (내림 적용)
    huntMid = math.floor(items_info[id_mid]['Each_Price']) * 20 * 0.95
    huntMidGap = huntMid - huntMidPrice
    add_result('상급 오레하 (수렵)', huntMidPrice, huntMid, huntMidGap, math.floor(items_info[id_mid]['Each_Price']))

    # 비교할 가격 계산 최상레하
    huntHighPrice = (
        items_info[huntId_0]['Each_Price'] * 142
        + items_info[huntId_1]['Each_Price'] * 69
        + items_info[huntId_3]['Each_Price'] * 52
        + 300 * ((100 - int(n)) / 100)
    )

    # 최상급 융화재료의 초기 가격 계산 (내림 적용)
    huntHigh = math.floor(items_info[id_high]['Each_Price']) * 15 * 0.95
    huntHighGap = huntHigh - huntHighPrice
    add_result('최상급 오레하 (수렵)', huntHighPrice, huntHigh, huntHighGap, math.floor(items_info[id_high]['Each_Price']))


    # 비교할 가격 계산 아비도스
    huntT4Price = (
        items_info[huntId_0]['Each_Price'] * 86
        + items_info[huntId_1]['Each_Price'] * 45
        + items_info[huntId_4]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    huntT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    huntT4Gap = huntT4 - huntT4Price
    add_result('아비도스 (수렵)', huntT4Price, huntT4, huntT4Gap, math.floor(items_info[id_t4]['Each_Price']))

    #
    # 채집
    #

    #비교할 가격 계산 아비도스
    herbT4Price = (
        items_info[herbId_0]['Each_Price'] * 86
        + items_info[herbId_1]['Each_Price'] * 45
        + items_info[herbId_3]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    herbT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    herbT4Gap = herbT4 - herbT4Price
    add_result('아비도스 (채집)', herbT4Price, herbT4, herbT4Gap, math.floor(items_info[id_t4]['Each_Price']))

    #
    #벌목
    #

    #비교할 가격 계산 아비도스
    lumbT4Price = (
        items_info[lumbId_0]['Each_Price'] * 86
        + items_info[lumbId_1]['Each_Price'] * 45
        + items_info[lumbId_3]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    lumbT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    lumbT4Gap = lumbT4 - lumbT4Price
    add_result('아비도스 (벌목)', lumbT4Price, lumbT4, lumbT4Gap, math.floor(items_info[id_t4]['Each_Price']))

    #
    #채광
    #
    #비교할 가격 계산 아비도스
    mineT4Price = (
        items_info[mineId_0]['Each_Price'] * 86
        + items_info[mineId_1]['Each_Price'] * 45
        + items_info[mineId_3]['Each_Price'] * 33
        + 400 * ((100 - int(n)) / 100)
    )

    # 아비도스 융화재료의 초기 가격 계산 (내림 적용)
    mineT4 = math.floor(items_info[id_t4]['Each_Price']) * 10 * 0.95
    mineT4Gap = mineT4 - mineT4Price
    add_result('아비도스 (채광)', mineT4Price, mineT4, mineT4Gap, math.floor(items_info[id_t4]['Each_Price']))


# Gap 값 기준으로 내림차순 정렬
    sorted_results = sorted(results, key=lambda x: x['Gap'], reverse=True)

    # 결과 출력
    for result in sorted_results:
        if result['Gap'] > 0:
            print(f"{result['ItemPrice']} 골드로 판매 시 {result['Category']} 융화재료 묶음 당 {result['Gap']:.2f} 골드 이득.")
        else:
            print(f"{result['ItemPrice']} 골드로 판매 시 {result['Category']} 융화재료 묶음 당 {result['Gap']:.2f} 골드 손해.")

# 계산 및 비교 함수 호출
calculate_and_compare(each_prices)

os.system("pause")

price_list = []

while True:
    try:
        if len(price_list) < 5:
            enter_price = int(input("가격을 입력하세요: "))
            if enter_price < 100 or 2000 < enter_price:
                print("범위 내의 가격을 입력하세요")
                continue
            else:
                price_list.append(enter_price)
        else:
            break
    except ValueError:
        print("가격은 숫자로 입력하세요")

result = min([i + j - 50 for i in price_list[0:3] for j in price_list[3:]])
print("가장 싼 세트의 가격: ", result)
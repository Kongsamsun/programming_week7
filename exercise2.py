num_list = []
result_list = []

while True:
    try:
        if len(num_list) < 10:
            enter_num = int(input("숫자 입력: "))
            if enter_num < 0 or 2000 < enter_num:
                print("범위 내의 값을 입력하세요")
                continue
            else:
                num_list.append(enter_num)
        else:
            break
    except:
        print("숫자로 입력하세요")
        continue

distribute = [n % 42 for n in num_list]
for d in distribute:
    if d not in result_list:
        result_list.append(d)
    else:
        pass
print("서로 다른 나머지의 개수: ", len(result_list))
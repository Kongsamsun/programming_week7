while True:
    enter_str = input("문자열들을 입력하세요: ")
    split_list = enter_str.split()
    result_list =[]
    if enter_str == 'done':
        print("프로그램 종료")
        break
    elif len(split_list) < 1:
        print("최소 한 개 이상의 문자열을 입력하세요")
        continue
    else:
        for s in split_list:
            if len(s) < 5:
                pass
            else:
                result_list.append(s)

        result = [i[::-1] for i in result_list]
        print(result)
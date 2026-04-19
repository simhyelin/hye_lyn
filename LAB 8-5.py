a = [1, 2, 3, 4, 5]
try:
    user_input = input("a의 요소를 하나 선택하시오 : ")
    idx_val = int(user_input)
        search_idx = a.index(idx_val)
    ordinals = ['첫', '두', '세', '네', '다섯']
    print("{} 은(는) {} 번째 요소입니다.".format(idx_val, ordinals[search_idx]))
except ValueError:
    print("오류 : 입력 값이 정수나 실수가 아님")
except Exception as e:
    print("오류가 발생했습니다:", e)

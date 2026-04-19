try:
    res = 10 * (30 / 0)
except ZeroDivisionError:
    print("에러: 0으로 나눌 수 없습니다.")

try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print("에러: 입력 값이 정수가 아니다다.")

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print("에러: 'myfile.txt' 파일을 찾을 수 없습니다.")

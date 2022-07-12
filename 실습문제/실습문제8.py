# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.(max() 함수 사용 금지)

from tkinter import N


numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

# 1. wjscp tntwkfmf qksqhr
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n :
        #최댓값이었던 것이 두번째로 큰 수
        second_number = max_number
        max_number = n 

print(second_number)
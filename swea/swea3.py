# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

import sys

sys.stdin = open("input.txt")

a = int(input())

for t in range(1, a+1):
    number=list(map(int,input().split()))
    num_sum = 0
    for z in number:
        num_sum+=z

    result = round(num_sum/10)

    print('#{} {}'.format(t, result))

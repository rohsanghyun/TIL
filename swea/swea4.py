# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

import sys

sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t+1):
    numbers = list(map(int,input().split()))
    if numbers[0] > numbers[1]:
        result = '>'
    if numbers[0] == numbers[1]:
        result = '='
    if numbers[0] < numbers[1]:
        result = '<'

    print('#{} {}'.format(i, result))

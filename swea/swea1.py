# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.


import sys

sys.stdin = open("input.txt", "r")

number = int(input())

for t in range(1, number+1):
    a, b = map(int, input().split())

    print('#{}{}{}'.format(t, a//b, a%b))
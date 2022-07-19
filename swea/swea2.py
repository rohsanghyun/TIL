# 주어진 숫자부터 0까지 순서대로 찍어보세요

import sys

sys.stdin = open("input.txt")

i = int(input())

for t in range(i, -1, -1):
    print(t, end='')
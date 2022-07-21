# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

import sys

sys.stdin = open("input.txt")

t = input()

for i in range(0, len(t)):

    print(ord(t[i])-64, end=' ')
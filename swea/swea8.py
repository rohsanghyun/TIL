# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


import sys

sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t+1):
    n = int(input())

    total = 1
    for j in range(2, n+1):
        if j % 2:
            total += i
        else :
            total -+ i

print(f'#{i} {total}')

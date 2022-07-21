# 종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open("input.txt")

# A : w * P 
# B : 
#  R이하 : Q
#  R초과 : Q + S*(W-R)

t = input()
for test_case in range(1, t+1):
    P, Q, R, S, W = (int, input().split())
    print(P, Q, R, S, W)
    # PRINT(P, Q, R, S, W)
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q +S*(W-R)
        print(f'#{test_case} {min(A, B)}')
# 입력으로 1개의 정수 N 이 주어진다.

# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

t = int(input())

for i in range(1, t+1):
    if t%i == 0:
        print(i, end='')
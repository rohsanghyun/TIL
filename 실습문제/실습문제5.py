# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
numbers = [3, 10, 20]

# 값 초기화
result = 0 
coumt = 0

# 반복
for number in numbers :
    result = result + number
    # result += number
    count = coumt + 1
    # count += 1

print(result/coumt)
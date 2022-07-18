# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1
#파이썬은 위에서 아래로 내려오면서 읽어간다. 설명하기 애매하다 공백 정렬..
print(total / count)
#나누기 연산 후 소수점 뺴는것이 아닌 그냥 나누기.

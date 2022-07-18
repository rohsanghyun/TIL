# 문제 19. 숫자의 길이 구하기


number = 123456

# 2. 123
result = 0
# 몫이 0이 되면 종료 해야하니까!
# int : 0이 아닌 다른 수면 무조건 True! 
while number != 0:
    # number = number // 10
    number //= 10
    result += 1

print(result)

# 1. 문자열로 형변환
# print(len(str(number)))

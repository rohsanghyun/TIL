# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 튜플은 데이터를 변경할수 없기에 리스트를 사용하였다.
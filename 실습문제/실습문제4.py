# 1
n = int(input())
num = 1
x = 1
while x <= n:
    num *= x
    x += 1
print(num)

# 2
n = int(input())
x = 1
for i in range(1,n+1) :
    x *= i
print(x)
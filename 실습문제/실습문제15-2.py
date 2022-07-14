#추가문제

word = input()
count = 0

for i in range(len(word)):
    if word[i] == 'a':
        count = i
        break

print(count)

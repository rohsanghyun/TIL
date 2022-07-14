word = input()
count = -1

for i in range(len(word)):
    if word[i] == 'a':
        count = i
        break

print(count)

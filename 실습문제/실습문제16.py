word = input()
vowel = ""

for s in word:
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        vowel += s

print(len(vowel))
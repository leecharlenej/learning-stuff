S = input()

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
answer = ''

for i in S:
    if i.lower() in vowels:
        answer = answer + i

print(answer)
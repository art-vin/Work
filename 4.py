text = input().split()
result = ''
for i in text:
    total = 0
    for j in range(len(i)):
        if i[j].isalpha() == True:
            total += 1
    for l in i:
        if l.isalpha() == True and l.islower() == True:
            result += chr((ord(l) - 97 + total) % 26 + 97)
        elif l.isalpha() == True and l.isupper() == True:
            result += chr((ord(l) - 65 + total) % 26 + 65)
        else:
            result += l
    result += ' '
result = result.rstrip(' ')
print(result)
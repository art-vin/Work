with open("2.txt", 'r', encoding='utf-8') as f:
    text = [
        line.split()
        for line in f.readlines()
    ]
new_text = []
for line in text:
    new_line = []
    for word in line:
        if 'дождь' in word.lower():
            new_line.append(word.upper())
        else:
            new_line.append(word)
        new_text.append(' '.join(new_line))
print('\n'.join(new_text))
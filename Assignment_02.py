words = []

with open('romeo.txt', 'r') as f:
    for line in f:
        for word in line.strip().split(' '):
            if word and word not in words:
                words.append(word)

words = sorted(words, key=lambda s: s.casefold())
print(words)
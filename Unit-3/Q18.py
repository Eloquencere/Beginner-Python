file = open("words.txt", "r")
wordfreq = {}
for i in (file.read()).split():
    if i in wordfreq:
        wordfreq[i] += 1
    else:
        wordfreq[i] = 1
print(wordfreq)
file.close()

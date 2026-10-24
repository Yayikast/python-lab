"""Find the most and least frequent words in a sentence, ignoring punctuation and case."""

words = {}

x = input("Input: ").split()

for i in x:
    wrd = ""
    for j in i:
        if j.isalpha():
            wrd += j.lower()
    if wrd in words:
        words[wrd] += 1
    elif wrd != "":
        words[wrd] = 1

if len(words) == 0:
    print("No input!")
else:
    awords = dict(sorted(words.items(), key=lambda item: item[1]))
    lst = list(awords.keys())
    lstmax = []
    lstmin = []

    for i in range(len(lst)-1, -1, -1):
        if awords[lst[i]] == awords[lst[-1]]:
            lstmax.append(lst[i])
        else:
            break
        
    for i in range(len(lst)):
        if awords[lst[i]] == awords[lst[0]]:
            lstmin.append(lst[i])
        else:
            break
        
    lstmax.sort()
    lstmin.sort()
    
    print("Most Frequent Words: " + ", ".join(lstmax))
    print("Least Frequent Words: " + ", ".join(lstmin))

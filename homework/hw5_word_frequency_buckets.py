"""Count word frequencies across lines of text and group words by how often they appear."""

char = {}
x = ""
fst = 0
sec = 0
trd = 0

while [y.upper() for y in x] != ["END"]:
    x = input("Enter a line (or 'END' to finish): ").split()
    for word in x:
        word = word.strip(".").strip(",").upper()
        if len(x) == 1 and word == "END":
            break
        if word in char:
            char[word] += 1
        else:
            char[word] = 1

for key, num in char.items():
    if 1 <= num <= 2:
        fst += 1
    elif 3 <= num <= 4:
        sec += 1
    elif 4 < num:
        trd += 1
print("1. Number of words that appear once or twice:", fst)
print("2. Number of words that appear three and four times:", sec)
print("3. Number of words that appear more than four times:", trd)

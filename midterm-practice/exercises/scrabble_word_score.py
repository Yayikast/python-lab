"""Score a word using Scrabble letter values."""

word = input("Input a word: ")
score = 0
if word.isalpha():
    for char in word:
        if char.upper() in "QZ":
            score = score + 10
        elif char.upper() in "JX":
            score = score + 8
        elif char.upper() == "K":
            score = score + 5
        elif char.upper() in "FHVWY":
            score = score + 4
        elif char.upper() in "BCMP":
            score = score + 3
        elif char.upper() in "DG":
            score = score + 2
        else:
            score = score + 1
    print("Output:", score)
else:
    print("Invalid input")

"""Extract the consonants from a string and print them sorted."""

x = input("Input a string: ")
s = []
for i in x:
    if i.isalpha():
        if i.lower() not in "aeiou":
            s.append(i.lower())
s.sort()
print("".join(s))

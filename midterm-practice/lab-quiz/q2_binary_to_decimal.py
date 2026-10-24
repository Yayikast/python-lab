"""Convert a binary string to decimal, skipping and reporting non-binary symbols."""

seq = input("Input: binary = ")
v = 0
n = -1
flip_seq =""
alpha_seq = ""

for char in seq:
    if char in "01":
        flip_seq = char + flip_seq
    else:
        alpha_seq = alpha_seq + char

for char in flip_seq:
    n = n + 1
    v = v + ((2**n)*int(char))

for char in alpha_seq:
    print("Output: Ignore symbol", char)
    
print("Output:", v)

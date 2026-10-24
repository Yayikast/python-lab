"""Print an N x N upper-triangular grid filled with increasing numbers."""

N = input("Input: ")
N = int(N)
num = 1


if 1 <= N <= 15:
    for row in range(N):
        for col in range(N):
            if row > col:
                print(0, end="\t")
            else:
                print(num, end="\t")
                num += 1
        print()
else:
    print("Invalid input")

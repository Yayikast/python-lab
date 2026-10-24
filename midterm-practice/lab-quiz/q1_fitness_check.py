"""Decide fit or unfit from age and a yes/no lifestyle question."""

age = input("Input: What is your age ")
if age.isnumeric():
    age = int(age)
    if age > 30:
        ver = input("Input: Do you exercise regularly (Y/N)? ")
        if ver == "Y":
            print("Output: You are fit")
        elif ver == "N":
            print("Output: You are unfit")
        else:
            print("Output: Your answer must be either Y or N")
    else:
        ver = input("Input: Do you eat lot of junk food (Y/N)? ")
        if ver == "Y":
            print("Output: You are unfit")
        elif ver == "N":
            print("Output: You are fit")
        else:
            print("Output: Your answer must be either Y or N")
else:
    print("Output: age must be a number")

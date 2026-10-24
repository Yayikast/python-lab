"""Group positive integers by their last digit."""

x = input("Integer inputs: ").split()

pos = []
for i in x:
    if i.isnumeric():
        i = int(i)
        pos.append(i)

pos.sort()
dct = {}

for i in pos:
    k = list(str(i))
    end = int(k[-1])
    if end in dct:
        dct[end].append(i)
    else:
        dct[end] = [i]

###Sort###
key = list(dct.keys())
key.sort()
sortdct = {n: dct[n] for n in key}

for grp, val in sortdct.items():
    print("Group %d, Total %d, Values: %s" % (grp, len(val), val))

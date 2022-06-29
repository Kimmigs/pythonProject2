fname = input("Enter file name:")
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for item in words:
        if item in lst:
            continue
        if item not in lst:
            lst.append(item)
print(sorted(lst))
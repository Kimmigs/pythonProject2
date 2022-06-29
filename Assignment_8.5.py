fname = input("Enter file name:")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    lines = line.split()
    lst.append(lines[1])
count = len(lst)
for item in lst:
    print(item)
print("There were", count, "lines in the file with From as the first word")


fname = input("Enter file name:")
fh = open(fname)
names = list()
counts = dict()
for line in fh:
    if not line.startswith("From "): continue
    words = line.split()
    name = words[1]
    names.append(name)
for key in names:
    counts[key] = counts.get(key, 0) + 1
address = 0
addresscount = 0
for key, count in counts.items():
    if addresscount == 0 or count > addresscount:
        address = key
        addresscount = count
print(address, addresscount)

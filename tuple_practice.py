fname = "romeo.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
lst=(sorted([(v, k) for k, v in counts.items()]))
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print (key, val)


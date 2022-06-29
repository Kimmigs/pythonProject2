fname = "mbox-short.txt"
fh = open(fname)
times = list()
lst = list()
for line in fh:
    if not line.startswith("From "): continue
    lines = line.split()
    for item in lines:
        if ":" in item:
            times.append(item)
for time in times:
    hours = time.split(":")
    lst.append(hours[0])

counts = dict()
for hour in lst:
    counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)





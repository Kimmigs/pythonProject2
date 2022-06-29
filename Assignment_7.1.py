fname = input("Enter file name:")
fh = open(fname)
words = fh.read()
wordsup = words.upper()
wordsupf = wordsup.rstrip()
print(wordsupf)


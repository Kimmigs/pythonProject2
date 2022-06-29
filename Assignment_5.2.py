smallest = None
largest = None
while True:
    num = input("Enter Number:")
    if num == "done":
        break
    try:
        inum = int(num)
    except:
        print("Invalid Input")
    if smallest == None:
        smallest = inum
    elif inum < smallest:
        smallest = inum
    if largest == None:
        largest = inum
    elif inum > largest:
        largest = inum
print("Maximum is", largest)
print("Minimum is", smallest)

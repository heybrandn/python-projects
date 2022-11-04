phr1 = input("Enter Phrase 1: " )
phr2 = input("Enter Phrase 2: " )
lst1 = []
lst2 = []
y = 0

for x in phr1:
    x = x.lower()
    x = str(x)
    lst1.append(x)
for x in phr2:
    x = x.lower()
    x = str(x)
    lst2.append(x)

for x in lst1:
    if x in lst2:
        y += 1
        if y == len(lst1):
            print("Yes")
            break
    else:
        print("No")
        break
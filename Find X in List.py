list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
find = 9
found = False

for i in range(len(list)):
    found = list[i]==find
    if found:
        break

if found:
    print("found at", i)
else:
    print("nvm")
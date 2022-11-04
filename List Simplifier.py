list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in list:
    x = list[i]
    if x in list:
        del list[i]

print("The list with unique elements only:")
print(list)

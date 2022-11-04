list = [3, 1, 6, 4, 2, 5]
swap = True

while swap:
    print(list)
    swap=False
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            print(i, i+1)
            swap=True
            list[i], list[i+1]=list[i+1], list[i]
print(list)
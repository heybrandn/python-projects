def lstTest(y):
    lst=[]
    for x in range(0, y):
        x+=1
        lst.insert(0, x)
    return lst
print(lstTest(6))
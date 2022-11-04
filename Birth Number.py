nums = input("enter birth numbers: ")
numList = []
ans = 0
y = 0
test = True
testTest = False
for x in nums:
    x = int(x)
    numList.append(x)
for y in numList:
    ans += y
if ans > 10:
    numList = []
    for x in str(ans):
        x = int(x)
        numList.append(x)
    ans = 0
    for y in numList:
        ans += y
print(ans)
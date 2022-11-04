word = input("Enter word: ")
inp = input("Enter string: ")
wordList = []
inpList = []
ans = "Yes"
for x in str(word):
    x = x.lower()
    wordList.append(x)
    
for x in str(inp):
    x = x.lower()
    inpList.append(x)

for x in wordList:
    if inpList.index(x) >= 1:
        ans = "Yes"
        continue
    else:
        print(x)
        ans = "No"
        break
print(ans)
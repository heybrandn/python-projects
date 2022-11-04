phrase = input("Enter a phrase: " )
lst = []
for letter in phrase:
    if letter == ' ':
        del letter
    else:
        letter = letter.lower()
        lst.append(letter)
lstLen = len(lst)
test = True
x = 0
while test:
    for x in range(lstLen):
        if lst[x] == lst[lstLen-x-1]:
            if lst[x] == lst[lstLen-2] and x != 0:
                x += 1
            else:
                continue
        else:
            x = 0
            break
    break
if x > 0:
    print("Palindrome")
else:
    print("Not Palindrome")
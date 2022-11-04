phr1 = input("Enter Phrase 1: " )
phr2 = input("Enter Phrase 2: " )
lst1 = []
lst2 = []
for letter in phr1:
    if letter.isalpha():
        letter = letter.lower()
        lst1.append(letter)
    else:
        del letter
for letter in phr2:
    if letter.isalpha():
        letter = letter.lower()
        lst2.append(letter)
    else:
        del letter
lst1.sort()
lst2.sort()
if lst1 == lst2:
    print("Anagrams")
else:
    print("Not Anagrams")
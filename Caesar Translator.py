inp = input("Enter: ")
translation = ''
for letter in inp:
    if letter == ' ':
        translation += ' '
    else:
        if not letter.isalpha():
            continue
        if letter == letter.upper():
            letter = letter.upper()
            sub = ord(letter) + 2
            if sub == ord('Z') + 1:
                sub = ord('A')
            elif sub == ord('Z') + 2:
                sub = ord('B')
        else:
            letter = letter.lower()
            sub = ord(letter) + 2
            if sub == ord('z') + 1:
                sub = ord('a')
            elif sub == ord('z') + 2:
                sub = ord('b')
        translation += chr(sub)
print(translation)
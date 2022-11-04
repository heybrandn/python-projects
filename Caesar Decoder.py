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
            sub = ord(letter) - 2
            if sub == ord('?'):
                sub = ord('Z')
            elif sub == ord('@'):
                sub = ord('Y')
        else:
            letter = letter.lower()
            sub = ord(letter) - 2
            if sub == ord('`'):
                sub = ord('z')
            elif sub == ord('_'):
                sub = ord('y')
        translation += chr(sub)
print(translation)
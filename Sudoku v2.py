print("Enter Rows")
row1 = input()
row2 = input()
row3 = input()
row4 = input()
row5 = input()
row6 = input()
row7 = input()
row8 = input()
row9 = input()

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
rr = 1

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
cc = 1

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
bb = 0
test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for x in range(0, 10):
    print(test.index[x])

for rr in range(1, 10):
    if rr == 1:
        for x in row1:
            x = int(x)
            r1.append(x)
            print()
            if r1.index(x) == 1:
                continue
    elif rr == 2:
        for x in row2:
            r2.append(x)
    elif rr == 3:
        for x in row3:
            r3.append(x)
    elif rr == 4:
        for x in row4:
            r4.append(x)
    elif rr == 5:
        for x in row5:
            r5.append(x)
    elif rr == 6:
        for x in row6:
            r6.append(x)
    elif rr == 7:
        for x in row7:
            r7.append(x)
    elif rr == 8:
        for x in row8:
            r8.append(x)
    elif rr == 9:
        for x in row9:
            r9.append(x)

c1 = [r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0]]
c2 = [r1[1], r2[1], r3[1], r4[1], r5[1], r6[1], r7[1], r8[1], r9[1]]
c3 = [r1[2], r2[2], r3[2], r4[2], r5[2], r6[2], r7[2], r8[2], r9[2]]
c4 = [r1[3], r2[3], r3[3], r4[3], r5[3], r6[3], r7[3], r8[3], r9[3]]
c5 = [r1[4], r2[4], r3[4], r4[4], r5[4], r6[4], r7[4], r8[4], r9[4]]
c6 = [r1[5], r2[5], r3[5], r4[5], r5[5], r6[5], r7[5], r8[5], r9[5]]
c7 = [r1[6], r2[6], r3[6], r4[6], r5[6], r6[6], r7[6], r8[6], r9[6]]
c8 = [r1[7], r2[7], r3[7], r4[7], r5[7], r6[7], r7[7], r8[7], r9[7]]
c9 = [r1[8], r2[8], r3[8], r4[8], r5[8], r6[8], r7[8], r8[8], r9[8]]

for x in range(0, 3):
    b1 += int(r1[x]) + int(r2[x]) + int(r3[x])
for x in range(0, 3):
    b2 += int(r1[x+3]) + int(r2[x+3]) + int(r3[x+3])
for x in range(0, 3):
    b3 += int(r1[x+6]) + int(r2[x+6]) + int(r3[x+6])
for x in range(0, 3):
    b4 += int(r4[x]) + int(r5[x]) + int(r6[x])
for x in range(0, 3):
    b5 += int(r4[x+3]) + int(r5[x+3]) + int(r6[x+3])
for x in range(0, 3):
    b6 += int(r4[x+6]) + int(r5[x+6]) + int(r6[x+6])
for x in range(0, 3):
    b7 += int(r7[x]) + int(r8[x]) + int(r9[x])
for x in range(0, 3):
    b8 += int(r7[x+3]) + int(r8[x+3]) + int(r9[x+3])
for x in range(0, 3):
    b9 += int(r7[x+6]) + int(r8[x+6]) + int(r9[x+6])

if b1 == 45 and b2 == 45 and b3 == 45 and b4 == 45 and b5 == 45 and b6 == 45 and b7 == 45 and b8 == 45 and b9 == 45:
    print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    print("yes")

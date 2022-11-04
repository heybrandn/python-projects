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

for rr in range(1, 10):
    if rr == 1:
        for x in row1:
            r1.append(x)
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
def ccAdd():
    global c1, cc, r
    c1.append(r1[cc])
    c2.append(r1[cc])
    c3.append(r1[cc])
    c4.append(r1[cc])
    c5.append(r1[cc])
    c6.append(r1[cc])
    c7.append(r1[cc])
    c8.append(r1[cc])
    c9.append(r1[cc])
for cc in range(1, 10):
    if cc == 1:
        
    elif cc == 2:
        for x in row2:
            r2.append(x)
    elif cc == 3:
        for x in row3:
            r3.append(x)
    elif cc == 4:
        for x in row4:
            r4.append(x)
    elif cc == 5:
        for x in row5:
            r5.append(x)
    elif cc == 6:
        for x in row6:
            r6.append(x)
    elif cc == 7:
        for x in row7:
            r7.append(x)
    elif cc == 8:
        for x in row8:
            r8.append(x)
    elif cc == 9:
        for x in row9:
            r9.append(x)
            
            
print(r1, r2, r3, r4, r5, r6, r7, r8, r9, sep = "\n")
print(c1, c2, c3, c4, c5, c6, c7, c8, c9, sep = "\n")
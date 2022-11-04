blocks = int(input("Enter the number of blocks: "))
height = 0
num = 0
while blocks > num:
    num+=1
    height+=1
    blocks-=num
    
print("The height of the pyramid:", height)
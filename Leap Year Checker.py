def leapCheck(year):
    rslts=[]
    for x in year:
        if x%4==0:
            rslts.insert(0, True)
        else:
            rslts.insert(0, False)
    rslts.reverse()
    print(rslts)    
leapCheck([2000, 2001, 2010, 2016])
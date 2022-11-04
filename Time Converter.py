hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

if dura>=60:
    hour+=dura//60
    mins+=dura%60
    dura=0
if mins+dura>=60:
    mins = mins+dura-60
    hour+=1
if hour>=24:
    hour-=24*(hour//24)
print(hour,":",mins, sep="")
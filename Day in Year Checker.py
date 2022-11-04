def leapYear(year):
    if year%4==0:
        return True
    else:
        return False

def yearDay(year, month, day):
    response = str(day) + " " + str(month) + " " + str(year) + " " + "is day "
    days = 0
    if year%4==0 and month is not "January":
            days+=1
    if month=="January":
        days += day
        print(response + str(days))
    elif month=="February":
        days += day + 31
        print(response + str(days))
    elif month=="March":
        days += day + 59
        print(response + str(days))
    elif month=="April":
        days += day + 90
        print(response + str(days))
    elif month=="May":
        days += day + 120
        print(response + str(days))
    elif month=="June":
        days += day + 151
        print(response + str(days))
    elif month=="July":
        days += day + 181
        print(response + str(days))
    elif month=="August":
        days += day + 212
        print(response + str(days))
    elif month=="September":
        days += day + 243
        print(response + str(days))
    elif month=="October":
        days += day + 273
        print(response + str(days))
    elif month=="November":
        days += day + 304
        print(response + str(days))
    elif month=="December":
        days += day + 334
        print(response + str(days))
yearDay(2022, "September", 16)
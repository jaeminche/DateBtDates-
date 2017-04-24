def isLeapYear(year):
    if year%4 != 0:
      return 'common'
    elif year%100 != 0:
      return year
    elif year%400 != 0:
      return 'common'
    return year

def daysInMonth(year, month):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if daysInMonth[month-1] == daysInMonth[1]:
        if daysInMonth(year) == isLeapYear(year):
            return 29
        return 28
    return(daysInMonth[month-1]) 
    
print daysInMonth(2000, 2)
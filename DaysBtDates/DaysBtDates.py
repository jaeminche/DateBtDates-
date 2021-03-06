# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
#----def. of leap year----brought from wiki------
#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)
#-----------------------------------------------------------------------------------
#------notes : basic algebraic equation for brainstorming-(down to line 18)
#BUT THIS DID NOT HELP AT ALL, DAVE SOLVED IT IN A DIFFERENT WAY, though, just for record----------
###365*(ty-by)+s(# of leap yr in between ty, by) + (tm-bm)*30+x(# of bm~tm = 1,3,5..., if bm~tm = 2, then -2)) + (td-bd)
#-------------------------------------------------------------------------------------------------------
#
#

def isLeapYear(year):             #define leap year
    if year%4 != 0:               
      return 'common'
    elif year%100 != 0:
      return year
    elif year%400 != 0:
      return 'common'
    return year                   #return leap year

def daysInMonth(year, month):
    daysOfMonth = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]
    if month == 2:                                    #when month is 2,                                 
        if year == isLeapYear(year):                  #see year if it is leapyear
          return 29                                   #if it is, return 29
    return(daysOfMonth[month-1])                      #if not, just return 28 for Feb and #s accordingly for the rest of months
    
def nextDay(year, month, day):              #ok, define what nextDay is
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):      #if day is less than 31, 28, 30, or 29
        return year, month, day + 1         #return next day
    else:                                   #in other cases, in other words, when day is 30(31,28,29) or more,
        if month == 12:                     #if month is 12 (12.30)
            return year + 1, 1, 1           #return next year and Jan. 1
        else:                               #if not, in other words, when month is not 12
            return year, month + 1, 1       #return next month, 1

def whetherbefore(year1, month1, day1, year2, month2, day2):  #HELPER FUNCTION!!!! define what whetherbefore is : only returns T/F for the while loop below
    if year1 < year2:           #if year1 is before year2
      return True               #return True
    if year1 == year2:          #if year1 is the same yr as year2
      if month1 < month2:       #if month1 is before month2
        return True             #return True
      if month1 == month2:      #if month1 is the same yr as month2
        return day1 < day2      #and if day1 is before day2, return True
    return False
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):       #Functions always take (variables).
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
     
    assert not whetherbefore(year2, month2, day2, year1, month1, day1)  #AssertionError gets raised if date2 is before date1
    totaldates = 0                                                    #below is a PSEUDOCODE!!!
    while whetherbefore(year1, month1, day1, year2, month2, day2):    #while True (as long as date1 is before date2; see helper function)
      (year1, month1, day1) = nextDay(year1, month1, day1)            #so, date1 gets added by 1 until it gets the day before date2, and it stops (only while true)
      totaldates += 1                                                 #this functions as a counter for the loop, as to how many times nextDay worked in this loop until it gets the day before date2
    return totaldates                                                 #return total days between dates of the two *the reason for the indentation in this way is to escape the while block(? maybe)

print daysBetweenDates(1983,2,7,1987,1,2)   

    ##





# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

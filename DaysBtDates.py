# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
#----def. of leap year----------
#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)
#-------------------------------
#------basic equation-----------
# 2017. 3. 22
#-2016. 8. 22
#
#def true:
# if true:
#  by + s / 4.0 
#
#def 
#if member of by~ty = ly,
#
###365*(ty-by)+s(# of leap yr in between ty, by) + (tm-bm)*30+x(# of bm~tm = 1,3,5..., if bm~tm = 2, then -2)) + (td-bd)
#-------------------------------------------------
#
#

def nextDay(year, month, day):              #ok, define what nextDay is
    """Simple version: assume every month has 30 days"""
    if day < 30:                            #if day is less than 30
        return year, month, day + 1         #return next day
    else:                                   #if not, in other words, when day is 30 or more,
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
        
    # YOUR CODE HERE!
    totaldates = 0                                                    #below is a PSEUDOCODE!!!
    while whetherbefore(year1, month1, day1, year2, month2, day2):    #while True (as long as date1 is before date2; see helper function)
      (year1, month1, day1) = nextDay(year1, month1, day1)            #so, date1 gets added by 1 until it gets the day before date2, and it stops (only while true)
      totaldates += 1                                                 #this functions as a counter for the loop, as to how many times nextDay worked in this loop until it gets the day before date2
    return totaldates                                                 #return total days between dates of the two *the reason for the indentation in this way is to escape the while block(? maybe)

print daysBetweenDates(1983,2,7,2017,4,23)   

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

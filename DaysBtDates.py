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
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day < 30:
      return year, month, day + 1
    else:
      if month < 12:
        return year, month + 1, 1
      else:
        return year + 1, 1, 1

print nextDay(1999, 12, 30)




def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.


    return
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

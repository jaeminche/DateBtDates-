yr = 1983  
while yr <= 2017:
  def year(y):
    if y%4 != 0:
      return 'common'
    elif y%100 != 0:
      return 'leap'
    elif y%400 != 0:
      return 'common'
    return 'leap'
  print yr, year(yr)
  yr = yr + 1
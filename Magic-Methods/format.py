"""UseCase for __format__()
  __format__(self,format_spec)
  format_spec -- is a string containing string formatting.
Defines behavior for when an instance of your class is used in new-style string formatting. 

"""
#Example 1
_formats = {
  'ymd':'{d.year}-{d.month}-{d.day}',
  'mdy':'{d.month}/{d.day}/{d.year}',
  'dmy':'{d.day}/{d.month}/{d.year}'
  }
  
class Date:
  def __init__(self,year,month,day):
    self.year = year
    self.month = month
    self.day = day
  def __format__(self,code):
    if code == '':
      code = 'ymd'
      
    fmt = _formats[code]
    return fmt.format(d = self)
    
if __name__ == "__main__":
  
  d = Date(2015,6,11)
  print(format(d))       #d.__format__()
                         #'{d.year}-{d.month}-{d.day}'.format(d)
                         #2015-6-11
  print(format(d,'mdy')) # d.__format('mdy')
                         #'{d.month}/{d.day}/{d.year}'.format(d)
                         #6/11/2015

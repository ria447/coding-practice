import math 

  def isPerfectSquare(num):
      sqrt = math.sqrt(num)

      string = str(sqrt)
      if string[-1] == '0' and string[-2] == '.':
          return True
      else:
          return False

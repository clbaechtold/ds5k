def compare(a, b):
   try:
      a_greater = (a > b)
   except:
      a_greater = None
      b_greater = None
   else:
      b_greater = (b > a)
   finally:
      print(a_greater, b_greater)

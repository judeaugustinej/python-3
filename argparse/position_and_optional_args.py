"""Adding two numbers.
   We take two number as positiona arguments,
   and we have an option of writing the sum to
   a file base on --output option.
   
   --output is optional
"""

import argparse

def sum(a,b):
 return a + b

if __name__ == "__main__":

 parser = argparse.ArgumentParser()
 parser.add_argument("a",help="The first number",type=int)
 parser.add_argument("b",help="The second number",type= int)
 parser.add_argument("-o","--output",help="Output to in the form a + b = sum ",action = "store_true")

 args = parser.parse_args()

 if args.output:

  newList = [ ]
  newList.append(str(args.a))
  newList.append(" + ")
  newList.append(str(args.b))
  newList.append(" = ")
  newList.append(str(sum(args.a,args.b)))

  print(' '.join(newList))
 else:
  print(args.a,args.b,args.output)

#--Output---
"""
-sh-3.2$ python3 opt_pos.py -h
usage: opt_pos.py [-h] [-o] a b

positional arguments:
  a             The first number
  b             The second number

optional arguments:
  -h, --help    show this help message and exit
  -o, --output  Output to in the form a + b = sum
-sh-3.2$
-sh-3.2$ python3 opt_pos.py 2 4
2 4 False
-sh-3.2$
-sh-3.2$ python3 opt_pos.py 2 4 -o
2  +  4  =  6
-sh-3.2$

"""

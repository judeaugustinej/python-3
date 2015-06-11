"""Simple example using argparser """

import argparse

def squareFunc(num):

  return num ** 2
 
def add(a,b):
  return a + b

if __name__ == "__main__":

  parser = argparse.ArgumentParser()    #created a parser called parser.
  parser.add_argument("num1",help="Enter a valid interger",type = int)  #we add an argument called number of type interger
  parser.add_argument("num2",help="Enter the second number",type = int)
  args = parser.parse_args()     #The argument are stored in args
 
  print("The square of the first number {}".format(squareFunc(args.num1)))
  print("The sum of {0} and {1} is {2}".format(args.num1,args.num2,add(args.num1,args.num2)))

#--Output---
"""
-sh-3.2$ python3 basic_args.py  -h
usage: basic_args.py [-h] num1 num2

positional arguments:
  num1        Enter a valid interger
  num2        Enter the second number

optional arguments:
  -h, --help  show this help message and exit
-sh-3.2$
-sh-3.2$
-sh-3.2$ python3 basic_args.py  --help
usage: basic_args.py [-h] num1 num2

positional arguments:
  num1        Enter a valid interger
  num2        Enter the second number

optional arguments:
  -h, --help  show this help message and exit
-sh-3.2$
-sh-3.2$
-sh-3.2$ python3 basic_args.py  4 5
The square of the first number 16
The sum of 4 and 5 is 9
-sh-3.2$
-sh-3.2$
-sh-3.2$ python3 basic_args.py  4
usage: basic_args.py [-h] num1 num2
basic_args.py: error: the following arguments are required: num2
-sh-3.2$
-sh-3.2$
-sh-3.2$ python3 basic_args.py
usage: basic_args.py [-h] num1 num2
basic_args.py: error: the following arguments are required: num1, num2
-sh-3.2$
-sh-3.2$

"""

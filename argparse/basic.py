"""Simple example using argparser """

import argparse

 def squareFunc(num):

         return num ** 2

 if __name__ == "__main__":

         parser = argparse.ArgumentParser()    #created a parser called parser.
          parser.add_argument("num",help="Enter a valid interger",type = int)  #we add an argument called number of type interger
         args = parser.parse_args()     #The argument are stored in args
         print(squareFunc(args.num))    

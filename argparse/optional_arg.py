"""Optional arguments"""

#syntax
"""
parser.add_argument(optional argument,help,action)
action make
parser.args == True if optional argument is used else False
parser.add_argument("--verbose",help="what is verbose",action="store_true")
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",help="what is this",action="store_true")

args = parser.parser_args()

if args.verbose:
  print("why did you chose verbose")
  
#--Output----
"""
-sh-3.2$ python3 optional_args.py
-sh-3.2$
-sh-3.2$ python3 optional_args.py -h
usage: optional_args.py [-h] [--verbosity]

optional arguments:
  -h, --help   show this help message and exit
  --verbosity  increase output verbose
-sh-3.2$
-sh-3.2$
-sh-3.2$ python3 optional_args.py --verbosity
verbosity turned on

"""

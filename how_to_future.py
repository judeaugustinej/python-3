"""
A future statement is a directive to the compiler that a particular module should be compiled 
using syntax or semantics that will be available in a specified future release of Python.
Intended to ease migration to future versions of Python  
"""

from __future__ import print_function

print('# of entries', len(dictionary), file=sys.stderr)



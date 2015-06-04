#Break---Is used when we need to completely exit a loop when a condition is meet.

for letter in "Jude Augustine Job":
    if letter == "A":
       break
    print("The letter is ",letter)

"""--Output---
The letter is  J
The letter is  u
The letter is  d
The letter is  e
The letter is
"""
    
#Continue --Statement is used to skip the rest of the code inside a loop for the current iteration ,but the iteration continues.

for number in range(10):
  
    if number == 5:
        continue
    print("The numbers are ",number)
    
"""--Output---
The numbers are  0
The numbers are  1
The numbers are  2
The numbers are  3
The numbers are  4
The numbers are  6
The numbers are  7
The numbers are  8
The numbers are  9
"""

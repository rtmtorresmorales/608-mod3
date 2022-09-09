# restaurant bill.py Ramon Torres AGO 21 2022
import math
import decimal
import statistics


# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter number of dice rolls : , then the dice roll up to the total number of rolls.  Hit enter after each number"))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      

# Variance and standard deviation calculations

statistics.pvariance(lst)
statistics. pstdev(lst)


# Return summary

print ("P varince",statistics.pvariance(lst))
print ("P varince",statistics. pstdev(lst))

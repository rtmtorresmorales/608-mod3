# restaurant bill.py Ramon Torres AGO 21 2022
import math
import decimal


meal_cost = float(input('Enter meal cost: '))
meal_tip_percentage= float(input('Enter tip percentage: '))
meal_tax_percentage= float(input('Enter tax in percentage: '))


meal_tip = meal_cost * (meal_tip_percentage/100)
meal_tax = meal_cost * (meal_tax_percentage/100)
total_bill = meal_cost + meal_tip + meal_tax 


# Return summary of bill

print ("meal cost",meal_cost)
print ("meal tip percentage",meal_tip_percentage , "%")
print ("meal tip before tax in $",meal_tip)
print ("meal tax in $ depending on your state $",meal_tax)
print ("Total bill (cost + tip +tax) in $",total_bill)
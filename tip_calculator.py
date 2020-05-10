#Hi. This is my tip and share calculator
bill_amount = int( input("Enter bill amount: "))
percentage = int(input("Enter tip percentage: "))
friends = int(input("How many are you? "))

def calculateBill(bill_amount, percentage, friends):
    bill = bill_amount
    tip = bill * (percentage/100)
    total = bill + tip
    share = total / friends
     
    return total , share

total, share = calculateBill(bill_amount, percentage, friends )
print("\n", "-------" , "Total to pay: ", str(total),
"-------", "\n\b", 
 "and everyone should pay :", str(share), "\n\b", "----------------------------")

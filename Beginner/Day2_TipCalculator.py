print("Welcome to the Tip Calculator")

#Input to be asked and converting into appropriate data type
bill = float(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15: "))
people = int(input("Among how many people the bill is to be splitted?"))

#Calculations
total_bill = (bill+(bill * (tip/100)))/people
final_amt = round(total_bill,2) 

#Printing Out
print(f"Each person should pay: ₹{final_amt}")



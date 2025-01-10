# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?")) # Asks user for bill
tip = float(input("How much would you like to tip? 10%, 12% or 15%")) # Prompts user for disired tip
number_of_people = float(input("How many people to split the bill?")) # Asks the user to specify how many people to split the with
tip_converstion = tip / 100 # converts tip into a percentage
tip_calc = tip_converstion * bill # calculates the tip percentage from the bill
bill_with_tip = bill + tip_calc # adds the tip to the bill
bill_split = round(bill_with_tip / number_of_people, 2) # divides the sum of the bill and tip between the amount of people - rounds float to 2 decimal places
print(f"Each person should pay: {bill_split}") # Displays how much each person should pay








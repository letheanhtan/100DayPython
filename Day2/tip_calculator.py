print("Welcome to the tip calculator.")
total_bill = float(raw_input("What was the total bill? $"))
tip_percentage = float(raw_input("What percentage tip would you like to give? 10, 12 or 15? "))
people_num = float(raw_input("How many people to split the bill? "))
paid_per_person = round(total_bill * (1 + tip_percentage/100)/people_num, 2)

# python version 2.7
print("Each person should pay: $" + str(paid_per_person))

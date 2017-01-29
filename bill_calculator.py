def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * tip_percentage * .01

#raw_input("Would you like to calculate your tip?")

tip_amount = calculate_tip (100, 18)
print tip_amount

def calculate_total_bill(tip_amount, bill_amount):
    return tip_amount + bill_amount

total_amount = calculate_total_bill (18, 100)
print total_amount









# TIP_PERCENTAGE = 18

# def calculate_bill(original_bill_amount, tip):
#     calculated_tip = original_bill_amount * (tip * .01)
#     total_bill = original_bill_amount + calculated_tip
#     return total_bill   

# def split_bill(total_bill, split_number=1):
#     return total_bill / split_number

# bill_plus_tip = calculate_bill(500, TIP_PERCENTAGE)
# print split_bill(bill_plus_tip, 4)


# def calculate_tip(bill_amount, tip_percentage):
#     return bill_amount * tip_percentage * .01


# def calculate_total_bill(tip_amount, bill_amount):
#     return tip_amount + bill_amount


# def split_bill(bill_amount, num_people):
#     return bill_amount / num_people


# def main():
#     user_choice = raw_input("Would you like to calculate the tip or split the bill? Type 1 for tip or 2 for split ")
#     if user_choice == "1":
#         bill_amount = float(raw_input("What is the bill amount? "))
#         tip_percentage = float(raw_input("What is the tip percentage? "))
#         tip = calculate_tip(bill_amount, tip_percentage)
#         bill_total = calculate_total_bill(tip, bill_amount)
#         print "Your tip is: ", tip, "and the total amount to pay is: ", bill_total
#         bill_split = raw_input("Would you like to split the bill? y/n ")
#         if bill_split == "y":
#             num_diners = int(raw_input("How many ways would you like to split the bill? "))
#             print "Each diner must pay:", split_bill(bill_total, num_diners)
#     elif user_choice == "2":
#         bill_amount = float(raw_input("What is the bill amount? "))
#         num_diners = int(raw_input("How many ways would you like to split the bill? "))
#         print "Each diner must pay: ", split_bill(bill_amount, num_diners)


# if __name__ == '__main__':
#     main()

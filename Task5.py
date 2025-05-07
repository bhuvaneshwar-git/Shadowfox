# Task5 Dictonary

# 1)Create a list of your friends' names. The list should have at least 5 names.Create a list of tuples. Each tuple should contain a friend's name and the length of the name

friends_name = ["Dragon","Dhanush","Ashwanth","Pradeep","siddhu"]
names=[]
for name in friends_name:
    names.append((name,len(name)))
print(names)
    

# 2) You and your partner are planning a trip, and you want to track expenses.Create two dictionaries, one for your expenses and one for your partner'sepenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts


your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}

partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
tot_partner_expenses = sum(partner_expenses.values())
tot_your_expenses = sum(your_expenses.values())
total_expenses = tot_partner_expenses + tot_your_expenses
print(f"The total expenses are : {total_expenses}")

if tot_partner_expenses > tot_your_expenses:
    print("Your expenses are higher!")
else:
    print("Partner expenses are higher!")

differences = {}
for expenses in your_expenses:
    if expenses in partner_expenses:
        my_amount = your_expenses[expenses]
        partner_amount = partner_expenses[expenses]

    difference = my_amount - partner_amount
    differences[expenses] = difference
    print(f"{expenses}:{difference}")
    
max_diff_category = max(differences, key=differences.get)
print(f"\nBiggest difference is : {max_diff_category} with a difference of {differences[max_diff_category]}")




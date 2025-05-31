# Task4 Forloops
import random 
Die = [1,2,3,4,5,6]
number_six = 0
number_one = 0
number_two_6 = 0
previous_number = None
for _ in range(1,21):
    random_number = random.choice(Die)
    print(random_number)
    if random_number == 6:
        number_six +=1
        if previous_number == 6: 
            number_two_6 +=1
    if random_number == 1:
        number_one +=1


    previous_number = random_number 

print(f"How many times you rolled a 6 :{number_six}")
print(f"How many times you rolled a 1 :{number_one}")
print(f"How many times you rolled two 6 :{number_two_6}")


# 2) magine you are doing a workout routine, and you have to complete 100jumping jacks.Write a program that:Asks you to perform 10 jumping jacks at a time.After each set, it asks, "Are you tired?"
jummping_jacks = 100
for value in range(0,101):
    print(value)
    if value == 10:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 =="Y":
            print(f"You completed a total of {value}jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")
    elif value == 20:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 30:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 40:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 50:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 60:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 70:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 80:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 90:
        set1 = input("Are you tired Type 'Y' OR 'N' :")
        if set1 == "Y":
            print(f"You completed a total of {value} jumping jacks")
            break
        else:
            print(f"Remaining jumping jacks : {100-value}")    
    elif value == 100:
            print("Congratulations! You completed the workout,")
            break 
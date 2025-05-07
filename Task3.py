# Task3 If condition

# 1) Write a program to determine the BMI Category based on user input

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

caluculation = weight / height ** 2
rounding_caluculation = round(caluculation)

if rounding_caluculation < 18.5:
    print("your in under weight.")
elif rounding_caluculation < 25:
    print(" your in normal weight.")
elif rounding_caluculation < 30:
    print("your in over weight.")
elif rounding_caluculation < 35:
    print("your in obese stage")
else:
    print("your in clinicaly obese")


# 2) Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("enter the city name :")

if city == "syndney":
    print("Syndney is in Australia")
elif city == "Melbourne":
    print("Melbourne is in Australia")
elif city == "Brisbane":
    print("Brisbane is in Australia")
elif city == "Perth":
    print("Perth is in Australia")
else:
    if city == "Dubai":
        print("Dubai is in UAE")
    elif city == "Abu Dhabi":
        print("Abu Dhaabi is in UAE")
    elif city == "sharjah":
        print("sharjah is in UAE")
    elif city == "Ajman":
        print("Ajman is in UAE")
    else:
        if city == "Mumbai":
            print("Mumbaai is in India")
        elif city == "Banglore":
            print("Banglore is in India")
        elif city == "Chennai":
            print("Chennai is in India")
        elif city == "Delhi":
            print("Delhi is in India")

# 3) Write a program to check if two cities belong to the same country.Ask the user to enter two cities and print whether they belong to the same country or not.
city_1 = input("Enter the first city: ")
city_2 = input("Enter the second city: ")

if city_1 == "syndney" and city_2 == "Melbourne":
    print("Both cities are in Australia")
elif city_1 == "syndney" and city_2 == "Brisbane":
    print("Both cities are in Australia")
elif city_1 == "syndney" and city_2 == "Perth":
    print("Both cities are in Australia")
elif city_1 == "Melbourne" and city_2 == "Syndney":
    print("Both cities are in Australia")
elif city_1 == "Melbourne" and city_2 == "Brisbane":
    print("Both cities are in Australia")
elif city_1 == "Melbourne" and city_2 == "Perth":
    print("Both cities are in Australia")
elif city_1 == "Brisbane" and city_2 == "Syndney":
    print("Both cities are in Australia")
elif city_1 == "Brisbane" and city_2 == "Melbourne":
    print("Both cities are in Australia")
elif city_1 == "Brisbane" and city_2 == "Perth":
    print("Both cities are in Australia")
elif city_1 == "Perth" and city_2 == "Syndney":
    print("Both cities are in Australia")
elif city_1 == "Perth" and city_2 == "Melbourne":
    print("Both cities are in Australia")
elif city_1 == "Perth" and city_2 == "Brisbane":
    print("Both cities are in Australia")
else:
    if city_1 == "Dubai" and city_2 == "Abu Dhabi":
        print("Both cities are in UAE")
    elif city_1 == "Dubai" and city_2 == "Sharjah":
        print("Both cities are in UAE")
    elif city_1 == "Dubai" and city_2 == "Ajman":
        print("Both cities are in UAE")
    elif city_1 == "Abu Dhabi" and city_2 == "Dubai":
        print("Both cities are in UAE")
    elif city_1 == "Abu Dhabi" and city_2 == "Sharjah":
        print("Both cities are in UAE")
    elif city_1 == "Abu Dhabi" and city_2 == "Ajman":
        print("Both cities are in UAE")
    elif city_1 == "sharjah" and city_2 == "Dubai":
        print("Both cities are in UAE")
    elif city_1 == "sharjah" and city_2 == "Abu Dhabi":
        print("Both cities are in UAE")
    elif city_1 == "sharjah" and city_2 == "Ajman":
        print("Both cities are in UAE")
    elif city_1 == "Ajman" and city_2 == "Dubai":
        print("Both cities are in UAE")
    elif city_1 == "Ajman" and city_2 == "Abu Dhabi":
        print("Both cities are in UAE")
    elif city_1 == "Ajman" and city_2 == "Sharjah":
        print("Both cities are in UAE")
    else:
        if city_1 == "Mumbai" and city_2 == "Banglore":
            print("Both cities are in India")
        elif city_1 == "Mumbai" and city_2 == "Chennai":
            print("Both cities are in India")
        elif city_1 == "Mumbai" and city_2 == "Delhi":
            print("Both cities are in India")
        elif city_1 == "Banglore" and city_2 == "Mumbai":
            print("Both cities are in India")
        elif city_1 == "Banglore" and city_2 == "Chennai":
            print("Both cities are in India")
        elif city_1 == "Banglore" and city_2 == "Delhi":
            print("Both cities are in India")
        elif city_1 == "Chennai" and city_2 == "Mumbai":
            print("Both cities are in India")
        elif city_1 == "Chennai" and city_2 == "Banglore":
            print("Both cities are in India")
        elif city_1 == "Chennai" and city_2 == "Delhi":
            print("Both cities are in India")
        elif city_1 == "Delhi" and city_2 == "Mumbai":
            print("Both cities are in India")
        elif city_1 == "Delhi" and city_2 == "Banglore":
            print("Both cities are in India")
        elif city_1 == "Delhi" and city_2 == "Chennai":
            print("Both cities are in India")    
        else:
            print("They don't belong to the same country")




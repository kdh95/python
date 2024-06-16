print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Operator
# >
# <
# >=
# <=
# ==
# !=

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7")
    elif age > 12:
        print("Please pay $14")
    else:
        print("Please pay $18")
else:
    print("Sorry, you have to grow taller before you can ride.")

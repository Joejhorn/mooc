# Fix the program
points = 0.0
points = float(input("How many points are on your card? "))

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print(f"You now have {points}, points")
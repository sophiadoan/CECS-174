#automobile service cost

autoservice = input("Enter desired auto service:\n")
if autoservice == "Oil change" or "oil change" :
    print(f"You entered: {autoservice}")
    print("Cost of oil change: $35")
elif autoservice == "Tire rotation":
    print(f"You entered: {autoservice}")
    print("Cost of tire rotation: $19")
elif autoservice == "Car wash":
    print(f"You entered: {autoservice}")
    print("Cost of car wash: $7")
else:
    print(f"You entered: {autoservice}")
    print("Error: Requested service is not recognized")

print("===== RENT CALCULATOR =====")

try:
    rent = float(input("Enter room rent: "))
    electricity = float(input("Enter electricity bill: "))
    water = float(input("Enter water bill: "))
    internet = float(input("Enter internet bill: "))
    roommates = int(input("Enter number of roommates: "))

    if rent < 0 or electricity < 0 or water < 0 or internet < 0:
        print("Expenses cannot be negative!")

    elif roommates <= 0:
        print("Enter a valid number of roommates!")

    else:
        total = rent + electricity + water + internet
        share = total / roommates

        print("\n===== MONTHLY EXPENSES =====")
        print("Room Rent:", rent)
        print("Electricity Bill:", electricity)
        print("Water Bill:", water)
        print("Internet Bill:", internet)
        print("Total Expenses:", total)
        print("Each Person Should Pay:", round(share, 2))

except ValueError:
    print("Please enter valid numbers!")

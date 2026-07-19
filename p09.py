while True:
    
    print("\n===== Mini Chai Ledger =====")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Per Person")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ---------------- Add Expense ----------------
    if choice == "1":

        name = input("Enter Name: ")
        amount = input("Enter Amount: ")

        with open("chai_ledger.txt", "a") as file:
            file.write(name + "," + amount + "\n")

        print("Expense Added Successfully!")

    # ---------------- Show All Expenses ----------------
    elif choice == "2":

        try:
            with open("chai_ledger.txt", "r") as file:

                print("\nAll Expenses:")

                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    data = line.split(",")

                    print(data[0], ":", data[1])

        except:
            print("No expense file found.")

    # ---------------- Show Totals ----------------
    elif choice == "3":

        totals = {}

        try:
            with open("chai_ledger.txt", "r") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    data = line.split(",")

                    name = data[0]
                    amount = int(data[1])

                    totals[name] = totals.get(name, 0) + amount

            print("\nTotal Expenses:")

            for person in totals:
                print(person, ": Rs", totals[person])

        except:
            print("No expense file found.")

    # ---------------- Exit ----------------
    elif choice == "4":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")
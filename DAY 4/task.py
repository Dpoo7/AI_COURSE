total = 0

while True:
    print("\n--- Restaurant Menu ---")
    print("1. Pizza  - ₹120")
    print("2. Burger - ₹80")
    print("3. Pasta  - ₹100")
    print("4. Coffee - ₹50")
    print("5. View Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        total += 120
        print("Pizza added.")

    elif choice == "2":
        total += 80
        print("Burger added.")

    elif choice == "3":
        total += 100
        print("Pasta added.")

    elif choice == "4":
        total += 50
        print("Coffee added.")

    elif choice == "5":
        print("Total Bill = ₹", total)

    elif choice == "6":
        print("Final Bill = ₹", total)
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice.")

# ☕ Simple Coffee App

coffee_menu = {
    "1": ("Espresso", 300),
    "2": ("Americano", 400),
    "3": ("Latte", 500),
    "4": ("Cappuccino", 550)
}


def show_menu():
    print("\n☕ COFFEE MENU")
    print("----------------")
    for number, (name, price) in coffee_menu.items():
        print(f"{number}. {name} - ¥{price}")


def coffee_app():
    total = 0

    print("☕ Welcome to My Coffee Shop!")

    while True:
        show_menu()

        choice = input("\nChoose coffee (1-4) or q to quit: ")

        if choice == "q":
            break

        if choice in coffee_menu:
            name, price = coffee_menu[choice]

            quantity = int(input(f"How many {name}s? "))

            cost = price * quantity
            total += cost

            print(f"✅ {quantity} x {name} = ¥{cost}")
        else:
            print("❌ Invalid choice!")

    print("\n----------------")
    print(f"💰 Total: ¥{total}")
    print("🙏 Thank you for visiting!")


coffee_app()
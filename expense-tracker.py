filename = "expenses.txt"

f = open(filename, "a")
f.close()

def show_menu():
    print("")
    print("=== My Personal Expense Tracker ===")
    print("1. Add something I bought")
    print("2. See my list of expenses")
    print("3. Check total spent")
    print("4. Exit")

def add_new():
    thing = input("\nName of the item: ")
    price = input("How much was it? ")
    
    if price.isdigit():
        f = open(filename, "a")
        entry = thing + "," + price + "\n"
        f.write(entry)
        f.close()
        print("Great, I added " + thing + " to the list!")
    else:
        print("Oops, price needs to be a number.")

def view_all():
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    
    print("\n--- List of stuff I bought ---")
    if len(lines) > 0:
        for line in lines:
            if "," in line:
                parts = line.strip().split(",")
                name = parts[0]
                cost = parts[1]
                print("- " + name + ": " + cost)
    else:
        print("Nothing in the list yet.")

def get_total():
    total_money = 0
    f = open(filename, "r")
    for line in f:
        if "," in line:
            parts = line.strip().split(",")
            cost = int(parts[1])
            total_money = total_money + cost
    f.close()
    
    print("\nTotal money spent so far: " + str(total_money))

print("Welcome to the tracker!")

while True:
    show_menu()
    user_choice = input("Pick a number (1-4): ")

    if user_choice == "1":
        add_new()
    elif user_choice == "2":
        view_all()
    elif user_choice == "3":
        get_total()
    elif user_choice == "4":
        print("Okay, goodbye!")
        break
    else:
        print("Sorry, I didn't understand that.")
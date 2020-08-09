# initial supplies
money = 550
water_ml = 400
milk_ml = 540
beans_g = 120
cups = 9


def print_status():
    print("The coffee machine has:")
    print(water_ml, "of water")
    print(milk_ml, "of milk")
    print(beans_g, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


# buy prompted option (1 - espresso, 2 - latte, 3 - cappuccino)
def buy():
    def attemptBuy(cost_water, cost_milk, cost_beans, price, cost_cups=1):
        global water_ml, milk_ml, beans_g, cups, money
        if water_ml >= cost_water and milk_ml >= cost_milk and beans_g >= cost_beans and cups >= cost_cups:
            print("I have enough resources, making you a coffee!")

            water_ml -= cost_water
            milk_ml -= cost_milk
            beans_g -= cost_beans
            cups -= cost_cups
            money += price
        else:
            if water_ml < cost_water:
                print("Sorry, not enough water!")
            if milk_ml < cost_milk:
                print("Sorry, not enough milk!")
            if beans_g < cost_beans:
                print("Sorry, not enough coffee beans!")
            if cups < cost_cups:
                print("Sorry, not enough disposable cups!")

    drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if drink == "back":
        return

    if drink == "1":  # espresso (250 ml water, 16 g coffee beans, $4)
        attemptBuy(250, 0, 16, 4)
    elif drink == "2":  # latte (350 ml water, 75 ml milk, 20 g coffee beans, $7)
        attemptBuy(350, 75, 20, 7)
    elif drink == "3":  # <3> cappuccino (200 ml water, 100 ml milk, 12 g coffee beans, $6)
        attemptBuy(200, 100, 12, 6)
    else:
        print("Invalid option.")


# fill supplies with prompted amounts
def fill():
    global water_ml, milk_ml, beans_g, cups
    water_ml += int(input("Write how many ml of water do you want to add: "))
    milk_ml += int(input("Write how many ml of water do you want to add: "))
    beans_g += int(input("Write how many grams of coffee beans do you want to add: "))
    cups += int(input("Write how many disposable cups of coffee do you want to add: "))


# take all money from machine
def take():
    global money
    print("I gave you $" + str(money))
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")

    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_status()
    elif action == "exit":
        break
    else:
        print("Invalid option.")
        continue

    print()

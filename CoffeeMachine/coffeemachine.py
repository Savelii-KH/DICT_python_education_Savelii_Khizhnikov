money_in = 550
water_In = 400
milk_in = 540
beans_in = 120
cups_in = 9


def ing_in():
    print("\nThe coffee machine has:")
    print(str(water_In) + " ml of water")
    print(str(milk_in) + " ml of milk")
    print(str(beans_in) + " g of coffee beans")
    print(str(cups_in) + " of disposable cups")
    print(str(money_in) + " of money")


ing_in()


def espresso():
    global money_in, water_In, milk_in, beans_in, cups_in
    money_in += 4
    water_In -= 250
    beans_in -= 16
    cups_in -= 1
    return


def latte():
    global money_in, water_In, milk_in, beans_in, cups_in
    money_in += 7
    water_In -= 350
    milk_in -= 75
    beans_in -= 20
    cups_in -= 1


def cappuccino():
    global money_in, water_In, milk_in, beans_in, cups_in
    money_in += 6
    water_In -= 200
    milk_in -= 100
    beans_in -= 12
    cups_in -= 1


while True:
    print("Write action (buy, fill, take)")
    answer = input()
    if answer == "buy":
        while True:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
            x = input()
            if x == "1":
                espresso()
                ing_in()
                break
            elif x == "2":
                latte()
                ing_in()
                break
            elif x == "3":
                cappuccino()
                ing_in()
                break
            else:
                print("Please, answer what do you want buy")
    elif answer == "take":
        print("I gave you " + str(money_in))
        money_in *= 0
        ing_in()
    elif answer == "fill":
        added_water = int(input("Write how many ml of watter you want add: "))
        added_milk = int(input("Write how many ml of milk you want add: "))
        added_beans = int(input("Write how many grams of coffee beans you want add: "))
        added_cups = int(input("Write how many disposable cups you want add: "))

        water_In += added_water
        milk_in += added_milk
        beans_in += added_beans
        cups_in += added_cups

        ing_in()
    break

class Coffee_Machine():
    def __init__(self):
        self.money_in = 550
        self.water_In = 400
        self.milk_in = 540
        self.beans_in = 120
        self.cups_in = 9

    def ing_in(self):
        print("\nThe coffee machine has:")
        print(str(self.water_In) + " ml of water")
        print(str(self.milk_in) + " ml of milk")
        print(str(self.beans_in) + " g of coffee beans")
        print(str(self.cups_in) + " of disposable cups")
        print(str(self.money_in) + " of money")

    def espresso(self):
        self.money_in += 4
        self.water_In -= 250
        self.beans_in -= 16
        self.cups_in -= 1
        print("I have enough resources, making you a coffee!")
        if self.water_In < 0:
            print("Sorry, not enough water")
            self.money_in -= 4
            self.water_In += 250
            self.beans_in += 16
            self.cups_in += 1
        elif self.beans_in < 0:
            print("Sorry, not enough coffee beans")
            self.money_in -= 4
            self.water_In += 250
            self.beans_in += 16
            self.cups_in += 1
        elif self.cups_in < 0:
            print("Sorry, not enough cups")
            self.money_in -= 4
            self.water_In += 250
            self.beans_in += 16
            self.cups_in += 1
        return

    def latte(self):
        self.money_in += 7
        self.water_In -= 350
        self.milk_in -= 75
        self.beans_in -= 20
        self.cups_in -= 1
        print("I have enough resources, making you a coffee!")
        if self.water_In < 0:
            print("Sorry, not enough water")
            self.money_in -= 7
            self.water_In += 350
            self.milk_in += 75
            self.beans_in += 20
            self.cups_in += 1
        elif self.milk_in < 0:
            print("Sorry, not enough milk")
            self.money_in -= 7
            self.water_In += 350
            self.milk_in += 75
            self.beans_in += 20
            self.cups_in += 1
        elif self.beans_in < 0:
            print("Sorry, not enough coffee beans")
            self.money_in -= 7
            self.water_In += 350
            self.milk_in += 75
            self.beans_in += 20
            self.cups_in += 1
        elif self.cups_in < 0:
            print("Sorry, not enough cups")
            self.money_in -= 7
            self.water_In += 350
            self.milk_in += 75
            self.beans_in += 20
            self.cups_in += 1
        return

    def cappuccino(self):
        self.money_in += 6
        self.water_In -= 200
        self.milk_in -= 100
        self.beans_in -= 12
        self.cups_in -= 1
        print("I have enough resources, making you a coffee!")
        if self.water_In < 0:
            print("Sorry, not enough water")
            self.money_in -= 6
            self.water_In += 200
            self.milk_in += 100
            self.beans_in += 12
            self.cups_in += 1
        elif self.milk_in < 0:
            print("Sorry, not enough milk")
            self.money_in -= 6
            self.water_In += 200
            self.milk_in += 100
            self.beans_in += 12
            self.cups_in += 1
        elif self.beans_in < 0:
            print("Sorry, not enough milk")
            self.money_in -= 6
            self.water_In += 200
            self.milk_in += 100
            self.beans_in += 12
            self.cups_in += 1
        elif self.cups_in < 0:
            print("Sorry, not enough milk")
            self.money_in -= 6
            self.water_In += 200
            self.milk_in += 100
            self.beans_in += 12
            self.cups_in += 1
        return


coffee = Coffee_Machine()

while True:
    print("Write action (buy, fill, take, remaining, exit)")
    answer = input()
    if answer == "buy":
        while True:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to main menu:")
            x = input()
            if x == "1":
                coffee.espresso()
                break
            elif x == "2":
                coffee.latte()
                break
            elif x == "3":
                coffee.cappuccino()
                break
            elif x == "4":
                break
            else:
                print("Please, answer what do you want buy")
    elif answer == "take":
        print("I gave you " + str(coffee.money_in))
        coffee.money_in *= 0
    elif answer == "fill":
        added_water = int(input("Write how many ml of watter you want add: "))
        added_milk = int(input("Write how many ml of milk you want add: "))
        added_beans = int(input("Write how many grams of coffee beans you want add: "))
        added_cups = int(input("Write how many disposable cups you want add: "))

        coffee.water_In += added_water
        coffee.milk_in += added_milk
        coffee.beans_in += added_beans
        coffee.cups_in += added_cups
    elif answer == "remaining":
        coffee.ing_in()
    elif answer == "exit":
        break

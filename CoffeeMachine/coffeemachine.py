water_in = int(input("Write how many ml of water the coffee machine has: "))
milk_in = int(input("Write how many ml of milk the coffee machine has: "))
beans_in = int(input("Write how may g of coffee beans the coffee machine has: "))
needed_cups = int(input("Write how many cups of coffee you will need: "))

water = water_in // 200
milk = milk_in // 50
beans = beans_in // 15

ing = (water, milk, beans)
min_ing = min(ing)

if needed_cups == min_ing:
    print("Yes, I can make that amount of coffee")
elif needed_cups > min_ing:
    print("No, I can make only " + str(min_ing) + " cups of coffee")
elif needed_cups < min_ing:
    print("Yes, I can make that amount of coffee (and even " + str(int(min_ing-needed_cups)) + " more than that)")

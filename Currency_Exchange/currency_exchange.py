if __name__ == "__main__":
    while True:
        try:
            a = float(input("Please, enter the number of tugriks you have: "))
            b = float(input("Please, enter the exchange rate: "))
            break
        except ValueError:
            print("Only numerical values!")
    print(f"The total amount of dollars: {round(a * b, 2)}")

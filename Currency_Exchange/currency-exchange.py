cd = {"ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208, "USD": 0.033, "EUR": 0.028}
while True:
    try:
        tugriks = float(input("Please, enter the number of tugriks you have: "))
        [print(f"I will get {round(cd[i] * tugriks, 2)} {i} from the sale of {tugriks} tugriks.") for i in cd.keys()]
        break
    except ValueError:
        print("ERROR!!! ONLY NUMERICAL VALUES!!!\n")

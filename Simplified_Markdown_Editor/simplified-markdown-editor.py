while True:
    str_parameter = "plain bold italic header link inline-code ordered-list unordered-list new-line"
    parameter = ["plain", "bold", "italic",
                 "header", "link", "inline-code",
                 "ordered-list", "unordered-list", "new-line"]
    choice = input("Choose a formatter: ")
    if choice == "!help":
        print(f"""Available parameters: {str_parameter}""")
    elif choice == "!done":
        break
    else:
        print("Unknown formatting type or command")

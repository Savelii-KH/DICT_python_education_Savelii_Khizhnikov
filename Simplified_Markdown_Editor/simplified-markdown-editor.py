markdown = []
str_parameter = "plain bold italic header link inline-code ordered-list unordered-list new-line"
parameter = ["plain", "bold", "italic",
             "header", "link", "inline-code",
             "ordered-list", "unordered-list", "new-line"]
while True:
    print("\n".join(markdown))
    choice = input("Choose a formatter: ")
    if choice == "!help":
        print(f"Available formatters: {str_parameter}")
    elif choice == "!done":
        break
    elif choice == parameter[0]:
        text = input("Text: ")
        markdown.append(text)
    elif choice == parameter[3]:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                levels = "#" * level
                header = input("Text: ")
                markdown.append(f"{levels} {header}")
            else:
                print("Value must be between 1 and 6")
        except ValueError:
            print("Enter a numeric value!")
    elif choice == parameter[8]:
        markdown.append(" ")
    elif choice == parameter[4]:
        label = input("Label: ")
        url = input("URL: ")
        markdown.append(f"""[{label}] ({url})""")
    else:
        print("Unknown formatter type or command")

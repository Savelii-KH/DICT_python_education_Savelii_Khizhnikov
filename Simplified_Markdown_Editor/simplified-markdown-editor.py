class Markdown:
    def __init__(self):
        self.markdown = []
        self.str_parameter = """plain, bold, italic, 
bold italic, header, 
link, inline-code, ordered-list, 
unordered-list, new-line"""

        self.parameter = ["plain", "bold", "italic", "bold italic",
                          "header", "link", "inline-code", "ordered-list",
                          "unordered-list", "new-line", "!help", "!done", "!exit"]

        self.menu()

    def menu(self):
        while True:
            print(f"""{"-"*70}\n{"".join(self.markdown)}\n{"-"*70}""")
            choice = input("Choose formatter: ")
            if choice == self.parameter[0]:
                self.plain()
            elif choice == self.parameter[4]:
                self.header()
            elif choice == self.parameter[5]:
                self.link()
            elif choice == self.parameter[6]:
                self.inline_code()
            elif choice == self.parameter[7]:
                self.ordered_list()
            elif choice == self.parameter[8]:
                self.unordered_list()
            elif choice == self.parameter[9]:
                self.new_line()
            elif choice == self.parameter[10]:
                self.help()
            elif choice == self.parameter[11]:
                self.done()
            elif choice == self.parameter[12]:
                break
            else:
                print("Incorrect parameter! Please try again")
            break

    def plain(self):
        print(f"""{"-"*70}\nDo you want to change the font type (yes/no)? """)
        choice = input("• ").lower()
        if choice == "yes":
            self.font_type()
            self.menu()
        elif choice == "no":
            text = input("Text: ")
            self.markdown.append(f"\n{text}")
            self.menu()
        else:
            print("Incorrect parameter! Please try again")
            self.plain()

    def font_type(self):
        print(f"""{"-"*70}\nChoose what type of font you want: bold, italic or bold italic""")
        choice = input("• ").lower()
        if choice == self.parameter[1]:
            self.bold()
        elif choice == self.parameter[2]:
            self.italic()
        elif choice == self.parameter[3]:
            self.bold_italic()
        else:
            print("Incorrect parameter! Please try again")
            self.font_type()

    def bold(self):
        print("-"*70)
        text = input("Text: ")
        self.markdown.append(f"**{text}**\n")
        self.menu()

    def italic(self):
        print("-" * 70)
        text = input("Text: ")
        self.markdown.append(f"*{text}*\n")
        self.menu()

    def bold_italic(self):
        print("-" * 70)
        text = input("Text: ")
        self.markdown.append(f"***{text}***\n")
        self.menu()

    def header(self):
        try:
            print("-" * 70)
            level = int(input("Level: "))
            if 1 <= level <= 6:
                levels = "#" * level
                header = input("Text: ")
                self.markdown.append(f"{levels} {header}\n")
                self.menu()
            else:
                print("Value must be between 1 and 6")
        except ValueError:
            print("Enter a numeric value!")

    def link(self):
        print("-" * 70)
        label = input("Label: ")
        url = input("URL: ")
        self.markdown.append(f"""[{label}] ({url})\n""")
        self.menu()

    def inline_code(self):
        print("-" * 70)
        code = input("Code: ")
        self.markdown.append(f"""`{code}`\n""")
        self.menu()

    def ordered_list(self):
        try:
            print("-" * 70)
            num_of_rows = int(input("Number of rows: "))
            for i in range(0, num_of_rows):
                row = input(f"Row #{i + 1}: ")
                self.markdown.append(f"{i + 1}. {row}\n")
            self.menu()
        except ValueError:
            print("Only numerical values!")

    def unordered_list(self):
        try:
            print("-" * 70)
            num_of_rows = int(input("Number of rows: "))
            for i in range(0, num_of_rows):
                row = input(f"Row #{i + 1}: ")
                self.markdown.append(f"* {row}\n")
            self.menu()
        except ValueError:
            print("Only numerical values!")

    def new_line(self):
        self.markdown.append("\n")
        self.menu()

    def help(self):
        print(f"""{"-"*70}\nAvailable formatters: {self.str_parameter}""")
        self.menu()

    def done(self):
        print(f"""{"-"*70}\nDo you want save your file (yes/no)?""")
        choice = input().lower()
        if choice == "yes":
            self.save()
        elif choice == "no":
            self.menu()
        else:
            print("Incorrect parameter! Please try again")
            self.done()

    def save(self):
        print("-"*70)
        name = input("Enter name of file: ")
        with open(f"{name}.md", "w+") as f:
            f.write(f"""{"".join(self.markdown)} \n""")
            self.markdown.clear()
        self.menu()


if __name__ == "__main__":
    Markdown()

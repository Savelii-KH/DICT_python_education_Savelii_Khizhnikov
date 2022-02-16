import sys


class Markdown:
    def __init__(self):
        self.markdown = []

        self.parameter = ["plain", "bold", "italic", "bold italic",
                          "header", "link", "inline-code", "ordered-list",
                          "unordered-list", "new-line", "!help", "!done", "!exit"]
        self.greetings()

    def greetings(self):
        print(f"""\n{"-"*27} Markdown editor {"-"*26}
| It's a simple markdown editor where you can easily create something|
| beautiful with a set of commands. If you type "plain" you will be  |
| given the choice to further format the text you enter or not. From |
| the valid formats you can choose: italic, bold, bold italic. This  |
| way you can format headers as well. For more information type      |
|"!help"                                                             |""")
        self.menu()

    def menu(self):
        pass

    def stop(self):
        sys.exit()

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
        choice = input("• ").lower().split()
        if choice[0] == self.parameter[1]:
            self.bold()
        elif choice[0] == self.parameter[2]:
            self.italic()
        elif choice[0] == self.parameter[3]:
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
        levels = 0
        try:
            print(f"""{"-"*70}\nWrite number of rows:""")
            level = int(input("• "))
            if 1 <= level <= 6:
                levels = "#" * level
                self.header_type(levels)
        except ValueError:
            print("Number must be between 1 and 6")
            self.header()
        return levels

    def header_type(self, levels):
        print(f"""{"-" * 70}\nDo you want to change the font type (yes/no)? """)
        choice = input("• ").lower().split()
        if choice[0] == "yes":
            self.header_choice_type(levels)
        elif choice[0] == "no":
            self.header_plane(levels)
        else:
            print("Incorrect parameter! Please try again")
            self.header_type(levels)

    def header_choice_type(self, levels):
        print(f"""{"-"*70}\nChoose what type of font you want: bold, italic or bold italic""")
        choice = input("• ").lower().split()
        if choice[0] == self.parameter[1]:
            self.header_bold(levels)
        elif choice[0] == self.parameter[2]:
            self.header_italic(levels)
        elif choice[0] == self.parameter[3]:
            self.header_bold_italic(levels)
        else:
            print("Incorrect parameter! Please try again")
            self.header_choice_type(levels)

    def header_plane(self, levels):
        header = input("Text: ")
        self.markdown.append(f"{levels} {header}\n")
        self.menu()

    def header_bold(self, levels):
        header = input("Text: ")
        self.markdown.append(f"{levels}**{header}**\n")
        self.menu()

    def header_italic(self, levels):
        header = input("Text: ")
        self.markdown.append(f"{levels}*{header}*\n")
        self.menu()

    def header_bold_italic(self, levels):
        header = input("Text: ")
        self.markdown.append(f"{levels}***{header}***\n")
        self.menu()

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
        print(f"""{"-"*70}
{self.parameter[0]}{" " * (14 - len(self.parameter[0]))} -      your text;
{self.parameter[1]}{" " * (14 - len(self.parameter[1]))} -      bold text;
{self.parameter[2]}{" " * (14 - len(self.parameter[2]))} -      italic text;
{self.parameter[3]}{" " * (14 - len(self.parameter[3]))} -      bold italic text;
{self.parameter[4]}{" " * (14 - len(self.parameter[4]))} -      head of text;
{self.parameter[5]}{" " * (14 - len(self.parameter[5]))} -      link to a web resource with its signature;
{self.parameter[6]}{" " * (14 - len(self.parameter[6]))} -      your script;
{self.parameter[7]}{" " * (14 - len(self.parameter[7]))} -      numbered list;
{self.parameter[8]}{" " * (14 - len(self.parameter[8]))} -      list without numbering;
{self.parameter[9]}{" " * (14 - len(self.parameter[9]))} -      indent;
{self.parameter[10]}{" " * (14 - len(self.parameter[10]))} -      help;
{self.parameter[11]}{" " * (14 - len(self.parameter[11]))} -      save;
{self.parameter[12]}{" " * (14 - len(self.parameter[12]))} -      shutdown without saving.""")
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
    mark = Markdown()
    while True:
        print(f"""{"-" * 70}\n{"".join(mark.markdown)}\n{"-" * 70}""")
        print("Write a command:")
        action = input("• ").lower().split()
        if action[0] == mark.parameter[0]:
            mark.plain()
        elif action[0] == mark.parameter[4]:
            mark.header()
        elif action[0] == mark.parameter[5]:
            mark.link()
        elif action[0] == mark.parameter[6]:
            mark.inline_code()
        elif action[0] == mark.parameter[7]:
            mark.ordered_list()
        elif action[0] == mark.parameter[8]:
            mark.unordered_list()
        elif action[0] == mark.parameter[9]:
            mark.new_line()
        elif action[0] == mark.parameter[10]:
            mark.help()
        elif action[0] == mark.parameter[11]:
            mark.done()
        elif action[0] == mark.parameter[12]:
            mark.stop()
        else:
            print("Incorrect parameter! Please try again")

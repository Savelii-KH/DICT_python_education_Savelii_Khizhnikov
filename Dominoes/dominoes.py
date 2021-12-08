import random
dominoes = [[x, y] for x in range(0, 7) for y in range(x, 7)]
random.shuffle(dominoes)
player_d = []
comp_d = []
players = []
snake = []
height = -1
pole_snake = []
move = None

for i in range(0, 7):
    deleted_d = random.choice(dominoes)
    player_d.append(deleted_d)
    dominoes.remove(deleted_d)
for i in range(0, 7):
    deleted_d = random.choice(dominoes)
    comp_d.append(deleted_d)
    dominoes.remove(deleted_d)
players = player_d + comp_d
schedule = [i for i in players if i[0] == i[1]]
for i in schedule:
    if i[0] >= height:
        height = i[0]
        snake = i
pole_snake.append(snake)
if snake in player_d:
    player_d.remove(snake)
    move = "player"
else:
    comp_d.remove(snake)
    move = "computer"


def pole():
    print("=" * 70)
    print(f"Stock size: {len(dominoes)}")
    print(f"Computer pieces: {len(comp_d)} \n")
    if len(pole_snake) <= 6:
        print(pole_snake)
    else:
        print(f"{pole_snake[:3]} ... {pole_snake[-3:]}")
    print("\nYour pieces:")
    [print(f"{i+1}: {player_d[i]} ") for i in range(len(player_d))]


def player_move(player_action):
    global move
    if 0 < player_action <= int(len(player_d)):
        if pole_snake[-1][1] == player_d[player_action-1][0]:
            pole_snake.append(player_d[player_action-1])
            player_d.remove(player_d[player_action - 1])
            move = "computer"
        elif pole_snake[-1][1] == player_d[player_action-1][1]:
            pole_snake.append(player_d[player_action - 1][::-1])
            player_d.remove(player_d[player_action - 1])
            move = "computer"
        else:
            print("Illegal move. Please try again.")
    elif -int(len(player_d)) <= player_action < 0:
        if pole_snake[0][0] == player_d[-player_action - 1][1]:
            pole_snake.insert(0, player_d[-player_action - 1])
            player_d.remove(player_d[-player_action - 1])
            move = "computer"
        elif pole_snake[0][0] == player_d[-player_action - 1][0]:
            pole_snake.insert(0, player_d[-player_action - 1][::-1])
            player_d.remove(player_d[-player_action - 1])
            move = "computer"
        else:
            print("Illegal move. Please try again.")
    elif player_action == 0:
        player_d.append(dominoes[0])
        dominoes.remove(dominoes[0])
    elif player_action == 0:
        print("Invalid input. Please try again.")


def comp_move():
    global move
    while True:
        comp_action = random.randint(-len(comp_d)+1, len(comp_d)-1)
        if 0 < comp_action <= len(comp_d):
            if pole_snake[-1][1] == comp_d[comp_action][0]:
                pole_snake.append(comp_d[comp_action])
                comp_d.remove(comp_d[comp_action])
                move = "player"
                break
            elif pole_snake[-1][1] == comp_d[comp_action][1]:
                pole_snake.append(comp_d[comp_action][::-1])
                comp_d.remove(comp_d[comp_action])
                move = "player"
                break
            else:
                continue
        elif -len(comp_d) <= comp_action < 0:
            if pole_snake[0][0] == comp_d[-comp_action - 1][1]:
                pole_snake.insert(0, comp_d[-comp_action-1])
                comp_d.remove(comp_d[comp_action])
                move = "player"
                break
            elif pole_snake[0][0] == comp_d[-comp_action - 1][0]:
                pole_snake.insert(0, comp_d[-comp_action - 1][::-1])
                comp_d.remove(comp_d[comp_action])
                move = "player"
                break
            else:
                continue
        elif comp_action == 0:
            comp_d.append(dominoes[0])
            dominoes.remove(dominoes[0])
            move = "player"
            break


pole()
while True:
    if move == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        move = "player"
        comp_move()
    else:
        player_choice = input("Status: It's your turn to make a move. Enter your command: ")
        try:
            int(player_choice)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            if 0 <= int(player_choice) <= int(len(player_d)):
                player_move(int(player_choice))
                move = "computer"
            elif -int(len(player_d)) <= int(player_choice) < 0:
                player_move(int(player_choice))
                move = "computer"
            elif int(player_choice) == 0:
                player_move(int(player_choice))
                move = "computer"
            else:
                print("Invalid input. Please try again.")
    pole()
    if len(comp_d) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(player_d) == 0:
        print("Status: The game is over. You won!")
        break
    elif pole_snake[0][0] == pole_snake[-1][1]:
        count = 0
        for i in range(len(pole_snake)):
            for j in pole_snake[i]:
                if j == pole_snake[0][0]:
                    count += 1
        if count == 8:
            print("Status: The game is over. It's a draw!")
            break

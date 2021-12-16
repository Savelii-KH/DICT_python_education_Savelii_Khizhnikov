import random
from itertools import chain
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
    print(f"Computer pieces: {len(logic)} \n")
    if len(pole_snake) <= 6:
        print(*pole_snake)
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


def comp_logic(comp_d):
    len_comp_d = len(comp_d)
    comp_d = list(chain(*comp_d))
    value = {}
    for i in range(0, 7):
        value[i] = comp_d.count(i)
    last_dict = {}
    len_comp_dm = len(comp_d)
    for i in range(len_comp_d):
        comp_d.append(comp_d[i+i:2*i+2])
    del comp_d[:len_comp_dm]
    for i in comp_d:
        value_index = value.get(i[0])
        value_index += value.get(i[1])
        last_dict[comp_d.index(i)] = value_index
    max_value = sorted(last_dict.items(), key=lambda x: x[1], reverse=True)
    last_dict = [comp_d[c[0]] for c in max_value]
    return last_dict


comp_logic(comp_d)
logic = comp_logic(comp_d)

pole()
while True:
    if move == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        for i in range(len(logic)):
            if logic[i][0] == pole_snake[-1][1]:
                pole_snake.append(logic[i])
                logic.remove(logic[i])
                move = "player"
                break
            elif logic[i][1] == pole_snake[-1][1]:
                pole_snake.append(logic[i][::-1])
                logic.remove(logic[i])
                move = "player"
                break
            elif logic[i][1] == pole_snake[0][0]:
                pole_snake.insert(0, logic[i])
                logic.remove(logic[i])
                move = "player"
                break
            elif logic[i][0] == pole_snake[0][0]:
                pole_snake.insert(0, logic[i][::-1])
                logic.remove(logic[i])
                move = "player"
                break
        else:
            logic.append(dominoes[0])
            dominoes.remove(dominoes[0])
            move = "player"
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
    if len(logic) == 0:
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

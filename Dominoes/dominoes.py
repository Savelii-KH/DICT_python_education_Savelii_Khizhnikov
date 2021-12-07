import random
dominoes = [[x, y] for x in range(0, 7) for y in range(x, 7)]
player_d = []
comp_d = []
players = []
snake = []
height = -1
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
        snake = [i[0], i[0]]
if snake in player_d:
    player_d.remove(snake)
    move = "player"
else:
    comp_d.remove(snake)
    move = "computer"
print("=" * 70)
print(f"Stock size: {len(dominoes)}")
print(f"Computer pieces: {len(comp_d)} \n")
print(snake)
print("\nYour pieces:")
[print(f"{i+1}: {player_d[i]} ") for i in range(len(player_d))]
if move == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
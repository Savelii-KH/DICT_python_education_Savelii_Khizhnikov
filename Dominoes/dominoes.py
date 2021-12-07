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
print(f"Stock pieces: {dominoes}")
print(f"Player pieces: {player_d}")
print(f"Computer pieces: {comp_d}")
print(f"Domino snake: {snake}")
print(f"Status: {move}")

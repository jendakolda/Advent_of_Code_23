all_games = {}
limits = {'blue': 14, 'green': 13, 'red': 12}
with open('input2.txt', 'r') as source:
    for line in source.read().splitlines():
        game = line.split(':')
        all_games[int(game[0].strip('Game '))] = tuple(i.strip().split(', ') for i in tuple(game[1].strip().split(';')))

    for k, v in all_games.items():
        all_games[k] = tuple({j.split()[1]: int(j.split()[0]) for j in i} for i in v)

key_sum = 0
for key, game in all_games.items():
    for draw in game:
        for k, v in draw.items():
            if v > limits[k]:
                break
        else:
            continue
        break
    else:
        key_sum += key
print('Part A: ', key_sum)
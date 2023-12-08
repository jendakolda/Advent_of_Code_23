from collections import defaultdict

sumA = 0
card_count = defaultdict(lambda: 1)

with open('src/input4.txt', 'r') as source:
    for line in source.read().splitlines():
        game = line.split(':')
        win, numbers = game[1].strip().split('|')
        winlist = set(map(int, win.strip().split()))
        numlist = set(map(int, numbers.strip().split()))
        win_count = sum(1 for i in winlist if i in numlist)
        sumA += (2 ** (win_count - 1) if win_count else 0)

        for v in range(1, win_count + 1):
            card_count[int(game[0].strip('Card ')) + v] += card_count[int(game[0].strip('Card '))]

print(f'Part A: {sumA}\nPart B: {sum(v for v in card_count.values())}')

octopus_state = [
    [7, 3, 1, 3, 5, 1, 1, 5, 5, 1],
    [3, 7, 2, 4, 8, 5, 5, 8, 6, 7],
    [2, 3, 7, 4, 3, 3, 1, 5, 7, 1],
    [4, 4, 3, 8, 2, 1, 3, 4, 3, 7],
    [6, 5, 1, 1, 5, 6, 6, 2, 8, 7],
    [6, 7, 2, 7, 2, 4, 5, 5, 3, 2],
    [3, 7, 3, 6, 8, 6, 8, 6, 6, 2],
    [2, 3, 4, 8, 1, 3, 8, 2, 6, 3],
    [2, 4, 1, 7, 4, 8, 3, 1, 2, 1],
    [8, 8, 1, 2, 6, 1, 7, 1, 1, 2],
]


def print_state():
    for row in octopus_state:
        print(row)


def reset_flashes() -> list:
    return [[0 for col in range(10)] for row in range(10)]


def count_flashes(flashes) -> int:
    return sum(map(lambda row: sum(row), flashes))


def flash(x, y):
    if octopus_state[x][y] <= 9 or flashes[x][y] == 1:
        return

    flashes[x][y] = 1

    # -1,-1
    if x > 0 and y > 0:
        octopus_state[x - 1][y - 1] += 1
        flash(x - 1, y - 1)
    # -1,0
    if x > 0:
        octopus_state[x - 1][y] += 1
        flash(x - 1, y)
    # -1,+1
    if x > 0 and y < 9:
        octopus_state[x - 1][y + 1] += 1
        flash(x - 1, y + 1)
    # 0,-1
    if y > 0:
        octopus_state[x][y - 1] += 1
        flash(x, y - 1)
    # 0,+1
    if y < 9:
        octopus_state[x][y + 1] += 1
        flash(x, y + 1)
    # +1,-1
    if x < 9 and y > 0:
        octopus_state[x + 1][y - 1] += 1
        flash(x + 1, y - 1)
    # +1,0
    if x < 9:
        octopus_state[x + 1][y] += 1
        flash(x + 1, y)
    # +1,+1
    if x < 9 and y < 9:
        octopus_state[x + 1][y + 1] += 1
        flash(x + 1, y + 1)


total_number_of_flashes = 0
flashes = reset_flashes()

# part 2
step = 1
while True:
    # step 1 - increase all energy level
    for i, row in enumerate(octopus_state):
        for j, value in enumerate(row):
            octopus_state[i][j] += 1

    # step 2 - flashes
    for i, row in enumerate(octopus_state):
        for j, value in enumerate(row):
            flash(i, j)

    # part 1
    total_number_of_flashes += count_flashes(flashes)
    if step == 100:
        print(f"Number of flash after {step} round: {total_number_of_flashes}")

    # step 3 - reset flashed octopus to 0
    for i, row in enumerate(octopus_state):
        for j, value in enumerate(row):
            if octopus_state[i][j] > 9:
                octopus_state[i][j] = 0
    flashes = reset_flashes()

    # part 2
    if count_flashes(octopus_state) == 0:
        print(f"All octopuses flashed on step {step}")
        break
    step += 1

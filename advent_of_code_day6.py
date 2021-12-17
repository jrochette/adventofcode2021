from typing import Dict


fishes = [
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    3,
    5,
    1,
    1,
    3,
    1,
    1,
    3,
    1,
    4,
    4,
    4,
    5,
    1,
    1,
    1,
    3,
    1,
    3,
    1,
    1,
    2,
    2,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    5,
    2,
    5,
    1,
    1,
    2,
    1,
    3,
    3,
    5,
    1,
    1,
    4,
    1,
    1,
    3,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,
    1,
    5,
    1,
    2,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    4,
    5,
    1,
    1,
    3,
    4,
    1,
    1,
    1,
    3,
    5,
    1,
    1,
    1,
    2,
    1,
    1,
    4,
    1,
    4,
    1,
    2,
    1,
    1,
    2,
    1,
    5,
    1,
    1,
    1,
    5,
    1,
    2,
    2,
    1,
    1,
    1,
    5,
    1,
    2,
    3,
    1,
    1,
    1,
    5,
    3,
    2,
    1,
    1,
    3,
    1,
    1,
    3,
    1,
    3,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    4,
    1,
    1,
    3,
    2,
    1,
    2,
    1,
    1,
    2,
    2,
    1,
    2,
    1,
    1,
    1,
    4,
    1,
    2,
    4,
    1,
    1,
    4,
    4,
    1,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    1,
    2,
    1,
    1,
    2,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    3,
    1,
    1,
    2,
    3,
    4,
    4,
    1,
    1,
    1,
    3,
    2,
    4,
    4,
    1,
    1,
    3,
    5,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    5,
    3,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    4,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    3,
    1,
    4,
    1,
    1,
    2,
    2,
    2,
    1,
    1,
    2,
    1,
    1,
]


def compute_fish_reproduction_model(grouped_fishes: Dict, days: int):
    for iterator in range(days):
        # print(f"Day {iterator} - Current distribution of fishes: {grouped_fishes}")
        previous_state = dict(grouped_fishes)
        next_state = dict(grouped_fishes)
        for i in range(9):
            if i == 8:
                next_state[i] = previous_state.get(0, 0)
            elif i == 6:
                next_state[i] = previous_state.get(i + 1, 0) + previous_state.get(0, 0)
            else:
                next_state[i] = previous_state.get(i + 1, 0)
        grouped_fishes = next_state

    print(f"Total number of fish: {sum(grouped_fishes.values())}")


grouped_fishes = {}
for fish in fishes:
    if fish in grouped_fishes:
        grouped_fishes[fish] += 1
    else:
        grouped_fishes[fish] = 1

# Part 1
compute_fish_reproduction_model(dict(grouped_fishes), 80)
# Part 2
compute_fish_reproduction_model(dict(grouped_fishes), 256)
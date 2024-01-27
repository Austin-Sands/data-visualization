import plotly.express as px

from die import Die


def roll_dice():
    """Roll all dice in dice list once"""
    result = 0
    for die in dice:
        result += die.roll()

    return result


def get_max_roll():
    """return maximum possible roll of dice"""
    result = 0
    for die in dice:
        result += die.num_sides

    return result


def get_dice_string():
    """Return a string describing list of dice for figure title"""
    dice_string = ""
    last = False
    for die in dice:
        if die == dice[-1]:
            last = True
            dice_string += "and "
        dice_string += f"D{die.num_sides}"
        if not last:
            dice_string += ", "

    return dice_string


dice = []

# create dice until user stops
while True:
    new_dice_sides = input(
        "Enter sides for new dice or 'n' to finish adding dice: ")
    if new_dice_sides == 'n':
        break
    if new_dice_sides.isnumeric():
        dice.append(Die(int(new_dice_sides)))
    else:
        print(f"{new_dice_sides} is not a valid numeric value.")

# make some rolls and store results in list
results = []
results = [roll_dice() for roll_num in range(50_000)]

# get frequency of results
frequencies = []
max_roll = get_max_roll()
poss_results = range(len(dice), max_roll+1)
frequencies = [results.count(value) for value in poss_results]

# visualize the results
dice_string = get_dice_string()
title = f"Results of Rolling a {dice_string} 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customization
if len(poss_results) > 20:
    dtick = int(len(poss_results) * .05)
else:
    dtick = 1

fig.update_layout(xaxis_dtick=dtick)

fig.show()

print(frequencies)

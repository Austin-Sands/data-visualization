import plotly.express as px

from die import Die

# create two D6
die_1 = Die()
die_2 = Die()

# make some rolls and store results in list
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# get frequency of results
frequencies = []
max_roll = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_roll+1)
for value in poss_results:
    frequencies.append(results.count(value))

# visualize the results
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customization
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)

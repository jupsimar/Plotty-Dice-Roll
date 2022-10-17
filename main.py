from die import Die 
from plotly.graph_objs import Bar, Layout
from plotly import offline 

die1 = Die()
die2 = Die()

results = []
for roll_num in range(30):
    result = die1.roll() + die2.roll() 
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    freq = results.count(value)
    frequencies.append(freq)

x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result', 'dtick':1}
y_axis_config = {'title' : 'Frequency of Result'}

my_layout = Layout(title='Results of D6 and a D6 100,000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout' : my_layout}, filename='d6-d10.html')
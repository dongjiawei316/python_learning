#-*- coding:utf-8 -*-
from die import Die
import pygal

samples = "you can get more from http://pygal.org/"
s = "从入门到实践的例子-15-4"
print(s)
print(samples)

die = Die()
die1 = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    result1 = die1.roll()
    results.append(result + result1)

frequencies = []

for value in range(2, die.num_sides + die1.num_sides + 1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

#print(results)
print(frequencies)
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times"

x_lables = []

for value in range(2, 13):
    x_lables.append(str(value))

print(x_lables)
hist.x_labels = x_lables
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12']
hist.x_title = 'Result'

hist.y_title = 'Frequency of Result'
hist.add('D6 + D6', frequencies)
hist.render_to_file("die_visual1.svg")




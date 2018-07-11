#-*- coding:utf-8 -*-
from die import Die
import pygal

samples = "you can get more from http://pygal.org/"
s = "从入门到实践的例子-15-4"
print(s)
print(samples)

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, die.num_sides + 1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

#print(results)
print(frequencies)
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'

hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file("die_visual.svg")




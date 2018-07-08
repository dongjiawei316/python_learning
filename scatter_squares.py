#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
s = "从入门到实践的例子-15"
print(s)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=(0.8,0,0), edgecolor='none', s = 4)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize = 14)

#设置每一个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
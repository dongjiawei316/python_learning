#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
s = "从入门到实践的例子-15"

print(s)
squares = [1, 4, 9, 16, 25, 36]
input_values = [1, 2, 3, 4, 5, 6]

plt.plot(input_values, squares, linewidth = 5)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize = 14)

#设置标记刻度标记的大小
plt.tick_params(axis='both', labelsize=14)


plt.show()
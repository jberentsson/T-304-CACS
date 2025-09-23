import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return ((x**2) + (2*x) + 1) / ((x**2) + (3*x) + 3)


x = np.linspace(-10, 10, 1000)
y = func(x)

# High Point
high_point_x = -3
high_point_y = func(high_point_x)

# Low Point
low_point_x = -1
low_point_y = func(low_point_x)

plt.figure(figsize=(11, 6))

plt.plot(x, y, label='y = f(x)')

plt.xlabel('x')
plt.ylabel('y')

#plt.title("Plot of y = (x^2 + 2x + 1)/(x^2 + 3x + 3)")
plt.grid(True)
plt.scatter(high_point_x, high_point_y, color='red', s=100, label=f'Peak     ({high_point_x:.2f}, {high_point_y:.2f})')
plt.scatter(low_point_x, low_point_y, color='green', s=100, label=f'Bottom ({low_point_x:.2f}, {low_point_y:.2f})')

plt.yticks(np.linspace(-0.1, 1.5, 16))

plt.axhline(0, color='black', linewidth=0.5) # x-asis
plt.axvline(0, color='black', linewidth=0.5) # y-asis
plt.legend()

plt.savefig('plot.png', dpi=500, bbox_inches='tight')

plt.show()



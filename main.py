import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
ax = plt.gca()

ax.set_aspect('equal', 'box')
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))

def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color = 'w', linewidth = 2, fill = False)
    ax.add_patch(circle)
    plt.plot([np.cos(-np.pi / 6), np.cos(np.pi / 2)], [np.sin(-np.pi / 6), np.sin(np.pi / 2)], linewidth = 2, color = 'green')
    plt.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)], [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='green')
    plt.plot([np.cos(7 * np.pi / 6), np.cos(-np.pi / 6)], [np.sin(7 * np.pi / 6), np.sin(-np.pi / 6)], linewidth=2, color='green')
    plt.show()

def show_random(ax, n):
    ct = 0
    while(n):
        n1, n2 = np.random.random() * 2 - 1, np.random.random() * 2 - 1
        x1, x2 = np.cos(n1 * np.pi), np.cos(n2 * np.pi)
        y1, y2 = np.sin(n1 * np.pi), np.sin(n2 * np.pi)

        n -= 1
        length = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if(length > np.sqrt(3)):
            plt.plot([x1, x2], [y1, y2], linewidth = 0.5, color = 'red', alpha = 0.2)
            ct += 1
        else:
            plt.plot([x1, x2], [y1, y2], linewidth=0.5, color='blue', alpha = 0.2)
    print(ct)

def ok(ax,n):
    ct = 0
    while(n):
        o = np.random.random() * 2 * np.pi
        r = np.random.random()
        x = r * np.cos(o)
        y = r * np.sin(o)
        n -= 1
        p = np.arccos(r)
        x1, x2 = np.cos(o - p), np.cos(o + p)
        y1, y2 = np.sin(o - p), np.sin(o + p)
        length = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if (length > np.sqrt(3)):
            plt.scatter(x, y, linewidth=0.2, color='blue')
            ct += 1
        else: plt.scatter(x, y, linewidth = 0.2, color='red', alpha = 0.5)
    print(ct)
show_random(ax, 1000)
ok(ax, 1000)
draw_circle_and_triangle(ax)
import matplotlib.pyplot as plt
import numpy as np


def draw_tree(ax, x, y, size, angle, level):
    if level == 0:
        return

    # Розрахунок координат наступного квадрата
    x0, y0 = x, y
    x1 = x0 + size * np.cos(angle)
    y1 = y0 + size * np.sin(angle)

    # Малювання квадрата
    ax.plot([x0, x1], [y0, y1], color='brown', lw=2)

    # Координати наступного рівня
    new_size = size * np.sqrt(0.5)  # Зменшення розміру квадрата
    angle_left = angle + np.pi / 3.5  # Трохи більший кут для лівої гілки
    angle_right = angle - np.pi / 6  # Трохи менший кут для правої гілки

    # Рекурсія для лівої та правої гілок
    draw_tree(ax, x1, y1, new_size, angle_left, level - 1)
    draw_tree(ax, x1, y1, new_size, angle_right, level - 1)


def pythagoras_tree(level):
    # Налаштування графіка
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'Pythagoras Tree (Level {level})')

    # Початкові умови з нахилом вправо
    size = 1.0
    angle = np.pi / 2.2  # Початковий нахил вправо
    x, y = 0, 0  # Початкова координата

    # Виклик рекурсивної функції для малювання дерева
    draw_tree(ax, x, y, size, angle, level)
    plt.show()


# Виклик функції з рівнем рекурсії
level = 5
pythagoras_tree(level)

level = 8
pythagoras_tree(level)

level = 10
pythagoras_tree(level)

level = 12
pythagoras_tree(level)

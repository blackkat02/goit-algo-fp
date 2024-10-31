from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий нащадок вузла
        self.right = None  # Правий нащадок вузла
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def get_all_nodes(root):
    """Функція для підрахунку всіх вузлів дерева.
    Використовує чергу для обходу вузлів дерева в ширину."""
    nodes = []
    queue = deque([root])  # Ініціалізуємо чергу, додаючи корінь дерева
    while queue:
        node = queue.popleft()  # Вилучаємо вузол з початку черги
        nodes.append(node)  # Додаємо вузол до списку всіх вузлів
        if node.left:  # Якщо існує лівий нащадок
            queue.append(node.left)  # Додаємо лівого нащадка до черги
        if node.right:  # Якщо існує правий нащадок
            queue.append(node.right)  # Додаємо правого нащадка до черги
    return nodes  # Повертаємо список всіх вузлів


def get_color_gradient(step, total_steps, start_color="#8B0000", end_color="#FFC0CB"):
    """Генерує колір між стартовим та кінцевим значенням у градієнті RGB.
    Використовує відображення кольору від темно-червоного до світло-рожевого."""
    # Конвертуємо стартовий і кінцевий кольори з 16-системи у RGB
    start_color_rgb = tuple(int(start_color[i:i + 2], 16) for i in (1, 3, 5))
    end_color_rgb = tuple(int(end_color[i:i + 2], 16) for i in (1, 3, 5))

    # Вираховуємо новий колір на основі поточного кроку і загальної кількості кроків
    new_color_rgb = tuple(
        int(start_color_rgb[i] + (end_color_rgb[i] - start_color_rgb[i]) * step / total_steps) for i in range(3))

    # Повертаємо колір у 16-системі
    return f"#{new_color_rgb[0]:02x}{new_color_rgb[1]:02x}{new_color_rgb[2]:02x}"


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає ребра до графа на основі структури дерева."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол до графа
        if node.left:  # Якщо є лівий нащадок
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро між вузлом і його лівим нащадком
            l = x - 1 / 2 ** layer  # Обчислюємо нову позицію для лівого нащадка
            pos[node.left.id] = (l, y - 1)  # Встановлюємо позицію лівого нащадка
            add_edges(graph, node.left, pos, x=l, y=y - 1,
                      layer=layer + 1)  # Рекурсивно додаємо ребра для лівого піддерева
        if node.right:  # Якщо є правий нащадок
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро між вузлом і його правим нащадком
            r = x + 1 / 2 ** layer  # Обчислюємо нову позицію для правого нащадка
            pos[node.right.id] = (r, y - 1)  # Встановлюємо позицію правого нащадка
            add_edges(graph, node.right, pos, x=r, y=y - 1,
                      layer=layer + 1)  # Рекурсивно додаємо ребра для правого піддерева


def draw_tree(tree_root):
    """Візуалізує дерево за допомогою бібліотеки NetworkX і Matplotlib."""
    tree = nx.DiGraph()  # Створюємо направлений граф
    pos = {tree_root.id: (0, 0)}  # Встановлюємо позицію кореня дерева
    add_edges(tree, tree_root, pos)  # Додаємо ребра до графа

    # Отримуємо кольори та мітки вузлів для відображення
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))  # Налаштовуємо розмір фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Відображаємо граф
    plt.show()  # Показуємо графік


def bfs_visualize(root):
    """Візуалізація обходу дерева в ширину (BFS)."""
    queue = deque([root])  # Ініціалізуємо чергу з коренем
    steps = 0  # Лічильник кроків
    total_steps = len(get_all_nodes(root))  # Загальна кількість вузлів у дереві

    while queue:  # Поки черга не порожня
        node = queue.popleft()  # Вилучаємо вузол з початку черги
        node.color = get_color_gradient(steps, total_steps)  # Змінюємо колір вузла відповідно до кроку
        draw_tree(root)  # Візуалізуємо дерево
        steps += 1  # Збільшуємо лічильник кроків
        if node.left:  # Якщо є лівий нащадок
            queue.append(node.left)  # Додаємо лівого нащадка до черги
        if node.right:  # Якщо є правий нащадок
            queue.append(node.right)  # Додаємо правого нащадка до черги


def dfs_visualize(root):
    """Візуалізація обходу дерева в глибину (DFS)."""
    stack = [root]  # Ініціалізуємо стек з коренем
    steps = 0  # Лічильник кроків
    total_steps = len(get_all_nodes(root))  # Загальна кількість вузлів у дереві

    while stack:  # Поки стек не порожній
        node = stack.pop()  # Вилучаємо вузол з верхівки стеку
        node.color = get_color_gradient(steps, total_steps)  # Змінюємо колір вузла відповідно до кроку
        draw_tree(root)  # Візуалізуємо дерево
        steps += 1  # Збільшуємо лічильник кроків
        if node.right:  # Якщо є правий нащадок
            stack.append(node.right)  # Додаємо правого нащадка до стеку
        if node.left:  # Якщо є лівий нащадок
            stack.append(node.left)  # Додаємо лівого нащадка до стеку


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(5)

# Запуск обходів
print("Візуалізація BFS:")
bfs_visualize(root)  # Виконуємо візуалізацію обходу в ширину

# Скидаємо кольори
for node in get_all_nodes(root):
    node.color = "skyblue"  # Скидаємо кольори для наступного обходу

print("Візуалізація DFS:")
dfs_visualize(root)  # Виконуємо візуалізацію обходу в глибину

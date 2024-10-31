import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Клас Node для вузлів дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла (за замовчуванням "skyblue")
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання вузлів та ребер у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол до графа
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро до лівого нащадка
            l = x - 1 / 2 ** layer  # Позиція лівого вузла
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро до правого нащадка
            r = x + 1 / 2 ** layer  # Позиція правого вузла
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Позиція кореневого вузла
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Кольори вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Мітки вузлів

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови дерева з купи
def build_tree_from_heap(heap):
    nodes = [Node(val) for val in heap]  # Створюємо вузли для кожного елемента купи
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]  # Зв'язуємо лівого нащадка
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]  # Зв'язуємо правого нащадка
    return nodes[0] if nodes else None  # Повертаємо корінь дерева

# Функція для побудови мін-куп
def create_min_heap(data):
    min_heap = data.copy()
    heapq.heapify(min_heap)  # Перетворюємо список на мін-купу
    print("Мін-купа як список:", min_heap)
    root = build_tree_from_heap(min_heap)
    draw_tree(root)

# Функція для побудови макс-куп
def create_max_heap(data):
    max_heap = [-i for i in data]  # Інвертуємо значення для побудови макс-купи
    heapq.heapify(max_heap)  # Створюємо мін-купу із інвертованих значень
    max_heap = [-i for i in max_heap]  # Повертаємо значення до початкових
    print("Макс-купа як список:", max_heap)
    root = build_tree_from_heap(max_heap)
    draw_tree(root)

# Вхідні дані для створення купи
data = [15, 10, 7, 3, 1, 6, 5, 2, 8, 7]

# Побудова та візуалізація мін-купи
print("Побудова мін-купи:")
create_min_heap(data)

# Побудова та візуалізація макс-купи
print("\nПобудова макс-купи:")
create_max_heap(data)

data.append(8)
# Побудова та візуалізація мін-купи після додавання елемента
print("Побудова мін-купи:")
create_min_heap(data)

# Побудова та візуалізація макс-купи після додавання елемента
print("\nПобудова макс-купи:")
create_max_heap(data)

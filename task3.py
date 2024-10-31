import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Граф для транспортної мережі
graph = {
    "Київ": [("Умань", 200), ("Житомир", 140), ("Полтава", 350), ("Чернігів", 150), ("Кропивницький", 300)],
    "Умань": [("Київ", 200), ("Первомайськ", 100), ("Одеса", 300), ("Вінниця", 160), ("Кропивницький", 160)],
    "Первомайськ": [("Умань", 100), ("Вознесенськ", 70), ("Кропивницький", 130)],
    "Миколаїв": [("Вознесенськ", 100), ("Одеса", 140), ("Херсон", 70), ("Кропивницький", 120)],
    "Вінниця": [("Умань", 160), ("Житомир", 120)],
    "Одеса": [("Вознесенськ", 120), ("Миколаїв", 140), ("Ізмаїл", 250)],
    "Черкаси": [("Київ", 170), ("Полтава", 220)],
    "Кропивницький": [("Київ", 300), ("Черкаси", 130), ("Умань", 160)],
    "Житомир": [("Київ", 140), ("Вінниця", 120)],
    "Полтава": [("Київ", 350), ("Черкаси", 220)],
    "Чернігів": [("Київ", 350)],
    "Вознесенськ": [("Первомайськ", 70), ("Миколаїв", 140), ("Одеса", 120)],
    "Ізмаїл": [("Одеса", 250)],
    "Херсон": [("Миколаїв", 70)],
}

# Координати міст
coordinates = {
    "Київ": (50.45, 30.52),
    "Умань": (48.75, 30.22),
    "Житомир": (50.25, 28.67),
    "Полтава": (49.59, 34.54),
    "Чернігів": (51.49, 31.30),
    "Первомайськ": (48.04, 30.85),
    "Вознесенськ": (47.56, 31.33),
    "Одеса": (46.48, 30.73),
    "Вінниця": (49.23, 28.48),
    "Херсон": (46.63, 32.62),
    "Ізмаїл": (45.35, 28.84),
    "Черкаси": (49.43, 32.06),
    "Кропивницький": (48.50, 32.27),
    "Миколаїв": (46.97, 31.99)
}

# Створення об'єкта графа
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Візуалізація стану купи на кожному кроці алгоритму
def visualize_heap(heap):
    print("Стан купи:", sorted(heap))

# Алгоритм Дейкстри для знаходження найкоротших шляхів
def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Пріоритетна черга для вузлів (відстань, вузол)
    visited = set()

    while priority_queue:
        # Витягуємо вузол з найменшою відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо вузол вже відвіданий, ігноруємо його
        if current_node in visited:
            continue
        visited.add(current_node)

        # Оновлюємо сусідів
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                # Візуалізація купи після кожного оновлення
                visualize_heap(priority_queue)

    return distances

# Виконуємо алгоритм Дейкстри та виводимо результати
for start_node in graph:
    print(f"\nShortest paths from {start_node}:")
    shortest_paths = dijkstra(graph, start_node)
    for node, distance in shortest_paths.items():
        print(f"Відстань до {node}: {distance} км")

# Візуалізація графа з використанням географічних координат
if __name__ == "__main__":
    pos = {node: (long, lat) for node, (lat, long) in coordinates.items()}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_color='black')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title('Transport Network for Logistics Company')
    plt.show()

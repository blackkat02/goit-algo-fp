import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> "

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, node):
        if self.head is None:
            return
        if self.head == node:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next == node:
                current.next = current.next.next
                return
            current = current.next

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def change(self):
        first_node = self.head
        while first_node and first_node.next:
            next_node = first_node.next
            self.delete_node(next_node)
            self.insert_at_beginning(next_node.data)
        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def visualize(self):
        G = nx.DiGraph()
        current = self.head
        while current and current.next:
            G.add_edge(current.data, current.next.data)
            current = current.next

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_color='black')
        plt.title('Visualization of Linked List')
        plt.show()


# Приклад використання зв'язного списку
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(3)
llist.insert_at_beginning(2)
llist.insert_at_beginning(1)

# Вставляємо вузли в кінець
llist.insert_at_end(4)
llist.insert_at_end(5)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Візуалізація зв'язаного списку
llist.visualize()

llist.change()
print("\nЗв'язний список після change:")
llist.print_list()
llist.visualize()



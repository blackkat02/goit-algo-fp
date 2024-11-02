import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def reverse(self):
        first_node = self.head
        while first_node and first_node.next:
            next_node = first_node.next
            self.delete_node(next_node)
            self.insert_at_beginning(next_node.data)
        return

    def insertion_sort_nod(self):
        if self.head is None:
            return

        sorted_list = Node(0)  # Віртуальний початковий вузол для впорядкованого списку
        current = self.head  # Поточний вузол в оригінальному списку

        while current is not None:
            next_node = current.next  # Зберігаємо наступний вузол

            # Знаходимо місце для вставки поточного вузла в упорядкованому списку
            prev = sorted_list
            while prev.next is not None and prev.next.data < current.data:
                prev = prev.next

            # Вставка поточного вузла
            current.next = prev.next
            prev.next = current

            # Переход до наступного вузла в оригінальному списку
            current = next_node

        # Оновлюємо голову списку
        self.head = sorted_list.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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


def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    if p1:
        tail.next = p1
    if p2:
        tail.next = p2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Приклад використання зв'язного списку
llist = LinkedList()
plist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(3)
llist.insert_at_beginning(2)
llist.insert_at_beginning(1)
llist.insert_at_beginning(7)
llist.insert_at_beginning(8)
llist.insert_at_beginning(10)

plist.insert_at_end(1)
plist.insert_at_end(7)
plist.insert_at_end(4)
plist.insert_at_end(3)

# Вставляємо вузли в кінець
llist.insert_at_end(4)
llist.insert_at_end(5)

# Друк зв'язного списку
print("Зв'язний список до сортування:")
llist.print_list()
plist.print_list()

# Візуалізація зв'язаного списку
llist.visualize()
plist.visualize()

llist.reverse()
plist.reverse()
print("\nЗв'язний список після reverse:")
llist.print_list()
plist.print_list()
llist.visualize()
plist.visualize()

llist.insertion_sort_nod()
plist.insertion_sort_nod()
print("\nЗв'язний після insertion_sort:")
llist.print_list()
plist.print_list()
llist.visualize()
plist.visualize()

merged_list = merge_two_sorted_lists(llist, plist)
print("Злитий відсортований список:")
merged_list.print_list()
merged_list.visualize()


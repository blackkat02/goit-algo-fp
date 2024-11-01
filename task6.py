from typing import List, Dict
from colorama import Fore, Style
from tabulate import tabulate


class Item:
    """
    Class to store information about an item.

    Attributes:
    name (str): The name of the item.
    calories (int): The number of calories in the item.
    cost (int): The cost of the item.
    ratio (float): The ratio of calories to cost.
    """
    def __init__(self, name: str, cost: int, calories: int):
        self.name = name
        self.calories = calories
        self.cost = cost
        self.ratio = calories / cost

def greedy_algorithm(d_items: Dict[str, Dict[str, int]], max_costs: int) -> tuple[list[str], int, int, list[float]]:
    """
    Greedy algorithm for selecting items based on maximum budget.

    Arguments:
    d_items (Dict[str, Dict[str, int]]): Dictionary containing information about items.
    max_costs (int): The maximum budget.

    Returns:
    List[str]: List of selected item names.
    """
    items = []
    selected_list = []

    # Створення списку об'єктів Item з даних словника
    for i in d_items:
        name, cost, calories = i, d_items[i]['cost'], d_items[i]['calories']
        items.append(Item(name, cost, calories))

    # Сортування продуктів за співвідношенням калорій до вартості у спадному порядку
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_calories = 0
    total_cost = 0
    ratios = []

    # Вибір продуктів поки не вичерпано бюджет
    for item in items:
        if max_costs >= item.cost:
            max_costs -= item.cost
            total_cost += item.cost
            total_calories += item.calories
            selected_list.append(item.name)
            ratios.append(item.ratio)

    return selected_list, total_cost, total_calories, ratios


def dynamic_programming(W: int, wt: List[int], val: List[int], n: int, name: List[str]) -> tuple[
    list[str], int, int, list[float]]:
    """
    Dynamic programming algorithm for selecting items based on maximum budget.

    Arguments:
    W (int): The maximum budget.
    wt (List[int]): List of item costs.
    val (List[int]): List of item calories.
    n (int): Number of items.
    name (List[str]): List of item names.

    Returns:
    List[str]: List of selected item names.
    """
    # Створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Будуємо таблицю K знизу вгору
    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Для відновлення вибраних предметів
    selected_items = []
    total_costs_list = []
    ratios = []
    remaining_capacity = W

    for i in range(n, 0, -1):
        if K[i][remaining_capacity] != K[i - 1][remaining_capacity]:
            selected_items.append(name[i - 1])
            total_costs_list.append(wt[i - 1])
            ratios.append(val[i - 1] / wt[i - 1])
            remaining_capacity -= wt[i - 1]

    selected_items.reverse()
    ratios.reverse()
    total_costs = sum(total_costs_list)
    total_calories = K[n][W]

    return selected_items, total_costs, total_calories, ratios


def parser(d_items: Dict[str, Dict[str, int]], max_costs: int) -> tuple[list[str], int, int, list[float]]:
    """
    Parses the item dictionary and calls the dynamic programming algorithm.

    Arguments:
    d_items (Dict[str, Dict[str, int]]): Dictionary containing information about items.
    max_costs (int): The maximum budget.

    Returns:
    List[str]: List of selected item names.
    """
    name = []
    value = []
    weight = []

    for item_name, details in d_items.items():
        name.append(item_name)
        value.append(details["calories"])
        weight.append(details["cost"])

    return dynamic_programming(max_costs, weight, value, len(d_items), name)


# Дані продуктів
list_items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def display_results(budget: int):
    """
    Display the results of both greedy and dynamic programming algorithms for a given budget.

    Arguments:
    budget (int): The maximum budget.
    """
    greedy_result = greedy_algorithm(list_items, budget)
    dp_result = parser(list_items, budget)

    # Перевірка на співпадіння результатів
    if greedy_result[1] == dp_result[1] and greedy_result[2] == dp_result[2]:
        color = Fore.GREEN
        match_status = "Results match."
    else:
        color = Fore.RED
        match_status = "Results differ."

    # Таблиця з результатами
    table_data = [
        ["Algorithm", "Items", "Total Cost", "Total Calories", "Ratios"],
        ["Greedy", greedy_result[0], greedy_result[1], greedy_result[2], [f"{r:.2f}" for r in greedy_result[3]]],
        ["Dynamic Programming", dp_result[0], dp_result[1], dp_result[2], [f"{r:.2f}" for r in dp_result[3]]]
    ]

    # Друк таблиці з кольоровим оформленням
    print(f"\n{color}Budget: {budget}{Style.RESET_ALL}")
    print(f"{color}{tabulate(table_data, headers='firstrow', tablefmt='grid')}{Style.RESET_ALL}")
    print(f"{color}{match_status}{Style.RESET_ALL}")


# Приклади результатів для різних бюджетів
display_results(150)
display_results(100)
display_results(40)
display_results(120)

import random
import collections
import matplotlib.pyplot as plt


def imitation_cubes(n):
    """
    Function to simulate the rolling of two dice.

    Arguments:
    n (int): Number of simulations.

    Returns:
    collections.Counter: A counter of the sums of the dice rolls.
    """
    cubes_marks = []
    for _ in range(n):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        res = cube1 + cube2
        cubes_marks.append(res)
    cubes_counts_dict = collections.Counter(cubes_marks)
    return cubes_counts_dict


def calculate_probabilities(cubes_counts_dict, total_rolls):
    """
    Calculate the probabilities of each sum based on the simulation results.

    Arguments:
    cubes_counts (collections.Counter): Counter of the sums of dice rolls.
    total_rolls (int): Total number of dice rolls.

    Returns:
    dict: A dictionary of sums and their probabilities.
    """
    probabilities = {sum_val: count / total_rolls for sum_val, count in cubes_counts_dict.items()}
    return probabilities


def plot_probabilities(probabilities):
    """
    Plot a bar chart of the probabilities of each sum.

    Arguments:
    probabilities (dict): A dictionary of sums and their probabilities.
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Sums of Two Dice Rolls')
    plt.xticks(sums)
    plt.show()


# Number of simulations
num_simulations = 10000

# Simulate dice rolls
cubes_counts = imitation_cubes(num_simulations)

# Calculate probabilities
probabilities = calculate_probabilities(cubes_counts, num_simulations)

# Print results
print("Sum\tProbability")
for sum_val, prob in probabilities.items():
    print(f"{sum_val}\t{prob:.4f}")

# Plot probabilities
plot_probabilities(probabilities)

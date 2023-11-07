import time

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_unit = value / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.value_per_unit, reverse=True)
    total_value = 0
    selected_items = []

    start_time = time.time()
    for item in items:
        if capacity >= item.weight:
            total_value += item.value
            selected_items.append(item)
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += fraction * item.value
            selected_items.append(Item(item.weight * fraction, item.value * fraction))
            break
    end_time = time.time()

    total_time = end_time - start_time
    return total_value, selected_items, total_time

def main():
    items = []
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1} (separated by space): ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the capacity of the knapsack: "))

    total_value, selected_items, total_time = fractional_knapsack(items, capacity)

    print("Selected items:")
    for item in selected_items:
        print(f"Weight: {item.weight}, Value: {item.value}")

    print("Total value in the knapsack:", total_value)
    print("Total time taken:", total_time, "seconds")

if __name__ == "__main__":
    main()


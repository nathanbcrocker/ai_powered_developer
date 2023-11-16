import math
import statistics

def std_dev_chat_gpt_attempt_1(lst):
    # Step 1: Calculate the mean
    mean = sum(lst) / len(lst)

    # Step 2: Find squared differences
    squared_diffs = [(x - mean) ** 2 for x in lst]

    # Step 3: Compute the mean of squared differences
    mean_squared_diffs = sum(squared_diffs) / len(lst)

    # Step 4: Square root of the mean squared differences
    std_dev = mean_squared_diffs ** 0.5

    return std_dev


def std_dev_llama_attempt_1(numbers):
    n = len(numbers)
    sum = 0
    for i in range(n):
        sum += numbers[i] ** 2
    return math.sqrt(sum / (n - 1))


def std_dev_llama_attempt_2(numbers):
    sum_squared = 0
    mean = statistics.mean(numbers)
    for num in numbers:
        sum_squared += (num - mean) ** 2

    # Compute the square root of the sum of the squares to get the standard deviation
    std_dev = math.sqrt(sum_squared/len(numbers))
    return std_dev


def std_dev_mistrail_attempt_1(numbers):
    mean = sum(numbers) / len(numbers)
    
    differences = [x - mean for x in numbers]  # Subtract the mean from each number.
    squared_differences = [y * y for y in differences]  # Square each difference.
    
    variance = sum(squared_differences) / len(numbers)  # Calculate average of squared differences (variance).
    return math.sqrt(variance)  # Return the standard deviation.



if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(std_dev_chat_gpt_attempt_1(numbers))
    print(std_dev_llama_attempt_1(numbers))
    print(std_dev_llama_attempt_2(numbers))
    print(std_dev_mistrail_attempt_1(numbers))

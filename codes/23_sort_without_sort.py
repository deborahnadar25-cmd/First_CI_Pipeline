
def bubble_sort(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    numbers = [5, 2, 9, 1]
    print(bubble_sort(numbers))

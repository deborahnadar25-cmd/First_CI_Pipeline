
def rotate_list(items, k):
    if len(items) == 0:
        return []

    k = k % len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))


def is_anagram(first, second):
    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")

    return sorted(first) == sorted(second)


print(is_anagram("Listen", "Silent"))
print(is_anagram("Hello", "World"))

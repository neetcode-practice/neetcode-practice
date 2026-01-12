from typing import List


# def string_length(s):
#     return len(s)

# def number_abs(num):
#     return abs(num)

# def sort_words(words: List[str]) -> List[str]:
#     len_sorted_words = words
#     len_sorted_words.sort(key=string_length, reverse=True)
#     return len_sorted_words


# def sort_numbers(numbers: List[int]) -> List[int]:
#     abs_sorted_numbers = numbers
#     abs_sorted_numbers.sort(key=number_abs)
#     return abs_sorted_numbers


def sort_words(words: List[str]) -> List[str]:
    len_sorted_words = words
    len_sorted_words.sort(key=len, reverse=True)
    return len_sorted_words


def sort_numbers(numbers: List[int]) -> List[int]:
    abs_sorted_numbers = numbers
    abs_sorted_numbers.sort(key=abs)
    return abs_sorted_numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

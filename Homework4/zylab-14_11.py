# Name: Quang Le
# Student ID: 1768324


def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if int(numbers[j]) > int(numbers[index_largest]):
                index_largest = j

        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp

        for num in numbers:
            print(str(num), end=' ')
        print()

if __name__ == "__main__":
    numbers = input().split()

    selection_sort_descend_trace(numbers)


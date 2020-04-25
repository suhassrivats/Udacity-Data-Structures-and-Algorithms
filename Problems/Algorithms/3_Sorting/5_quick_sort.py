def sort_a_little_bit(items, start_index, end_index):
    # Choose a pivot index
    left_index = start_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:
        item = items[left_index]
        if item <= pivot_value:
            left_index += 1
            continue
        else:
            # Place item before pivot to left index
            items[left_index] = items[pivot_index-1]
            # Shift pivot to the left
            items[pivot_index-1] = items[pivot_index]
            # Place the item to pivot's previous position
            items[pivot_index] = item
            # Update pivot index
            pivot_index -= 1

    return pivot_index


def sort_all(items, start_index, end_index):
    if end_index <= start_index:
        return

    pivot_index = sort_a_little_bit(items, start_index, end_index)
    sort_all(items, start_index, pivot_index-1)
    sort_all(items, pivot_index+1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items)-1)


# Tests
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)

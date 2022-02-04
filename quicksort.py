def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    
    print(quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


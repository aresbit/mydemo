def bubble_sort(lst: list[int]) ->list[int]:
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			if lst[i] > lst[j]:
				lst[i], lst[j] = lst[j], lst[i]
	return lst

if __name__ == '__main__':
	lst = [3, 2, 1, 5, 4]
	print(bubble_sort(lst))
def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0] # Управляющее число (опорный элемент)
		less = [i for i in array[1:] if i <= pivot] # Числа меньше управляющего числа.

		greater = [i for i in array[1:] if i > pivot ]
		return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
	print(quicksort([1, 314, 234, 12, 13]))


def binary_search(list_:list, item):
	low = 0
	high = len(list_) - 1

	while low <= high:
		mid = (low + high)//2
		guess = list_[mid]

		if guess == item:
			return mid

		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 5, 7, 8, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -3))
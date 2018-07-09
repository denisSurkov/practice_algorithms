
def count_list(list_:list):
	if not list_:
		return 0
	return 1 + count_list(list_[1:])

if __name__ == '__main__':
	print(count_list([1, 3, 4, 5, 7, 10]))
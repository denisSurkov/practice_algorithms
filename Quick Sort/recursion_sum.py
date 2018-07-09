
def sum(arr:list):
	if not arr:
		return 0
	return (arr[0] + sum(arr[1:]))

if __name__ == '__main__':
	print(sum([1, 13, 14]))
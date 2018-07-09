

def max_in_list(list_:list):
	if len(list_) == 2:
		if list_[0] >= list_[1]:
			return list_[0]
		return list_[1]
	else:
		other_max = max(list_[1:])
		if list_[0] >= other_max:
			return list_[0]
		return other_max

if __name__ == '__main__':
	print(max_in_list([30, 1, 2, 3, 10, 2334, 10]))

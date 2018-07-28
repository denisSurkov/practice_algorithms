def get_absolute_residual(list_: list) -> list:
    res = []
    for i in range(len(list_) - 1):
        res.append(abs(list_[i] - list_[i + 1]))
    return sorted(res)


user_arr = list(map(int, input().split()))
n = len(user_arr)

if n == 1:
    print('Jolly')
else:
    print(get_absolute_residual(user_arr))
    for correct, from_array in enumerate(1, get_absolute_residual(user_arr)):
        print(correct, from_array)
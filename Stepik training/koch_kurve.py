import itertools

def get_degrees(n):
    if n == 1:
        return [60, -120, 60]
    return [*get_degrees(n - 1), 60, *get_degrees(n - 1), -120, *get_degrees(n - 1), 60, *get_degrees(n- 1)]


if __name__ == '__main__':
    res = get_degrees(int(input()))
    for i in res:
        print(f'turn {i}')
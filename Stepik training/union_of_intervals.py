def is_in_interval(num):
    return num == -10 or \
           -5 < num <= 3 or \
           8 < num < 12 or \
           16 <= num

print(is_in_interval(int(input())))
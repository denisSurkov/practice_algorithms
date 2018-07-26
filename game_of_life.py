from functools import lru_cache

def parse_line(line):
    return [1 if i == 'X' else 0 for i in line]

def get_zero_generation(ground):
    for col in range(len(ground)):
        input_line = input()
        converted_line = parse_line(input_line)
        ground[col] = converted_line
    return ground


def show_pretty_ground(ground):
    for col in range(len(ground)):
        current_row = ground[col]
        for cell in range(len(current_row)):
            print('X' if current_row[cell] == 1 else '.', end='')
        print()


def get_table(cols, rows):
    return [[0 for i in range(rows)] for n in range(cols)]


def main():
    cols, rows = map(int, input().split())
    ground = get_table(cols, rows)
    ground = get_zero_generation(ground)
    first_generation = generate_life(ground, 1)
    show_pretty_ground(first_generation)

@lru_cache(maxsize=30)
def get_correct_index(list_length, index):
    return index % list_length


def get_naighbor_cells(ground: list, row: int, coll: int) -> list:
    check_row = (-1, -1, 0, 1, 1, 1, 0, -1)
    check_coll = (0, -1, -1, -1, 0, 1, 1, 1)
    check_list = zip(check_coll, check_row)

    ans = []

    for coordinates in check_list:
        add_to_row, add_to_coll = coordinates
        correct_coll = get_correct_index(len(ground[0]), coll + add_to_coll)
        correct_row = get_correct_index(len(ground), row + add_to_row)
        ans.append(ground[correct_row][correct_coll])

    return ans


def generate_life(zero_generation, generation_count=1):
    generate_count = 0
    prev_generation = zero_generation
    cur_generation = get_table(len(zero_generation), len(zero_generation[0]))

    while generate_count < generation_count:

        for row in range(len(prev_generation)):
            for coll in range(len(prev_generation[row])):
                current_cell = prev_generation[row][coll]

                neighbors_sum = sum(get_naighbor_cells(prev_generation, row, coll))

                if neighbors_sum == 3:
                    cur_generation[row][coll] = 1
                elif current_cell and neighbors_sum == 2 or neighbors_sum == 3:
                    cur_generation[row][coll] = 1
                else:
                    cur_generation[row][coll] = 0


        generate_count += 1

    return cur_generation

if __name__ == '__main__':
    main()
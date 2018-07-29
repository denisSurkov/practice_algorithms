
items = [['water', 3, 10], ['book', 1, 3], ['food', 2, 9], ['jacket', 2, 5], ['camera', 1, 6]]

table = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


what_to_take = []

smth = []

for i in range(len(items)):
    current_item = items[i][0]
    current_weight = items[i][1] - 1  # - 1 for index from 0 to len - 1
    current_score = items[i][2]

    for j in range(len(table[i])):
        if j >= current_weight:
            # Сколько можно ещё положить
            costs = j - current_weight
            print(current_item, j, costs)
            # Если costs = 0 и ячейка в текущем столбце в предыдущей строке меньше чем эта ячейка
            # то меняем значение на текущее (без сложения, т.к не остаётся больше свободного места)
            if costs == 0:
                if i - 1 == -1:
                    table[i][j] = current_score
                    continue

                prev_score = table[i - 1][j]

                if current_score > prev_score:
                    table[i][j] = current_score
                else:
                    table[i][j] = prev_score
                continue
            # Если же costs > 0, то нам нужно вычислить максимум из оставшейся ячейки (j - costs) + j - 1
            else:
                if i - 1 == - 1:
                    table[i][j] = current_score
                    continue

                prev_score = table[i - 1][j]
                new_score = table[i - 1][costs - 1] + current_score

                if new_score > prev_score:
                    if what_to_take:
                        what_to_take.pop()
                    what_to_take.append(current_item)

                table[i][j] = max(prev_score, new_score)

        else:
            if i - 1 == -1:
                continue

            table[i][j] = table[i - 1][j]


best_score = table[-1][-1]

[print(i) for i in table]

# Нужно понять, как получили best score
for i in range(len(table) -1, -1, -1):
    print(i)
    current_item = items[i][0]
    current_weight = items[i][1] - 1
    current_score = items[i][2]

    if i - 1 != -1:
        foo = table[i][current_weight] + table[i - 1][len(table[i]) - 1 - current_weight]
        print(current_item, table[i][current_weight] == current_score, table[i - 1][len(table[i]) - current_weight - 1])
    else:
        foo = table[i][current_weight] + table[i][len(table[i]) - 1 - current_weight]

    print(foo)

    if best_score == foo:
        what_to_take.append(current_item)
        best_score = table[i - 1][len(table[i]) - current_weight]

print(what_to_take)
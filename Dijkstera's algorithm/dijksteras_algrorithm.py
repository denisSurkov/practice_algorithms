
def find_lowest_cost_node(costs):
    global processed
    lowest_cost = float('inf')
    lowest_cost_node = None

    # Перебор всех стоимостей узлов
    for node in costs:
        cost = costs[node]  # Текушая стоимость

        # Если текущая стоимость меньше предыдущих стоимостей
        # И если узел ещё не был проверен
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # Наименьшой стоимостей теперь считается текущая
            lowest_cost_node = node  # Узлом с наименьшей стоимостей считается текущей

    return lowest_cost_node

# Инициализация графа путей
graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = dict()
graph['a']['final'] = 1

graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['final'] = 5

# Конечный узел. Соседей нет
graph['final'] = dict()


# Инициализаця начальной (! т.е первой, потом цены могут меняться) таблицы стоимости.
costs = dict()
costs['a'] = 6  # Перейти от start к a стоит 6 (возможно пока что!)
costs['b'] = 2  # Перейти от start к b стоит 2 (если было бы ребро с меньшой стоимостью от start, то тоже можно сказать, что пока что!)

# Пока неизвестно, сколько займет стоит перейти от start к final
# А так же неизвестно, можем ли мы вообще к нему прийти (поэтому infinity, т.е бесконечность (пока не знаем, как прийти))
costs['final'] = float('inf')

# Иницализация таблицы родителей
parents = dict()
parents['a'] = 'start'  # Родитель узла "a" узел "start"
parents['b'] = 'start'  # Родитель узла "b" узел "start"
parents['final'] = None  # Родитель узла "final" пока не известен, поэтому None

# Список для уже обработанных узлов
# Нужен, чтобы не было двойных проверок
processed = []


# В начале находим узел с наименьшей стоимостью (В НАЧАЛЬНОМ ПОЛОЖЕНИИ)
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]  # Достаем вес данного узла
    neighbors = graph[node]  # Достаём всех соседий данного узла

    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]

        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('Наименьшая стоимость:', costs['final'])
print('Наименьший путь: ', end='')

# Двигаемся с конца
path = ['final']
current_node = 'final'
while current_node != 'start':
    current_node = parents[current_node]
    path.append(current_node)
path.reverse()
print(' -> '.join(path))
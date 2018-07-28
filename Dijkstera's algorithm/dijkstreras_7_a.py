def find_lowest_cost_node(node_costs):
    global processed
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in node_costs:
        current_cost = node_costs[node]

        if node not in processed and current_cost < lowest_cost:
            lowest_cost = current_cost
            lowest_cost_node = node
    return lowest_cost_node

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = dict()
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = dict()
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = dict()
graph['c']['d'] = 6
graph['c']['final'] = 3

graph['d'] = dict()
graph['d']['final'] = 1

graph['final'] = dict()


# Стоимости
costs = dict()
costs['final'] = float('inf')
costs['a'] = 5
costs['b'] = 2

# Родители
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['final'] = None


# Список уже обработанных узлов
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]

    # Обновляем соседей
    neighbors = graph[node]
    for n in neighbors.keys():
        updated_cost = cost + neighbors[n]

        # Если узел ещё не занесен в стоимости
        if not costs.get(n):
            costs[n] = updated_cost
            parents[n] = node
        else:
            if updated_cost < costs[n]:
                costs[n] = updated_cost
                parents[n] = node  # Обновление родителя
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
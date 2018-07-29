states = ['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']
states_needed = set(states)  # Множество

stations = dict()
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'id', 'wa', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_covered_by_station in stations.items():
        # Пересечение множества, т.е есть и там и там
        # {a, b, c} & {c, d, f} = {c}
        covered = states_needed & states_covered_by_station

        # В случае, если данная станция покрывает больше штатов, чем предыдущие
        # То мы ставим её лучшей
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    # Нам больше не нужны штаты, которые были покрыты в данной итерации
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

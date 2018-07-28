import collections

def person_is_seller(person):
    """
    Check if person is mango seller

    Функция, которая проверяет, является ли данный человек продавцом манго
    :param person: Name of person
    :return: bool
    """
    return person[-1] == 'm'

# Инициализация графа
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# Создание очереди для поиска.
# deque - двусторонняя очередь
search_queue = collections.deque()
search_queue += graph['you']  # Начинаем искать с моей позиции

searched = []  # Список тех, кого мы уже проверили

while search_queue:  # Пока очередь не пуста
    # Текущая персона
    # Забираем персону с самого начала очереди, т.е с "нулевого" элемента
    person = search_queue.popleft()

    if person in searched: continue

    if person_is_seller(person):
        print(f'{person} is a mango seller!')
        break
    else:
        search_queue += graph[person]
        searched.append(person)
else:
    print('There no mango seller in your friends list')
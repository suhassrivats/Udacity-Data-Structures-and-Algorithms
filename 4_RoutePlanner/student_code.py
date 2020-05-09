import math

global _intersections, _roads, _path_list, interested_values, _next
interested_values, _intersections = {}, {}
_roads, _path_list, _next = [], [], []


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return not self.queue

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            _min = 0
            for i in range(len(self.queue)):
                if (self.queue[i][-1] + self.queue[i][-2]) < (self.queue[_min][-1] + self.queue[_min][-2]):
                    _min = i
            item = self.queue[_min]
            del self.queue[_min]
            return item
        except IndexError:
            pass


def shortest_path(M, start, goal):
    if start == goal:
        return [start]

    global _intersections, _roads, _path_list, interested_values, _next
    interested_values = {}
    _intersections = M.intersections
    _roads = M.roads
    for node in _intersections:
        interested_values[node] = math.sqrt((_intersections[node][0] - _intersections[goal][0]) ** 2 + abs(
            _intersections[node][1] - _intersections[goal][1]) ** 2)

    _next = []
    for i in range(len(_roads)):
        temp = []
        for path in _roads[i]:
            temp.append(math.sqrt((_intersections[i][0] - _intersections[path][0]) ** 2 + abs(
                _intersections[i][1] - _intersections[path][1]) ** 2))
        _next.append(temp)

    _path_list = PriorityQueue()
    _path_list.insert([[start], 0, interested_values[start]])
    return helper_path(start, goal)


def helper_path(start, goal):
    global _intersections, _roads, _path_list, interested_values, _next
    item = 0
    if _path_list.is_empty():
        return "No possible path"
    else:
        item = _path_list.delete()
    current = item[0][-1]
    if current == goal:
        return item[0]

    for i, front in enumerate(_roads[current]):
        if front in item[0]:
            continue
        g = _next[current][i] + item[-2]
        h = interested_values[front]
        _path_list.insert([item[0] + [front], g, h])

    return helper_path(current, goal)

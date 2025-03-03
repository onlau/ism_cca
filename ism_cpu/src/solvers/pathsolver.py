from src.utils.config import config
import numpy as np
import heapq

'''Optisen paksuuden laskemiseksi on löydettävä (uv-)valonsäteen kulkema reitti solujen läpi.
Lasketaan lyhin polku jokaisesta solusta keskustähteen, ja approksimoidaan
valonsäteen kulkema polku lyhimmällä polulla. Optinen paksuus lasketaan jokaisessa solussa integroimalla
lyhimmän polun solujen yli.'''
#--------------------------------------------------------------------------------------------------
def generate_graph():
    e = config.GRID_EDGE_LENGTH
    nodes = [(i, j) for i in range(e) for j in range(e)]

    edges = {node: [] for node in nodes}

    for i in range(e):
        for j in range(e):
            node = (i, j)
            
            if i > 0:
                edges[node].append(((i - 1, j), 1))
            if i < e - 1:
                edges[node].append(((i + 1, j), 1))
            if j > 0:
                edges[node].append(((i, j - 1), 1))
            if j < e - 1:
                edges[node].append(((i, j + 1), 1))

            # viistosti olevien naapurisolujen välisen kaaren paino on sqrt(2) ja vierekkäisten 1
            if i > 0 and j > 0:
                edges[node].append(((i - 1, j - 1), np.sqrt(2)))
            if i > 0 and j < e - 1:
                edges[node].append(((i - 1, j + 1), np.sqrt(2)))
            if i < e - 1 and j > 0:
                edges[node].append(((i + 1, j - 1), np.sqrt(2)))
            if i < e - 1 and j < e - 1:
                edges[node].append(((i + 1, j + 1), np.sqrt(2)))

    return edges

def find_paths():
    source = (config.GRID_EDGE_LENGTH // 2, config.GRID_EDGE_LENGTH // 2)
    prev = {}

    edges = generate_graph()
    dist = {node: float("inf") for node in edges}
    dist[source] = 0
    prev[source] = None

    q = []
    heapq.heappush(q, (0, source))

    visited = set()
    while q:
        node = heapq.heappop(q)[1]
        if node in visited:
            continue
        visited.add(node)

        for next_node, w in edges[node]:
            new_dist = dist[node] + w
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
                prev[next_node] = node

    paths = {}

    for node in edges:
        path = []
        next_node = node
        while next_node != source:
            path.append(next_node)
            next_node = prev[next_node]
        paths[node] = (path, dist[node])
        
    return paths
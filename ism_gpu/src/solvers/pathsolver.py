from src.mappings.mappings import param_map
from src.utils.setuputils import setup_params as params
import cupy as cp
import heapq

def pad(path, l):
    n = []
    e = int(params[param_map["grid_edge"]].item())
    for i in range(l):
        n.append(path[i] if i < len(path) else (e,e))
    return n

'''Optisen paksuuden laskemiseksi on löydettävä (uv-)valonsäteen kulkema reitti solujen läpi.
Lasketaan Dijkstran algoritmilla lyhin polku jokaisesta solusta keskustähteen, ja approksimoidaan
valonsäteen kulkema polku lyhimmällä polulla. Optinen paksuus lasketaan jokaisessa solussa integroimalla
lyhimmän polun solujen yli. Funktio find_paths palauttaa sanakirjan, jossa avaimet ovat solujen koordinaatteja
ja arvot tupleja, joiden ensimmäinen alkio on lista lyhimpään polkuun kuuluvien solujen koordinaateista ja
jälkimmäinen polun pituus. Ensimmäisenä alkiona oleva lyhin polku on jätetty kääntämättä, koska polun suunnalla
ei ole merkitystä integroitaessa polun hiukkastiheyttä.'''
#--------------------------------------------------------------------------------------------------
def generate_graph():
    e = int(params[param_map["grid_edge"]].item())
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
                edges[node].append(((i - 1, j - 1), cp.sqrt(2)))
            if i > 0 and j < e - 1:
                edges[node].append(((i - 1, j + 1), cp.sqrt(2)))
            if i < e - 1 and j > 0:
                edges[node].append(((i + 1, j - 1), cp.sqrt(2)))
            if i < e - 1 and j < e - 1:
                edges[node].append(((i + 1, j + 1), cp.sqrt(2)))

    return edges

def find_paths():
    e = int(params[param_map["grid_edge"]].item())
    source = (e // 2, e // 2)
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

    maxl = 0

    for node in edges:
        path = []
        next_node = node
        while next_node != source:
            path.append(next_node)
            next_node = prev[next_node]
        if len(path) > maxl:
            maxl = len(path)
        if path:
            path.pop(0)
        paths[node] = path

    mask = cp.empty((e, e, e, e))

    for i in range(e):
        for j in range(e):
            for coords in paths[(i, j)]:
                mask[i, j, coords[0], coords[1]] = True

    return mask.astype(cp.bool_)

paths = find_paths()
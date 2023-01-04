from typing import List, Tuple


class Graph:
    def __init__(self):
        self.edges: List[str] = []
        self.vertices: List[Tuple[str, str]] = []

    def add_edge(self, edge: str) -> None:
        if edge in self.edges:
            raise Exception(f'Edge {edge} is already in graph')
        self.edges.append(edge)

    def add_vertex(self, start_edge: str, end_edge: str) -> None:
        vertex = (start_edge, end_edge)
        if start_edge not in self.edges:
            raise Exception(f'Edge {start_edge} is not in graph')
        if end_edge not in self.edges:
            raise Exception(f'Edge {end_edge} is not in graph')
        if vertex in self.vertices:
            raise Exception(f'Vertex {vertex} is already in graph')
        self.vertices.append((start_edge, end_edge))

    def way_of_edges(self, start_edge: str, end_edge: str):
        try:
            res = self.way_of_edges_inn(start_edge, end_edge)
            return bool(res[1])
        except Exception as e:
            return False

    def way_of_edges_inn(self, start_edge: str, end_edge: str):
        if start_edge == end_edge:
            return None, [end_edge]
        start_vertices = [x for x in self.vertices if x[0] == start_edge]
        for vertex in start_vertices:
            _, res = self.way_of_edges_inn(vertex[1], end_edge)
            res.insert(0, start_edge)
            return None, res
        return start_vertices, None




if __name__ == '__main__':
    g = Graph()
    g.add_edge('1')
    g.add_edge('2')
    g.add_edge('3')
    g.add_edge('4')
    g.add_edge('5')
    g.add_edge('6')
    g.add_edge('7')

    g.add_vertex('1', '2')
    g.add_vertex('1', '3')
    g.add_vertex('2', '3')
    g.add_vertex('2', '4')
    g.add_vertex('3', '4')

    res = g.way_of_edges('2', '4')
    print(res)









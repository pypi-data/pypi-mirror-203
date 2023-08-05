from laegr.featurization.Dump2Features import Dump2Features, Graph
from ovito.data import NearestNeighborFinder
from typing import Union, Any


class GraphFeatures(Dump2Features):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def to_graph(self, N: int) -> Graph:
        nodes = self.get_graph_node()
        edge_index, edge_attr = self.get_edge(N)
        labels = self.get_labels()
        graph_features = Graph(nodes, edge_index, edge_attr, None, labels)
        return graph_features

    def get_graph_node(self) -> list[list[Union[float, int]]]:
        raise NotImplementedError

    def get_edge(self, N: int) -> tuple[list[list[int | Any]], list[list[float]]]:
        finder = NearestNeighborFinder(N, self.data)
        edge_index = []
        edge_attr = []
        for index in range(self.data.particles.count):
            for neigh in finder.find(index):
                edge_index.append([index, neigh.index])
                edge_attr.append(self.get_edge_attr(neigh))
        return edge_index, edge_attr

    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        raise NotImplementedError


class AtomicNumber(GraphFeatures):
    def get_graph_node(self) -> list[list[int]]:
        ptypes = self.data.particles.particle_types
        nodes = []
        transform = {1: 42, 2: 41, 3: 73, 4: 74}
        for atom_type in ptypes:
            cur_node = transform[atom_type]
            nodes.append([cur_node])
        return nodes


class AtomicNumberDistance(AtomicNumber):
    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        return [neigh.distance]


class AtomicNumberPos(AtomicNumber):
    def to_graph(self) -> Graph:
        nodes = self.get_graph_node()
        pos = self.get_pos()
        labels = self.get_labels()
        graph_features = Graph(nodes, None, None, pos, labels)
        return graph_features

    def get_pos(self) -> list[list[float]]:
        pos_list = []
        for cur_pos in self.data.particles.positions:
            pos_list.append(list(cur_pos))
        return pos_list


class AtomicMass(GraphFeatures):
    def get_graph_node(self) -> list[list[float]]:
        nodes = self.data.particles['Mass'][...]
        nodes = [[i] for i in nodes]
        return nodes


class AtomicMassDistance(AtomicMass):
    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        return [neigh.distance]


class AtomicMass3D(AtomicMass):
    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        return neigh.delta


class OneHotGraph(GraphFeatures):
    def get_graph_node(self) -> list[list[int]]:
        ptypes = self.data.particles.particle_types
        nodes = []
        for atom_type in ptypes:
            cur_node = self.to_onehot(atom_type)
            nodes.append(cur_node)
        return nodes

    @staticmethod
    def to_onehot(atom_type: int) -> list[int]:
        raise NotImplementedError


class OneHotDistance(OneHotGraph):
    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        return [neigh.distance]


class OneHot3D(OneHotGraph):
    @staticmethod
    def get_edge_attr(neigh: NearestNeighborFinder) -> list[float]:
        return neigh.delta


class OneHotDistance_TypeOrder(OneHotDistance):
    @staticmethod
    def to_onehot(atom_type: int) -> list[int]:
        feature = [0, 0, 0, 0]
        feature[atom_type - 1] = 1
        return feature


class OneHotDistance_AtomicOrder(OneHotDistance):
    @staticmethod
    def to_onehot(atom_type: int) -> list[int]:
        if atom_type == 1:
            new_atom_type = 2
        elif atom_type == 2:
            new_atom_type = 1
        else:
            new_atom_type = atom_type
        feature = [0, 0, 0, 0]
        feature[new_atom_type - 1] = 1
        return feature


class OneHot3D_TypeOrder(OneHot3D):
    @staticmethod
    def to_onehot(atom_type: int) -> list[int]:
        feature = [0, 0, 0, 0]
        feature[atom_type - 1] = 1
        return feature


class OneHot3D_AtomicOrder(OneHot3D):
    @staticmethod
    def to_onehot(atom_type: int) -> list[int]:
        if atom_type == 1:
            new_atom_type = 2
        elif atom_type == 2:
            new_atom_type = 1
        else:
            new_atom_type = atom_type
        feature = [0, 0, 0, 0]
        feature[new_atom_type - 1] = 1
        return feature

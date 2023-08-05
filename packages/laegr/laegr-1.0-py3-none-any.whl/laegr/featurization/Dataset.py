import os, re, pickle
from tqdm import tqdm
from torch_geometric.data.data import Data
import torch


from laegr.featurization.Dump2Features import Graph
from laegr.featurization.GraphFeatures import AtomicMassDistance, AtomicMass3D, AtomicNumberDistance, AtomicNumberPos
from laegr.featurization.GraphFeatures import OneHotDistance_TypeOrder, OneHotDistance_AtomicOrder, OneHot3D_TypeOrder, \
    OneHot3D_AtomicOrder


class DataSaving:
    def __init__(self, sourcePath: str, outputDir: str, filer=1000) -> None:
        self.files = self.__read_data(sourcePath, filter=filer)
        self.outputDir = outputDir

    def save_data(self) -> None:
        raise NotImplementedError

    def to_features(self, dumpPath: str) -> Graph:
        raise NotImplementedError

    def __read_data(self, read_path: str, filter=1) -> list[str]:
        if os.path.isdir(read_path):
            return self.__read_data_dir(read_path, filter)
        else:
            return self.__read_data_single(read_path)

    @staticmethod
    def __read_data_dir(data_path: str, filter: int) -> list[str]:
        files = os.listdir(data_path)
        files = [f for f in files if ("mc" in f and "dump" in f)]
        files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
        L = []
        for f in files:
            [x] = re.findall('[0-9]+', f)
            x = int(x)
            if x % filter == 0:
                L.append(os.path.join(data_path, f))
        return L

    @staticmethod
    def __read_data_single(data_path: str) -> list[str]:
        return [data_path]


class GNN_Data(DataSaving):
    def __init__(self, sourcePath: str, outputDir: str, num: int, feature: str, filer=1000) -> None:
        super().__init__(sourcePath, outputDir, filer)
        self.num = num
        self.feature = feature

    def saveData(self) -> None:
        output = []
        for file in tqdm(self.files):
            graph = self.to_features(file)
            data = self.to_GNN_data(graph)
            output.append(data)
        open_file = open(self.outputDir, "wb")
        pickle.dump(output, open_file)
        open_file.close()

    def to_features(self, dumpPath: str) -> Graph:
        match self.feature:
            case "AtomicMassDistance":
                graph = AtomicMassDistance(dumpPath).to_graph(self.num)
            case "AtomicMass3D":
                graph = AtomicMass3D(dumpPath).to_graph(self.num)
            case "AtomicNumberDistance":
                graph = AtomicNumberDistance(dumpPath).to_graph(self.num)
            case "AtomicNumberPos":
                graph = AtomicNumberPos(dumpPath).to_graph()
            case "OneHotDistance_TypeOrder":
                graph = OneHotDistance_TypeOrder(dumpPath).to_graph(self.num)
            case "OneHotDistance_AtomicOrder":
                graph = OneHotDistance_AtomicOrder(dumpPath).to_graph(self.num)
            case "OneHot3D_TypeOrder":
                graph = OneHot3D_TypeOrder(dumpPath).to_graph(self.num)
            case "OneHot3D_AtomicOrder":
                graph = OneHot3D_AtomicOrder(dumpPath).to_graph(self.num)
            case _:
                raise Exception('''Only support eight different features:   
                                        AtomicMassDistance,             AtomicMass3D,
                                        AtomicNumberDistance,           AtomicNumberPos,
                                        OneHotDistance_TypeOrder,       OneHotDistance_AtomicOrder,
                                        OneHot3D_TypeOrder,             OneHot3D_AtomicOrder.''')
        return graph

    @staticmethod
    def to_GNN_data(graph: Graph) -> Data:
        labels = graph.labels
        if graph.labels:
            labels = torch.tensor(graph.labels, dtype=torch.float)
        if graph.pos:
            nodes = torch.tensor(graph.nodes, dtype=torch.long)
            edge_pos = torch.tensor(graph.pos, dtype=torch.float)
            data = Data(z=nodes, edge_attr=None, pos=edge_pos, y=labels)
        else:
            nodes = torch.tensor(graph.nodes, dtype=torch.float)
            edge_index = torch.tensor(graph.edge_index, dtype=torch.long)
            edge_attr = torch.tensor(graph.edge_attr, dtype=torch.float)
            data = Data(x=nodes, edge_index=edge_index.t().contiguous(), edge_attr=edge_attr, y=labels)
        return data



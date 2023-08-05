import os
import pickle
from typing import Tuple, Union, Optional
from torch_geometric.loader import DataLoader
import random

class LoadData():
    def __init__(self, path: Union[str, list[str]]):
        self.__List = self.__readList(path)

    @staticmethod
    def __readList(path: Union[str, list[str]]):
        print("Start reading Data")
        listRawData = []
        if isinstance(path, str):
            print("single data")
            open_file   = open(path, "rb")
            listRawData = pickle.load(open_file)
            open_file.close()
        elif isinstance(path, list):
            print("Multiple data.")
            for cur_path in path:
                print("Read current data ...")
                cur_file = open(cur_path, 'rb')
                cur_data = pickle.load(cur_file)
                cur_file.close()
                listRawData.extend(cur_data)
        else:
            raise Exception("Please provide correct data path!")
        print("Reading data Done")
        return listRawData
    
    def transformInput(self, partition: float = 0.8, train_batch_size: int = 1, val_batch_size: int = 1, shuffle: bool = True, random_see: int = 66) -> Tuple[DataLoader, Optional[DataLoader]]:
        data_size    = len(self.__List)
        random.seed(random_see)
        if (shuffle):
            random.shuffle(self.__List)
        if partition == -1:
            train_loader = DataLoader(self.__List, batch_size=train_batch_size)
            return train_loader, None
        train_loader       = DataLoader(self.__List[:int(data_size*partition)], batch_size=train_batch_size)
        validation_loader  = DataLoader(self.__List[int(data_size*partition):], batch_size=val_batch_size)
        return train_loader, validation_loader
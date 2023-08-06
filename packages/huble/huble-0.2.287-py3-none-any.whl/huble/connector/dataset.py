import pandas as pd
import boto3
from ..util.data_types import get_dataframe_types
import boto3


class Dataset:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.dataframe = self.__load_dataset(file_name)

    def __load_dataset(self, file_name: str) -> pd.DataFrame:
        return pd.read_csv("https://const-bucket.s3.ap-south-1.amazonaws.com/" + file_name)

    def parse_dataset(self):
        data_dict = get_dataframe_types(self.dataframe)
        data_dict["rows"] = len(self.dataframe.axes[0])
        return data_dict

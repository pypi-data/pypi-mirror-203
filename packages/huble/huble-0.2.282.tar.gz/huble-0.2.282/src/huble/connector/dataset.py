import pandas as pd
import requests
from pydantic import BaseModel

# import woodwork as ww
from ..util.data_types import get_dataframe_types
import boto3


class Dataset:
    def __init__(self, url) -> None:
        self.url = url
        self.dataframe = self.__load_dataset(url)

    def __load_dataset(self, url: str) -> pd.DataFrame:
        return pd.read_csv(url)

    def parse_dataset(self):
        data_dict = get_dataframe_types(self.dataframe)
        data_dict["rows"] = len(self.dataframe.axes[0])
        return data_dict

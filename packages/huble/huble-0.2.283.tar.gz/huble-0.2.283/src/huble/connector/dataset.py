import pandas as pd
import boto3
# import woodwork as ww
from ..util.data_types import get_dataframe_types
import boto3


class Dataset:
    def __init__(self, url) -> None:
        self.url = url
        self.dataframe = self.__load_dataset(url)

    def __load_dataset(self, url: str) -> pd.DataFrame:
        bucket = "const-bucket"
        file_name = url.split("/")[-1]
        s3 = boto3.client('s3') 
        obj = s3.get_object(Bucket= bucket, Key= file_name)
        return pd.read_csv(obj['Body'])

    def parse_dataset(self):
        data_dict = get_dataframe_types(self.dataframe)
        data_dict["rows"] = len(self.dataframe.axes[0])
        return data_dict

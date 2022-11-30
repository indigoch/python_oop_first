import json

from data_define import Record


class FileReader:
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):

    def read_data(self) -> list[Record]:
        record_list : list[Record] = []
        with open(self.path, "r", encoding="UTF-8") as f:
            for line in f.readlines():
                line = line.strip()
                data_list = line.split(",")
                record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
                record_list.append(record)
        return record_list


class JsonFileReader(FileReader):
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        with open(self.path, "r", encoding="UTF-8") as f:
            for line in f.readlines():
                data_dict = json.loads(line)
                record = Record(data_dict['date'],data_dict["order_id"],
                                data_dict["money"],data_dict["province"])
                record_list.append(record)
        return record_list

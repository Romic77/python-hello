import json

from data_define import Record


class FileRead:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileRead):
    path = None

    # 将外部的path传入到对象内
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = open(self.path, "r", encoding="UTF-8")
        for line in f.readlines():
            # strip()去除空格或换行符
            row = line.strip().split(",")
            record_list.append(Record(row[0], row[1], float(row[2]), row[3]))

        f.close()
        return record_list


class JSONFileReader(FileRead):
    path = None

    # 将外部的path传入到对象内
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = open(self.path, "r", encoding="UTF-8")
        for line in f.readlines():
            data_dic = json.loads(line)

            record_list.append(
                Record(data_dic["date"], data_dic["order_id"], float(data_dic["money"]), data_dic["province"]))
        f.close()
        return record_list


if __name__ == '__main__':
    # for i in TextFileReader("./2011年1月销售数据.txt").read_data():
    #     print(i)
    for i in TextFileReader("./2011年2月销售数据JSON.txt").read_data():
        print(i)

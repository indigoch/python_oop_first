from file_define import TextFileReader,JsonFileReader
from  data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


if __name__ == '__main__':
    text_file_reader = TextFileReader("201101.txt")
    json_file_reader = JsonFileReader("201102.txt")

    jan_data = text_file_reader.read_data()
    feb_data = json_file_reader.read_data()

    all_data:list[Record] = jan_data+feb_data
    data_dict = {}
    for record in all_data:
        if record.date in data_dict.keys():
            data_dict[record.date] += record.money
        else:
            data_dict[record.date] = record.money

        bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(list(data_dict.keys()))
        bar.add_yaxis("sales",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
        bar.set_global_opts(
            title_opts=TitleOpts(title="daily sales")
        )
        bar.render("Daily_sales_histogram.html")

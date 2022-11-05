from csv import reader
from pandas import DataFrame
from datetime import datetime


def read_csv(filename: str, delimiter: str, quotechar: str, column_line_num: int) -> tuple:
    ONLY_READ = 'r'
    with open(filename, ONLY_READ) as dest_file:
        all_data = [data for data in reader(dest_file, delimiter = delimiter, quotechar = quotechar)]
        columns = all_data[column_line_num]
        for i in range(len(columns)):
            columns[i] = columns[i].replace(' ', '', 1)
        table_data = all_data[column_line_num + 1:]
        for i in range(len(table_data)):
            for j in range(len(columns)):
                table_data[i][j] = table_data[i][j].replace(' ', '', 1)
                if table_data[i][j].replace('.', '', 1).replace('-', '', 1).isdigit():
                    table_data[i][j] = float(table_data[i][j])
                elif table_data[i][j].find('E') != -1:
                    table_data[i][j] = float(table_data[i][j].replace('E', 'e'))
                else:
                    table_data[i][j] = datetime.strptime(table_data[i][j], '%Y-%m-%d %H:%M:%S.%f') # 2022-11-02 12:43:14.338'
        return table_data, columns


def transpose_list_of_list(l: list):
    return list(map(list, zip(*l)))


def csv_data_array_to_dataframe(table_data: list, column_names: list) -> DataFrame:
    return DataFrame(data=dict(zip(column_names, transpose_list_of_list(table_data))))


def dataframe_to_dataframes_dict(dataframe: list, column_names: list) -> dict:
    result = {}
    for column_name in column_names:
        result[column_name] = dataframe[[column_name]]
    return result


def csv_data_array_to_dataframes_dict(table_data: list, column_names: list) -> dict:
    return dataframe_to_dataframes_dict(csv_data_array_to_dataframe(table_data, column_names), column_names)


def read_csv_as_dataframes_dict(filename: str, delimiter: str, quotechar: str, column_line_num: int) -> dict:
    data_array, column_names = read_csv(filename, delimiter, quotechar, column_line_num)
    return csv_data_array_to_dataframes_dict(data_array, column_names)
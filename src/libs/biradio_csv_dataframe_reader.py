from csv import reader
from datetime import datetime
from enum import Enum
from pandas import DataFrame


class NewBioRadioColumnsName(Enum):
    ELAPSED_TIME = 'Elapsed Time'
    FP1 = 'FP1'
    FP2 = 'FP2'
    O1 = 'O1'
    O2 = 'O2'
    HEART_RATE_PULSE = 'Heart Rate pulse'
    PPG_PULSE = 'PPG pulse'
    SP02_PULSE = 'SpO2 pulse'
    BIO_RADIO_EVENT = 'BioRadio Event'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OldBioRadioColumnsName(Enum):
    ELAPSED_TIME = 'Elapsed Time'
    EEG1 = 'EEG1'
    EEG2 = 'EEG2'
    EEG3 = 'EEG3'
    EEG4 = 'EEG4'
    HEART_RATE_PULSE = 'Heart Rate pulse'
    PPG_PULSE = 'PPG pulse'
    SP02_PULSE = 'SpO2 pulse'
    BIO_RADIO_EVENT = 'BioRadio Event'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


def read_csv(filepath: str) -> tuple:
    ONLY_READ = 'r'
    with open(filepath, ONLY_READ, newline='') as dest_file:
        all_data = [data for data in reader(dest_file, delimiter='\t')]
        columns = all_data[0][:-1]

        table_data = all_data[1:-1]

        for i in range(len(table_data)):
            for j in range(len(columns)):
                if table_data[i][j].replace(',', '', 1).replace('-', '', 1).isdigit():
                    table_data[i][j] = float(table_data[i][j].replace(',', '.', 1))
                elif table_data[i][j].find('E') != -1:
                    table_data[i][j] = float(table_data[i][j].replace(',', '.', 1).replace('E', 'e'))
                elif table_data[i][j].find('.') != -1:
                    table_data[i][j] = datetime.strptime(table_data[i][j], '%H:%M:%S.%f')  # 12:43:14.338
                else:
                    table_data[i][j] = datetime.strptime(table_data[i][j], '%H:%M:%S')  # 12:43:14.338
        return table_data, columns


def transpose_list_of_list(l: list) -> list:
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


def read_csv_as_dataframes_dict(filename: str) -> dict:
    data_array, column_names = read_csv(filename)
    return csv_data_array_to_dataframes_dict(data_array, column_names)

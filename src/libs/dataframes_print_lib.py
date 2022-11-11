PRINT_DATAFRAME_DELIMETER = '-'
PRINT_DATAFRAME_DELIMETER_COUNT = 50
PRINT_DATAFRAME_COMMON_DELIMITER = PRINT_DATAFRAME_DELIMETER * PRINT_DATAFRAME_DELIMETER_COUNT


def print_dataframe(dataframe_0, dataframe_1):
    print(dataframe_0, ':\n', dataframe_1, '\n', PRINT_DATAFRAME_COMMON_DELIMITER)


def print_dataframes(dataframes: dict):
    for dataframe_0, dataframe_1 in dataframes.items():
        print_dataframe(dataframe_0, dataframe_1)
#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import butter, lfilter, lfilter_zi

import matplotlib.pyplot as plt

from src.libs.bci_csv_dataframe_reader import read_csv_as_dataframes_dict as read_bci, BciColumnsName
from src.libs.biradio_csv_dataframe_reader import read_csv_as_dataframes_dict as read_bioradio, NewBioRadioColumnsName, OldBioRadioColumnsName
from src.libs.dataframes_print_lib import print_dataframes

BCI_PATHNAME = 'resources/IlyaMono.txt'
BCI_START_POINT = 20000 # Разница должны быть кратна 90
BCI_END_POINT = 20450


def show_bci():
    dataframes: dict = read_bci(BCI_PATHNAME)
    print_dataframes(dataframes)

    print(dataframes[BciColumnsName.EXG_CHANNEL_8.value][BCI_START_POINT:BCI_END_POINT].to_numpy())
    plt.plot(dataframes[BciColumnsName.EXG_CHANNEL_8.value][BCI_START_POINT:BCI_END_POINT].to_numpy())
    plt.show()




BIORADIO_START_POINT = 15028
BIORADIO_END_POINT = 16500
BIORADIO_PATHNAME = 'resources/monoVladCSV.csv'


def show_bioradio(dataframes, col):
    print_dataframes(dataframes)

    print(dataframes[OldBioRadioColumnsName.EEG1.value][BIORADIO_START_POINT:BIORADIO_END_POINT].to_numpy())
    plt.plot(dataframes[OldBioRadioColumnsName.EEG1.value][BIORADIO_START_POINT:BIORADIO_END_POINT].to_numpy())
    plt.show()

def method_fourier_transform(data):
    pass


def method_butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = method_butter_bandpass(lowcut, highcut, fs, order=order)
    zi = lfilter_zi(b, a) * data[0]
    y, _ = lfilter(b, a, data, zi=zi)
    return y


def load_data(path):
    pass


def analiz_spectr_eeg(data):
    pass


def analiz_spectr_ecg_variability(data):

    pass



if __name__ == '__main__':
    dataframes_bioradio_ilya_mono: dict = read_bioradio("resources/ilyaMonoCSV.csv")
    #dataframes_bioradio_ilya_stress: dict = read_bioradio("resources/ilyaStressCSV.csv")
    #dataframes_bioradio_vadim_mono: dict = read_bioradio("resources/monoVadimWaterfallCSV.csv")
    #dataframes_bioradio_vadim_stress: dict = read_bioradio("resources/stressTestVadimaCSV.csv")
    dataframes_bioradio_vlad_mono: dict = read_bioradio("resources/monoVladCSV.csv")
    #dataframes_bioradio_vlad_stress: dict = read_bioradio("resources/stressTestVladCSV.csv")

    plt.plot(dataframes_bioradio_ilya_mono[NewBioRadioColumnsName.FP1.value][20000:25000].to_numpy())
    plt.show()







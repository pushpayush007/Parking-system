import pandas as pd
import numpy as np

def data_reader(file_path):
    df = pd.read_csv(file_path)

    # Extract columns into NumPy arrays
    vehicle_type = df["vehicle_type"].to_numpy()
    entry_exit = df["entry_exit"].to_numpy()
    time_stayed = df["time_stayed"].to_numpy()
    vehicle_number = df["vehicle_number"].to_numpy()
    return vehicle_type,entry_exit,time_stayed,vehicle_number


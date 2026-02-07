import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_plot(CSV_dict):
    data = pd.read_csv(CSV_dict["file"])
    X_axis_list = data[CSV_dict["X_axis"]]
    #window_size = 50
    #X_axis_list = np.convolve(X_axis_list,np.ones(window_size)/window_size,mode='same')
    X_axis_list = X_axis_list[250:1250]
    Y_axis_list = data[CSV_dict["Y_axis"]]
    Y_axis_list = Y_axis_list[250:1250]
    Y_mean = np.mean(X_axis_list)
    tmp_list = Y_axis_list
    Y_axis_list = []
    for entry in tmp_list:
        Y_axis_list += [entry - Y_mean]
    #Y_axis_list = np.convolve(Y_axis_list,np.ones(window_size)/window_size,mode='same')
    
    #print(f"{X_axis_list=} {Y_axis_list=}")
    plt.plot(X_axis_list,Y_axis_list)
    plt.xlabel(CSV_dict["X_axis"])
    plt.ylabel(CSV_dict["Y_axis"])
    plt.title(f"{CSV_dict["X_axis"]} vs {CSV_dict["Y_axis"]}")
    plt.savefig(f"lab2_plot_cleaning_4_3_6_{CSV_dict["X_axis"]}_vs_{CSV_dict["Y_axis"]}.png")
    plt.show

CSV_dict = {"file":"lab2_ecg.csv", "X_axis": "t", "Y_axis": "lead_I"}
#print(f"{CSV_dict=}")
create_plot(CSV_dict)

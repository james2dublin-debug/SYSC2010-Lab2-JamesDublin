import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
global DEBUG

class MyGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CSV Plotter")
        self.window.geometry("400x250")
        self.label_1 = tk.Label(self.window, text="CSV_file_name", font=('Arial', 12))
        self.label_1.pack(padx=5, pady=5)
        self.textbox1 = tk.Text(self.window, height=1, font=('Arial', 10))
        self.textbox1.pack(padx=20)
        self.label_2 = tk.Label(self.window, text="X-axis column name", font=('Arial', 12))
        self.label_2.pack(padx=5, pady=5)
        self.textbox2 = tk.Text(self.window, height=1, font=('Arial', 10))
        self.textbox2.pack(padx=20)
        self.label_2 = tk.Label(self.window, text="Y-axis column name", font=('Arial', 12))
        self.label_2.pack(padx=5, pady=5)
        self.textbox3 = tk.Text(self.window, height=1, font=('Arial', 10))
        self.textbox3.pack(padx=20)
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.pack(fill="x",padx=5,pady=5)
        self.button = tk.Button(self.window, text="load & plot", font=('Arial',10),
command=self.show_message)
        self.button.pack(padx=10,pady=10)
    def show_message(self):
        print("Button Clicked")        
    def show_message(self):
        file_name = self.textbox1.get("1.0", "end-1c")
        X_axis_name = self.textbox2.get("1.0", "end-1c")
        Y_axis_name = self.textbox3.get("1.0", "end-1c")
        if DEBUG: print(f"DEBUG: {file_name=} {X_axis_name=} {Y_axis_name=}")
        CSV_dict = {"file":file_name, "X_axis": X_axis_name, "Y_axis": Y_axis_name}
        return self.create_plot(CSV_dict)
    def create_plot(self,CSV_dict):
        data = pd.read_csv(CSV_dict["file"])
        X_axis_list = data[CSV_dict["X_axis"]]
        Y_axis_list = data[CSV_dict["Y_axis"]]
        plt.plot(X_axis_list,Y_axis_list)
        plt.xlabel(CSV_dict["X_axis"])
        plt.ylabel(CSV_dict["Y_axis"])
        plt.title(f"{CSV_dict["X_axis"]} vs {CSV_dict["Y_axis"]}")
        plt.savefig(f"lab2_plot_{CSV_dict["X_axis"]}_vs_{CSV_dict["Y_axis"]}.png")
        plt.show
     

DEBUG = 1
gui = MyGui()
gui.window.mainloop()
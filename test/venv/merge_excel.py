import pandas as pd

files = []
import tkinter as Tk
from tkinter import filedialog


def choose_file(files):
    count = int(input("Введите колличество файлов: "))
    for i in range(count):
        root = Tk.Tk()
        root.filename = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx"), ("Excel file", "*.xls")])
        root.destroy()
        filename = root.filename
        f = open(filename)
        f.close()
        files.append(filename)
    return (files)


excel_names = choose_file(files)

excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]

# delete the first row for all frames except the first
a = int(input("Введите колличество строк шапки: "))
frames[1:] = [df[a:] for df in frames[1:]]
combined = pd.concat(frames)
root = Tk.Tk()
root.withdraw()
combined.to_excel('{!s}\\{!r}.xlsx'
                  .format((filedialog.askdirectory(parent=root, initialdir="\\", title='Выберите папку: ')),
                          input("Введите название файла: ")), header=False, index=False)

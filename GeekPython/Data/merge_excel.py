import pandas as pd

files = []
import tkinter as Tk
from tkinter import filedialog


def choose_file(my_file):
    count = int(input("Введите колличество файлов: "))
    for i in range(count):
        rooter = Tk.Tk()
        rooter.filename = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx"), ("Excel file", "*.xls")])
        rooter.destroy()
        filename = rooter.filename
        f = open(filename)
        f.close()
        my_file.append(filename)
    return my_file


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

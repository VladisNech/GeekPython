import clr

clr.AddReference('System')
clr.AddReference("System.Windows.Forms")
clr.AddReference('Microsoft.Office.Interop.Excel')
import System
from System.IO import File
from System.Windows.Forms import OpenFileDialog, MessageBox, MessageBoxButtons, DialogResult
from Microsoft.Office.Interop.Excel import ApplicationClass
from Spotfire.Dxp.Data import AddRowsSettings, RowSelection, DataType, DataColumnSignature
from Spotfire.Dxp.Data.Import import DataTableDataSource
from Spotfire.Dxp.Data.Transformations import ReplaceColumnTransformation, ChangeDataTypeTransformation, \
    AddCalculatedColumnTransformation


def get_file_location(unit_name, period):
    dialog = OpenFileDialog()
    if "Текущий" in period:
        title = "Выбор файлов текущего периода по филиалу '%s'" % unit_name
    else:
        title = "Выбор файлов сравнительного периода по филиалу '%s'" % unit_name
    dialog.Title = title
    dialog.InitialDirectory = '%USERPROFILE%\\Documents'
    dialog.Filter = "Excel spreadsheet|*.xlsm;*.xlsx;*.xls|All files|*.*"
    dialog.Multiselect = True
    if dialog.ShowDialog() == DialogResult.OK:
        return list(dialog.FileNames)
    else:
        return None


def open_excel_application():
    new_application = ApplicationClass()
    new_application.Visible = False
    new_application.DisplayAlerts = False
    return new_application


def close_excel_application(application):
    application.Quit()
    System.Runtime.InteropServices.Marshal.ReleaseComObject(application)


def open_workbook(application, file_location):
    workbook = application.Workbooks.Add(file_location)
    return workbook


def save_workbook(workbook, file_location):
    workbook.SaveAs(file_location)


def close_workbook(workbook):
    workbook.Close(True)
    System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook)


def delete_file(file_location):
    File.Delete(file_location)


def remove_extra_headers(workbook):
    for sheet in workbook.Sheets:
        # if sheet.Name in accounts:
        if sheet.Range["E1"].Value2 is not None:
            continue
        while sheet.Range["E1"].Value2 is None:
            sheet.Range["E1"].EntireRow.Delete()


def remove_duplicate_headers(table):
    column_with_invalid_rows = table.Columns["Дата"]
    selection_of_invalid_rows = column_with_invalid_rows.RowValues.InvalidRows
    table.RemoveRows(RowSelection(selection_of_invalid_rows))


def define_business_unit(table):
    table.AddTransformation(AddCalculatedColumnTransformation("Название фабрики", "'%s'" % business_unit))


def date_transformation(table):
    date_column = table.Columns["Дата"]
    if date_column.DataType != DataType.Date:
        if len(date_column.RowValues.GetMinValue().ToString().split(".")) == 3:
            signature = DataColumnSignature(date_column)
            expression = "ParseDate([Дата], 'dd.MM.yyyy')"
            table.AddTransformation(ReplaceColumnTransformation(signature, "", expression))
        table.AddTransformation(ChangeDataTypeTransformation([DataColumnSignature(date_column)], DataType.Date))


def move_sheet_to_first(workbook, sheet_index):
    sheet_to_move = workbook.Sheets.Item[sheet_index]
    first_sheet = workbook.Sheets.Item[1]
    sheet_to_move.Move(first_sheet)


def change_numbers_to_text(
        workbook):  # В некоторых случаях импорта происходит потеря данных в столбце "сумма по дебету", исправлено форматированием столбца как текст
    for sheet in workbook.Sheets:
        # if sheet.Name in accounts:
        sheet.Range["K:K"].NumberFormat = "@"


def disable_filters(workbook):
    for sheet in workbook.Sheets:
        # if sheet.Name in accounts:
        sheet.AutoFilterMode = False


def remove_pivots(workbook):
    for sheet in workbook.Sheets:
        for pivot in sheet.PivotTables():
            pivot.TableRange2.Clear()


def define_type_of_columns(workbook):
    for sheet in workbook.Sheets:
        sheet.Range["A2"].EntireRow.Insert()
        types = ["String", "String", "String", "String",
                 "String", "String", "String", "String",
                 "String", "String", "String", "String", "String"]
        for index, type in enumerate(types):
            sheet.Range["A2"].Offset[0, index].Value = type


def inside_cleanup(workbook):
    remove_pivots(workbook)
    remove_extra_headers(workbook)
    change_numbers_to_text(workbook)
    disable_filters(workbook)
    define_type_of_columns(workbook)


def create_temp_file_location(file_location):  # создание пути к временному файлу xlsx, чтобы не изменять исходный файл
    directories = file_location.split("\\")
    directories[-1] = "_" + directories[-1]
    return "\\".join(directories)


def define_period(table, period):
    table.AddTransformation(AddCalculatedColumnTransformation("Origin", "'%s'" % period))


def check_amounts(table):
    columns_to_check = [DataColumnSignature(column) for column in table.Columns if
                        column.Name == "Дебет" or column.Name == "Кредит"]
    table.AddTransformation(ChangeDataTypeTransformation(columns_to_check, DataType.Real))


def execute_cleanup_in_spotfire(table, period):
    date_transformation(table)
    remove_duplicate_headers(table)
    define_business_unit(table)
    define_period(table, period)
    check_amounts(table)


def add_rows_to_table(table, file_location, period_to_load):
    status, temp_table = Document.Data.Tables.TryGetValue("temp")
    data_source = Document.Data.CreateFileDataSource(file_location)
    if status:
        temp_table.ReplaceData(data_source)
    else:
        temp_table = Document.Data.Tables.Add("temp", data_source)
    execute_cleanup_in_spotfire(temp_table, period_to_load)
    dtds = DataTableDataSource(temp_table)
    settings = AddRowsSettings(table, dtds)
    table.AddRows(dtds, settings)
    Document.Data.Tables.Remove(temp_table)


def file_manipulation(workbook, file_location, period_to_load):
    table = Document.Data.Tables["Data"]
    status, column = table.Columns.TryGetValue("Сумма")
    if status:
        table.Columns.Remove(column)
    sheet_count = workbook.Sheets.Count
    for index in range(1, sheet_count + 1):
        # if workbook.Sheets.Item[index].Name in accounts:
        if index != 1:
            move_sheet_to_first(workbook, index)
            save_workbook(workbook, file_location)
        add_rows_to_table(table, file_location, period_to_load)
    table.Columns.AddCalculatedColumn("Сумма", "[Дебет] - [Кредит]")


try:
    # accounts = ['60.01.10', '60.01.20', '60.01.40', '60.01.50', '60.01.60', '60.01.70', '60.01.71', '60.01.80', '60.02.10', '76.01.01', '76.01.10', '76.01.99', '76.01.20', '76.02.62']
    app = None
    if business_unit:
        periods_to_load = []
        response = MessageBox.Show(
            "Загрузить файл с расшифровкой по расходам текущего периода по филиалу '%s' в формате Excel?" % business_unit,
            "Импорт данных", MessageBoxButtons.OKCancel)
        if response == DialogResult.Cancel:
            response = MessageBox.Show(
                "Загрузить файл с расшифровкой по расходам сравнительного периода по филиалу '%s' в формате Excel?" % business_unit,
                "Импорт данных", MessageBoxButtons.OKCancel)
            if response == DialogResult.Cancel:
                files = None
            else:
                periods_to_load.append("Сравнительный период")
        else:
            periods_to_load.append("Текущий период")
        if periods_to_load:
            for i in range(2):
                if i == 0 or len(periods_to_load) == 2:
                    files = get_file_location(business_unit, periods_to_load[i])
                    if files is not None:
                        MessageBox.Show("Подождите несколько минут пока выполняется импорт данных.", "Импорт данных")
                        if app is None:
                            app = open_excel_application()
                        for file in files:
                            temp_file = create_temp_file_location(file)
                            wb = open_workbook(app, file)
                            inside_cleanup(wb)
                            save_workbook(wb, temp_file)
                            file_manipulation(wb, temp_file, periods_to_load[i])
                            close_workbook(wb)
                            delete_file(temp_file)
                        if len(periods_to_load) == 1 and periods_to_load[i] == "Текущий период":
                            response = MessageBox.Show(
                                "Загрузить файл с расшифровкой по расходам сравнительного периода по филиалу '" + business_unit + "' в формате Excel?",
                                "Импорт данных", MessageBoxButtons.OKCancel)
                            if response == DialogResult.OK:
                                periods_to_load.append("Сравнительный период")
except Exception:
    MessageBox.Show("Произошла ошибка во время импорта. Повторите процедуру.", "Импорт данных")
else:
    if business_unit:
        if files is None:
            MessageBox.Show("Процедура прервана пользователем.", "Импорт данных")
        else:
            MessageBox.Show("Процедура импорта завершена.", "Импорт данных")
    else:
        MessageBox.Show("Для выполнения процедуры импорта введите наименование филиала.", "Импорт данных")
finally:
    if app is not None:
        close_excel_application(app)

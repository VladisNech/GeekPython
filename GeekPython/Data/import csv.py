import clr
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
from System import IServiceProvider, ArgumentException
from System.Windows.Forms import OpenFileDialog, MessageBox, MessageBoxButtons, DialogResult
from System.Collections.Generic import Dictionary, List
from Spotfire.Dxp.Data import DataSourcePromptMode, AddRowsSettings, DataTableSaveSettings
from Spotfire.Dxp.Framework.ApplicationModel import *
from Spotfire.Dxp.Data.Exceptions import ImportException
from Spotfire.Dxp.Data.Import import DataTableDataSource, TextFileDataSource, TextDataReaderSettings
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import DataTableDataSource
from Spotfire.Dxp.Data.Transformations import AddCalculatedColumnTransformation


def create_table(name, data_file, data_header):
    progress_service.CurrentProgress.ExecuteSubtask('Creating new data table...')  # вывод служебного окна
    source = DataTableDataSource(data_header)  # указывает путь к пустой таблице с "шапкой"
    new_table = Document.Data.Tables.Add(name, source)  # создает новую таблицу, где будут храниться обработанные данные
    new_table.ReplaceData(data_file)  # заменяет полученные из файла данные на обработанные
    settings = DataTableSaveSettings(new_table, False, False);  # (True, False) - linked; (False, False) - embedded
    Document.Data.SaveSettings.DataTableSettings.Add(settings);
    return new_table


def mapping_different_columns(source_table,
                              target_table):  # функция мепит столбцы ( mapping уникален для каждого регистра (слева - столбцы из анализатора, справа - из регистра)
    mapping = {
        "Номер актива": "Asset number",
        "Описание актива": "Asset description",
        "Местоположение": "Location",
        "Право владения": "Tenure",
        "Категория актива": "Asset category",
        "Тип актива": "Asset type",
        "Амортизирующийся актив": "Depreciating asset",
        "Метод амортизации": "Depreciation method",
        "Стоимость покупки": "Purchase cost",
        "Ликвидационная стоимость": "Residual balance",
        "Уменьшающийся остаток %": "Reducing balance %",
        "Срок полезного использования (в годах)": "Useful life (years)",
        "Оставшийся срок службы на начало периода": "Opening remaining life (years)",
        "Оставшийся срок службы на конец периода": "Closing remaining life (years)",
        "Дата оприходования": "Date capitalized",
        "Дата выбытия": "Disposal date",
        "Дата перемещения": "Transfer date",
        "Стоимость ОС на начало периода": "Opening cost",
        "Стоимость поступивших ОС": "Additions cost",
        "Стоимость перемещенных ОС": "Transfers cost",
        "Стоимость выбывших ОС": "Disposals cost",
        "Стоимость ОС на конец периода": "Closing cost",
        "Амортизация на начало периода": "Opening depreciation",
        "Начисленная амортизация": "Depreciation charged",
        "Амортизация при перемещении": "Depreciation transferred",
        "Амортизация при выбытии": "Depreciation disposed",
        "Амортизация на конец периода": "Closing depreciation",
        "Остаточная стоимость на начало периода": "Opening NBV",
        "Остаточная стоимость на конец периода": "Closing NBV",
        "Остаточная стоимость выбывших ОС": "NBV of disposals",
        "Остаточная стоимость перемещенных ОС": "NBV of transfers",
        "Доход от реализации": "Proceeds",
        "Прибыль от выбытия": "Profit on disposal",
        "Поле, заданное пользователем 1": "User defined 1",
        "Поле, заданное пользователем 2": "User defined 2",
        "Поле, заданное пользователем 3": "User defined 3",
        "Поле, заданное пользователем 4": "User defined 4",
        "Поле, заданное пользователем 5": "User defined 5",
        "Поле, заданное пользователем 6": "User defined 6",
        "Поле, заданное пользователем 7": "User defined 7",
        "Поле, заданное пользователем 8": "User defined 8",
        "Корректировка амортизации ЭЯ": "EY depreciation override"
    }
    settings_mapping = dict()
    data_source = DataTableDataSource(source_table)
    for target_column in target_table.Columns:
        if target_column.Name in mapping:
            source_column_name = mapping[target_column.Name]
            status, source_column = source_table.Columns.TryGetValue(source_column_name)
            if status:
                settings_mapping[DataColumnSignature(target_column)] = DataColumnSignature(source_column)

    ignoredColumns = List[DataColumnSignature]()
    for source_column in source_table.Columns:
        if source_column.Name not in mapping.values():
            ignoredColumns.Add(DataColumnSignature(source_column.Name, DataType.Undefined))

    settings = AddRowsSettings(settings_mapping, ignoredColumns)
    return settings


def getDataSourceFile():
    MessageBox.Show("Выберите файл с ОСВ", "Загрузка данных", MessageBoxButtons.OK)
    dialog = OpenFileDialog()  # открывает окно выбора
    dialog.InitialDirectory = '%USERPROFILE%\\Documents'  # начальная директория окна выбора
    dialog.Filter = 'Comma-separated Values (*.csv)|*.csv;|Text (*.txt)|*.txt|All files (*.*)|*.*'  # тип файлов
    dialog.ShowDialog()
    return dialog.FileName


def getDataSourceFile1():
    MessageBox.Show("Выберите файл со сравнительным периодом", "Загрузка данных", MessageBoxButtons.OK)
    dialog = OpenFileDialog()  # открывает окно выбора
    dialog.InitialDirectory = '%USERPROFILE%\\Documents'  # начальная директория окна выбора
    dialog.Filter = 'Comma-separated Values (*.csv)|*.csv;|Text (*.txt)|*.txt|All files (*.*)|*.*'  # тип файлов
    dialog.ShowDialog()
    return dialog.FileName

def execute():
    try:

        progress_service.CurrentProgress.ExecuteSubtask('Opening file...')  # вывод служебного окна
        status, table = Document.Data.Tables.TryGetValue(
            main_table)  # выясняет, добавлены ли уже у нас проводки текущего периода
        settings = TextDataReaderSettings()
        settings.Separator = ","  # Настройка сепаратора
        settings.AddColumnNameRow(0)  # Указание на номер строки, в которой указанно имя

        datecol = [14, 15, 16]
        for colnum in datecol:
            settings.SetDataType(colnum, DataType.Date)

        realcol = [8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 41]
        for colnum in realcol:
            settings.SetDataType(colnum, DataType.Real)

        strcol = [0, 1, 2, 3, 4, 5, 6, 7, 33, 34, 35, 36, 37, 38, 39, 40]
        for colnum in strcol:
            settings.SetDataType(colnum, DataType.String)

        ds = TextFileDataSource(fileloc, settings)
        ds.IsPromptingAllowed = True
        ds.ReuseSettingsWithoutPrompting = True
        dt = Document.Data.Tables["new_table"]
        dt2 = Document.Data.Tables["FAR"]  # пустая таблица с "шапкой"
        provider = dt.GetService(IServiceProvider)

        if status:
            new_table = create_table(tempr_table, ds, dt)
            # после обработки проводок прошлого периода, данные из временной таблицы переносятся в основную
            settings = mapping_different_columns(new_table, table)
            table.AddRows(DataTableDataSource(new_table), settings)
            Document.Data.Tables.Remove(new_table)

        else:
            create_table(main_table, ds, dt)
            dt2.AddRows(DataTableDataSource(new_table), settings)
        progress_service.CurrentProgress.CheckCancel()  # вывод служебного окна

    # обработка ошибок
    except (ArgumentException, PromptCanceledException, ProgressCanceledException):
        MessageBox.Show("Процедура импорта была прервана пользователем", "Ошибка импорта", MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table)

    except ImportException:
        MessageBox.Show("Во время импорта произошла ошибка", "Ошибка импорта", MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table)

    except:
        MessageBox.Show("Произошла непредвиденная ошибка, процедура импорта прервана", "Ошибка импорта",
                        MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table)

    else:
        MessageBox.Show("Загрузка файла завершена", "Загрузка данных", MessageBoxButtons.OK)


dt2 = Document.Data.Tables["data"]
rows_c = Document.ActiveFilteringSelectionReference.GetSelection(dt2).AsIndexSet()
t_rows = rows_c.Count

dialogResult = 0
progress_service = Application.GetService[ProgressService]()
if t_rows <= 0:
    fileloc = getDataSourceFile()
    if fileloc != "":
        progress_service.ExecuteWithProgress("Import from text-based file", "Importing tables", execute)
    else:
        MessageBox.Show("Процедура импорта была прервана пользователем", "Ошибка импорта", MessageBoxButtons.OK)
elif t_rows > 0:
    dialogResult = MessageBox.Show("Данные уже загружены. Очистить данные?", "Ошибка импорта", MessageBoxButtons.YesNo)
if (dialogResult == DialogResult.Yes):
    dtTarget = Document.Data.Tables['data']
    dtTarget.RemoveRows(RowSelection(IndexSet(dtTarget.RowCount, True)))
    MessageBox.Show("Данные успешно удалены.", "Очистка данных")

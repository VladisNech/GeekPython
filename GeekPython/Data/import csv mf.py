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
        "Табельный номер сотрудника": "Employee number",
        "Имя сотрудника": "Employee name",
        "Дата приема на работу": "Joining date",
        "Дата увольнения": "Leaving date",
        "Дата рождения": "Date of birth",
        "Адрес": "Address",
        "City": "City",
        "Country": "Country",
        "Postcode": "Postcode",
        "Идентификационный номер налогоплательщика": "Tax ID",
        "Идентификатор банка": "Bank ID",
        "Bank account number": "Bank account number",
        "Должность": "Job title",
        "Тип сотрудника": "Employee type",
        "Подразделение": "Business unit",
        "Location": "Location",
        "Пол": "Gender",
        "Employee pension contribution %": "Employee pension contribution %",
        "Employer pension contribution %": "Employer pension contribution %",
        "User defined MF1": "User defined MF1",
        "User defined MF2": "User defined MF2",
        "User defined MF3": "User defined MF3",
        "User defined MF4": "User defined MF4",
        "User defined MF5": "User defined MF5",
        "User defined MF6": "User defined MF6",
        "User defined MF7": "User defined MF7",
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
    MessageBox.Show("Выберите файл для загрузки", "Загрузка данных", MessageBoxButtons.OK)
    dialog = OpenFileDialog()  # открывает окно выбора
    dialog.InitialDirectory = '%USERPROFILE%\\Documents'  # начальная директория окна выбора
    dialog.Filter = 'Comma-separated Values (*.csv)|*.csv;|Text (*.txt)|*.txt|All files (*.*)|*.*'  # тип файлов
    dialog.ShowDialog()
    return dialog.FileName


def execute():
    try:

        progress_service.CurrentProgress.ExecuteSubtask('Opening file...')  # вывод служебного окна
        status, table = Document.Data.Tables.TryGetValue(
            main_table_mf)  # выясняет, добавлены ли уже у нас проводки текущего периода
        settings = TextDataReaderSettings()
        settings.Separator = "|"  # Настройка сепаратора
        settings.AddColumnNameRow(0)  # Указание на номер строки, в которой указанно имя

        datecol = [2, 3, 4]
        for colnum in datecol:
            settings.SetDataType(colnum, DataType.Date)

        realcol = [17, 18]
        for colnum in realcol:
            settings.SetDataType(colnum, DataType.Real)

        strcol = [0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25]
        for colnum in strcol:
            settings.SetDataType(colnum, DataType.String)

        ds = TextFileDataSource(fileloc, settings)
        ds.IsPromptingAllowed = True
        ds.ReuseSettingsWithoutPrompting = True
        dt = Document.Data.Tables["table_mf"]  # пустая таблица с "шапкой"
        provider = dt.GetService(IServiceProvider)

        if status:
            table_mf = create_table(tempr_table_mf, ds, dt)
            # после обработки проводок прошлого периода, данные из временной таблицы переносятся в основную
            settings = mapping_different_columns(table_mf, table)
            table.AddRows(DataTableDataSource(table_mf), settings)
            Document.Data.Tables.Remove(table_mf)

        else:
            create_table(main_table_mf, ds, dt)
        progress_service.CurrentProgress.CheckCancel()  # вывод служебного окна

    # обработка ошибок
    except (ArgumentException, PromptCanceledException, ProgressCanceledException):
        MessageBox.Show("Процедура импорта была прервана пользователем", "Ошибка импорта", MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table_mf)

    except ImportException:
        MessageBox.Show("Во время импорта произошла ошибка", "Ошибка импорта", MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table_mf)

    except:
        MessageBox.Show("Произошла непредвиденная ошибка, процедура импорта прервана", "Ошибка импорта",
                        MessageBoxButtons.OK)
        Document.Data.Tables.Remove(tempr_table_mf)

    else:
        MessageBox.Show("Загрузка файла завершена", "Загрузка данных", MessageBoxButtons.OK)


dt2 = Document.Data.Tables['Employee Master File']
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
    dtTarget = Document.Data.Tables['Employee Master File']
    dtTarget.RemoveRows(RowSelection(IndexSet(dtTarget.RowCount, True)))
    MessageBox.Show("Данные успешно удалены.", "Очистка данных")

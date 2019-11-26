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


def create_table(name, period, data_file, data_header):
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
        'Номер актива': 'Инвентарный номер',
        'Описание актива': 'Наименование объекта основных средств',
        'Местоположение': 'Местонахождение',
        'Категория актива': 'Группа основных средств',
        'Тип актива': 'Тип ОС',
        'Срок полезного использования (в годах)': 'СПИ год',
        'Дата оприходования': 'Дата ввода в эксплуатацию',
        'Стоимость ОС на начало периода': 'Первоначальная стоимость на начало периода',
        'Стоимость поступивших ОС': 'Поступило',
        'Стоимость выбывших ОС': 'Выбыло правильный знак',
        'Стоимость ОС на конец периода': 'Первоначальная стоимость на конец периода',
        'Амортизация на начало периода': 'Накопленная амортизация на начало периода правильный знак',
        'Начисленная амортизация': 'Амортизация за период правильный знак',
        'Амортизация на конец периода': 'Накопленная амортизация на конец периода правильный знак',
        'Остаточная стоимость на начало периода': 'Остаточная стоимость на начало периода',
        'Остаточная стоимость на конец периода': 'Остаточная стоимость на конец периода',
        "Компания": "Компания"}
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

        # Настройка типа столбцов по номеру столбца
        datecol = [9, 10]
        for colnum in datecol:
            settings.SetDataType(colnum, DataType.Date)

        realcol = [8, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        for colnum in realcol:
            settings.SetDataType(colnum, DataType.Real)

        strcol = [0, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 37]
        for colnum in strcol:
            settings.SetDataType(colnum, DataType.String)

        ds = TextFileDataSource(fileloc, settings)
        ds.IsPromptingAllowed = True
        ds.ReuseSettingsWithoutPrompting = True
        dt = Document.Data.Tables["RawDataHeader"]  # пустая таблица с "шапкой"
        provider = dt.GetService(IServiceProvider)

        if status:
            # если проводки текущего года уже загружены, создается временная таблица с проводками предыдущего периода
            new_table = create_table(tempr_table, period, ds, dt)
            # после обработки проводок прошлого периода, данные из временной таблицы переносятся в основную
            settings = mapping_different_columns(new_table, table)
            table.AddRows(DataTableDataSource(new_table), settings)

            Document.Data.Tables.Remove(new_table)  # временная таблица удаляется
        elif not status:
            create_table(main_table, period, ds, dt)

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
        MessageBox.Show("Загрузка файла завершена", "Загрузка текстовых файлов", MessageBoxButtons.OK)


progress_service = Application.GetService[ProgressService]()

fileloc = getDataSourceFile()
if fileloc != "":
    progress_service.ExecuteWithProgress("Import from text-based file", "Importing tables", execute)
else:
    MessageBox.Show("Процедура импорта была прервана пользователем", "Ошибка импорта", MessageBoxButtons.OK)

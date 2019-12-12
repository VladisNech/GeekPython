from Spotfire.Dxp.Data import DataTableSaveSettings
from Spotfire.Dxp.Data import *
from System.IO import Path, File
import datetime, time
import clr

clr.AddReferenceByName(
    'Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
clr.AddReference("System.Windows.Forms")

from Microsoft.Office.Interop import Excel
from System.Windows.Forms import MessageBox


def add_data_to_table(table_instance, data_source):
    """
    If there are any rows in table, then data is added to existing rows,
    else - data source replaces table contents.
    """

    if table_instance.RowCount:
        # Table has rows, data is added
        settings = AddRowsSettings(table_instance, data_source)
        table_instance.AddRows(data_source, settings)
    else:
        # Table is empty
        table_instance.ReplaceData(data_source)


# Function to perform the data import for a particular worksheet
def importWorksheet(excelApp, workbook, dataTableExcel, dataTableSpotfire):
    try:
        print
        'importing ' + dataTableExcel
        # export the worksheet into a temporary file
        tmpWorkbook = excelApp.Workbooks.Add()
        rngFrom = workbook.worksheets(dataTableExcel).UsedRange
        rngTo = tmpWorkbook.worksheets(1).Range("A1").Resize(rngFrom.Rows.Count, rngFrom.Columns.Count)
        rngFrom.Copy(rngTo)

        tempName = Path.GetTempPath() + dataTableExcel + datetime.datetime.now().strftime("%y%m%d_%H%M%S") + '.xlsx'
        print
        tempName
        tmpWorkbook.SaveAs(tempName)
        tmpWorkbook.Close()

        # Find out if a data table already exist in the DXP file
        table = Document.Data.Tables.Item[dataTableSpotfire]

        # Create data source
        ds = Document.Data.CreateFileDataSource(tempName)
        ds.IsPromptingAllowed = False
        ds.ReuseSettingsWithoutPrompting = True

        # Add new data if table has rows
        # Else - replace data in table
        add_data_to_table(table, ds)

        # clean up
        File.Delete(tempName)

        # report success
        return True

    except Exception, e:
        print
        e
        print
        Exception
        excelApp.Workbooks.Close()
        excelApp.Quit()
        # remove the temporary file, if the code had got that far
        if 'tempName' in locals():
            if File.Exists(tempName):
                File.Delete(tempName)
        # report failure
        return False


MessageBox.Show("Начало импорта - это может занять несколько минут")

# these are the expected tables in the Excel file
dictExcelDataTablesExist = {"Cover sheet": False, "Instructions for use": False, "Transaction data": False,
                            "Employee master data": False, "Transaction data for import": False,
                            "Employee master data for import": False}

# Local path and name of the excel file.
FileLocation = Document.Data.Properties.GetProperty(DataPropertyClass.Document, "ImportTemplatePath").Value
filename = FileLocation.replace("\\", "\\\\")
print
filename

# Microsoft Excel application
excelApp = Excel.ApplicationClass()
print
'Excel defined'
excelApp.Visible = False
print
'Excel non-visible'
excelApp.AutomationSecurity = 3  # MsoAutomationSecurity.msoAutomationSecurityForceDisable (not available in clr reference)
# excelApp.DisplayAlerts = False
# print 'Excel alerts off'

try:
    workbook = excelApp.Workbooks.Open(filename, 2, True)  # open readonly
    openStatus = "success"
except:
    MessageBox.Show("Ошибка при открытии файла - проверьте корректность Excel таблицы", "Ошибка импорта")
    openStatus = "fail"

if openStatus == "success":
    print
    'Загружена книга Excel:' + filename

    # for each sheet in the Excel workbook, check if it is one we care about and if so, record that it exists
    for sheet in workbook.Worksheets:
        if sheet.Name in dictExcelDataTablesExist.keys():
            dictExcelDataTablesExist[sheet.Name] = True

    # import the main Payroll tables.  If they does not exist, inform the user and quit
    if dictExcelDataTablesExist["Transaction data for import"] == True:
        # try the transaction table import
        transactionImportSucceeds = importWorksheet(excelApp, workbook, "Transaction data for import",
                                                    "Payment Data - Raw Data")
        # if the first import failed, then abort
        if transactionImportSucceeds == True:
            # try to import the Employee master data.  If it does not exist, abort the process
            if dictExcelDataTablesExist["Employee master data for import"]:
                masterImportSucceeds = importWorksheet(excelApp, workbook, "Employee master data for import",
                                                       "Employee Master File - Raw Data")
            else:
                MessageBox.Show(
                    "Ошибка: файл не содержит лист 'Employee master data for import'\n\nУбедитесь, что вы нажали кнопку 'Prepare data for import' в шаблоне импорта данных Excel.",
                    "Отсутствуют данные - Импорт отменен")
                masterImportSucceeds = False

        # Exit MS Excel
        excelApp.Workbooks.Close()
        excelApp.Quit()

        # report to the user
        if transactionImportSucceeds == True:
            if masterImportSucceeds == True:
                reportMessage = "Импорт завершен:\nИмпорт транзакций завершен успешно\nИмпорт основных данных сотрудников завершен успешно"
            else:
                reportMessage = "Импорт завершен:\nИмпорт транзакций завершен успешно\nОшибка импорта основных данных сотрудников"
        else:
            reportMessage = "Ошибка импорта:\nОшибка импорта транзакций\nИмпорт основных данных сотрудников пропущен"

        MessageBox.Show(reportMessage)

        # if successful, then call the setup script
        if transactionImportSucceeds == True and masterImportSucceeds == True:
            from Spotfire.Dxp.Application.Scripting import ScriptDefinition
            from System.Collections.Generic import Dictionary

            scriptDef = clr.Reference[ScriptDefinition]()
            Document.ScriptManager.TryGetScript("LoadedScriptNew", scriptDef)
            params = Dictionary[str, object]()
            params['Masterfile'] = Masterfile
            params['Payment'] = Payment
            Document.ScriptManager.ExecuteScript(scriptDef.ScriptCode, params)

    else:
        MessageBox.Show(
            "Ошибка: этот файл не содержит лист 'Transaction data for import'\n\nУбедитесь, что вы нажали кнопку 'Prepare data for import' в шаблоне импорта данных Excel.",
            "Отсутствуют данные - Импорт отменен")

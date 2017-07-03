#Author: Marisa L. Roman
#QueryResultFormatterForJira:
#Copy the active query (or all queries in the editor if none is selected)
#and results to the text output tab in MySQLWorkbench, with Jira formatting.

#Workbench imports
from wb import *
import grt
import mforms

#Plugin definition
ModuleInfo = DefineModule(name='QueryResultFormatterForJira', author='Marisa L. Roman', version='1.0')
@ModuleInfo.plugin("wb.sqlide.executeToJiraFormat", caption="Execute Query to Jira Format", input=[wbinputs.currentQueryBuffer()], pluginMenu="SQL/Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_query_QueryBuffer)

#Formatter
def executeQueryToJiraFormat(qbuffer):
    editor = qbuffer.owner
    sql = qbuffer.selectedText or qbuffer.script
    resultsets = editor.executeScript(sql)

    #Copy column headers to output with Jira column header formatting
    for result in resultsets:

        #Copy query to resulting text, wrapped in Jira SQL code formatting tags.
        resultText = "{code:sql}\n" + result.sql + "\n{code}\n"
        rowCount = result.rowCount

        #If there are no results, display a statement indicating such.
        #Otherwise, format each row in Jira table formatting.
        if rowCount == 0:
            resultText += "Empty result set.\n"
        else:
            #Format column headers
            columnHeaders = "||"
            for column in result.columns:
                columnHeaders += column.name + "||"
                
            resultText += columnHeaders + "\n"

            #Format rows
            for rowIndex in range(rowCount):
                result.goToRow(rowIndex)
                resultText += "|"

                for columnIndex in range(len(result.columns)):
                    value = result.stringFieldValue(columnIndex)

                    if value is None:
                        value = "NULL"
                    elif len(value.strip()) == 0:
                        value = " "

                    resultText += value + "|"

                resultText += "\n"
                
        editor.addToOutput(resultText, 0)

    return 0

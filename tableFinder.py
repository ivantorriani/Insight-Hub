# - - - - - - - - - - - - -

import win32com.client as client

word = client.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

numOfTables = doc.Tables.Count



def findTable(key):
    for tables in range(1, int(numOfTables)):
        checkTable = doc.Tables(tables)
        checkCell = checkTable.Cell(1,1)
        if str(key) in checkCell.Range.Text:
            checkCell = checkTable.Cell(1,2)
            return checkCell.Range.Text




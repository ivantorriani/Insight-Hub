# - - - - - - - - - - - - -
'''
import win32com.client as client
from tableFinder import findTable
import easygui as ez

# - - - - - - - - - - - - -
word = client.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

numOfTables = doc.Tables.Count


def followUpTables():
    checkRequest = ez.enterbox("Gil: Do you have a follow up? ")
    if (checkRequest == "y"):
        doc.SaveAs(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
        checkKey = str(ez.enterbox("Gil: Type in table key please! "))
        findTable(checkKey)
        return int((findTable(checkKey)))

def followUpGrabber():
    followUpQ = ez.enterbox("Gil: What's your follow up?")
    return followUpQ



'''



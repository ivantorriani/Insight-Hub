# - - - - - - - - - - - - -

import win32com.client as client
from tableFinder import findTable

# - - - - - - - - - - - - -
word = client.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

numOfTables = doc.Tables.Count


def followUpTables():
    checkRequest = input("Gil: Do you have a follow up? ")
    if (checkRequest == "y"):
        checkKey = str(input("Gil: Type in table key please! "))
        findTable(checkKey)
        return int((findTable(checkKey)))

def followUpGrabber():
    followUpQ = input("Gil: What's your follow up?")
    return followUpQ


print(followUpTables)




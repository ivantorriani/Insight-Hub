#README
#Use the crated lists from entryGrabber (Questions) and aiParser (Answer) 
#Current Problem: I can only create one table entry currently. 

import win32com.client as win32
from aiParser import listOfAnswers, listOfEntries, secparseAI
from keyGenerator import generateKey
from follupGrabber import followUpTables,followUpGrabber




word = win32.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

start = 0


def createTables():
    global start
    
    while start < len(listOfEntries):
        range_obj.InsertParagraphAfter()
        table_range = doc.Paragraphs(doc.Paragraphs.Count).Range
        table = doc.Tables.Add(table_range, 2,2)
        table.Borders.Enable = True
        
        questionsCell = table.Cell(1,1)
        answersCell = table.Cell(1,2)


        questionsCell.Range.Text = (

            "Key:" + str(generateKey()    ) + 
            listOfEntries[start]
        )

        answersCell.Range.Text = listOfAnswers[start]

def addFollowUp():
        checkValidity = followUpTables()
        if checkValidity != None:
            tabValue = int(followUpTables())
            range_obj.InsertParagraphAfter()
            table = doc.Tables(tabValue)
            followUpQ = table.Cell(2,1)
            followUpA = table.Cell(2,2)

            followUpQ.Range.Text = str(followUpGrabber())
            followUpA = str(secparseAI())
        else:
             print("Gil: Ok, thanks!")


addFollowUp()






        


doc.SaveAs(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')


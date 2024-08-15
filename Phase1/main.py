
#imports- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import win32com.client as win32
from aiParser import listOfAnswers, listOfEntries
from keyGenerator import generateKey
import easygui 
import json

#pywin init - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

word = win32.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

#json init - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

try:
    with open('newInfo.json', 'r') as jsonFile:
        newInfo = json.load(jsonFile)
except FileNotFoundError:
    newInfo = []

# create tables - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

start = 0
def createTables():
    global start

    while start < len(listOfEntries):

        #create tables - - - - - - - - - - - - -

        range_obj.InsertParagraphAfter()
        table_range = doc.Paragraphs(doc.Paragraphs.Count).Range
        table = doc.Tables.Add(table_range, 2,2)
        table.Borders.Enable = True
        
        questionsCell = table.Cell(1,1)
        answersCell = table.Cell(1,2)

        #fill in tables - - - - - - - - - - - - -

        questionsCell.Range.Text = (

            "Key:" + str(generateKey()) + 
            listOfEntries[start]
        )

        answersCell.Range.Text = listOfAnswers[start]

        #save to json file - - - - - - - - - - - - -

        newInfo.append(

            "Question: " + str(listOfEntries[start]) + 
            "Answers: " + str(listOfAnswers[start])
        )

        with open('newInfo.json', 'w') as file:
            json.dump(newInfo, file, indent=2)
            
        #save doc - - - - - - - - - - - - -

        doc.SaveAs(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
        start += 1

        

createTables()

'''with open('newInfo.json', 'w') as file:
    json.dump([], file)'''






'''def addFollowUp():
        checkValidity = int(followUpTables())
        if checkValidity is not None:
            follUpGrabs = followUpGrabber()
            aiPhase2 = secparseAI(str(follUpGrabs))
            tabValue =int(checkValidity)
            range_obj.InsertParagraphAfter()
            table = doc.Tables(tabValue)
            followUpQ = table.Cell(2,1)
            followUpA = table.Cell(2,2)
            followUpA.Range.Text = str(aiPhase2[0])
            followUpQ.Range.Text = str(aiPhase2[1])
            
        else:
             print("Gil: Ok, thanks!")'''









        




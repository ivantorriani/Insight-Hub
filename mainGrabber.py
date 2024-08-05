#README
#This version of entry grabber creates the list of questions beforehand instead of concurrently.
#Meant to create easier access for AI parsing, and possibly easier table making.

import win32com.client as win32
import tkinter as tk 
from tkinter import messagebox

#pywin initialization
word = win32.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

#tkinter imports
    



#initialize list
entriesList = []


def gatherEntries():
    while True:
        checkInquiry = input("Do you have any questions to add?: ")
        if checkInquiry == "y":
            entry = input("Type in your question here please: ")
            entriesList.append(str(entry))
        else:   
            print("Thanks! Your summary will arrive shortly")
            return entriesList
        
# follup grabber


def createTables(inputs):
    range_obj.InsertParagraphAfter()
    table_range = doc.Paragraphs(doc.Paragraphs.Count).Range

    # Create a table with the specified data
    table = doc.Tables.Add(table_range, 1,2)
    table.Borders.Enable = True

    questionsCell = table.Cell(1,1)

    questionsCell.Range.Text = inputs









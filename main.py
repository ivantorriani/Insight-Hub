# import statements
import win32com.client as win32
from openai import OpenAI

'''
# pywin32 and AI initializations
word = win32.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(r'C:\Users\sotiv\Documents\Reflections\Subject Reflections\Linear Algebra\conceptualCelina.docx')
range_obj = doc.Content

api_key = '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'
client = OpenAI(api_key=api_key)


#Function 

def getResponse():
    user_input = input("Test test: ")
            
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Give me short concise answers, this is a test run"},
                {"role": "user", "content": user_input}
            ]
        )

    answer = str(completion.choices[0].message.content)
    return answer
response = getResponse()
def createTables(content1, content2):
    range_obj.InsertParagraphAfter()
    table_range = doc.Paragraphs(doc.Paragraphs.Count).Range

    # Create a table with the specified data
    table = doc.Tables.Add(table_range, 1,2)
    table.Borders.Enable = True

    #add content
    cell = table.Cell(1, 1)
    cell.Range.Text = content1
    cell2 = table.Cell(1,2)
    cell2.Range.Text = content2

    #getResponses
    testText = table.Cell(1,1).Range.Text
    return testText



createTables(response, "hello!")
#EXPL'''





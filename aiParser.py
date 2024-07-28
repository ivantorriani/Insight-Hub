#Read Me
#aiParser uses the list created from entryGrabber, indexes through it, 



#initializations
from entryGrabber import gatherEntries
from openai import OpenAI

api_key = 'skeeeeee'
client = OpenAI(api_key=api_key)


listOfEntries = gatherEntries()
answersList = []

start = 0
AIdesc = (
    "You are Gilbert, a great Linear Algebra teacher! Your job is to provide students with a clear,short answer" +
    "Here are some pointers: Always assume the student has background knowledge, no buildup needed!" + 
    "Don't use any symbols or math rendering things -- only words!"
    "Always provide a geometric perspective and a algeabraic example. Thanks Gil!"
)

def parseAI():
    global start, AIdesc
    while (start < len(listOfEntries)):
        completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc},
                {"role": "user", "content": listOfEntries[start]}
            ]
        )

        start += 1
        answer = str(completion.choices[0].message.content)
        answersList.append(answer)

    return answersList


        

listOfAnswers = parseAI()


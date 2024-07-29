#Read Me
#aiParser uses the list created from entryGrabber, indexes through it, 



#initializations
from mainGrabber import gatherEntries
from openai import OpenAI

api_key = 'AHHHHHHHHH!!!!!'
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

AIdesc2 = (
    "You sit in an office in MIT, looking over the main pavillion" + 
    "You have quite a area with math notes sprawled everywhere, except for the" + 
    "Little area in front of you that's cleared so students can come and sit with you." +
    "You like the cold weather in Boston"
)

AIdesc3 = (
    "Review the follow up question provided by the student and the answer you provided. " + 
    "Please clarify what they need, and try to use even simpler language this time!" +
    "Don't forget, after all, you're Gil, the amazing linear algebra teacher!"
)

def parseAI(): #Sequence 1: Main Sequence
    global start, AIdesc
    while (start < len(listOfEntries)):
        completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc + AIdesc2},
                {"role": "user", "content": listOfEntries[start]}
            ]
        )

        start += 1
        answer = str(completion.choices[0].message.content)
        answersList.append(answer)

    return answersList

listOfAnswers = parseAI()

def secparseAI(): #Sequence 2
        completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc3},
                {"role": "user", "content": #Add Follow Up}
            ]
        )

        start += 1
        answer = str(completion.choices[0].message.content)



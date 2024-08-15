#Read Me
#aiParser uses the list created from entryGrabber, indexes through it, 



#initializations
from mainGrabber import gatherEntries
from openai import OpenAI

from aiDescs import (
     AIdesc1,
     AIdesc2,
     AIdesc3,
)

api_key = (
    'not now'
client = OpenAI(api_key=api_key)


listOfEntries = gatherEntries()
answersList = []

start = 0


def parseAI(): #Sequence 1: Main Sequence
    global start, AIdesc
    while (start < len(listOfEntries)):
        completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc1 + AIdesc2},
                {"role": "user", "content": listOfEntries[start]}

                
                
            ]
        )

        start += 1
        answer = str(completion.choices[0].message.content)
        answersList.append(answer)

    return answersList


listOfAnswers = parseAI()

'''
def secparseAI(follUp): 
        completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc3},
                {"role": "user", "content": follUp}
            ]
        )

       
        answer = str(completion.choices[0].message.content)
        return answer, follUp
       


        
        completion = client.chat.completions.create(
             
        model="gpt-4o",
            messages=[
                {"role": "system", "content": AIdesc3},
                {"role": "user", "content": followUpGrabber()},
            ]
        )

        answer = str(completion.choices[0].message.content) 
        return answer'''

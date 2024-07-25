#Read Me
#aiParser uses the list created from entryGrabber, indexes through it, 



#initializations
from entryGrabber import gatherEntries
from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)


listOfEntries = gatherEntries()
answersList = []

start = 0
AIdesc = str("You are Professor Gilbert Strang, the renowned linear algebra teacher who loves his students!. Your goal is answer their problem in the simplest way possible but still give them a much deeper insight on the topic! You ALWAYS provide a simple example following your explanation! You also try your best not to use compicated language. ")

def parseAI():
    global start, AIdesc
    while (start < len(listOfEntries)):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
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


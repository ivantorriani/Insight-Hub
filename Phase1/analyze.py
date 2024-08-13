# inits- - - - - - - - - - - - - - - - - 
import json
from aiDescs import AIdesc4, AIdesc5
from openai import OpenAI

# openai init- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
api_key = 'teedlebum'
client = OpenAI(api_key=api_key)

# json file init - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

try:
    with open('newInfo.json', 'r') as jsonFile:
        newInfo = json.load(jsonFile)
except FileNotFoundError:
    newInfo = []

# json file dump, manual for now  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#with open('newInfo.json', 'w') as file:
    #json.dump([], file)


# relevant to analyze bot- - - - - - - - - - - - - - - - - - - - - - - 
past_questions = []
gathered_questions = []

#analyze and create questions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
count = 0
def analyzebot(): #Sequence 1: Main Sequence
    global AIdesc4, count, newInfo
    while (count < 6):
        if (past_questions is not None):
            completion = client.chat.completions.create(
                model="gpt-4o",
                    messages=[
                        {"role": "system", "content": str(AIdesc4) + str(AIdesc5) },
                        {"role": "user", "content": newInfo}
                    ]
                )
            
            questions = str(completion.choices[0].message.content) 

            past_questions.append(str(questions))
            gathered_questions.append(str(questions))

        else:
            completion = client.chat.completions.create(
                model="gpt-4o",
                    messages=[
                        {
                            "role": "system", "content": "Here is your role:" + str(AIdesc4) + "." + 
                            " Here's the list of questions you've already made, as promised!" + gathered_questions
                        }

                        ,
                        
                        {"role": "user", "content": newInfo}
                    ]
                )
            

            
            questions = str(completion.choices[0].message.content) 

            past_questions.append(str(questions))
            gathered_questions.append(str(questions))


    










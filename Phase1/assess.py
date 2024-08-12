# inits- - - - - - - - - - - - - - - - - 
import json
from aiDescs import AIdesc4
from openai import OpenAI

# openai init- - - - - - - - - - - - - - - - - 
api_key = 'teedlebum'
client = OpenAI(api_key=api_key)

# json file init - - - - - - - - - - - - - - - - - 

try:
    with open('newInfo.json', 'r') as jsonFile:
        newInfo = json.load(jsonFile)
except FileNotFoundError:
    newInfo = []

def parseAI(): #Sequence 1: Main Sequence
    global start, AIdesc
    completion = client.chat.completions.create(
        model="gpt-4o",
            messages=[
                {"role": "system", "content":#tbc},
                {"role": "user", "content": #tbc}
            ]
        )

       
    answer = str(completion.choices[0].message.content)











# - - - - - - - - - - - - -
import random 



def generateKey():
    key = []
    for i in range(4):
        i = random.randint(1,9)
        key.append(i)
    return key

preKey = generateKey()

key = (

    str(preKey[0]) + 
    str(preKey[1]) + 
    str(preKey[2]) 
)




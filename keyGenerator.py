# - - - - - - - - - - - - -
import random 



def generateKey():
    key = []
    for i in range(4):
        i = random.randint(1,9)
        key.append(i)

    randKey =(
        str(key[0]) + 
        str(key[1]) + 
        str(key[2]) 
    )

    return randKey










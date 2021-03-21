#fortune ball

import random

def getA(AnswerN):
    if AnswerN == 1:
        print('you will marry a hottie')
    elif AnswerN == 2:
        print('you will have a sad life')
    elif AnswerN == 3:
        print('you will be cool, but your friends won\'t like you')
    elif AnswerN == 4:
        print('you will die very old')
    elif AnswerN == 5:
        print('you will die young')
    elif AnswerN == 6:
        print('you will be rich out of your mind')
    elif AnswerN == 7:
        print('you will poor out of your mind')

r = random.randint(1,7)
fortune = getA(r)
print(fortune)


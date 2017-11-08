#author:KAI
import random

def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield(pos,)
            else:
                for result in queens(num,state+(pos,)):#Recursion
                    yield (pos,)+result


def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False


def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '.'*(pos)+'X'+'.'*(length-pos-1)
    for pos in solution:
        print(line(pos))



#prettyprint(random.choice(list(queens(8))))
#prettyprint(list(queens(8)))
prettyprint(random.choice(list(queens(4))))

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:10:19 2017

@author: KAI
"""
#import numpy as np

puzzle=[['t','h','i','s'],
        ['w','a','t','s'],
        ['o','a','h','g'],
        ['f','g','d','t']]
dicti=['at','this','two','fat','that']
S=len(puzzle) # the size of puzzle

def word_exist(i,j,direaction,length,puzzle,d):
    word=str(puzzle[i][j])#当前字符
    for l in range(length):
        if direaction==0:
            j+=1
        elif direaction==1:
            i-=1;j+=1
        elif direaction==2:
            i-=1;
        elif direaction==3:
            i-=1;j-=1
        elif direaction==4:
            j-=1
        elif direaction==5:
            i+=1;j-=1
        elif direaction==6:
            i+=1
        elif direaction==7:
            i+=1;j+=1
        try:
            word=word+puzzle[i][j]
        except:
            pass
    flag=(True if word in d else False)
    
    return(word,flag)
          
# x,y= index
# the number of direactions is 8
for x, y in zip(range(0,S), range(0,S)):#第一个字母
    for direaction in range(0,8):
        for length in range(0,S):
            (word,flag)=word_exist(x,y,direaction,length,puzzle,dicti)
            if flag:
                print(word+' found')
                    
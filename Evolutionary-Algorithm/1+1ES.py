# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:24:34 2017

@author: KAI

{1+1}-ES
"""
import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 1             # DNA (real number)
DNA_BOUND = [0, 5]       # solution upper and lower bounds
N_GENERATIONS = 200
MUT_STRENGTH=5

def F(x): return np.sin(10*x)*x + np.cos(2*x)*x + np.sin(5*x)*x**2     # to find the maximum of this function


# find non-zero fitness for selection
def get_fitness(pred): return pred.flatten()


def make_kid(parent):
    # generate empty kid holder
    kids = parent+MUT_STRENGTH*np.random.randn(DNA_SIZE)
    kids = np.clip(kids,*DNA_BOUND)#*turple参数读法
    return kids


def kill_bad(parent, kids):
    # put pop and kids together
    global MUT_STRENGTH
    fp = get_fitness(F(parent))#[0]
    fk = get_fitness(F(kids))#[0]
    p_target = 1/5
    if fp < fk:     # kid better than parent
        parent = kids
        ps = 1.     # kid win -> ps = 1 (successful offspring)
    else:
        ps = 0.
    # adjust global mutation strength
    MUT_STRENGTH *= np.exp(1/np.sqrt(DNA_SIZE+1) * (ps - p_target)/(1 - p_target))
    ms=MUT_STRENGTH
    return parent,ms

parent=np.abs(5*np.random.randn(DNA_SIZE))

plt.ion()       # something about plotting
x = np.linspace(*DNA_BOUND, 200)
#plt.plot(x, F(x))

for i in range(N_GENERATIONS):
    # something about plotting
        # ES part
    kids = make_kid(parent)
    (parent,ms) = kill_bad(parent, kids)   # keep some good parent for elitism
    if ms<=10e-5:
        break
    plt.cla()
    plt.scatter(parent, F(parent), s=200, lw=0, c='red', alpha=0.5,)
    plt.scatter(kids,F(kids), s=200, lw=0, c='blue', alpha=0.5)
    plt.text(0, -7, 'Mutation strength=%.2f' % MUT_STRENGTH)
    plt.plot(x, F(x))
    plt.pause(0.05)

plt.ioff(); plt.show()

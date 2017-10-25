# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:39:29 2017

@author: KAI
"""
import numpy as np

TARGET_PHRASE = 'I like you~'       # 目标 DNA
POP_SIZE = 300                      # 种群大小
CROSS_RATE = 0.8                    # 交叉率
MUTATION_RATE = 0.01                # 变异率
N_GENERATIONS = 1000

DNA_SIZE = len(TARGET_PHRASE)
TARGET_ASCII = np.fromstring(TARGET_PHRASE, dtype=np.uint8)  # 字符串转ASCII码
ASCII_BOUND = [32, 127] #space~~ #upper bound+1

def translateDNA(DNA):                 # ASCII码转字符串
    return DNA.tostring().decode('ascii')

def get_fitness(pop):                      # 匹配度
    match_count = (pop == TARGET_ASCII).sum(axis=1)
    return match_count

def select(pop,fitness):
    index = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness/fitness.sum())
    return pop[index]

def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)                        
        cross_points = np.random.randint(0, 2, DNA_SIZE).astype(np.bool)   
        parent[cross_points] = pop[i_, cross_points]                            
    return parent

def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() <MUTATION_RATE:
            child[point] = np.random.randint(*ASCII_BOUND)  # 随机 ASCII 
        return child


if __name__ == '__main__':
    pop = np.random.randint(*ASCII_BOUND, (POP_SIZE, DNA_SIZE)).astype(np.int8)  #种群初始化
    for generation in range(N_GENERATIONS):
        fitness = get_fitness(pop)#计算适应度
        best_phrase=translateDNA(pop[np.argmax(fitness)])
        print('Gen', generation, ': ', best_phrase)

        if best_phrase == TARGET_PHRASE:
            break
        pop = select(pop, fitness)#最大适应度的点
        pop_copy = pop.copy()
        for parent in pop:
            child = crossover(parent, pop_copy)#交叉配对
            child = mutate(child)#变异
            parent[:] = child   #替换
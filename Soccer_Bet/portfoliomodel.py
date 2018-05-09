#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" determine lottery portfolio model """

import lottery
import numpy as np
import time
#以下为遗传算法用到的函数
DNA_SIZE=10  #3个变量*10条DNA
DNA_NUM=3
POP_SIZE = 300                   # 种群大小
CROSS_RATE = 0.8                    # 交叉率
MUTATION_RATE = 0.02                # 变异率
N_GENERATIONS = 500
X_BOUND=[0,1]#0-1的界
def translateDNA(pop):
    pop_list=np.hsplit(pop,DNA_NUM)
    pop_norm=[]
    for i in range(len(pop_list)):
        pop_norm.append(pop_list[i].dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1])#二进制转十进制
    pop=np.vstack(pop_norm).T
    for j in range(len(pop)):
        pop[j,:]=pop[j,:]/sum(pop[j,:])   
    return pop#返回的是三个比率

def get_fitness(pop,portfolio):                      # 匹配度
    odds=np.array([portfolio.win_item.cw_odds,portfolio.draw_item.cd_odds,portfolio.lose_item.cl_odds])
    odds=np.repeat(odds,POP_SIZE).reshape(DNA_NUM,POP_SIZE).T
    expect_gain=np.array(100*(pop*odds))#期望收益
    fitness = np.exp(np.min(expect_gain,axis=1)/100)#胜负平中最小的期望收益
    return fitness

def select(pop,fitness):
    index = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=np.squeeze(fitness/fitness.sum()))
    return pop[index]

def crossover(parent, pop):     
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)                             # select another individual from pop
        cross_points = np.random.randint(0, 2, size=DNA_NUM*DNA_SIZE).astype(np.bool)   # choose crossover points
        parent[cross_points] = pop[i_, cross_points]                            # mating and produce one child
    return parent

def mutate(child):
    for point in range(DNA_SIZE*DNA_NUM):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

#遗传算法主函数
def get_best_profit_GA(portfolio):
    max_profit=0
    pop = np.random.randint(0, 2, (1, DNA_SIZE*DNA_NUM)).repeat(POP_SIZE, axis=0)  # 二进制序列DNA初始化
    for generation in range(N_GENERATIONS):
        fitness = get_fitness(translateDNA(pop),portfolio)#计算适应度
        #best_pop=pop[np.argmax(fitness)].dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1]
        best_DNA=pop[np.argmax(fitness)]
        best_odds=translateDNA(best_DNA)[0]
        best_profit=np.log(max(fitness))*100
        print('Gen', generation, ': ',best_profit,best_odds)
        #time.sleep(0.2)
        if best_profit >= max_profit:
            max_profit=best_profit
            max_best_odds=best_odds
            
        pop = select(pop, fitness)#最大适应度的点
        pop_copy = pop.copy()
        for parent in pop:
            child = crossover(parent, pop_copy)#交叉配对
            child = mutate(child)#变异
            parent[:] = child[:]  #替换


    portfolio.profit = max_profit
    portfolio.win_percentage = max_best_odds[0]*100
    portfolio.draw_percentage = max_best_odds[1]*100
    portfolio.lose_percentage = max_best_odds[2]*100

    return portfolio


def best_portfolio(match):

    portfolio = lottery.LotteryPortfolio()#

    for item in match.item_arr:

        if portfolio.win_item.cw_odds < item.cw_odds:
            portfolio.win_item = item

        if portfolio.draw_item.cd_odds < item.cd_odds:
            portfolio.draw_item = item

        if portfolio.lose_item.cl_odds < item.cl_odds:
            portfolio.lose_item = item
#以上为第一步贪婪算法，找出即时胜负平赔率最高的公司item
    portfolio = get_best_profit_GA(portfolio)#遗传寻优-投资分配比

    return portfolio
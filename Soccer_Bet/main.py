#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

import spider#所有爬取信息的函数的py文件
import portfoliomodel#投注寻优py文件
import time

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
def main():
    m_match_ids = spider.crawl_match_list()#当日所有比赛的id
    
    for m_match_id in m_match_ids:
        print(m_match_id)#当前比赛id
        m_match = spider.crawl_match_info(m_match_id)#获取当前比赛信息
    
        best_portfolio_strategy = portfoliomodel.best_portfolio(m_match)#为该场比赛寻求最佳投注
    
        m_match.display()#打印比赛信息
        best_portfolio_strategy.display()#打印最佳投注
        time.sleep(0.2)
    #input('按任意键继续')
        
if __name__=='__main__':
    main()
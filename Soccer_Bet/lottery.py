#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" lottery related class """
import time
class LotteryItem(object):
#每个博彩公司的类
    def __init__(self):
        self.company = ""
        self.id = 0
        self.w_odds = float(0)#初盘赔率
        self.d_odds = float(0)
        self.l_odds = float(0)
        self.cw_odds = float(0)#即时欧赔c=current
        self.cd_odds = float(0)
        self.cl_odds = float(0)
        self.c_wp=float(0)#即时胜率
        self.c_dp=float(0)
        self.c_lp=float(0)
        self.wp=float(0)#初盘概率(胜)
        self.dp=float(0)
        self.lp=float(0)
        self.back_ratio = 0#返还率
        self.count = 1

    def display(self):
        print("%s\t%s\t%s\t%s\t%s\t" % (self.id, self.company, self.cw_odds, self.cd_odds, self.cl_odds))


class LotteryMatch(object):
#比赛match类
    def __init__(self, match_name, match_link,  match_time, host_team, guest_team, item_arr):
        self.match_name = match_name
        self.match_link = match_link
        self.match_time = match_time
        self.host_team = host_team
        self.guest_team = guest_team
        self.item_arr = item_arr#该场比赛所有的博彩公司

    def display(self):
        file=open('%s soccer_bet.txt'%(time.strftime('%Y_%m_%d')),'a+')
        print("match name:\t%s\nmatch members:\t%s VS %s\nmatch time:\t%s" % \
              (self.match_name, self.host_team, self.guest_team, self.match_time),file=file)

    def display_items(self):
        for item in self.item_arr:
            item.display()


class LotteryPortfolio(object):
#投注策略类
    def __init__(self):
        self.fund_count = 0

        self.profit = 0#按照下面的比例购买彩票，能够获得的收益

        self.win_item = LotteryItem()#押胜的公司信息
        self.draw_item = LotteryItem()
        self.lose_item = LotteryItem()
#从company下注 27%的资金押胜 (其中168是公司id，Pinnbet是公司名称，4.2是赔率，27是押27%的资金)
        self.win_percentage = 0#在胜押x%的资本
        self.draw_percentage = 0#在平押x%的资本
        self.lose_percentage = 0#在负押x%的资本

    def display(self):
        file=open('%s soccer_bet.txt'%(time.strftime('%Y_%m_%d')),'a+')
        print("min_profit:\t%s\nwin:\t%s %s\t%s\t%.2f\ndraw:\t%s %s\t%s\t%.2f\nlose:\t%s %s\t%s\t%.2f" % \
              (self.profit,
               self.win_item.id, self.win_item.company, self.win_item.cw_odds, self.win_percentage,
               self.draw_item.id, self.draw_item.company, self.draw_item.cd_odds, self.draw_percentage,
               self.lose_item.id, self.lose_item.company, self.lose_item.cl_odds, self.lose_percentage),file=file)
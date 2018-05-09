#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" lottery item class """

import re
import lottery
import datetime
import requests
#from bs4 import BeautifulSoup

#以下为用来获取url信息的函数
def url_get(url_str, decode):
    r = requests.get(url_str)
    return r.content.decode(decode, "ignore")#.encode('utf-8')

#以下为获取当日所有比赛的id的爬虫函数
def crawl_match_list():

    today = datetime.datetime.now()
    date=str(today.year) + "-" + str(today.month) + "-" + str(today.day)
    url_str = "http://trade.500.com/jczq/dgp.php?date="+ date +"&playtype=both"
    content = url_get(url_str, "gbk")
    match_id_r = re.compile(r'http://odds.500.com/fenxi/ouzhi-(\d+).shtml')

    match_ids = []

    for m in match_id_r.finditer(content):
        match_ids.append(m.group(1))

    return match_ids

#以下为获取一场比赛的信息+收集所有投注策略
def crawl_match_info(match_id):
    url_str = "http://odds.500.com/fenxi/ouzhi-" + str(match_id) + ".shtml"
    print(url_str)
    content = url_get(url_str, "gbk")
    #print content

    match = lottery.LotteryMatch("match_name", "match_link",  "match_time", "host_team", "guest_team", "item_arr")

    match_info_r = re.compile(r'<a class="hd_name"[\s\S]*?>([\s\S]*?)<')

    match_info=re.findall(match_info_r,content)
    match.host_team = match_info[0].strip()
    match.match_name = match_info[1].strip()
    match.guest_team = match_info[2].strip()

    match_time_r = re.compile(r'<p class="game_time">([\s\S]*?)</p>')

    match.match_time = re.findall(match_time_r,content)[0]
    match.item_arr = crawl_lottery_items(match_id)#所有博彩公司
#所有博彩公司信息收集完，返回该场比赛(一个类)接下来寻优
    return match


def crawl_lottery_items(match_id):

    url_str = "http://odds.500.com/fenxi1/ouzhi.php?id=" + str(match_id) + "&ctype=1&start="+str(1)+"&r=1&style=0&last=1&guojia=0&chupan=0"
    content = url_get(url_str, "utf-8")

    item_r = re.compile(r'(xls="row"[\s\S]*?)<tr class="tr\d"')#每一个博彩公司的所有信息
    lottery_items = []#所有博彩公司

    item_seq = 0

    for m in item_r.finditer(content):#所有公司做完，返回公司类的list

        item_seq += 1
        lottery_item = lottery.LotteryItem()
        lottery_item.id = item_seq

        one_item = m.group(1)
        company_pattern = re.compile(r'class="tb_plgs" title="(.*?)"')
        company_match = company_pattern.search(one_item)

        if company_match:
            lottery_item.company = company_match.group(1)#公司名称

        odds_pattern = re.compile(r'style="cursor:pointer" >(.*?)</td>')
        probability_pattern=re.compile(r'>(\d+\.\d+)?%')

        seq = 0
        for odd in odds_pattern.finditer(one_item):
            seq += 1
            odd_f = float(odd.group(1))
            if seq == 1:
                lottery_item.w_odds = odd_f#初盘赔率
            elif seq == 2:
                lottery_item.d_odds = odd_f
            elif seq == 3:
                lottery_item.l_odds = odd_f
            elif seq == 4:
                lottery_item.cw_odds = odd_f#即时赔率
            elif seq == 5:
                lottery_item.cd_odds = odd_f
            elif seq == 6:
                lottery_item.cl_odds = odd_f
        probability=re.findall(probability_pattern,one_item)[0:6]
        lottery_item.wp=float(probability[0])/100#初盘胜率
        lottery_item.dp=float(probability[1])/100
        lottery_item.lp=float(probability[2])/100
        lottery_item.c_wp=float(probability[3])/100
        lottery_item.c_dp=float(probability[4])/100
        lottery_item.c_lp=float(probability[5])/100

        return_pattern = re.compile(r'</tr>\s*<tr>\s*<td row="1">(.*?)%</td>')

        return_rate_match = return_pattern.search(one_item)

        if return_rate_match:
            lottery_item.back_ratio = float(return_rate_match.group(1))
        lottery_items.append(lottery_item)

    return lottery_items

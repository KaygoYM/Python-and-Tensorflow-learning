Soccer Bet 寻找竟足博彩收益最优投资方案
====
GA+Greedy 贪婪算法+遗传算法
----

**根据不同公司的赔率寻找最优的博彩投资方案**</br>
`2018俄罗斯世界杯就要来啦！`</br>
`各博彩公司的赔率数据来自于500.com.仅适用于在所爬公司拥有账户并能实时下注`</br>

**参考和致谢_Reference & Thanks: [A Soccer Bet Strategy Project-wzhe06](https://github.com/wzhe06/soccerbet) **</br>

## 文件介绍_Introduction
* `main.py`: 运行的主程序-**程序入口**</br>
* `lottery.py`: 所有的类的所在文件</br>
* `portfoliomodel.py`: 寻优算法及投注策略类所在文件</br>
* `spider.py`: 所有爬虫的程序所在文件</br>

## 程序_How to use
运行`main.py`之后，生成`Year_Month_Day soccer_bet.txt`为所有投注策略结果文档</br>
Just run `main.py` with python 3.6

## 结果分析_Results
`
match name:	17/18西甲第34轮</br>
match members:	巴塞罗那 VS 比利亚雷亚尔</br>
match time:	比赛时间2018-05-10 02:00</br>
min_profit:	133.864864865</br>
win:	3 立博	1.95	68.65</br>
draw:	56 Balkan Bet	6.5	20.62</br>
lose:	30 Matchbook	12.5	10.73</br>
`
match name = 比赛名称 match members = 比赛双方(主队在先)  match time = 比赛时间(北京时间)</br>
**min_profit = 按以下策略投资下注的最小收益(含本金)为 133.864865 %**</br>
策略如下：</br>
**win:3 立博 1.95 68.65 = 去`立博`公司(id=`3`)买`胜`，当时该公司的胜的赔率为`1.95`，下注`68.65%`的本金</br>**
**draw:56 Balkan Bet 6.5 20.62 = 去`Balkan Bet`公司(id=56)买`平`，当时该公司的平的赔率为`6.5`，下注`20.62%`的本金</br>**
**lose:30 Matchbook 12.5 10.73 = 去`Matchbook`公司(id=30)买`负`，当时该公司的负的赔率为`12.5`，下注`10.73%`的本金</br>**

然后就可以安稳睡觉，不管踢成什么样，最少都有33.86%的收益到手啦~</br>

## 最后注意_ATTENTION: 以上程序仅供学习使用(简单的遗传算法寻优)，结果仅作为参考.如需应用于实际具体情况，请谨慎酌情使用，后果自负。

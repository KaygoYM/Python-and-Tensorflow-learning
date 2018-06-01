# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:15:44 2018

@author: hamch
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import itchat
import jieba.posseg as psg
from collections import Counter
from wordcloud import WordCloud,STOPWORDS
from pyecharts import Map 
import re
import os

class Wechat_friends(object):
    def __init__(self):
        itchat.login()#启动登陆
        itchat.auto_login(hotReload=True)#不用重复扫码登陆
        self.friends_list=itchat.get_friends()[1:]#0是自己
        #print(self.friends_list)
        self.friends_dict_info={'nickname':[],'sign':[],'sex':[],'photo_url':[],
                                'province':[],'city':[]}#朋友信息

        plt.rcParams['font.family']='sans-serif'  #设定
        plt.rcParams['font.sans-serif']=[u'SimHei']
    
    def get_friend(self):
        for each_friend in self.friends_list:
            self.friends_dict_info['nickname'].append(each_friend['NickName'])
            self.friends_dict_info['sign'].append(each_friend['Signature'])
            self.friends_dict_info['sex'].append(each_friend['Sex'])#1:male 2:female
            self.friends_dict_info['photo_url'].append(each_friend['HeadImgUrl'])
            self.friends_dict_info['province'].append(each_friend['Province'])
            self.friends_dict_info['city'].append(each_friend['City'])
    
    def final_plot(self):
        #处理nickname
        nicknames=self.friends_dict_info['nickname']
        print('您的所有好友昵称：',len(nicknames))
        
        #处理signature
        signs=self.friends_dict_info['sign']#有哪些中二的签名
        signs_all=''.join(signs)
        sign_words_flags=[(x.word,x.flag) for x in psg.cut(signs_all)]#获取词的属性以便过滤
        stop_attr = ['a','b','c','d','f','df','p','r','rr','s','t','u','ule','ude1','v','z','x','y','e','m','mq']
        stop_word = ['我','你','了','的','吧','吗','个','人','部','span','class','emoji1f64f']
        true_words = [x[0] for x in sign_words_flags if x[1] not in stop_attr and x[0] not in stop_word]
        c=dict(Counter(true_words).most_common(20))
        #print(c)
        wc = WordCloud(background_color = 'white',    # 设置背景颜色
                stopwords = STOPWORDS,        # 设置停用词
                font_path = './fonts/simhei.ttf',# 设置字体格式，如不设置显示不了中文
                max_font_size = 100,# 设置字体最大值
                random_state = 24,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
        wc.generate_from_frequencies(c)
        plt.figure(1)
        plt.title('签名热词')
        plt.axis('off')
        plt.imshow(wc)
        
        #男女比sex
        sex_part=dict(Counter(self.friends_dict_info['sex']))
        print(sex_part)
        sex_part['美少女']=sex_part.pop(2)
        sex_part['猛男']=sex_part.pop(1)
        sex_part['未知']=sex_part.pop(0)
        labels=sex_part.keys()
        percentage=np.array(list(sex_part.values()))
        percentage=percentage/sum(percentage)
        colors = ['lightpink','yellowgreen','lightskyblue']
        explode=0.2,0.1,0.1
        plt.figure(2)
        plt.pie(tuple(percentage),labels=labels,autopct='%1.1f%%',explode=explode,shadow=True,colors=colors)
        plt.title('性别比')
        plt.axis('off')
        plt.axis('equal')
        #plt.show()
        
        #头像展示photo
        
        num = 0
        for i in self.friends_list:
            img = itchat.get_head_img(userName=i["UserName"])
            #print(img)
            fileImage = open('Wechat_Head' + "/" + str(num) + ".jpg",'wb')
            fileImage.write(img)
            fileImage.close()
            num += 1
        #抓一遍就好
        ls = os.listdir('Wechat_Head')
        each_size = int(np.sqrt(float(1000*1000)/(len(ls)+20)))
        lines = int(1000/each_size)
        image = Image.new('RGBA', (1000, 1000))
        x = 0
        y = 0
        for i in range(0,len(ls)):
            try:
                img = Image.open('Wechat_Head' + "/" + str(i) + ".jpg")
            except Exception as e:
                print(e)
            else:
                img = img.resize((each_size, each_size), Image.ANTIALIAS)
                image.paste(img, (x * each_size, y * each_size))
                x += 1
                if x == lines:
                    x = 0
                    y += 1
        image.save("Wechat_All_Head.jpg")
        
        #地域分布
        
        provinces=dict(Counter(self.friends_dict_info['province']))
        del provinces['']
        del_list=[]
        for name in provinces.keys():
            if re.search(r'^[a-zA-z]',name):
                del_list.append(name)
        for i in del_list:
            del provinces[i]
        data=list(provinces.items())
        print(data)
        friend_map=Map("各省微信好友分布", width=1200, height=600)
        attr, value = friend_map.cast(data)
        friend_map.add("", attr, value, maptype='china', is_visualmap=True,visual_text_color='#000')  
        friend_map.show_config()  
        friend_map.render()  
        
        
        citys=dict(Counter(self.friends_dict_info['city']).most_common(8))
        del citys['']
        print(citys)
        plt.figure(3)
        city_range=list(range(0,len(citys.keys())))
        plt.xticks(city_range,list(citys.keys()))
        plt.bar(city_range,list(citys.values()),facecolor='red',edgecolor='black',align="center")
        plt.show()
        
        

def main():
    my_wechat=Wechat_friends()#初始化
    my_wechat.get_friend()#获取信息
    my_wechat.final_plot()#处理信息并画图
    
if __name__=='__main__':
    main()

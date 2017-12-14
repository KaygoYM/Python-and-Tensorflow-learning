import sqlite3,sys
conn=sqlite3.connect('food.db')
curs=conn.cursor()

query='SELECT * FROM food' 
print(query)
curs.execute(query)

names=[f[0] for f in curs.description]#结果列描述的序列 只读
for rows in curs.fetchall():
#将所有剩余行作为序列的序列
    for pairs in zip(names,rows):
        print('%s,%s' %pairs)

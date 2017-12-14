#print
a,b,c=1+3,2,'bob'
d=b**a
print(str(a)+'\n',b,c,d)
name = 'qiwsir'
room = 703
website = 'qiwsir.github.io'
print( "MY name is:%s\nMy room is:%d\nMy website is:%s"%(name,room,website))

myinfo={'name':'kkk','website':'eee'}
print( "MY name is:%(name)s\nMy website is:%(website)s"%(myinfo))


#while
flag=1
while flag<=10:
    print(flag)
    flag+=1
    


#for
example_list=[1,2,56,158,2,55,5,6,7,888,999992,1]
for i in example_list:
    print(i)
    print('inner for')


for i in range(1,10,2):
    print(i)

#if else
x=1+1j;y=2;z=3
if x.real>y:
    print('x is greater than y')
elif x.real==y:
    print('x is equal to y')
else: 
    print('x is less than y')
print('finish if')


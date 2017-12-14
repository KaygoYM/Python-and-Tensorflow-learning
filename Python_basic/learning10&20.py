#function
def function(a,b):
    c=a**b;
    print('This c is',c)
    print('c=%f'%c)
function(4,5)

def sell_car(price,brand,is_sec_hand,color='red'):
    print('price:',price,
          'color:',color,
          'brand:',brand,
          'is_second_hand',is_sec_hand)

sell_car('$'+str(1000),'Ferrari',True)

#global var
KKK=100
a=None
def fun():
    global a;a=12
    print('KKK=',KKK);print('a=',a)
    return a+KKK
print('a past is',a)
print(fun())
print('a now is',a)

#input
a_input=int(input('Please give a number:')) #return a string
if a_input== 1:
    print('This input number is acceptable',a_input)
elif a_input==2:
    print('Good luck!')
else:
    print('Illegal input.See you.')



#tuple list
a_tuple=(1,2,33,56,9)
b_tuple=3,4,5,6,7,8
a_list=[1,1,2,3,98,2,56]

a_list.append(0)
a_list.insert(0,72)
a_list.remove(98)
#a_list[0]

for content in a_tuple:
    print(content)
for content in a_list:
    print(content)
for index in range(len(a_list)):
    print('index=',index+1,'number in list=',a_list[index])

print(a_list[-1])#最后一位

print(a_list[0:3])
print(a_list[5:])
print(a_list[-3:])

print(a_list.index(1))#第一次出现的索引
print(a_list.count(1))#出现的次数
a_list.sort(reverse=True)
print(a_list)#覆盖a_list

#多维列表
multi_dim_list=[[1,2,3],
                [5,6,7],
                [8,5,9]]
print(multi_dim_list[0][2])


#dictionary
d={'apple':[1,2,3],'pear':2,'orange':3}#key:value
d2={1:'a',2:'b','three':'c'}
print(d['apple'],d2[2])
del d['pear']
print(d)
d['banana']=20
print(d)


d3={'apple':[1,2,3],'pear':{1:3,3:'a'},'orange':function(3,4)}
print(d3['pear'][3])

s='This is an apple'
print(s.count(' '))

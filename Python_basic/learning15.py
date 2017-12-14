#open files read and write
text='This is my first text.\nThis is next line.\nThis is the last line.'
#print(text)
append_txt='\nThis is an additive sentence'
my_file=open('my_first_file.txt','a')
#读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
my_file.write(append_txt)
my_file.close()

file=open('my_first_file.txt','r')

s_conts=file.readline()
a_conts=file.readlines()
#conts=file.read()

print(s_conts)
print(a_conts)
#print(conts)

file.close()

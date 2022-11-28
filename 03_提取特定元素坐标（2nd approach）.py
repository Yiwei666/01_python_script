# https://www.computerhope.com/issues/ch001721.htm#read-text-from-file
# https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
# 主要时通过对比每一行的首字母来寻找目标元素行
# Build array of lines from file, strip newlines

import datetime                      # 导入时间模块
x = datetime.datetime.now()          # 显示时间
print("此刻时间：",x)


print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换

#下面是把文本中的每一行转换成列表中的字符串
mylines = []                                # Declare an empty list.
with open ( na , 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.
        
for element in mylines: # 对于列表中的每个元素，
    print(element) # 打印它。
    


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容

m = open( name, "x")   # 创建新文本
m.close()

print("请输入提取元素符号,如Si ")     # 提示命令行输入
bb = input()              # 注意字符串输入变量的数据类型转换
print("已输入元素大写首字母", bb)           # 显示输入的内容

nn = 0

#先写俩空行
h = open(name , "a")
h.write("1")       #换行
h.write('\n')       #换行
h.write("change line")       #换行
h.write('\n')       #换行
h.write("Modified by Python")       #换行
h.write('\n')       #换行
h.close()

print("此时的name", name)           # 显示输入的内容

for line in mylines:          # string to be searched
    
    index = line.find( bb , 0, 3 ) # 检索首字母是否为B，不是返回值为-1
    if index != -1:           # If nothing was found,
        h = open(name , "a")
        h.write(line)
        h.write('\n')       #换行
        print(line)
        nn += 1
        h.close()

print("共有",bb,"原子数:", nn )



#下面是给首行添加原子数的语句

with open( name ) as f: 
    lines = f.readlines() #read 
#modify 
lines[0] = str(nn) #you can replace zero with any line number.
lines[1] = '\n' #相当于把第二行给删掉了
with open(name, "w") as f: 
    f.writelines(lines) #write back 




#下面是给首行添加原子数的语句
#We read the existing text from file in READ mode 
#src = open(name,"r")
#fline = str(nn)
#fline = "newly added FIRST LINE\n"    #Prepending string 
#oline = src.readlines() 
#Here, we prepend the string we want to on first line 
#oline.insert(0,fline)
#oline.insert(1,'\n') #首行换行
#oline.insert(2,'\n') #第二行换行空格
#src.close()
#We again open the file in WRITE mode  
#src=open(name,"w") 
#src.writelines(oline) 
#src.close() 



#统计输出文件的行数
fobj = open( name ,'r')
row_len = len(fobj.readlines())
print("共有",row_len ,"行" )
fobj.close()    #打开文件之后记得要关掉，不然文件是打开状态，无法读写保存。



# 以下是计时程序
y = datetime.datetime.now()
z = y-x
print("共耗时",z ,"时:分:秒:毫秒")           # 显示输入的内容


print("-------------")
    









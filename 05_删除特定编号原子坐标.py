# Task requirements: delete atomic coordinates with a specific number and save the remaining coordinates to a new file
# Mainly use the for loop statement to handle the task
import os
import datetime                      # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
        
print("-------------")


print("请输出需要处理的文件名,xyz格式")     # 提示命令行输入
na = input()              # 注意字符串输入变量的数据类型转换


#下面是把文本中的每一行转换成列表中的字符串
mylines = []                                # Declare an empty list.
with open ( na , 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.
        
for element in mylines: # 对于列表中的每个元素，
    print(element) # 打印它。

    

fobj = open( na ,'r')
row_len = len(fobj.readlines()) # 统计文件行数
print("文件行数为:",row_len,"原子数为:", row_len-2)     # 提示命令行输入



print("请输入想要删除的原子编号，用英文逗号间隔 :")     # 提示命令行输入
atom = input()              # 注意字符串输入变量的数据类型转换
print("已输入原子编号： ", atom)           # 显示输入的内容

numbers = atom.split(",")
aaa = len(numbers)
print("目标删除原子个数为： ", aaa )           # 显示输入的内容


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容
m = open( name, "x")   # 创建新文本
m.close()



#先写一个空行
h = open(name , "a")
h.write("提前先写入一行，后会被覆盖为原子数")       #换行
h.write('\n')       #换行
h.close()

print("此时的name", name)           # 显示输入的内容





with open( na , 'r') as fd:           # 打开上述要处理的xyz源文件na
    lnum = 0
    for line in fd:        # 外循环是对每一行进行对比筛选
        lnum += 1
        cont = 0
        for number in numbers: # 内循环是遍历输入的原子标号以确定对应行
            cont += 1
            value = int(number)+2       
            if lnum == value:     # 排除掉选中的原子编号
                print ("此处删除原子编号：", number,"排除第：", value, "行")
#                print ("排除第：", value, "行")
                break   # break 打破了最小封闭for或while循环。
#            print ("写入原子编号为：", number )
#            print ("写入第：", value, "行")
            if cont == aaa:
                h = open(name , "a")# 找到不是特定编号的line，将其写入新文件
                h.write(line)
                h.close()
                line = line.strip()    # line.strip()把文本带有的'\n'移除
                print(line)
      
print("-------------")


#下面是给首行添加原子数的语句
#We read the existing text from file in READ mode

#下面是给首行添加原子数的语句

with open( name ) as f: 
    lines = f.readlines() #read 
#modify 
lines[0] = str(row_len-2-aaa) #you can replace zero with any line number.
lines[1] = '\n' #相当于把第二行给删掉了
with open(name, "w") as f: 
    f.writelines(lines) #write back 




#统计输出文件的行数
fobj = open( name ,'r')
row_len = len(fobj.readlines())
print("共有",row_len ,"行","还剩",row_len-2,"个原子" )
fobj.close()

print("-------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒.毫秒")           # 显示输入的内容

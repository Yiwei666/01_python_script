# Task requirements, given the atomic number to extract the atomic coordinates
# Mainly use the for loop statement to handle the task

import datetime                      # 导入时间模块
xx = datetime.datetime.now()          # 显示时间
print("此刻时间：",xx)


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



print("请输入想要提取的原子编号，用英文逗号间隔 :")     # 提示命令行输入
atom = input()              # 注意字符串输入变量的数据类型转换
print("已输入原子编号： ", atom)           # 显示输入的内容

numbers = atom.split(",")
aaa = len(numbers)
print("原子个数为： ", aaa )           # 显示输入的内容


print("请为输出文件命名,xyz格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
print("已输入文件名 ", name)           # 显示输入的内容


for number in numbers:
        value = int(number)+2
        print ("原子编号：", number)
        print ("行数为：", value)
        with open( na , 'r') as fd:           # 打开上述要处理的xyz源文件na
            lnum = 0
            for line in fd:        # 第二个实例
                lnum += 1;
                if lnum == value:     # 打印的行数范围
                    h = open(name , "a")         
                    h.write(line)
                    h.close()
                    line = line.strip()    # line.strip()把文本带有的'\n'移除
                    print(line)
                    print("-------------")
                    break   # break 打破了最小封闭for或while循环。
        
print("-------------")

#下面是给首行添加原子数的语句，注意下面的语法是直接插入而不是覆盖
#We read the existing text from file in READ mode

src = open(name,"r")
fline = str(aaa)  # aaa是原子个数
#fline = "newly added FIRST LINE\n"    #Prepending string 
oline = src.readlines() 
#Here, we prepend the string we want to on first line 
oline.insert(0,fline) #fline必须是字符串
oline.insert(1,'\n') #首行换行
oline.insert(2,'\n') #第二行换行空格
src.close()
#We again open the file in WRITE mode  
src=open(name,"w") 
src.writelines(oline) 
src.close() 



#统计输出文件的行数
fobj = open( name ,'r')
row_len = len(fobj.readlines())
print("共有",row_len ,"行" )

print("-------------")

# 以下是计时程序
yy = datetime.datetime.now()
zz = yy-xx
print("共耗时",zz ,"时:分:秒.毫秒")           # 显示输入的内容





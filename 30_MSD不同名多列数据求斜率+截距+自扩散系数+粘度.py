# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:36:36 2021

@author: sun78
"""

##最小二乘法

import numpy as np   ##科学计算库
import scipy as sp   ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法
import datetime                      # 导入时间模块
import math  #用来计算次方的，指数的

# 本脚本整合同体系导出的多个元素的MSD，如O，Si，Ca，F等。
# MSD[Ca]/MSD[F ]/MSD[O ]/MSD[Si]
# 本论文计算粘度的原理参考该论文：Structural and viscosity properties of CaO-SiO2-Al2O3-FeO slags based on molecular dynamic simulation

import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)  
        
print("-------------")
#print("如果需要为MSD曲线进行梯度增高变换，请输入梯度值，如3,将按照0*3,1*3,2*3,3*3等进行增高;如不需要，则输入0")     # 提示命令行输入
#nu = float(input())              # 注意字符串输入变量的数据类型转换

print("注意:该脚本会将横坐标的单位由fs变换成ps,默认纵坐标单位为Å \n")

print("请按顺序依次输入需要批量处理的文件名,用/号分隔，ISAACS导出的 MSD[Ca] 数据文件格式")     # 提示命令行输入
na_g = input()              # 注意字符串输入变量的数据类型转换

file_list = na_g.split("/")   # ['g(r)[Ca,F ]', 'g(r)[Ca,O ]', 'g(r)[O ,O ]', 'g(r)[Si,Ca]', 'g(r)[Si,F ]', 'g(r)[Si,O ]']
print ("输入的所有文件名为：",file_list)
length = len(file_list)

# 下面用循环创建多个列表并命名


list1 = []   #list1是所有列表名字集合
for i in range(length):  #注意range索引从0开始,1-5,共计6个数字
    name_x = "x"+ str(i) 
    name_y = "y"+ str(i)
    list1.append(name_x)
    list1.append(name_y)
#    [] = name_x 
#    [] = name_y 
print ("列表长度为:",length,"所有的列表名为:",list1)


list2 = []              # 所有空列表集合
for i in list1:  # ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']
    list1 = []
    list2.append(list1)
print ("空列表集合为:",list2)  # [[], [], [], [], [], [], [], [], [], [], [], []]

#以上循环创建多个列表并命名完毕
########################################


j  = 0

while j < length:
    pp = 0
    with open(file_list[j], 'r') as f:  # ['g(r)[Ca,F ]', 'g(r)[Ca,O ]', 'g(r)[O ,O ]', 'g(r)[Si,Ca]', 'g(r)[Si,F ]', 'g(r)[Si,O ]']
        print("-----")
        lines = f.readlines()
        for line in lines:
            pp += 1
#            x_f = "x"+ str(i)
#            y_f = "y"+ str(i)            
            if pp == 18:           #第16行的格式为:@    s0 legend  "MSD (Si) [\cE\C\S2\N]"    
                title = line.split( )[3] + line.split( )[4] + '"'  # @    s0 legend  "MSD (Si) [\cE\C\S2\N]"   
    #            title1 = title[1]+title[-10:-2]#
                list2[2*j].append("t/ps")
                list2[2*j+1].append(title)
            if pp > 20:
    
                p3x1 = float(line.split( )[0])*0.001  # 将x坐标单位由fs变换成ps          
                p3y1 = float(line.split( )[1])
    
                list2[2*j].append(p3x1)
                list2[2*j+1].append(p3y1)
    j += 1
    print("索引",j)

#list_all = []
#for i in range(length):
#    x_f = "x"+ str(i)
#    y_f = "y"+ str(i)   
#    list_all.append(x_f)
#    list_all.append(y_f)
    
print("写入的多维列表为:",list2)



'''

k = 0
while k < len(list2):
    len1 = len(list2[k])
    print("列表索引为",k,"时，该索引列表长度为:",len1)
    k += 1

f1 = []   # 每一行为一个列表

l = 0
while l < len(list2[0]):
    u = 0
    f = []
    while u < len(list2):
        f.append(list2[u][l])
        u += 1
    print ("每一行合并后的列表",f)
    f1.append(f)
    l += 1
print ("合并后的多维列表",f1)





print("请为输出文件命名,txt格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换
#print("已输入文件名 ", name)           # 显示输入的内容


#print("已输入文件名 ", name)           # 显示输入的内容

with open(name, 'w') as new_file:  # 有则覆盖，没有则创建
    for li in f1:
        l1 = 0
        str1 = ""
        while l1 < len(li):  # ['r', '"g\\sij\\N(r)[Ca,F]"', 'r', '"g\\sij\\N(r)[Ca,O]"', 'r', '"g\\sij\\N(r)[O,O]"', 'r', '"g\\sij\\N(r)[Si,Ca]"', 'r', '"g\\sij\\N(r)[Si,F]"', 'r', '"g\\sij\\N(r)[Si,O]"']
            str1 += str(li[l1])+"     "
            l1   +=  1
        new_file.write(str1+"\n")
'''

#############################################
# 以下为最小二乘法直线拟合部分
# 参考该网址代码： https://www.php.cn/python-tutorials-359035.html


'''
     设置样本数据，真实数据需要在这里处理
'''

print("请为输出文件命名,txt格式")     # 提示命令行输入
name = input()              # 注意字符串输入变量的数据类型转换

print("请输入模拟温度,单位为 K")     # 提示命令行输入
T = float(input())              # 注意字符串输入变量的数据类型转换

h = 0
with open(name, 'a') as new_file:  # 有则覆盖，没有则创建
    while h < length:
        Xi = np.array(list2[2*h][1:])
        Yi = np.array(list2[2*h+1][1:])
    
        ##样本数据(Xi,Yi)，需要转换成数组(列表)形式    
        #Xi=np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])    
        #Yi=np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])
            
        
        '''    
            设定拟合函数和偏差函数    
            函数的形状确定过程：    
            1.先画样本图像    
            2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)    
        '''
        
        ##需要拟合的函数func :指定函数的形状
        
        def func(p,x):
        
            k,b=p
        
            return k*x+b
        
        ##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
        
        def error(p,x,y):
        
            return func(p,x)-y
        
         
        '''    
            主要部分：附带部分说明    
            1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)    
            2.官网的原话（第二个值）：Value of the cost function at the solution    
            3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)    
            4.返回值元组中第一个值的数量跟需要求解的参数的数量一致    
        '''
        
        
        #k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
        
        p0=[1,20]
        
         
        
        #把error函数中除了p0以外的参数打包到args中(使用要求)
        
        Para = leastsq(error,p0,args=(Xi,Yi))
        
        #print ("Para:",Para)
        
        #读取结果
        
        k,b=Para[0]
        
        print("k=",k,"b=",b)    
        print("cost："+str(Para[1]))    
        print(file_list[h]," 体系求解的拟合直线为:")    
        print("y="+str(round(k,4))+"x+"+str(round(b,4)))
        
        print("自扩散系数为:",round(float(k/6*10),4),"E-5cm^2/s") #默认单位为A^2/ps,转换为cm^2/s要乘以10^4
        
        
        
        
        '''   
           绘图，看拟合效果.
           matplotlib默认不支持中文，label设置中文的话需要另行设置
           如果报错，改成英文就可以 
        '''
            
        #画样本点
        plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
        plt.scatter(Xi,Yi,color="green",label="Sample data  "+ file_list[h],linewidth=2)
                         
        #画拟合直线        
        x=np.linspace(0,12,100) ##在0-15直接画100个连续点    
        y=k*x+b ##函数式    
        plt.plot(x,y,color="red",label="Fitting Line",linewidth=2)    
        plt.legend() #绘制图例    
        plt.show()    
        new_file.write(str(datetime.datetime.now())+"\n")  #写入时间
        new_file.write(file_list[h]+" 体系求解的拟合直线为:"+"\n")
        new_file.write("y="+str(round(k,4))+"x+"+str(round(b,4))+"\n")
        new_file.write("k="+str(k)+"b="+str(b)+"\n")
        D = float(k/6*10) # D为自扩散系数，单位为E-5cm^2/s, 默认单位为Å^2/ps
        viscosity = float(1.38*math.pow(10,-23)*T/(k/6*2.8*math.pow(10,-18)))  # 粘度单位是Pa·s
        print("粘度为:",viscosity)
        new_file.write("自扩散系数为:"+str(D)+"E-5cm^2/s"+"\n")
        new_file.write("基于O自扩散系数计算的粘度为:"+str(viscosity)+"Pa·s"+"\n") #λ = 2.8 Å,
        new_file.write("\n")
        print("-------------------------------\n")
        h += 1 # 循环别忘了 

with open(name, 'a') as good:  # 有则覆盖，没有则创建
    good.write("----------\n")
        
print("信息已保存!")         
# MSD[Ca]/MSD[F ]/MSD[O ]/MSD[Si]










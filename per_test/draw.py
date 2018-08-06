# -*- coding: utf-8 -*-  
import numpy as np  
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  
import sys
name=sys.argv[1]
x=[]
y=[]
for i in range(2,100):
    try:
        y.append(sys.argv[i])
    except:
        break
#X轴，Y轴数据  
for i in range(0,len(y)):
    x.append(i)
#x = [0,1,2,3,4,5,6,7,8,9,10]  
#y = [0.3,0.4,2,5,3,4.5,4]  
plt.figure(figsize=(8,4)) #创建绘图对象  
plt.plot(x,y,"b",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）  
plt.xlabel("times") #X轴标签  
plt.ylabel("use")  #Y轴标签  
plt.title("%s used"%name) #图标题  
#plt.show()  #显示图  
plt.savefig("demo-%s.jpg"%name) #保存图

import selenium
from selenium import webdriver
import pandas as pd
import numpy as np
import os
import re
import requests
import time
from timeit import timeit

#打开浏览器
driver=webdriver.Chrome()
#开始计时
time_start=time.time()
#打开网页
driver.get('http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html')
#获取对应信息所在位置的标签，使用selenium方法
info=driver.find_elements_by_xpath('//tr/td')
#构造一个获取元素信息的函数
def GetData(info):
    a=[]
    for i in range(len(info)):#将提取的文本导入到一个list中
        a.append(info[i].text)
    step=14#从显示的表格上看，应该是每5个进行一次换行，虽然有些元素隐藏了，总共是14个元素一行
    b=[a[i:i+step]for i in range(0,len(a),step)]#每8个元素一组进行安排
    result=pd.DataFrame(b)#导出为表格，没有写上列名
    return result
#获取对应内容
data=GetData(info)
#删除实际上隐藏显示为空的几列数据，形成新的表格
s=data.loc[:,0:4]
#对表格进行列取名
s.columns=(['名次','学校名称','省市','总分','指标得分'])
#将数据存放到表格中，本身有排序，就不用自动添加INDEX,取FALSE，得到的表格就只有信息
s.to_excel('rank.xls',index=False)
print(s.head(10))
#计时结束
time_end=time.time()
#耗时计算
time_delta=time_end-time_start
print('time cost',time_delta,'s')
#关闭浏览器
driver.quit()
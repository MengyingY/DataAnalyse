#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:51:45 2018

@author: yangmengying1
"""

import pandas as pd
import numpy

data=pd.read_csv("/Users/yangmengying1/Downloads/5.1/data.csv")

#基本统计方法

'''
describe包含count,mean,std,min,1/4-3/4,max

'''
datades=data.score.describe()
data.score.size
data.score.var()
data.score.std()

#分组统计
#根据分组分析字段，将分析对象划分成不同部分，对比各组之间差异性的分析
'''
使用pandas的groupby函数
data.groupby(by=[分组字段，分组字段])[统计列].agg({ 统计列名：统计函数 })
'''
groupResult=data.groupby(by=['class'])['score'].agg(
        {
            '总分':numpy.sum,
            '人数':numpy.size,
            '平均分':numpy.mean
                
                }
        )

#分布分组
#对定量分组的数据，查看各组分布情况
'''
定量分组使用cut函数
pandas.cut(以哪一列分组，分组范围，各分组对应的名字)
'''
bins = [
    min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1
]
labels = [
    '20岁以及以下', '21岁到30岁', '31岁到40岁', '41岁以上'
]

data['年龄分层'] = pandas.cut(
    data.年龄, 
    bins, 
    labels=labels
)

aggResult = data.groupby(
    by=['年龄分层']
)['年龄'].agg({
    '人数': numpy.size
})
'''
四舍五入处理
round(number，小数点后保留几位)
'''
pAggResult = round(
    aggResult/aggResult.sum(), 
    2
)*100
pAggResult['人数'].map('{:,.2f}%'.format)

#交叉分析
#对多维度进行对比分析，通常两个维度较好
'''
使用python中的数据透视表函数
pivot_table(values＝值，index＝行，columns＝列，aggfunc＝统计方式，fill_value=NA值替换为什么)
'''
ptResult = data.pivot_table(
    values=['年龄'], 
    index=['年龄分层'], 
    columns=['性别'], 
    aggfunc=[numpy.size]
)

#相关分析
#研究变量之间依存关系的密切程度，线性相关及非线性相关
#皮尔逊系数   0<|r|<0.3 低度相关 0.3<|r|<0.8 中度相关   0.8<|r|<1 高度相关
'''
两列之间的相关度
使用Series.corr(Series)
'''
data['人口'].corr(data['文盲率'])

'''
多列之间的相关度的计算方法
DataFrame.corr()
'''
data[[
    '超市购物率', '网上购物率', '文盲率', '人口'
]].corr()
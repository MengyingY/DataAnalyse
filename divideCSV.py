#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:01:38 2018

@author: yangmengying1
"""

from pandas import read_csv

def dividedata(frompath,rows,destinationpath):
    df=read_csv(frompath)
    
    #df行数，开始行，结束行，time第几个csv
    df_length=len(df.index)
    start=0
    time=0
    rowspercsv=rows
    finishrows=rows-1
    
    
    #计算可分为几个表
    leftrows=df_length%rowspercsv
    if(leftrows==0):
        times=df_length/rowspercsv
    else:
        times=df_length/rowspercsv+1
    
    #分表
    while time<times:
        if time<times:
            start=time*rowspercsv
            finish=time*rowspercsv+finishrows
            df1=df.loc[start:finish]
            time_str=str(time)
            name=destinationpath+time_str+".csv"
            df1.to_csv(name,
            index=False
            )
            time=time+1
        else:
            start=time*rowspercsv
            finish=leftrows
            df1=df.loc[start:finish]
            name=destination+time_str+".csv"
            df1.to_csv(name,
            index=False
            )
            time=time+1
            
if __name__=="__main__":
   frompath_in=input("请输入需要分割的csv文件所在目录(only contain number and letter):")
   rows_in=int(input("每个分csv数据量（rows）:"))
   destinationpath_in=input("拆分后的csv文件目标路径(only contain number and letter):")
   #print(frompath_in)
   dividedata(frompath_in,rows_in,destinationpath_in)
   #dividedata("/Users/yangmengying1/Desktop/迈远数据 2/已发送/sent21.csv",1000000,"/Users/yangmengying1/Desktop/sent21分割/")
   



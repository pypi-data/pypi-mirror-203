# -*- coding: utf-8 -*-
"""
Created on Tue Apr 5 03:56:56 2023

@author: Napstablook
"""

import pandas as pd
import fitz
import pdfplumber
import re
import os
import requests


def download_report(code):  #根据找到的链接下载年报
    os.chdir('original')
    df=pd.read_csv(code+'.csv')
    os.chdir('../report')
    os.makedirs(code,exist_ok=True)
    os.chdir(code)
    name = df.iloc[0,2].replace('*','')
    for index,row in df.iterrows():
        title=row[3].replace('*','')
        href=row[4]
        f = requests.get(href)
        with open (name+title+".pdf", "wb") as report:
            report.write(f.content)
    for  index,row in df.iterrows():
        title=row[3].replace('*','')
        with pdfplumber.open("%s%s.pdf"%(name,title)) as pdf:
            page_count = len(pdf.pages)
        if page_count<30: 
           os.remove("%s%s.pdf"%(name,title))
           df1 = df.drop(df[df['公告标题']==title].index)
           df1.to_csv('../../original/%s.csv'%code,index=False)
    os.chdir('../..')

def findata(code,save):  #从年报pdf中提取金融数据
    d = annualreport_data(code)
    fin = d.pdf_to_data()
    if save == 1:        
        name = d.short_names[0].replace('*','')
        os.chdir('./financedata')
        fin.to_csv('%s %s.csv'%(code,name),mode='w')
        os.chdir('../')
    else:
        return fin
  
class annualreport_data():
    def __init__(self,code):
        original_table = pd.read_csv('./original/%s.csv'%(code))
        self.code = code
        self.short_names = original_table['股票简称'].to_list()
        self.titles = original_table['公告标题']
    
    def read_report(self):
        code = self.code
        name = self.short_names[0].replace('*','')
        txt=[]
        for title in self.titles:
            title = title.replace('*','')
            doc = fitz.open('./report/%s/%s%s.pdf'%(code,name,title))
            text_by_page = [doc.get_page_text(i) for i in range(15)]
            text = ' '.join(text_by_page)
            txt.append(text)
        self.txt=txt
        
    def matches(self):
        txt = self.txt
        
        p_year= re.compile('.*?(\d{4}) .*?年度报告.*?')
        p_rev = re.compile('(?<=\n)营业总?收入（?(\w*?)?）?\s?\n?\s*([\d+,.]*)\s\n?')
        p_eps = re.compile('(?<=\n)基本每股收益（元/?／?\n?股）\s?\n?([-\d+,.]*)\s?\n?')
        
        year = [int(p_year.findall(text)[0]) for text in txt]
        dw = [p_rev.search(text).group(1) for text in txt ]
        revenue=[float(p_rev.search(text).group(2).replace(',',''))*10000
                 if w=="万元" or w=="万" 
                 else float(p_rev.search(text).group(2).replace(',',''))
                 for text,w in zip(txt,dw)]
        eps=[p_eps.search(text).group(1) for text in txt]
        return [year,revenue,eps]
    
    def pdf_to_data(self):
        self.read_report()
        data = self.matches()
        df = pd.DataFrame({'Year':data[0],
                           'Revenue':data[1],
                           'Eps':data[2]}).set_index('Year').sort_index().drop_duplicates()
        self.data = df
        return df
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 5 03:54:34 2023

@author: Napstablook
"""


import pandas as pd
import re
import time
import os
from selenium.webdriver.common.by import By



def select_sh(data): #筛选沪市股票代码
    sh=['6','900']
    lst = [ x for x in data for startcode in sh if x[:3].startswith(startcode)==True ]
    df = pd.DataFrame(lst,columns=['code'])
    return df

def get_sse(code):
    searchbox=browser.find_element(By.ID,'inputCode')
    searchbox.send_keys(code)
    time.sleep(0.7)
    s=browser.find_elements(By.CLASS_NAME,'filter-option-inner-inner')[1]
    s.click()
    annual = browser.find_element(By.LINK_TEXT,'年报')
    annual.click()
    time.sleep(0.3)
    html = browser.find_element(By.CLASS_NAME, 'table-responsive')
    time.sleep(0.3)
    innerHTML = html.get_attribute('innerHTML')
    #open('%s.html' %code,'w',encoding='utf-8').write(innerHTML)
    browser.refresh()
    dt = DisclosureTable_sh(innerHTML)
    data = dt.get_data()
    os.chdir('original')
    data.to_csv(code+'.csv')
    os.chdir('../')
    
class DisclosureTable_sh():
    '''
    解析上交所定期报告页搜索表格
    '''
    def __init__(self, innerHTML):
        self.html = innerHTML
        self.prefix = 'http://www.sse.com.cn'
        p_code=re.compile('<span>(\d{6})</span>')
        p_name=re.compile('<span>[*]?(\w+|-)</span>')
        p_href=re.compile('<a.*?href="(.*?.pdf)".*?>')
        p_title=re.compile('<a.*?><span.*?>(.*?)</span></a>')
        self.get_code  = lambda td: p_code.search(td).group(1)
        self.get_name  = lambda td: p_name.search(td).group(1)
        self.get_href  = lambda td: p_href.search(td).group(1)
        self.get_title = lambda td: p_title.search(td).group(1)
        self.txt_to_df() #调用txt_to_df(self),得到初始化dataframe用于后续匹配

    def txt_to_df(self):
        # html table text to DataFrame
        html = self.html
        p_tr = re.compile('<tr>(.*?)</tr>', re.DOTALL)
        trs = p_tr.findall(html)
        p_td = re.compile('<td.*?>(.*?)</td>', re.DOTALL)
        tds=[p_td.findall(td) for td in trs if p_td.findall(td)!=[]]
        df = pd.DataFrame({'证券代码' : [td[0] for td in tds],
                           '股票简称' : [td[1] for td in tds],
                           '公告标题和链接' : [td[2] for td in tds],
                           '公告时间' : [td[3] for td in tds]})
        self.df_txt=df

    def get_data(self):
        get_code  = self.get_code
        get_name  = self.get_name
        get_href  = self.get_href
        get_title = self.get_title
        prefix = self.prefix
        
        df = self.df_txt
    
        codes   = [get_code(td) for td in df['证券代码']]
        names   = [get_name(td) for td in df['股票简称']]
        links   = [prefix+get_href(td) for td in df['公告标题和链接']]
        pubtime = [td for td in df['公告时间']]
        finy = [int(time[0:4]) for time in pubtime]
        titles = [get_title(td)+str(time)+'发布' for td,time in zip(df['公告标题和链接'],finy)]
        titles0 = [get_title(td) for td in df['公告标题和链接']]
        self.short_names = names
        data = pd.DataFrame({'证券代码':codes,
                             '股票简称':names,
                             '公告标题':titles,
                             '公告链接':links,
                             '公告时间':pubtime,
                             '原标题':titles0})
        
        for index,row in data.iterrows():
            time = row[4]
            title = row[2]
            a = re.search("摘要|取消|英文", title)
            if "年度报告" not in title and "年报" not in title or a != None or int(time[0:4])<int(start[0:4]):
                data = data.drop(index=index)
            elif '修订版' in title:
                data = data.drop(data[data['原标题']==title[0:-5]].index)
        data = data.reset_index(drop = True)
        self.df_data = data
        return data
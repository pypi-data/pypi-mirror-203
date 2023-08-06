# -*- coding: utf-8 -*-
"""
Created on Tue Apr 5 03:27:08 2023

@author: Napstablook
"""

import pandas as pd
import re
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def select_sz(data): #筛选深市股票代码
     sz=['200','300','301','00','080']   #深市股票代码A股是以000开头；深市B股代码是以200开头；中小板股票以002开头；
                                         #深市创业板的股票是以300、301开头(比如第一只创业板股票特锐德)。
                                         #另外新股申购代码以00开头、配股代码以080开头。
     lst = [ x for x in data for startcode in sz if x[:3].startswith(startcode)==True ]
     df = pd.DataFrame(lst,columns=['code'])
     return df
 
def Input_timeNtype(start,end,typ): #时间格式yyyy-mm-dd 种类格式"年度/半年度/一季度报告"
    START = browser.find_element(By.CLASS_NAME,'input-left') 
    END = browser.find_element(By.CLASS_NAME,'input-right')    
    START.send_keys(start)
    END.send_keys(end + Keys.RETURN)
    browser.find_element(By.LINK_TEXT,'请选择公告类别').click()
    browser.find_element(By.LINK_TEXT,typ).click()
    ActionChains(browser).move_by_offset(200, 100).click().perform()

def get_szse(code,count): #通过股票代码查找对应公司年报下载链接
                               #查询公司大于1时count传入1                           
    Searchbox = browser.find_element(By.ID, 'input_code') 

    Searchbox.send_keys(code)
    time.sleep(0.2)
    Searchbox.send_keys(Keys.RETURN)
    time.sleep(0.5)
    html = browser.find_element(By.ID, 'disclosure-table')
    innerHTML = html.get_attribute('innerHTML')
    
    if int(count)==1: #当批量查询股票时，每搜索一个后删去历史选择
        browser.find_elements(By.CLASS_NAME,'icon-remove')[-1].click()
        
    dt = DisclosureTable(innerHTML)
    data = dt.get_data()
    os.chdir('original')
    data.to_csv(code+'.csv',encoding='utf-8-sig')
    os.chdir('../')
 
class DisclosureTable():
    '''
    解析深交所定期报告页搜索表格
    '''
    def __init__(self, innerHTML):
        self.html = innerHTML
        self.prefix = 'https://disc.szse.cn/download'
        self.prefix_href = 'https://www.szse.cn/'
        # 获得证券的代码和公告时间
        p_a = re.compile('<a.*?>(.*?)</a>', re.DOTALL)
        p_span = re.compile('<span.*?>(.*?)</span>', re.DOTALL)
        self.get_code = lambda txt: p_a.search(txt).group(1).strip()
        self.get_time = lambda txt: p_span.search(txt).group(1).strip()
        # 将txt_to_df赋给self
        self.txt_to_df()
        
    def txt_to_df(self):
        # html table text to DataFrame
        html = self.html
        p = re.compile('<tr>(.*?)</tr>', re.DOTALL)
        trs = p.findall(html)
        
        p2 = re.compile('<td.*?>(.*?)</td>', re.DOTALL)
        tds = [p2.findall(tr) for tr in trs[1:]]
        df = pd.DataFrame({'证券代码': [td[0] for td in tds],
                           '简称': [td[1] for td in tds],
                           '公告标题': [td[2] for td in tds],
                           '公告时间': [td[3] for td in tds]})
        self.df_txt = df


    
    # 获得下载链接
    def get_link(self, txt):
        p_txt = '<a.*?attachpath="(.*?)".*?href="(.*?)".*?<span.*?>(.*?)</span>'
        p = re.compile(p_txt, re.DOTALL)
        matchObj = p.search(txt)
        attachpath = matchObj.group(1).strip()
        href       = matchObj.group(2).strip()
        title      = matchObj.group(3).strip()
        return([attachpath, href, title])

    def get_data(self):
        get_code = self.get_code
        get_time = self.get_time
        get_link = self.get_link
        # 
        df = self.df_txt
        codes = [get_code(td) for td in df['证券代码']]
        short_names = [get_code(td) for td in df['简称']]
        ahts = [get_link(td) for td in df['公告标题']]
        times = [get_time(td) for td in df['公告时间']]
        self.short_names = short_names
        #
        prefix = self.prefix
        prefix_href = self.prefix_href
        data = pd.DataFrame({'证券代码': codes,
                             '股票简称': short_names,
                             '公告标题': [aht[2] for aht in ahts],
                             'attachpath': [prefix + aht[0] for aht in ahts],
                             'href': [prefix_href + aht[1] for aht in ahts],
                             '公告时间': times})
        
        for index,row in data.iterrows():
            if re.search("摘要|取消|英文", row[2]) != None:
                data = data.drop(index=index)
        data = data.reset_index(drop = True)
        self.df_data = data
        return data
# arfindata子模块与函数介绍  


## 1.arfindata.sz 深交所官网爬虫

### （1）sh.select_sh(data) ——股票代码筛选函数
        data为list格式的股票代码列表，输出经过筛选后的深市股票列表。
        
### （2）Input_timeNtype(start,end,typ) ——爬虫函数
        在深交所官网输入查询起止时间与报告种类。
        start:查询开始时间 end：查询结束时间 typ：报告种类
        时间格式yyyy-mm-dd 种类格式"年度/半年度/一季度报告"
        建议三个变量单独使用代码定义，因为start需要定义来实现上交所爬虫的部分内容。
        例如：
        start = 2015-01-01
        end = 2021-12-31
        typ = "年度"
        想下载别的类型报告可以选择不同种类，但是下载后的报告不适用于后续的pdf数据解析。
        
### （3） get_szse(code,count) ——爬虫函数，通过股票代码查找对应公司年报下载链接
        code为str格式的股票代码查询公司大于1时count传入1,等于1时传入0。
        输出爬取并解析后的该上市公司年度报告披露表格。包含公司简称，年报标题，下载链接等。
        表格保存到本地original文件夹中，文件名为code.csv。
                                       

## 2.arfindata.sh 上交所官网爬虫

### （1）sh.select_sh(data) ——股票代码筛选函数
        data为list格式的股票代码列表，输出经过筛选后的沪市股票列表。
        
### （2）sh.get_sse(code)  ——爬虫函数，通过股票代码查找对应公司年报下载链接
        code为str格式的股票代码。
        输出爬取并解析后的该上市公司年度报告披露表格。包含公司简称，年报标题，下载链接等。
        表格保存到本地original文件夹中，文件名为code.csv。

## 3.arfindata.ARdata 年报下载与解析

### （1）download_report(code) ——年报下载函数
        code为str格式的股票代码。将读取由ARfindata.sh.get_sse(code) 得到的code.csv文件，对其中年报链接进行访问下载。
        年报文件将保存到本地report文件夹中，格式为pdf。
        
### （2）findata(code,save) —— 从年报pdf中提取金融数据
        code为str格式的股票代码。save为是否保存为文件选项。save传入1数据将保存到本地financedata文件夹，文件名为"股票代码 股票简称.csv"
        将读取report文件夹中由ARfindata.ARdata.download_report(code)下载的pdf格式年报文件并进行数据提取。
        金融数据包括Revenue（年度总收入）和 Eps（每股收益）。



## 注：本模块需要的第三方库如下,若未安装则不能顺利运行本模块
| 第三方库 | 在子模块中的应用 |
|   :---: |   :---: |
|pandas     |sz, sh, ARdata|
|selenium   |   sz, sh           |
|time      |sz, .sh |
|os       |       sz, sh, ARdata         |
|re|sz, sh, .ARdata |
|fitz|ARdata|
|pdfplumber|ARdata|
|requests|ARdata|

### 完整运行前请创建一个文件夹
文件夹中包含original，report，financedata三个文件夹及你的代码文件。
不想手动创建三个文件夹也可以使用代码创建，它们将建立在代码文件的当前路径下。
```
os.makedirs('report',exist_ok=True)
os.makedirs('original',exist_ok=True)
os.makedirs('financedata',exist_ok=True)
```

### 调用ARfindata.sz或ARfindata.sh时你的代码中请包含
    browser = webdriver.Chrome()#根据个人浏览器选择
    browser.get('https://www.szse.cn/disclosure/listed/fixed/index.html') —— 若调用的是ARfindata.sz
    browser.get('http://www.sse.com.cn/disclosure/listedinfo/regular/') ——若调用的是ARfindata.sh
    
    
##### Author：Napstablook  linkfr@163.com


```python

```

from urllib import response
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from random import *
global token
token = "xxxxxxxx" #这是彩云翻译的授权码，自己去彩云小译可免费获得100万字一个月翻译
# 彩云翻译API（用户也可以换其他API，但是注意主程序里面的translate也要改）
def tranlate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers,
    # and it should be replaced by your token

    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }

    headers = {
        "content-type": "application/json",
        "x-authorization": "token " + token,
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return json.loads(response.text)["target"]







# 选项部分
key = {"1":'',"2":'[journa]',"3":'[author]'}
dead = ['datesearch.y_1','datesearch.y_2']
page = 2 # 需要打印多少页的内容，如果为2，则打印2-1页，共10篇
fr = 'datesearch.y_1'#检索一年内的内容，修改数字部分可以选择其他年份
kw = input("输入关键词:")
kw = "\""+kw+"\""
kw = tranlate(kw,'auto2en')
cs1 = input("请输入你要搜索的范围:1为普通关键词、2为期刊名、3为作者名")
try:
    kw = kw+key[cs1]
except:
    kw = input("输入关键词（英文）:")
print(kw)
flag = input("输入任何字符使用标题翻译并继续,留空则不翻译标题:")

#邮箱部分设置（这部分设置不会的看readme的教程）
receiver = 'xxxxxxxx@qq.com'#这是你用来接受邮件的邮箱，按理论啥邮箱都可以
# 设置邮件接收人，可以是QQ邮箱
sender = 'xxxxxxxxxxx@163.com' #填写自己的邮箱，最好是163邮箱
# 设置发件邮箱，一定要自己注册的邮箱
pwd = 'XXXXXXXX'#你的163邮箱授权码
# 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码







######################！！！！以下部分，非必要不要尽量不要修改
# 主程序部分
paper_data = pd.DataFrame(columns=['title','authors','doi',"abstract","abstracte"])
url = 'https://pubmed.ncbi.nlm.nih.gov/'
fmt = 'abstract'
for num in range(1,page):
    response = requests.get(url,
                params={'term':kw,
                        'page':str(num),
                        'filter':fr,
                        'format':fmt},
                headers={"User-Agent":UserAgent().random})
    response.raise_for_status() #防止没正确解析出现错误运行
    response.encoding = response.apparent_encoding # 防止乱码

    print(response.url)
    soup = BeautifulSoup(response.text,'html.parser')

    paper_list = soup.find_all('div',attrs={"class":"results-article"})
    paper_record = {}
    
    for paper in paper_list:
        title = []
        print('正在运行')
        #清空字典
        paper_record.clear() 
        article = paper.article
        titles = article.h1.a.strings
        # strip函数用于删除头尾的空白符,包括\n\t等
        for s in titles:
            if flag:
                s = tranlate(s, "auto2zh")# 调用彩云
            title.append(s.strip())
        paper_record['title'] = ''.join(title)
        
        ## find author
        authors= []
        if article.find('em',attrs={"class":"empty-authors"}):
            authors.append('No author listed')
        else:
            author_list = article.find_all('a',attrs={'class':'full-name'})
            pa = 0 # 只要三个作者
            for author in author_list:
                authors.append(author.string.strip())
                pa +=1
                if pa == 4:
                    break
        # print(','.join(authors))
        paper_record['authors'] = ''.join(authors)

        # 获取DOI信息
        doi = article.find('span',attrs={"class":"citation-doi"})
        if doi is None:
            paper_record['doi'] = 'No doi'
        else:
            paper_record['doi'] = doi.string.strip()

        # 获取摘要信息
        abstract = []
        abstracte = []
        if article.find_all("em",attrs={"class":"empty-abstract"}):
            abstract.append("No abstract")
        else:
            content = article.find("div",attrs={"class":"abstract-content selected"})
            abstracts = content.find_all('p')

            for item in abstracts:
                for sub_content in item.strings:
                    sub_contentC = tranlate(sub_content, "auto2zh")#调用彩云
                    abstract.append(sub_contentC.strip())
                    abstracte.append(sub_content.strip())
            # print('\n'.join(abstract))
            paper_record['abstract'] = ''.join(abstract)
            paper_record['abstracte'] = ''.join(abstracte)
        paper_data = paper_data.append(paper_record,ignore_index=True)
paper_data.to_excel('./RX.xlsx',index=False)
print("运行结束")


# 邮箱预处理
x = randint(0,9)
df1=pd.read_excel('./RX.xlsx')
bt = df1.iloc[x,0]
dio = df1.iloc[x,2]
zy = df1.iloc[x,3]
zye = df1.iloc[x,4]
#### 邮箱部分
if type(zy) == type(1.0):
    zy = "无摘要"
    zye = "no abstract"
if type(dio) == type(1.0): 
    dio = "无d0i"
def sentemail():
    host = 'smtp.163.com'
    # 设置发件服务器地址
    port = 465
    msg = MIMEText("【摘要】"+zy+"\n 【abstract】"+zye+"\n【DOI】"+dio, "plain", "utf-8")
    msg['subject'] ="【爬文推荐】"+bt
    # 设置邮件标题
    msg['from'] = sender
    # 设置发送人
    msg['to'] = receiver
    # 设置接收人
    try:
        s = smtplib.SMTP_SSL(host, port)
        # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)
        # 登陆邮箱
        s.sendmail(sender, receiver, msg.as_string())
        # 发送邮件！
        print('Done.sent email success')
    except smtplib.SMTPException:
        print('Error.sent email fail')

if __name__ == '__main__':
    sentemail()




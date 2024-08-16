from bs4 import BeautifulSoup
import requests 
import chardet
import http.cookiejar as cj
import xlsxwriter
# def cookie_to_dict(cookie):
#     cookie_dict = {}
#     items = cookie.split(';')
#     for item in items:
#         key = item.split('=')[0].replace(' ', '')
#         value = item.split('=')[1]
#         cookie_dict[key] = value
#     return cookie_dict

#创建xlsx文件
workbook=xlsxwriter.Workbook('北大大数据.xlsx')
worksheet=workbook.add_worksheet('Sheet1')
worksheet.write(0,0,'标题')
worksheet.write(0,1,'Web地址')
worksheet.write(0,2,'大致内容')
data=[]

formade={}
#伪装浏览器进行登录
Header={'Header':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
url="https://bda.pku.edu.cn/xwzx/kycg.htm"

for start_num in range(1,6,4):
    print('正在爬取第',start_num,'页')
    if start_num!=1:
        url=url[:-4]+'/'+str(start_num)+'.htm'
    #创建session对象
    s=requests.session()

    #获取cookie
    s.cookies=cj.LWPCookieJar('D:\\PaChong\\data_pull_text\\cookies')
    s.cookies.load(ignore_discard=True, ignore_expires=True)

    #获取登录页面
    res=s.get(url,headers=Header)
    if res.status_code==200:
        print('网页请求成功')
    else:
        print('网页请求失败,失败码为：',res.status_code,'请重新填写Header或登录信息')

    #cookie保存
    s.cookies.save('data_pull_text\cookies')

    # 检测网页内容的编码
    encoding = chardet.detect(res.content)['encoding']
    print('网页内容编码格式为:',encoding)

    #使用BeautifulSoup解析网页
    soup=BeautifulSoup(res.content,"html.parser", from_encoding=encoding)
    text=soup.find_all('div',class_='list_xwyd')
   
    for i in text:
        t=i.find('a')['title']
        web='https://bda.pku.edu.cn'+i.find('a')['href'].strip('..')
        p=i.find('p').string
        tmp_data=[t,web,p]
        data.append(tmp_data)

#写入xlsx文件
for i in range(len(data)):
    worksheet.write_row(i+1,0,data[i])
workbook.close()

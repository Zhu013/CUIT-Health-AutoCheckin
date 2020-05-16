import requests
import re
import time
import threading



def checkin(session,id,username,cookiejar,dataAddress):

    url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/editSjRs.asp'

    header = {
        'Host': 'jszx-jxpt.cuit.edu.cn',
        'Content-Length': '667',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://jszx-jxpt.cuit.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/editSj.asp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
    }
    print(dataAddress['province'])
    province = dataAddress['province']
    print(dataAddress['city'])
    city = dataAddress['city']
    print(dataAddress['country'])
    country = dataAddress['country']
    data={
        'RsNum':'3',
        'Id':id,
        'Tx':'33_1',
        'canTj':'1',
        'isNeedAns':'0',
        'UTp':'Xs',
        'ObjId':username,
        'th_1':'21648',
        'wtOR_1':'N%26sF21648_2%5C%7C%2F%5C%7C%2FN%5C%7C%2F%5C%7C%2FN%5C%7C%2F',
        'sF21648_1':'N',
        'sF21648_2':'',
        'sF21648_3':'N',
        'sF21648_4':'',
        'sF21648_5':'N',
        'sF21648_6':'',
        'sF21648_N':'6',
        'th_2':'21649',
        'wtOR_2':'5%5C%7C%2F%25B8%25DF%25CB%25D9%25C2%25B7%5C%7C%2F2%5C%7C%2F20',
        'sF21649_1':'5',
        'sF21649_2':'',
        'sF21649_3':'2',
        'sF21649_4':'20',
        'sF21649_N':'4',
        'th_3':'21650',
        'wtOR_3':'6\|/'+province+'\|'+city+'\|/'+country+'\|/1\|/5\|/1\|/1\|/1\|/',
        'sF21650_1':'6',
        'sF21650_2':province.encode('gb2312'),
        'sF21650_3':city.encode('gb2312'),
        'sF21650_4':country.encode('gb2312'),
        'sF21650_5':'1',
        'sF21650_6':'5',
        'sF21650_7':'1',
        'sF21650_8':'1',
        'sF21650_9':'1',
        'sF21650_10':'',
        'sF21650_N':'10',
        'zw1':'',
        'cxStYt':'A',
        'zw2':'',
        'B2':'%CC%E1%BD%BB%B4%F2%BF%A8'
    }
    cookiejar.set('refreshCT','UserName=Xs%5F'+str(username))
    #print(cookiejar)
    req = session.post(url=url,headers = header,cookies = cookiejar,data=data)
    html = req.content.decode('gb2312')
    state = re.search('alert(.*?);',html).group(1)
    print(state)
    #print(req.content.decode('gb2312'))
    #print(cookiejar)
    #print(re.cookies)


def getId(session,cookie):
    url = 'http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/sj.asp'
    #cookieurl = 'http://login.cuit.edu.cn/Login/xLogin/Login.asp'
    #re = requests.get(url = cookieurl)
    #print(re.headers)
    #print(session.headers)

    headers={
        'Referer': 'http://jszx.cuit.edu.cn/Index.htm'
    }
    req = session.get(url=url,headers = headers,cookies=cookie)
    html = req.text
    #print(html)
    #timestring = print(time.strftime("%Y-%m-%d", time.localtime()))
    id = re.search('&Id=(.*?)target=_self>',html).group(1)
    url_end = re.search('a href=(.*?)target=_self>',html).group(1)
    print(id)
    url = 'http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/'+url_end
    req = session.get(url = url,headers=headers)

    return id

'''
<TR VALIGN=top ALIGN=left bgcolor=#E0E8FF>
<TD align="center" style="vertical-align: middle;">&nbsp;</TD>
<TD align="Left" style="vertical-align: middle;"><a href=sjDb.asp?UTp=Xs&jkdk=Y&ObjId=2017122088&Id=10969 target=_self>0419疫情防控――师生健康状态采集</a></TD>
<TD align="Left" style="vertical-align: middle;">2020-04-19 06:00<br>2020-04-19 23:59</TD>
</TR>

'''


def getSession(username,password):
    print(username,password)
    url ='http://login.cuit.edu.cn/Login/xLogin/Login.asp'
    data = {
        'txtId':username,
        'txtMM':password,
        'verifycode':'%B2%BB%B7%D6%B4%F3%D0%A1%D0%B4',
        'codeKey':'480980',
        'Login':'Check',
        'IbtnEnter.x':42,
        'IbtnEnter.y':4
    }

    headers={
        'Host': 'login.cuit.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '150',
        'Origin': 'http://login.cuit.edu.cn',
        'Connection': 'close',
        'Referer': 'http://login.cuit.edu.cn/Login/xLogin/Login.asp',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    session = requests.session()
    req = session.post(url = url,data=data,headers = headers,allow_redirects=False)
    #print(req.content.decode('gb2312'))
    
    cookiejar1 = requests.cookies.RequestsCookieJar()
    for cookie in req.cookies:
        cookiejar1.set(cookie.name,cookie.value)
    
    for cookie in req.headers['Set-Cookie'].split(";"):
        key = cookie.split('=')[0]
        value = cookie.split('=')[1]
        cookiejar1.set(key,value)
    #print(cookiejar1)

    headers2 = {
    'Host': 'jszx-jxpt.cuit.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie':'123',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
    }
    #取消自动重定向才可以获得cookie
    req2 = session.get(url = 'http://jszx-jxpt.cuit.edu.cn/jxgl/xs/netks/sj.asp?jkdk=Y',headers=headers2,allow_redirects=False)
    
    cookiejar2 = requests.cookies.RequestsCookieJar()
    for cookie in req2.cookies:
        cookiejar2.set(cookie.name,cookie.value)
    
    for cookie in req2.headers['Set-Cookie'].split(";"):
        key = cookie.split('=')[0]
        value = cookie.split('=')[1]
        cookiejar2.set(key,value)

    req3 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/UserPub/Login.asp?UTp=Xs',cookies = cookiejar2,allow_redirects=False)
    req4 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Login/tyLogin.asp',cookies=cookiejar2,allow_redirects=False)
    html = req4.text
    dircUrl = re.search('URL=(.*?)">',html).group(1)
    req4 = session.get(url=dircUrl,cookies = cookiejar1,allow_redirects=False)
    req5 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Login/tyLogin.asp',cookies = cookiejar1,allow_redirects=False)
    req6 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Login/syLogin.asp',cookies = cookiejar1,allow_redirects=False)
    req7 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/UserPub/Login.asp?UTp=Xs&Func=Login',cookies = cookiejar1,allow_redirects=False)
    req8 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/MainMenu.asp',cookies = cookiejar1,allow_redirects=False)
    req9 = session.get(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/sj.asp',cookies = cookiejar1,allow_redirects=False)

    #print(req9.content.decode('gb2312'))
    return session,cookiejar2

def fun_timer():
    main()
    global timer
    timer = threading.Timer(21600,fun_timer)
    timer.start()

def main():
    username = 
    password = 'xxxxx'
    data={
        'province':'四川',
        'city':'成都',
        'country':'XX'
    }
    session,cookie = getSession(username,password)
    id = getId(session,cookie)
    checkin(session,id,username,cookie,data)
    #print(re.content.decode('gbk'))

if __name__ == "__main__":
    '''
    请设置main函数里面的以下内容
    username = 
    password = 'xxxxxxxx'
    data={
        'province':'四川',
        'city':'成都',
        'country':'XX'
    }
    '''
    timer = threading.Timer(5,fun_timer)
    timer.start()

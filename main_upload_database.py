
import os,bs4,pymysql,re
from bs4 import BeautifulSoup

def read_html(htmlpath):
    with open(htmlpath,'r',encoding='utf-8') as file:
        html = file.read()
    
    return html


def get_password(htmlnumber):
    if htmlnumber<10:
        password = '000' + str(htmlnumber)
    elif htmlnumber<100:
        password = '00' +  str(htmlnumber)
    elif htmlnumber<1000:
        password = '0' +  str(htmlnumber)
    elif htmlnumber<10000:
        password =        str(htmlnumber)
    else:
        g = htmlnumber%10
        s = int(((htmlnumber - g)%100)/10)
        b = int(((htmlnumber - g - s*10)%1000)/100)
        password = str(b) + str(s) + str(g) + 'X'
    return password

 
#  it aim is parser gathering datas by BeautifulSoup 
def parser_html(html,password):
    infro = []
    soup = BeautifulSoup(html,"html.parser")
  
    tables = soup('table')[1]
    trs = tables('tr')
    trs.pop(0)

    n = 0   #行首[0]
    for i in trs:
        #跳过行首
        n+=1
        if n==1:
            continue

        tds = i('td')
       
        infro.append([password                      , tds[1].string.strip('\n     '), tds[2].string.strip('\n     '),
                      tds[3].string.strip('\n     '), tds[4].string.strip('\n     '), tds[5].string.strip('\n     '),
                      tds[6].string.strip('\n     '), tds[7].string.strip('\n     '), tds[8].string.strip('\n     ')])
    return infro

#   it aim is get html size
def get_size(htmlpath):
    # the size of a file without any data  is 489
    htmlsize = os.path.getsize(htmlpath)
    
    return htmlsize


        
def main():

    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='score')
    try:
        cur = conn.cursor()
 
        for htmlnumber in range(0,11000):
        
            htmlpath = './html/' + str(htmlnumber) + '.html'

            #the program will skip if size is less than 500
            htmlsize = get_size(htmlpath)
            if htmlsize<=500:
                continue
            
            html = read_html(htmlpath)

            password = get_password(htmlnumber)
            
            infro = parser_html(html,password)
            
            for i in infro:
                string  =i[8]
                rr = re.compile(r'\d{1,3}')
                try:
                    string = rr.findall(string)[0]
                except:
                    pass
                else:
                    
                    sql = "insert into score_182 values("+'"'+i[0]+'"'+","+'"'+i[1]+'"'+","+'"'+i[2]+'"'+","+'"'+i[3]+'"'+","+i[4]+","+'"'+i[5]+'"'+","+'"'+i[6]+'"'+","+'"'+i[7]+'"'+","+i[8]+");"

                   # print(sql)
                    cur.execute(sql)
                    conn.commit()
                    rows = cur.fetchall()
                   # print(rows)
            print('finished:' + str(htmlnumber) + '    counts:11000')
   
    finally:
        conn.close()

        
main()




"""

 for i in infro:

        file.write(i[0]+' '+i[1]+' '+i[2]+' '+i[3]+' '+i[4]+' '+i[5]+' '+i[6]+' '+i[7]+' '+i[8] + '\n')
        
        print(i[0]+' '+i[1]+' '+i[2]+' '+i[3]+' '+i[4]+' '+i[5]+' '+i[6]+' '+i[7]+' '+i[8])


        print(tds[0].string.strip('\n     ') + tds[1].string.strip('\n     ') + tds[2].string.strip('\n     '),
              tds[3].string.strip('\n     ') + tds[4].string.strip('\n     ') + tds[5].string.strip('\n     '),
              tds[6].string.strip('\n     ') + tds[7].string.strip('\n     ') + tds[8].string.strip('\n     '))
        print('------')
print(scoreinfro[0])
"""

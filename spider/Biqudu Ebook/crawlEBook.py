#!/usr/bin/env python
# coding:utf-8
# author: xinschen@foxmail.com
# Note:
#	基于python3.6
#   爬取笔趣网上小说

import re
from bs4 import BeautifulSoup
import requests
import os

downLoadFile = os.getcwd()  ##要下载到的目录
baseUrl = 'http://www.biqudu.com/{shuhao}'
shuhao = '13_13453'  
headers = {

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def getBookInfo(url,shuhao):
    try:
        url = baseUrl.format(shuhao = shuhao)
        response = requests.get(url, headers=headers,timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text,'html.parser')
        #获取小说名字,建立目录名
        title = soup.find('meta', property='og:title')
        titlename = title.attrs['content']
        if not os.path.exists(titlename):
            os.mkdir(titlename)
        chapter = soup.find_all('dd')
    except Exception as e:
        print(e)
    chapter_dict = {}
    try:
        for line in chapter:
            filename = line.a.string
            chapterUrl = line.a.attrs['href']
            chapter_dict[filename] = chapterUrl
    except Exception as e:
        print(e)
    return  chapter_dict,titlename

# 写入文件
def setDoc(string_list,filename,titlename):
    if (len(string_list) < 2):
        return
    try:
		# 因win系统不允许文件名含有？等特殊字符
        filename = re.sub('\?', '', filename)
        file_s = downLoadFile + os.sep + titlename + os.sep + filename + '.txt'
        file = open(file_s, 'w+', encoding='utf-8')
        for i in string_list:
            #file.write('\t')
            for ii in i.split('    '):
                file.write(ii)
            file.write('\n')
    except Exception as e:
        print(e)

def getALLChapterDoc(chapter_dict,titlename):
    try:
        for k,v in chapter_dict.items():
            string_list = []
            print('正在抓取[%s]的内容' %(k))
            string_list.append(str(k))
            url = baseUrl.format(shuhao = v)
            try:
                response = requests.get(url, headers=headers,timeout=10)
                response.encoding = "utf-8"
                soup = BeautifulSoup(response.text, 'html.parser')
                strings = soup.findAll('div', id="content")[0];
            except Exception as e:
                print(e)
            for string in strings:
                st = string.__str__()
                if (len(st.split('<br/>')) > 1) or (len(st.split('sript')) > 1):
                    pass
                else:
                    st = re.sub('[a-z]|[\<\>\(\)\|\&|\/\;]','',st)
                    string_list.append(st)
            #写入文件
            setDoc(string_list,k,titlename)
    except Exception as e:
        print(e)


def main():
    chapter_dict, titlename = getBookInfo(baseUrl,shuhao)
    getALLChapterDoc(chapter_dict, titlename )

if __name__ == '__main__':
    main()
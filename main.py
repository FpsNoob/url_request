import urllib.request
import os
import re

def gettgz(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    reg = r'href=".*\.tgz"'
    tgzre = re.compile(reg)
    tgzlist = re.findall(tgzre,html.decode('utf-8'))  # 找到所有.tgz文件
    for i in tgzlist:
        filename = i.replace('href="', '')
        filename = filename.replace('"', '')
        print('正在下载：'+filename)  # 提示正在下载的文件
        downfile = i.replace('href="', url)
        downfile = downfile.replace('"', '')  # 得到每个文件的完整连接
        ur = urllib.request.urlopen(downfile).read()
        open(filename, 'wb').write(ur)  # 把下载的文件以tgz格式存储在D盘

if __name__ == '__main__':
    file_url = r'http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/'
    os.chdir('D:\\chrome\\voxforge speech files\\')  # 改变当前工作目录到指定路径
    html = gettgz(file_url)
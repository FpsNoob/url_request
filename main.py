import urllib.request
import os
import re

def gettgz(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    reg = r'href=".*\.tgz"'
    tgzre = re.compile(reg)
    tgzlist = re.findall(tgzre,html.decode('utf-8'))  # find all tgz file
    for i in tgzlist:
        filename = i.replace('href="', '')  # detele href
        filename = filename.replace('"', '')
        if os.path.exists(filename):
            continue
        else:
            print('loading: '+filename)  # display the name of loadingfile
            downfile = i.replace('href="', url)  # loading path + filename
            downfile = downfile.replace('"', '')
            data = urllib.request.urlopen(downfile).read()  # loading filename
            open(filename, 'wb').write(data)  # save the file


if __name__ == '__main__':
    file_url = r'http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/'
    os.chdir('D:\\chrome\\voxforge speech files\\')  # change save path
    html = gettgz(file_url)
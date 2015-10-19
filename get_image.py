import urllib
import re
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    
    # save the pics to a new folder.
    os.mkdir('pics')
    local = os.getcwd() + '/pics/'
    x = 0
    
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, local + '%s.jpg' % x)
        x += 1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)

import requests
from lxml import etree

j=0
for i in range(0,6):
    r=requests.get('https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C?'+'start=%d&type=T'%i*20).content
    books=etree.HTML(r)
    imgs=books.xpath('//*[@id="subject_list"]/ul/li/div[1]/a/img/@src', stream=True)
    for img in imgs:
        j=j+1
        with open(str(j)+'.jpg', 'wb') as fd:
            picture=requests.get(img).content
            fd.write(picture)
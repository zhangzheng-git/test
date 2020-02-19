import urllib.request
import urllib.parse
import re
import os

header={
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
     'referer':"https://image.baidu.com"
}

url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
keyword=input("请输入关键字:")
#转码
keyword=urllib.parse.quote(keyword,'utf-8')

n=0
j=0
while(n<3000):
    n +=30
    #url
    urlnew=url.format(word=keyword,pageNum=str(n))

    #获取请求
    ret = urllib.request.Request(urlnew,headers=header)
    #打开网页
    ret =urllib.request.urlopen(ret)
    #获取网页内容
    try:
        html=ret.read().decode('utf-8')
        #print(html)
    #正则匹配，只匹配url
    except:
        print("出错了")
        continue
    r = re.compile("ObjURL.*?\.jpg")
    #获取匹配结果
    s = r.findall(html)
    print(s)
    if os.path.isdir("E://pic") !=True:
        os.mkdir("E://pic")
    with open("picture.txt","a") as f:
        for i in s:
            i=i.replace('ObjURL":"','')
            f.write(i)
            f.write('\n')
            #保存图片
            urllib.request.urlretrieve(i, "E://pic/pic{num}.jpg".format(num=j))
            j +=1
        f.close()
print("总共"+str(j))

# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: http2.py
@time: 2020/10/26 10:04
@desc:
'''
import urllib3
import urllib

"""
urllib库
urllib 是一个用来处理网络请求的python标准库，它包含4个模块。
urllib.request---请求模块，用于发起网络请求
urllib.parse---解析模块，用于解析URL
urllib.error---异常处理模块，用于处理request引起的异常
urllib.robotparser robots.tx---用于解析robots.txt文件

urllib.request模块
request模块主要负责构造和发起网络请求，并在其中添加Headers，Proxy等。 利用它可以模拟浏览器的请求发起过程。

发起网络请求
操作cookie
添加Headers
使用代理
关于urllib.request.urlopen参数的介绍
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
urlopen是一个简单发送网络请求的方法。它接收一个字符串格式的url，它会向传入的url发送网络请求，然后返回结果。
"""
"""
Python3.x中将urllib2合并到了urllib，之后此包分成了以下几个模块：
urllib.request 用于打开和读取URL
urllib.error 用于处理前面request引起的异常
urllib.parse 用于解析URL
urllib.robotparser用于解析robots.txt文件
Python3.x中，随着urllib2合入urllib，一些常用的方法也发生了变化：2
在Python2.x中使用import urlparse——在Python3.x中会使用import urllib.parse
在Python2.x中使用urllib2.urlopen或urllib.urlopen（已弃用）——在Python3.x中会使用urllib.request.urlopen
在Python2.x中使用urllib2.Request——在Python3.x中会使用urllib.request.Request
在Python2.x中使用urllib.quote——在Python3.x中会使用urllib.request.quote
在Python2.x中使用urllib.urlencode——在Python3.x中会使用urllib.parse.urlencode
在Python2.x中使用cookielib.CookieJar——在Python3.x中会使用http.CookieJar
异常处理：在Python2.x中使用urllib2.URLError,urllib2.HTTPError——在Python3.x中会使用urllib.error.URLError,urllib.error.HTTPError
"""

#sample1:
#urlopen默认会发送get请求，当传入data参数时，则会发起POST请求。data参数是字节类型、者类文件对象或可迭代对象。

from urllib import request
response = request.urlopen(url='http://www.httpbin.org/post',
                           data=b'username=q123&password=123')
print(response.read().decode())


# 还才可以设置超时，如果请求超过设置时间，则抛出异常。
# timeout没有指定则用系统默认设置，timeout只对，http，https以及ftp连接起作用。
# 它以秒为单位，比如可以设置timeout=0.1 超时时间为0.1秒。

response = request.urlopen(url='https://www.baidu.com/',timeout=0.1)


"""
1 . 请求头添加
通过urllib发送的请求会有一个默认的Headers: “User-Agent”:“Python-urllib/3.6”，指明请求是由urllib发送的。
所以遇到一些验证User-Agent的网站时，需要我们自定义Headers把自己伪装起来。
"""
from urllib import request
headers ={
    'Referer': 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=python%20urllib%E5%BA%93&oq=python%2520urllib%25E5%25BA%2593&rsv_pq=947af0af001c94d0&rsv_t=66135egC273yN5Uj589q%2FvA844PvH9087sbPe9ZJsjA8JA10Z2b3%2BtWMpwo&rqlang=cn&rsv_enter=0&prefixsug=python%2520urllib%25E5%25BA%2593&rsp=0',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
rps = request.Request(url='https://www.baidu.com/', headers=headers)
rlt = request.urlopen(rps)
print(rlt.read().decode())

#2. 操作cookie
#在开发爬虫过程中，对cookie的处理非常重要，urllib的cookie的处理如下案例

from urllib import request
from http import cookiejar
# 创建一个cookie对象
cookie = cookiejar.CookieJar()
# 创一个cookie处理器
cookies = request.HTTPCookieProcessor(cookie)
# 以它为参数，创建opener对象
opener = request.build_opener(cookies)
# 使用这个opener 来发请求
res =opener.open('https://www.baidu.com/')
print(cookies.cookiejar)

#3. 设置代理
#运行爬虫的时候，经常会出现被封IP的情况，这时我们就需要使用ip代理来处理，urllib的IP代理的设置如下：

url ='http://httpbin.org/ip'
#代理地址
proxy ={'http':'172.0.0.1:3128'}
# 代理处理器
proxies =request.ProxyBasicAuthHandler(proxy)
# 创建opener对象
opener = request.build_opener(proxies)
re =opener.open(url)
print(re.read().decode())


"""
 urlib库中的类或或者方法，在发送网络请求后，都会返回一个urllib.response的对象。
 它包含了请求回来的数据结果。它包含了一些属性和方法，供我们处理返回的结果
read() 获取响应返回的数据，只能用一次 
readline() 读取一行 
info() 获取响应头信息 
geturl() 获取访问的url
getcode() 返回状态码 

urllib.parse模块
parse.urlencode() 在发送请求的时候，往往会需要传递很多的参数，如果用字符串方法去拼接会比较麻烦，
parse.urlencode()方法就是用来拼接url参数的。
"""
from urllib import parse
params = {'wd':'测试', 'code':1, 'height':188}
rs = parse.urlencode(params)
print(rs)  #打印结果为wd=%E6%B5%8B%E8%AF%95&code=1&height=188
#也可以通过parse.parse_qs()方法将它转回字典
print(parse.parse_qs('wd=%E6%B5%8B%E8%AF%95&code=1&height=188'))

"""
urllib.error模块
error模块主要负责处理异常，如果请求出现错误，我们可以用error模块进行处理 主要包含URLError和HTTPError
URLError：是error异常模块的基类，由request模块产生的异常都可以用这个类来处理
HTTPError：是URLError的子类，主要包含三个属性
Code:请求的状态码
reason：错误的原因
headers：响应的报头
"""
from urllib import error
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except error.URLError as e:
    print(e.reason)

else:
    print("reqeust successfully")

"""
robotparse模块主要负责处理爬虫协议文件，robots.txt.的解析。 https://www.taobao.com/robots.txt
Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），
网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取
"""
#urllib3
"""
•线程安全
•连接池
•客户端SSL/TLS验证
•文件分部编码上传
•协助处理重复请求和HTTP重定位
•支持压缩编码
•支持HTTP和SOCKS代理

"""
import urllib3
# 创建连接
http = urllib3.PoolManager()
# 发送请求
res = http.request('GET','https://www.baidu.com/')
# 状态码
print(res.status)
# 返回的数据
print(res.data.decode())

import urllib3
# 创建连接
http = urllib3.PoolManager()
# 发送请求
res = http.request('POST','https://www.baidu.com/',fields={'hello':'word'})
# 状态码
print(res.status)
# 返回的数据
print(res.data.decode())

"""
http响应对象提供status, data,和header等属性
status--状态码
data--读取返回的数据
header--请求头
"""
#返回的json格式数据可以通过json模块，load为字典数据类型。
import json
data={'attribute':'value'}
encode_data= json.dumps(data).encode()

r = http.request('POST',
                     'http://httpbin.org/post',
                     body=encode_data,
                     headers={'Content-Type':'application/json'}
                 )
print(r.data.decode('unicode_escape'))

#urllib3库Proxies(代理IP)
proxy = urllib3.ProxyManager('http://101.236.19.165:8866')
res =proxy.request('GET','https://www.baidu.com/')
print(res.data)

#urllib3库headers(添加请求头)

http = urllib3.PoolManager()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
res = http.request('GET', 'https://www.baidu.com/', headers=headers)
print(res.data)

#JSON 当我们需要发送json数据时，我们需要在request中传入编码后的二进制数据类型的body参数，并制定Content-Type的请求头
#JSON:在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据：
import json
data={'attribute':'value'}
encode_data= json.dumps(data).encode()

r = http.request('POST',
                     'http://httpbin.org/post',
                     body=encode_data,
                     headers={'Content-Type':'application/json'}
                 )
print(r.data.decode('unicode_escape'))

#对于二进制的数据上传，我们用指定body的方式，并设置Content-Type的请求头
#使用multipart/form-data编码方式上传文件,可以使用和传入Form data数据一样的方法进行,并将文件定义为一个元组的形式　　　　　(file_name,file_data):
with open('1.txt','r+',encoding='UTF-8') as f:
    file_read = f.read()

r = http.request('POST',
                 'http://httpbin.org/post',
                 fields={'filefield':('1.txt', file_read, 'text/plain')
                         })
print(r.data.decode('unicode_escape'))

#二进制文件
with open('websocket.jpg','rb') as f2:
    binary_read = f2.read()
r = http.request('POST',
                 'http://httpbin.org/post',
                 body=binary_read,
                 headers={'Content-Type': 'image/jpeg'})
#
# print(json.loads(r.data.decode('utf-8'))['data'] )
print(r.data.decode('utf-8'))

#上传文件
# 元组形式
with open('a.html', 'rb') as f:
    data = f.read()
http = urllib3.PoolManager()
r = http.request('post', 'http://httpbin.org/post', fields={'filefield': ('a.html', data, 'text/plain')})
print(r.data.decode())

# 二进制形式
r = http.request('post', 'http://httpbin.org/post', body=data, headers={'Content-Type': 'image/jpeg'})
print(r.data.decode())


#llib3 本身设置了https的处理，但是有警告
urllib3.disable_warnings() #禁用各种警告
url = "https://www.12306.cn/mormhweb/"
http = urllib3.PoolManager()
r = http.request('get',url)
print(r.data.decode())



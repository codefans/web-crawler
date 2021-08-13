
import requests

print('hello test')
str='hello world'
print('zhangsan, ' + str)



url = "https://www.baidu.com"
# url = "http://plus.m.jd.com/index"
# url = "https://www.qq.com"
result = requests.get(url)
result.encoding='utf-8'
print("第一种方法")
# 获取状态码，200表示成功
print(result.text)
# 获取网页内容的长度
# print(len(response1.read()))
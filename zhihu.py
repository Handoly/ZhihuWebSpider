from pyquery import PyQuery as pq
import requests


url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'cookie':'_zap=7dac0dea-d9f7-49dd-ae08-ffdcc23d5ade; d_c0="AIASorxCUhWPTmBmbA4PjzNdtzbGSyakg4g=|1659077674"; _xsrf=HkMtgTjTNArVTTRRcI3hAgL5Dk7x3yXt; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1659077674,1659154247,1659255389; captcha_session_v2=2|1:0|10:1659255389|18:captcha_session_v2|88:MXNURGtFYTIxTjBwY095RXZmTDdsSU0vbGZIenVTUWJJcW1nUStaVDRZemZuOTZnQWg1MENRSENNK3RSOTlIMg==|75d4bf11499b86817313c764026d129853555b8c1bbd245b9884126777126207; SESSIONID=hmYN4lERRVBFGA2bvRA7KU3tuzQlXwCQmW10fWbHdnt; JOID=U1AcB0wjy1KQYxncPif0yJvTXoEjQqcG3VF8mGF3lBHbJ17nXXb9uvdsEdAw3FqxDNc2yZD84gVwuHOLPZYgXgo=; osd=WloWC0oqwVicZRDWNCvywZHZUocqSK0K21h2km1xnRvRK1juV3zxvP5mG9w21VC7ANE_w5rw5Ax6sn-NNJwqUgw=; __snaker__id=TQ09JMvinEHf622o; gdxidpyhxdE=pUo01XH3Lq7vI4Y5SbDUc5\Q9+4XWPL\cwwWr5WbOlmCt8LynJKbDl3HSUu0OP/x/gqrXLpWvwlHPqKupucy1\RikDGcEZO8IX7cdoQ+V7pKVoRCoz3QmLqHKfRw3IeRP56bJBrGny3aLP/4v6Mpj7ru/HffqhSi8zjQRma443fHhY3X:1659256289650; _9755xjdesxxd_=32; YD00517437729195:WM_NI=LLcCAyQF2+F3jq27IUbAIGwt+kYUXfBFzeY/LF4IbsAgk4ObMN6lSfcXXfCLBUf+7Na+K7KLx6qlzKI2b+cIWpUO/1JcRlP3837Vcx2sJNhhjgeqOYOZi4qIFddJilTlUkw=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6ee91ea7ca6a6fa9bfc7a9bbc8bb6c84e938f9bb0d54d9597aeaae94f878f8dd5dc2af0fea7c3b92a9094ada4c473939afeccc539aaaffed8cc5fa29f87a8f680e9b597b6db6e829ab686dc25909afcaae17983b9a5d5ce6a8f92fa8dd26ea1889887c248828baaccb646a3f585d8ca48bceabf8df9418beeaecce24395b09bb0ae3b8abd9e8dd339fcedf9b7e274f2ad86afeb64aab9ab92ce538d86a7d5f44386bcacabec6898b49b8cf637e2a3; YD00517437729195:WM_TID=Qq/6hqsk/aBARUUEUFbFGCJbZ2UUUHoZ; z_c0=2|1:0|10:1659255419|4:z_c0|92:Mi4xbG1zYkRnQUFBQUFBZ0JLaXZFSlNGU1lBQUFCZ0FsVk5lNGpUWXdBYkVjNUFKM3Vwck1NR252ajdQUFg1TzUtQzN3|8f0417d2a2c09cfd5eb8d1aa86cb839f42eba4b0cde724ce107ff93a30da174d; q_c1=0f125691b0ca42628d67db8d952ced5e|1659255419000|1659255419000; NOT_UNREGISTER_WAITING=1; SUBMIT_0=216fd1fe-932a-43e5-a893-5e1df302c52c; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1659255634; KLBRSID=975d56862ba86eb589d21e89c8d1e74e|1659255638|1659255388'
}

response = requests.get(url,headers=headers)
html = response.text
'''
with open('zhihu_explore.html','w',encoding='utf-8') as f:
    f.write(html)
    print('文件写入成功')'''
'''
with open('zhihu_explore.html',encoding='utf-8') as f:
    html = f.read()
'''
doc = pq(html)
items = doc('div')

for a in  items.children('.css-1nd7dqm').items():
    #获取标题
    title = str(a.text())
    print(title)
    #获取作者名称
    link = a.attr('href')
    reponse = requests.get(url=link,headers=headers)
    html = reponse.text
    doc1 = pq(html)
    text = str(doc1('.UserLink-link').text()).strip().split('  ')
    author = text[1]
    print(author)



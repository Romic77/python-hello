import json
import urllib.request
from http.client import HTTPResponse

import jsonpath

url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1629789477003_137&jsoncallback=jsonp138&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"
headers = {
    'authority': 'dianying.taobao.com',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'cna=CXZRGshYhioCAT2NQTnatP/r; t=e12c355242d216706cc9ec09e139b32e; lgc=chenqi19920630; tracknick=chenqi19920630; thw=cn; cookie2=283ad9fc9fc51766144fbee449d0c7e8; _samesite_flag_=true; cancelledSubSites=empty; v=0; _tb_token_=93305e684030; dnk=chenqi19920630; useNativeIM=false; sgcookie=E100Tajm9PKo8RsflV6gsF2QXeBhhhXb8qAKk8nH3PgR9u5QaRU1W3TtLlW2nbUUbVA1AA3mHIkKb0vzQRN8w%2FDN9CfzoBd6ZT%2Bstc%2BrJwTgeApGxKYCA4BgTNmfOP%2F0zegb; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=VWolk1ZNHJIQ&nk2=AHLS8YZ1SzayINb2lJQ%3D&vt3=F8dCsfAoL8JwiORQupA%3D; csg=87f2859a; skt=07f9643a13906336; existShop=MTY4Mzg3ODY3MA%3D%3D; uc4=id4=0%40V8sFkv24ZBBsAv1N%2B9Rmq%2FMGTv0%3D&nk4=0%40AhyE90VqxjkBAjhsSrlmrT5eP69DCmSrEA%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; uc1=pas=0&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=true&cookie14=Uoe8idvvLHGw0Q%3D%3D&cookie21=VT5L2FSpccV6%2BGPAVCK7&cart_m=0; xlly_s=1; isg=BFRUBz1FzGsxOGGFozvTYNeiJZTGrXiXBU3cve41H19i2fQjF7xYJfRQ2dHBIbDv; l=fBjPNCfHqDnwrZwTBO5Cnurza77OWIRb4sPzaNbMiIEGa6ARtFZacNC_v44JSdtjgTCfOeKygJ-c1dLHRntpvxDDB7kqm0Js3xv9A1HHZ; tfstk=cTZRBpsHktp-Yj5n00QDLIrsubBcZF6-gLMJvununccP_-tdiGEgXNUAPblZwtC..',
    'pragma': 'no-cache',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.HTTPSHandler
opener = urllib.request.build_opener(handler)
response = opener.open(request)

assert isinstance(response, HTTPResponse)
content = response.read().decode('utf-8')

print(content)

content = content.split('(')[1].split(')')[0]
print(content)

with open('./74-jsonpath解析淘票票.json', 'w', encoding='utf-8') as f:
    f.write(content)

obj = json.load(open('./74-jsonpath解析淘票票.json', 'r', encoding='utf-8'))
region_name_list = jsonpath.jsonpath(obj, '$..regionName')
print(region_name_list)

import json
import urllib.parse
import urllib.request
from http.client import HTTPResponse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    # 不写cookie 就会返回报错
    'Cookie': 'BIDUPSID=7373BEDB2D27D298AFB02BD55613D470; PSTM=1679721641; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=lhZRUVzbThMQU9Ndms3VGpnWTZGdE9kQkQ0QWIxNUd2WEMtTnJvVnlpZklZVTFrSVFBQUFBJCQAAAAAAAAAAAEAAAB0pXgKcXEyODAzODU1NTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjUJWTI1CVkY; BDUSS_BFESS=lhZRUVzbThMQU9Ndms3VGpnWTZGdE9kQkQ0QWIxNUd2WEMtTnJvVnlpZklZVTFrSVFBQUFBJCQAAAAAAAAAAAEAAAB0pXgKcXEyODAzODU1NTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjUJWTI1CVkY; BAIDUID=7373BEDB2D27D29884D07762522FD3FC:SL=0:NR=10:FG=1; MCITY=-340%3A; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1684117865; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=7373BEDB2D27D29884D07762522FD3FC:SL=0:NR=10:FG=1; PSINO=6; delPer=0; ZFY=ad6Vsan5ukkzmER4WDI80xhNsWD7ZTDdDWL48lFj9yA:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BAIDU_WISE_UID=wapp_1684739196407_535; arialoadData=false; RT="z=1&dm=baidu.com&si=e7162736-a80e-4e12-9f67-c2f3e7a6b82f&ss=lhyi7uz3&sl=7&tt=9wj&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=jq80&nu=3w2oaayq&cl=jv6m&ul=krnj&hd=krom"; H_PS_PSSID=38516_36553_38541_38610_38538_38593_38597_38485_38638_38503_26350_38568; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1684749396; ab_sr=1.0.1_ZjlmNzk1OTIwNDcwYWMwNDQ0ODU0MzQ4NWQ0OGIyYTVmMzE0N2NiMmQwZWJkOTJjNTkwZjc1NTllYzQzMDZiNzM2YzkwZWM2NjU0M2NlOTk1ZWJlMWYxOTdiZGEzMmE1YjA3N2E4MTIyZGMwNmZkYmRiNjI0YWFhZGJhNTdlYTk0NWFkNjM0NjM2MTY3MzA0NWQyNjA3ODhjY2JmODExMjVjMWMxNTUzOTYxNTEyODgwYmE2NGI1N2U0NjViZTEw'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'cb1e1d333f9a84170060dfb22b210f4a',
    'domain': 'common',
    'ts': '1684749420805'
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
assert isinstance(response, HTTPResponse)

content = response.read().decode('utf-8')

# 将字符串转为json对象
jsonObject = json.loads(content)
print(jsonObject)

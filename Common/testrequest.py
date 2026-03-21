import requests


# r = requests.get('https://www.baidu.com/')
# print(r.cookies)
# for k,v in r.cookies.items():
#     print(k+'='+v)


# if not r.status_code==requests.codes.ok:
#     print('fail')
# else:
#     print('success')

#响应内容（str类型）
# print(type(r.text),r.text)
# #响应内容（bytes类型）
# print(type(r.content),r.content)
# #状态码
# print(type(r.status_code),r.status_code)
# #响应头
# print(type(r.headers),r.headers)
# #Cookies
# print(type(r.cookies),r.cookies)
# #URL
# print(type(r.url),r.url)
# #请求历史
# print(type(r.history),r.history)


# data={
#     'name':'gerq',
#     'age':22
# }
# r=requests.get('http://httpbin.org/get')
# print(r)
# print(r.status_code)
# print('1111111')
# print(r.text)
# print(r.json())
#
url='https://t.10jqka.com.cn/portfolio/base/getPortfolioIncomeInfo?id=1751&startDate=2023-05-26&endDate=2024-05-26'
params=None
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/67.0.3396.99 Safari/537.36',
}

# cookies='Hm_lvt_722143063e4892925903024537075d0d=1694488870,1695198616,1695261226,1695349448; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1694488872,1695198616,1695278098,1695349449; hxmPid=sns_index_502217857.yellowV.visitor.all.no.show; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=sX5fJ6OD%2BbAyfwTWX6%2BaEg2UTzDzP939deAhosx3Bho%2BW89WHLpgUZAM7k8vyKp%2B%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; u_did=8423AB832D4547D68A367EAD5563B178; u_ttype=WEB; user_status=0; PHPSESSID=q9d03t6km48fpvbrg1rn6hv3m4; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1714959971,1715045912,1715132528,1715332023; Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333=1714959970,1715045912,1715132528,1715332023; ttype=WEB; user=MDp4eWphNzE6Ok5vbmU6NTAwOjM3MTQxMjg1Nzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoyNDo6OjM2MTQxMjg1NzoxNzE1MzMyMDQzOjo6MTQ3ODY3OTA2MDo2MDQ4MDA6MDoxMzcwMDFhNThiODBkY2IzOGNjYTA5MGMzZGVhMjYwY2U6ZGVmYXVsdF80OjE%3D; userid=361412857; u_name=xyja71; escapename=xyja71; ticket=b32cd0e9d46c345f9bc6c31576ea710e; utk=2bac36df537029c6f91621b131bcd51a; Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333=1715332066; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1715332066; v=Ax4H5Fjk9HRHkCAQG_Q_MFITb79l3-JZdKOWPcinimFc67BhMG8yaUQz5kGb'
# cookies={cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies.split(";")}
# print(cookies)

#response = requests.get(url=url,headers=headers,cookies=cookies)
response = requests.get(url=url,headers=headers)
data=response.json()
data1=data.get('result',{})
print(data1)
print(len(data1))
# print(data)
# data1=data.get('data',{}).get('baseInfo',{})
# print(data1.get('portfolioId',{}) == 1751)
# print(response.status_code)
# res=response.text
# print(response.text)
# print('组合17511' in res)
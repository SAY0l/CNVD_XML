import requests
from lxml import etree
from time import sleep
import os
from base import Request_base

session = requests.Session()

session.headers.update(Request_base.Header)
session.cookies.update(Request_base.Cookies) # 复用tcp链接
session.timeout = Request_base.Timeout # 待观察


def deal_page(pageurl):
    response = session.get(pageurl)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        base_urls = html.xpath('//*[@id="patchList"]/table/tbody/tr/td[1]/a/@href')
        for base_url in base_urls:
            deal_one(Request_base.Main_url+base_url)
            sleep(Request_base.Xml_delay)
    elif response.status_code == 521:
        print("cookie wrong, changing clearence")
    else:
        print("page wrong, please check")

def deal_one(base_url):
    response = session.get(base_url)

    if response.status_code == 200 and response.headers['Content-disposition']:
        filename=response.headers['Content-disposition'].split(";")[-1]
        if filename:
            filename = filename.split("=")[1].strip()

        save_xml(response.content,filename)
    else:
        print(f">>>>> {base_url}wrong, skipping...")

def get_all():
    while True:
        response = session.get(Request_base.page_url) #检测
        if "尚未公开" in response.text:
            print(">>>>>> task Done!")
            break
        elif response.status_code == 200:
            print(f">>>>> now dealing page: {Request_base.Page_num}")
            deal_page(Request_base.page_url)
            Request_base.Page_num+=1
            Request_base.page_url = f'https://www.cnvd.org.cn/shareData/list?max={Request_base.Page_data}&offset={((Request_base.Page_num-1)*Request_base.Page_data)}'
            sleep(Request_base.Page_delay)
        else:
            print(">>>>> something wrong! u can't get shareData, may your cookies are expired")
            break
        

def save_xml(content,filename):
    if not os.path.exists(f'./xml_store/{Request_base.Page_num}'):
        os.makedirs(f'./xml_store/{Request_base.Page_num}')

    with open(f'./xml_store/{Request_base.Page_num}/{filename}', 'wb') as file:
            file.write(content)



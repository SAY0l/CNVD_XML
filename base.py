
class Request_base:

    Page_num = 1

    Page_data = 10

    Main_url = 'https://www.cnvd.org.cn'

    page_url = f'https://www.cnvd.org.cn/shareData/list?max={Page_data}&offset={((Page_num-1)*Page_data)}'


    Cookies = {
        '__jsluid_s':'e711cdd284d5d11418ab4a6d29972a53',
        'JSESSIONID':'6B04A8B52D9AC4D1926787383D3CEABB',
        '__jsl_clearance_s':'1702882119.721|0|Knhpyd%2FdCUodKyPi9tgdh6Jf0dc%3D'
    }

    Header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Pragma':'no-cache',
        'Referer':'https://www.cnvd.org.cn/shareData/download/1471',
        'Sec-Ch-Ua':'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'same-origin',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        #'Cookie':'__jsluid_s=e711cdd284d5d11418ab4a6d29972a53; JSESSIONID=7D06908C96861ED6B6B81422D78965DE; __jsl_clearance_s=1702021792.201|0|YIHVfsdfO83pcMbdgigl7k%2FD5FM%3D',
    }

    Timeout = 8
    
    Xml_delay = 3

    Page_delay = 1

    Database_delay = 1

class Task:
    count = 0

    failure_flag = False # 用于停止的标志

    Skip_mode = False
    # False状态表示遇到主键重复错误会停止数据库传输，更新模式常用
    # True状态表示遇到错误使用跳过模式，减少数据丢失，全量爬取时常用

def title():
    print('+--------------------------------------------------------------')
    print('[+]  \033[34m作者:  sayo1                                            \033[0m')
    print('[+]  \033[34m功能:  用于爬取CNVD_xml信息                       \033[0m')
    print('[+]  \033[34m说明:  爬取速度--3s  \033[0m')
    print('[+]  \033[34m说明:  需要先修改自己的cookie  \033[0m')
    print('[+]  \033[34m版本:  V1.0  \033[0m')
    print('+--------------------------------------------------------------')
    print('>>>>>', "start")
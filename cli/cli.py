import sys
sys.path.append(r"..\\cnvd_xml")

import argparse

import xml_crawl
import xml_deal
from time import sleep
from base import title,Request_base,Task

def Gen_cli(information):
    parser = argparse.ArgumentParser(description=information[0],formatter_class=argparse.RawTextHelpFormatter)
    parser.epilog='''
Author: 
    {}  <{}>
Version: 
    {}
Config:
    {}
    '''.format(information[1],information[2],information[3],information[4])

    parser.add_argument('-A', '--all', action='store_true', help='Crawl all CNVD_XML data and be stored in a database (default_mode = `Skip`)')
    parser.add_argument('-U', '--update', action='store_true', help='Update the XML file and update the database (default_mode = `Stop`)')
    parser.add_argument('-c', '--crawl', action='store_true', help='Crawl all XML data only (default_save_path:./xml_store/ )')
    parser.add_argument('-d', '--to_database', action='store_true', help='Store all current XML files in the database')
    parser.add_argument('-s', '--skip_mode', action='store_true', help='We will skip when an error occurs If you set. In default, We will stop when an error occurs')

    args = parser.parse_args()

    Parse_cli(args,parser)

def Parse_cli(args,parser):
    if args.all:
        all_crawl()
    elif args.update:
        get_update()
    elif args.crawl:
        crawl_only()
    elif args.to_database:
        xml_deal_only()
    elif args.skip_mode:
        Task.Skip_mode = True
    else:
        parser.print_help()


# 全爬取，从当前页爬取至最后页，设置Page_num = 1 ，即可全部爬取
def all_crawl():
    title()
    print(">>>>> all_crawling ...")
    Task.Skip_mode = True
    xml_crawl.get_all()
    xml_deal.deal_all_xml()

def get_update():
    title()
    print(">>>>> updating ...")
    Task.Skip_mode = False
    while True:
        print(">>>>> now getting page data...")
        xml_crawl.deal_page(Request_base.page_url) # 需保持默认第一页开始
        print(">>>>> trying update...")
        xml_deal.deal_all_xml()
        if Task.failure_flag:
            print(">>>>> update finished")
            break
        Request_base.Page_num+=1
        Request_base.page_url = f'https://www.cnvd.org.cn/shareData/list?max={Request_base.Page_data}&offset={((Request_base.Page_num-1)*Request_base.Page_data)}'
        print(">>>>> next page...")
        sleep(Request_base.Page_delay)

def crawl_only():
    title()
    xml_crawl.get_all()

def xml_deal_only():
    title()
    xml_deal.deal_all_xml()

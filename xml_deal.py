from lxml import etree
import database
import os
import time
from base import Request_base,Task

def deal_one_file(filename):
    res = []
    xml_tree = etree.parse(filename)
    root = xml_tree.getroot()
    file_len = len(root.xpath("//vulnerabilitys/vulnerability/number/text()"))
    for i in range(1,file_len+1):
        one_res=deal_one_column(root,i)
        res.append(one_res)

    return res

def deal_one_column(root,i):
    one_res = ()

    cnvd_id = root.xpath(f"//vulnerabilitys/vulnerability[{i}]/number/text()")
    vulName = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//title/text()")
    cve_id  = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//cveNumber/text()")
    vulType = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//isEvent/text()")
    hazardLevel = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//serverity/text()")
    vulDesc  = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//description/text()")
    referUrl = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//referenceLink/text()")
    patch = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//formalWay/text()")
    publishTime = root.xpath(f"//vulnerabilitys/vulnerability[{i}]//openTime/text()")

    one_res=(cnvd_id[0],vulName[0],','.join(cve_id),vulType[0],','.join(hazardLevel), ','.join(vulDesc),','.join(referUrl),','.join(patch),publishTime[0])
    return one_res


def xml_to_database_stop_mode(data):
    database.mysql_insert_data(data)
    time.sleep(Request_base.Database_delay)

def xml_to_database_skip_mode(data):
    database.mysql_insert_data_skip(data)
    time.sleep(Request_base.Database_delay)

def deal_all_xml():
    folder_path = './xml_store'

    for root, dirs, files in os.walk(folder_path): #dirs表示文件夹
        files.reverse()
        for file in files:
            file_path = os.path.join(root, file)
            file_path=file_path.replace("\\","/")

            print("now dealing...",file_path)
            data = deal_one_file(file_path)

            if Task.Skip_mode:
                xml_to_database_skip_mode(data)

            elif not Task.Skip_mode:
                xml_to_database_stop_mode(data)
                if Task.failure_flag:
                    break
                # 确保是按时间从近到远的顺序进行处理，用于更新

        if Task.failure_flag:
            break
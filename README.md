# 使用说明
```
usage: main.py [-h] [-A] [-U] [-c] [-d] [-s]

CNVD_XML: Crawl and Store CNVD_XML Data Rapidly

options:
  -h, --help         show this help message and exit
  -A, --all          Crawl all CNVD_XML data and be stored in a database (default_mode = `Skip`)
  -U, --update       Update the XML file and update the database (default_mode = `Stop`)        
  -c, --crawl        Crawl all XML data only (default_save_path:./xml_store/ )
  -d, --to_database  Store all current XML files in the database
  -s, --skip_mode    We will skip when an error occurs If you set. In default, We will stop when an error occurs

Author:
    sayol  <github@sayol.com>
Version:
    1.0
Config:
    >>> Please edit base.py file when u first use <<<
```

# 注意事项
1. cnvd共享数据需登录后访问，需要配置cookie等参数，在base.py中修改。数据库配置在database.py中修改，推荐以cnvd编号作为主键。

2. 最好每次工作后需要更改'__jsl_clearance_s'的值，保证可行性

3. 设置起始爬取页数即可，每次工作后，最好清空xml_store文件夹，保证不会对后续数据处理产生影响

4. 全量爬取时默认为跳过模式。由于官方数据中仍然有少量重复，跳过模式会在产生错误时自动跳过错误数据。

5. 更新爬取时默认为停止模式。当检测到错误时，就停止更新

6. 仅爬取选项会爬取CNVD当前所有的XML数据，是覆盖的写入方式。

7. 仅存储至数据库选项会将当前'./xml_store/'目录下的xml文件写入数据库，可以脱网运行，推荐在隔绝外网的环境中使用

8. skip_mode选项，可以控制当前是否以跳过模式工作。只能配合to_database选项在隔绝外网的环境中。处理大量xml文件时，开启跳过模式，可以规避数据丢失；少量xml文件更新时就可以使用停止模式更新需要内容。

# 未来更新
1. 通过账户密码自动获取cookie

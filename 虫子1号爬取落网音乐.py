#! /usr/bin/env python 
#coding=utf-8

import requests
from os.path import dirname, abspath
import extract
import re
RE_CN = re.compile(ur'[\u4e00-\u9fa5]+')
PREFIX = dirname(abspath(__file__))

with open("%s/down.bat"%PREFIX,"w") as down:
    for i in xrange(1,396):
        for url in (
            'http://www.luoo.net/radio/radio%s/mp3.xml'%i,
            'http://www.luoo.net/radio/radio%s/mp3player.xml'%i
        ):

            r = requests.get(url)
            print url
            if r.status_code == 200:
                for path,name in zip(
                    extract.extract_all('path="','"',r.content),
                    extract.extract_all('title="','"',r.content)
                ):
                    if RE_CN.match(name.decode('utf-8','ignore')):
                        down.write('wget %s -O "%s/%s.mp3"\n'%(path,PREFIX,name.decode('utf-8',"ignore").encode("gb18030","ignore")))
                break


#! /usr/bin/python
# coding:utf-8

import re

with open("bootstraptree_location.tre","r") as infile1:
    for filedata in infile1:
        #print filedata 
        #a=re.findall(r'(:\d+.\d+|E-\d+)', filedata)
        #print a
        #print filedata
        filedata=filedata.strip()
        a=filedata.replace(':' ,' ')
        a=re.split("\s|\,|\)",a)
        #print a
        for string in a:
            if string.isdigit():
                print string,filedata
            else:
                continue

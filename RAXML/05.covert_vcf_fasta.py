#! /usr/bin/python
# coding:utf-8

import re
import random

infile=open("four_fold_final_file.vcf","r")
outfile=open("genotype_with_snps_from_four_fold_vcf.fa","w")
dict={}
name=[]
line=0
for info in infile:
    line+=1
    if line%10000==0:
        print "line:",line
    info=info.rstrip()
    if re.findall("^##",info):
        continue
    if re.findall("^#CHROM.*",info):
        name=re.split("\s+",info)
        continue

    info2=re.split("\s+",info)
    if len(info2[4])>1:
        continue
    for i in range(9,len(info2)):
        ind = name[i]
        base = "N"
        if re.findall("(\d)\/(\d)",info2[i]):
            GT=re.search("(\d)\/(\d)",info2[i])
            light = int(GT.group(1))+int(GT.group(2))
            if light == 0:
                base = info2[3]
            elif light == 2:
                base = info2[4]
            elif light == 1:
                list = [info2[3],info2[4]]
                base=random.choice(list)
        if ind in dict:
            dict[ind]=dict[ind]+base
        else:
            dict[ind]=base

for i in range(9,len(name)):
    ind = name[i]
    outfile.write(">"+ind+"\n"+dict[ind]+"\n")


infile.close()
outfile.close()

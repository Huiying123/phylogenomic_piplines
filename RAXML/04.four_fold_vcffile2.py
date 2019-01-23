#! /usr/bin/python
# coding:utf-8

import re
import string
from itertools import izip

infile1=open("/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/02.RaxMl_second/03.four_fold_position.txt","r")
infile2=open("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/08.final_all_filtered_discard_prot8714_discardhalfmissing.recode.vcf","r")

outfile=open("/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/02.RaxMl_second/four_fold_final_file.vcf","w")
infor=''
L=[]
for info1 in infile1:
    info1=info1.rstrip()
    L_info=re.split("\s+",info1)
    infor=L_info[0]+"_"+L_info[1]
    L.append(infor)
dict=dict(zip(L,range(len(L))))
#print dict

infor2=""
for info2 in infile2:
    info2=info2.rstrip()
    if re.findall(r"^#",info2):
        outfile.write(info2+"\n")
        continue
    L_info2=re.split(r"\s+",info2)
    infor2=L_info2[0]+"_"+L_info2[1]
    #print infor2
    if infor2 in dict:
        information="\t".join(L_info2)
        outfile.write(information+"\n")


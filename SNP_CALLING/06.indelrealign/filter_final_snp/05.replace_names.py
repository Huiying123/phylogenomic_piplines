#! /usr/bin/python
# coding:utf-8

import re
import string

L1=["pade01_21","pade311_9","pade320_18","pade55_8","pade63_7","pdav167_9","pdav221_10","pdav302_11","pdav425_21","pdav56_7","pqioT01_3","pqioT02_2","pqioT02_5","prot083A_4","prot123_19","prot177_18","prot261A_13","prot87_14"]

L2=["pade0121","pade31109","pade32018","pade5508","pade6307","pdav16709","pdav22110","pdav30211","pdav42521","pdav5607","pqioT0103","pqioT0202","pqioT0205","prot083A04","prot12319","prot17718","prot261A13","prot8714"]

dict_L=dict(zip(L1,L2))
#print dict_L

file2=open("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/06.populus_final_all_filtered.vcf","w")
with open ("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/02.populus_final_all_filtered.vcf","r")as file1:
    for strings in file1:
        strings=strings.rstrip()
        if re.findall(r"^#C.*",strings):
            for key,value in dict_L.items():
                strings=strings.replace(key,value)
                
        file2.write(strings+"\n")

file2.close()


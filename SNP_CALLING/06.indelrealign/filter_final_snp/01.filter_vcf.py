#! /user/bin/python
# coding:utf-8

import xlrd
import re
import os
import string
import json

data=xlrd.open_workbook("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/sum_depth.xlsx")
table=data.sheet_by_index(0)
sample_names=table.col_values(0)
average_depth=table.col_values(3)
average_depth.pop(0)
sample_names.pop(0)
sample_names_str=[s.encode("utf-8") for s in sample_names]
dict_name_depth=dict(zip(sample_names_str,average_depth))
#print dict_name_depth
with open("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/02.populus_final_all_filtered.vcf","w") as file:
    with open('/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/poplus.final.snps.vcf','r') as vcf_reader:
        L_mindepth=[]
        L_maxdepth=[]
        while 1:
            leader=vcf_reader.readline()
            
            leader=leader.rstrip()
            if re.findall(r'^##',leader):
                file.write(leader+"\n")
                continue
            
            infor=re.split("\s+",leader)
	  
            
	    if re.findall(r"^#",leader):
                leader_first="\t".join(infor[:])
                #print leader_first
                file.write(leader_first+"\n")
                for i in range(9,len(infor)):
                    meandepth= dict_name_depth[infor[i]]
                    mindepth=int(meandepth/3)
                    maxdepth=meandepth*3
                    #print mindepth
                    if maxdepth> int(maxdepth):
                         maxdepth+=1
                         #print maxdepth
                    L_mindepth.append(mindepth)
                    L_maxdepth.append(maxdepth)
                    # continue
                    # print L_maxdepth
                continue
                   
            if infor[5]=="." or float(infor[5])<20.00 :
                continue
          
    
            #print L_maxdepth
            #print L_mindepth
            L_num=range(9,len(infor))
            #print L_num
            max=dict(zip(L_num,L_maxdepth))
            min=dict(zip(L_num,L_mindepth))
            
            L=[]
            for j in range(9,len(infor)):
                if re.findall(r"\d\/\d\:\d+",infor[j]):
	            iddp=re.search("\d\/\d\:(\d+)",infor[j])
	            iddp=iddp.group(1)
                    #     print iddp,min[j],max[j]
                    
                    if iddp<min[j] or iddp> max[j]:
                        infor[j]=="./."
                #print infor[j]         
          
                if re.findall(r"\.\/\.",infor[j]):
                    L.append(infor[j])
            #print L
            n=len(L)
            #print n
            if n==37:
                continue
    
            contend='\t'.join(infor)
            #print contend
            file.write(contend+"\n")
    

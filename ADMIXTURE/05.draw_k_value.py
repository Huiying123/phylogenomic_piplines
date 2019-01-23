#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import string
import os

def dirlist(path):
    return os.listdir(path)
L_all=dirlist('/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/K_value_files')
L_file=[]
for files in L_all:
    if re.findall(r'value.txt$',files):
        L_file.append(files)
        
L_file_sort=sorted(L_file)
#print L_file
f=open('06.draw_k_value.r','w')
f.write("library('ggplot2')"+'\n')
for file in L_file_sort:
   f.write("a=read.table('/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/K_value_files/"+file+"',header=T)"+'\n')
   f.write("pdf(file='/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/K_value_files/"+file+".pdf')"+'\n')
   f.write("ggplot(a,aes(x=name,y=value,fill=k))+geom_bar(stat=\"identity\")"+'\n')
   f.write("dev.off()"+'\n')

f.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

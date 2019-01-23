#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import string
import os

#获取文件列表
def dirlist(path):
    return os.listdir(path)
L_all=dirlist('/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/PQ_files')
L_files=[]
for files in L_all:
    if re.findall(r'Q$',files):
        L_files.append(files)
L_files_sort=sorted(L_files)
#print L_files

#获取某一文件中一列作为ID
L_name=[]
f2=open('/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/01.populus_36.fam','r')
for strings in f2.readlines():
    strings=strings.rstrip()
    name=re.split(r'\s+',strings)
    L_name.append(name[0])
#print L_name

#获取所需文件中的内容并插入ID
for documents in L_files_sort:
    f=open('/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/PQ_files/'+documents,'r')
    f3=open("/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/03.Admixture/02.without_prot8714/K_value_files/"+documents+'_K_value.txt','w')

    L_line=[]
    L_row=[]
    i=0
    j=0

    for string in f.readlines():
        string=string.rstrip()
        number=re.split(r'\s',string)
        L_line.append(number)
    #print L_line
    #print 'k=',len(number)
    firstline=' '*5+'name'+' '*6+'value'+' '*3+'k'+' '*5+'\n'
    f3.write(firstline)
    L_k=[]
    for i in range(len(number)):
        for j in range(len(L_line)):
            L_row.append(L_line[j][i])
            L_k.append('k='+str(i+1))
    #print L_k
    #print L_row

    ID_firstrow=L_name*len(number)
    a=zip(ID_firstrow,L_row,L_k)
    for m in range(len(a)):
        #print m+1,a[m][0],a[m][1]
        f3.write(str(m+1)+' '+ a[m][0]+' '+a[m][1]+' '+a[m][2]+'\n')

f.close()
f2.close()
f3.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

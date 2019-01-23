#! /usr/bin/python
# coding: utf-8

import re
import string
from os import walk
import os.path

L_all_path=[]
for (dirpath,dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/"):
    for filename in filenames:
        L_all_path.append(os.path.join(dirpath,filename))

#print L_all_path


L_reads_path=[]

for path in L_all_path:
    if re.findall(r"_paired.fastq.gz$",path):
        L_reads_path.append(path)
L_reads_path_sort=sorted(L_reads_path)
#print L_reads_path_sort

left=""
right=""
num=0

for s in range(0,len(L_reads_path_sort),2):
    left=L_reads_path_sort[s]
    right=L_reads_path_sort[s+1]
#    print left, right
    name=re.search(".*([a-z]{4}.*)_R?1_trimmed_paired.fastq.gz", left)
    files_name=name.group(1)
#    print files_name
    print 'bwa mem -t 14 -R \'@RG'+'\t'+'ID:'+ files_name +'\t'+'SM:'+ files_name + '\t'+'LB:'+ files_name +'\'','/media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa',left, right,'2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_'+files_name+'.log | samtools sort --thread 14 -O bam -T','/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/'+ files_name,'-l 3 -o','/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/'+ files_name + '.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_'+files_name+'.log'                                                                                                                                                                                                                                                                                                                                                                                                                  

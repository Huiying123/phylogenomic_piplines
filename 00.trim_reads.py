#! /usr/bin/python
# coding:utf-8

#Get all the files of a directory.

import os
import re
def dirlist(path):
    return os.listdir(path)

L_file=dirlist("/media/uni/data/projects/Populus_phylogenomic/00.raw_data/populus_adenopoda/")

#Get fastq.gz file and sorted in order.

L_fastq_file=[]

for files in L_file:
    if re.findall(r".fastq.gz$",files):
        L_fastq_file.append(files)

L_fastq_file_sort=sorted(L_fastq_file)
#print L_fastq_file_sort


#Get left and right reads in order
    
for num in range(1,len(L_fastq_file_sort),2):
    left_reads=L_fastq_file_sort[num-1]
    right_reads=L_fastq_file_sort[num]
   # print left_reads
   # print right_reads


#Get the reads names

   # file_name=re.search(r"([a-z]{4}[0-9]{2}_[0-9]{2})_R1\.fastq\.gz",left_reads)
   # file_name2=file_name.group(1)
   # print file_name2

    file_name_left=re.search(r"([a-z]{4}[0-9]{1,4}_[0-9]{1,4}_R1)\.fastq\.gz",left_reads)
    file_name_left2=file_name_left.group(1)
   # print file_name_left2

    file_name_right=re.search(r"([a-z]{4}[0-9]{1,4}_[0-9]{1,4}_R2)\.fastq\.gz",right_reads)
    file_name_right2=file_name_right.group(1)
   # print file_name_right2
    
    
    print "java -jar /home/uni/programme/trimmomatic/Trimmomatic-0.36/trimmomatic-0.36.jar PE -threads 5 /media/uni/data/projects/Populus_phylogenomic/00.raw_data/populus_adenopoda/"+left_reads,"/media/uni/data/projects/Populus_phylogenomic/00.raw_data/populus_adenopoda/"+right_reads,"/media/uni/data/projects/Populus_phylogenomic/10.trimmed_reads/populus_adenopoda/"+file_name_left2+"_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/10.trimmed_reads/populus_adenopoda/"+file_name_left2+"_trimmed_unpaired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/10.trimmed_reads/populus_adenopoda/"+file_name_right2+"_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/10.trimmed_reads/populus_adenopoda/"+file_name_right2+"_trimmed_unpaired.fastq.gz ILLUMINACLIP:/home/uni/programme/trimmomatic/Trimmomatic-0.36/adapters/TruSeq3-SE.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:36"

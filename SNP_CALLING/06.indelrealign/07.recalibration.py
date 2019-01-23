#! /usr/bin/python
# coding: utf-8

import re
import os
from os import walk
import os.path

L_all=[]
for (dirpath, dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"):
    for filename in filenames:
        if re.findall(r".bam$",filename):
            L_all.append(os.path.join(dirpath,filename))
#print L_all

for file in L_all:
    name=re.search("([^\/]+).bam$",file)
    name2=name.group(1)
   # print name2
    print  "java -Xmx12g -jar /home/uni/programme/GenomeAnalysisTK-3.6/GenomeAnalysisTK.jar -T BaseRecalibrator -R /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa -I",file,"-knownSites /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/02.generate_vcf_file/poplus.raw.snps.indels.vcf -o /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/03.recalibration/"+name2+"_realign_recal.table --log_to_file /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/03.recalibration/"+name2+"_realign_recal.log"

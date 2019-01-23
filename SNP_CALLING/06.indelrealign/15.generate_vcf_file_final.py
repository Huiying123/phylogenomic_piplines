#! /usr/bin/python
# coding: utf-8

import re
import os
from os import walk
import os.path

L_all=[]
for (dirpath, dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/04.printreads/"):
    for filename in filenames:
        if re.findall(r".bam$",filename):
            L_all.append(os.path.join(dirpath,filename))
#print L_all


print  "java -Xmx12g -jar /home/uni/programme/GenomeAnalysisTK-3.6/GenomeAnalysisTK.jar -nct 14 -R /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa -T UnifiedGenotyper",

for file in L_all:
    print "-I",file,
 
print "-mbq 20 -out_mode EMIT_ALL_SITES -o /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/06.final_snp_file/poplus.final.snps.vcf"

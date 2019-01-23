#! /usr/bin/python
# coding:utf-8

import re

infile=open("/media/huiying/c99c227e-336c-40cb-a944-fab74491f6ae/first_analysis/01.admixture/07.final_snp_filtered_discard_prot8714_discardhalfmissing.recode.vcf","r")
outfile=open("final_snp_with_prot_pdav.vcf","w")

for string in infile:
    string=string.rstrip()
    if re.findall("^##",string):
        outfile.write(string+"\n")
        continue
    string_L=re.split("\s+",string)
    firststring="\t".join(string_L[0:9])
    secondstring="\t".join(string_L[14:19])
    third="\t".join(string_L[21:26])
    forth="\t".join(string_L[29:33])
    
    outfile.write(firststring+"\t"+secondstring+"\t"+third+"\t"+forth+"\n")

infile.close()
outfile.close()

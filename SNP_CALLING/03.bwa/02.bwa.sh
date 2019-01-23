bwa mem -t 14 -R '@RG	ID:ptmd01	SM:ptmd01	LB:ptmd01' /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd01_1_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd01_2_trimmed_paired.fastq.gz 2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_ptmd01.log | samtools sort --thread 14 -O bam -T /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd01 -l 3 -o /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd01.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_ptmd01.log
bwa mem -t 14 -R '@RG	ID:ptmd02	SM:ptmd02	LB:ptmd02' /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd02_1_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd02_2_trimmed_paired.fastq.gz 2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_ptmd02.log | samtools sort --thread 14 -O bam -T /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd02 -l 3 -o /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd02.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_ptmd02.log
bwa mem -t 14 -R '@RG	ID:ptmd03	SM:ptmd03	LB:ptmd03' /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd03_1_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd03_2_trimmed_paired.fastq.gz 2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_ptmd03.log | samtools sort --thread 14 -O bam -T /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd03 -l 3 -o /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd03.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_ptmd03.log
bwa mem -t 14 -R '@RG	ID:ptmd04	SM:ptmd04	LB:ptmd04' /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd04_1_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd04_2_trimmed_paired.fastq.gz 2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_ptmd04.log | samtools sort --thread 14 -O bam -T /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd04 -l 3 -o /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd04.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_ptmd04.log
bwa mem -t 14 -R '@RG	ID:ptmd05	SM:ptmd05	LB:ptmd05' /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd05_1_trimmed_paired.fastq.gz /media/uni/data/projects/Populus_phylogenomic/02.trimmed_reads/populus_tremuloides/ptmd05_2_trimmed_paired.fastq.gz 2>/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align1_ptmd05.log | samtools sort --thread 14 -O bam -T /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd05 -l 3 -o /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/ptmd05.bam - 2>&1|tee /media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/02.logfile/align2_ptmd05.log

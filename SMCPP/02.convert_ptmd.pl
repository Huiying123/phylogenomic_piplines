#! /usr/bin/env perl
use strict;
use warnings;

my $pop="pop_ptmd.list";
my $vcf="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/10.smcpp/all_snp.vcf.gz";
my $dict="/media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.dict";
my $smc="/home/uni/smcpp/bin/smc++";
my $min_len=10000;
my $out_dir="smc_input";

`mkdir $out_dir` if(!-e $out_dir);

my %pop;
open I,"< $pop";
while(<I>){
    chomp;
    my @a=split(/\s+/);
    my ($ind,$pop)=@a;
    $pop{$pop}{$ind}=1;
}
close I;

open O,"> $0.sh";
open I,"< $dict";
while(<I>){
    chomp;
    next unless(/SN:(\S+)\s+LN:(\d+)/);
    my ($chr,$len)=($1,$2);
    next if($len<$min_len);
    foreach my $pop(sort keys %pop){
	`mkdir $out_dir/$pop` if(!-e "$out_dir/$pop");
	my @ind=sort keys %{$pop{$pop}};
	my $ind=join ",",@ind;
	print O "$smc vcf2smc $vcf $out_dir/$pop/$chr.smc.gz $chr $pop:$ind\n";
    }
}
close I;
close O;

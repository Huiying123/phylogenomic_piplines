#! /usr/bin/env perl
use strict;
use warnings;

my $gff="/media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/annotation/Ptrichocarpa_210_v3.0.gene.gff3";
my $fasta_dir="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/07.mpest/out";
my $phb_dir="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/07.mpest/02.treefiles";
my $required_length=150;
my $ind_num=36;

my $out="$0.final.tre";
my $qualified_id="$0.qualified_id";

my %longest_cds;
open I,"< $gff" or die "Cannot open $gff!\n";
my $control=0;
while(<I>){
    chomp;
    next if(/^#/);
    next if(/^\s*$/);
    my @a=split(/\s+/);
    next unless($a[2] eq "mRNA");
    next unless(/ID=([^\;]+);/);
    my $cds_id=$1;
    next unless(/longest=1/);
    $longest_cds{$cds_id}=1;
    $control++;
}
close I;
print STDERR "$gff read complete!\n$control of mRNAs left\n";

my %qualified_cds;
$control=0;
open O1,"> $qualified_id" or die "Cannot open $qualified_id";
foreach my $id(sort keys %longest_cds){
    my $fa="$fasta_dir/$id/seq.fa";
    if(!-e $fa){
	#die "Cannot find $fa\n";
	next;
    }
    my $file=$fa;
    $/=">";
    my $light=0;
    open(I,"< $file");
    while (<I>) {
	chomp;
	my @lines=split("\n",$_);
	next if(@lines==0);
	my $id=shift @lines;# the name of fasta is $id
	my $seq=join "",@lines;# the sequence of fasta is $seq
	$light=(length($seq)>=$required_length)?1:0;
	last;
    }
    close I;
    $/="\n";
    if($light==1){
	$qualified_cds{$id}=1;
	$control++;
	# print O "$id\n";
    }
}
print STDERR "fasta files complete!\n$control of mRNAs left\nthe geneid is recorded in $qualified_id\n";

open O,"> $out" or die "Cannot create $out";
foreach my $id(sort keys %qualified_cds){
    my $phb="$phb_dir/RAxML_bipartitions.$id.phy.phb";
    if(!-e $phb){
	#die "Cannot find $phb\n";
	next;
    }
    my $tree;
    open I,"< $phb";
    while(<I>){
	chomp;
	$tree.=$_;
    }
    my @a=$tree=~/\w+/g;
    my $count=0;
    foreach my $a(@a){
	next unless($a=~/[a-zA-Z]/);
	$count++;
    }
    close I;
    next unless($count==$ind_num);
	print O1 "$id\n";
    print O "$tree\n";
}
close O;
close O1;

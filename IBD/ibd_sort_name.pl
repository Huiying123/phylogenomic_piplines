#! /usr/bin/env perl
use strict;
use warnings;

my $in_file="02.ibd_sta.pl5.sort.txt";
my $out_file="02.ibd_sta.pl5.sort2.txt";

open I,"< $in_file";
my $head=<I>;
my @head=split(/\s+/,$head);
my %hash;
while(<I>){
    chomp;
    my @a=split(/\s+/);
    my $id1=$a[0];
    for(my $i=1;$i<@a;$i++){
	my $id2=$head[$i];
	$hash{$id1}{$id2}=$a[$i];
    }
}
close I;

shift @head;
my @name=sort @head;

open O,"> $out_file";
print O "\t";
print O join "\t",@name;
print O "\n";
foreach my $id1(@name){
    my @line=($id1);
    foreach my $id2(@name){
	push @line,$hash{$id1}{$id2};
    }
    print O join "\t",@line;
    print O "\n";
}
close O;

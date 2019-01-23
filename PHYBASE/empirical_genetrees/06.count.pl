#! /usr/bin/env perl
use strict;
use warnings;

my $tree="clean.tre";
my $out="genetree.count";
my %hash;

open I,"< $tree";
while(<I>){
    chomp;
    my $line=$_;
    $line=~s/:[\d\.]+//g;
    $hash{$line}++;
}
close I;

my %new_hash;
foreach my $line(sort {$hash{$b}<=>$hash{$a}} keys %hash){
    my $new_tree=&sort_tree($line);
    # print "$new_tree\t$hash{$line}\n";
    $new_hash{$new_tree}+=$hash{$line};
    # last;
}

open O,"> $out";
foreach my $line(sort {$new_hash{$b}<=>$new_hash{$a}} keys %new_hash){
    print O "$line\t$new_hash{$line}\n";
}
close O;

sub sort_tree{
    my $tree=shift;
    $tree=~s/;//;
    my @parts=&split_tree($tree);
    foreach my $part(@parts){
        # print "$part\n";
        if($part=~/\(/){
            $part=&sort_tree($part);
        }
    }
    my @new_parts=sort(@parts);
    my $new_tree=join ",",@new_parts;
    $new_tree="(".$new_tree.")";
    return($new_tree);
}

sub split_tree{
    my $tree=shift;
    my @part;

    if($tree=~/^\(/){
        $tree=~s/^\(//;
        $tree=~s/\)$//;
    }

    my @a=split(//,$tree);
    my $left=0;
    my $right=0;
    my $flag=0;
    my $part=0;
    for(my $i=0;$i<@a;$i++){
        if($a[$i]=~/\(/){
            $left++;
        }
        if($a[$i]=~/\)/){
            $right++;
        }
        if($left==$right){
            $flag=1;
        }
        if($flag==1 && $a[$i]=~/,/){
            $part++;
            $flag=0;
            next;
        }
        last if($left<$right);
        $part[$part].=$a[$i];
    }
    return(@part);
}

my ($snp,$geno)=@ARGV;

my $pre="NA";
my $num=0;
open I1,"< $snp";
open I2,"< $geno";
open O1,"> $snp.filter.snp";
open O2,"> $geno.filter.geno";
while(my $l1=<I1>){
    chomp $l1;
    my $l2=<I2>;
    chomp $l2;
    next if($l1=~/scaffold/);
    my @a=split(/\s+/,$l1);
    my $chr=$a[1];
    if($chr ne $pre){
        $num++;
    }
    $chr="chr$num";
    $a[0]=$chr.":".$a[3];
    $a[1]=$chr;
    my $line=join "\t",@a;
    print O1 "$line\n";
    print O2 "$l2\n";
    $pre=$chr;
}
close I1;
close I2;

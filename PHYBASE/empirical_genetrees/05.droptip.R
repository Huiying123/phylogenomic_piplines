library("ape")
a=read.tree(file="07.filter.pl.tre")
b=a
for(i in 1:length(a)){
b[[i]]=drop.tip(a[[i]],c("ptma05","ptma01","ptma04","palb03","palb04","ptma03","palb05","palb02","pade5508","pade6307","pade32018","pade31109","ptri02"))
}
write.tree(b,file="clean.tre")
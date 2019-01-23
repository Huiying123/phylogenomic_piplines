library("ape")
a=read.tree(file="01.filter.pl.tre")
b=a
for(i in 1:length(a)){
b[[i]]=drop.tip(a[[i]],c("pdav16709","pdav22110","pdav42521","ptma05","prot261A13","prot17718","prot12319","ptma02","ptma04","palb03","palb04","ptma03","palb05","palb02","ptmd03","ptmd04","ptmd05","pade5508","pade6307","pade32018","pade31109","ptmd02","pqioT0205","pqioT0202","pbal02","ptri02"))
}
write.tree(b,file="clean.tre")
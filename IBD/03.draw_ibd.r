library('pheatmap')
library(RColorBrewer)
a=read.table('02.ibd_sta.pl5.sort2.txt',header=T)
b=log(a+1)
pdf(file='IBD5.pdf')                                       
pheatmap(b,border_color=NA,cluster_rows=F,cluster_cols=F,color=colorRampPalette(rev(brewer.pal(n = 11, name ="RdBu")))(10))
dev.off()           
                                                                                                                                                                                                                                   

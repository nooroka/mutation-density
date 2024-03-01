
import os
for i in range(23,25,1):
    os.system("bedtools subtract -a comp{}_gene.bed -b comp{}_out_gene_quadr_all_sorted.bed  > comp{}_gene_GC.bed".format(i,i,i))
    os.system("bedtools getfasta -fi hg38_new.fna -bed comp{}_gene_GC.bed > comp{}_gene_GC.fasta".format(i,i))

import sys
#w = open("KEK.txt","w")
for i in range(1,25,1):
    op = open("result13_coord_new_comp{}_gene_GC.fasta.txt".format(i),"r")
    w = open("gccoords_chr_new52_2_gene{}.txt".format(i),"w")
    #w = open("gccoords_promoter_{}".format("_"+str(sysa[3])+"_"+str(sysa[5])),"w")
    for line in op:
        line = line.strip()
        line2 = line.split()
        if float(line2[1]) >= 50:
            w.write(str(line)+"\n")
    w.close()
    op.close()


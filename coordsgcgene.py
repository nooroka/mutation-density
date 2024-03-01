import sys
#w = open("KEK.txt","w")
#for i in range(23,25,1):
op = open("result13_coord_new_all_with_genes.txt","r")
w = open("gccoords_chr_new52_all_with_genes.txt","w")
    #w = open("gccoords_promoter_{}".format("_"+str(sysa[3])+"_"+str(sysa[5])),"w")
for line in op:
        line = line.strip()
        line2 = line.split()
        if float(line2[2]) >= 50:
            w.write(str(line)+"\n")
w.close()
op.close()


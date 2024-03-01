import os
import subprocess
from collections import defaultdict
w = open("densities20.txt","a")
for i in range(1,25,1):  
    os.system("sort -nk2,3   bed_chr_{}.bed > bed_chr_{}_sorted.bed".format(i,i))
    os.system("bedtools intersect -a bed_chr_{}_sorted.bed -b comp{}_out_gene_quadr_all_sorted.bed > resultgene{}.bed".format(i,i,i))
    op2 = open("comp{}_out_gene_quadr_all_sorted.bed".format(i),"r")
    d4 = 0
    for line2 in op2:
        line2 = line2.strip()
        line2 = line2.split()
        sum22 = int(line2[2])-int(line2[1])
        d4+=sum22
    op2.close()
    op = open("gccoords_chr_new52_2_gene{}.txt".format(i),"r")
    w3 = open("gccoords_{}2.bed".format(i),"w")
    for line in op:
        line = line.strip()
        line = line.split()
        print("line "+str(line))
        line77 = int(line[7][1:-1])
        line88 = line[8][:-1]
        print("line77-88 "+str(line77)+"\t"+str(line88))
        w3.write("chr{}".format(i)+"\t"+str(line77)+"\t"+str(line88)+"\n")
    w3.close()
    op.close()
    d5 = subprocess.check_output("wc -l gccoords_chr_new52_2_gene{}.txt".format(i),shell = True)
    os.system("uniq gccoords_{}2.bed > gccoords_{}_un.bed".format(i,i))
    os.system("bedtools intersect  -a bed_chr_{}_sorted.bed -b gccoords_{}_un.bed > intmut{}.bed".format(i,i,i)) 
    d1 = subprocess.check_output('wc -l intmut{}.bed'.format(i),shell = True) #look at the number of mutations
    d2 = subprocess.check_output('wc -l resultgene{}.bed'.format(i), shell = True)
    d6 = subprocess.check_output('wc -l comp{}_out_gene_quadr_all_sorted.bed'.format(i),shell = True)
    d11 = d1.decode().split()[0]
    d22 = d2.decode().split()[0]
    d66 = d6.decode().split()[0]
    d55 = int(d5.decode().split()[0])*52
    print("d11-55-22-4 "+str(d11)+"\t"+str(d55)+"\t"+str(d22)+"\t"+str(d4))
    w.write("chr{}".format(i)+"\t"+"non G4 motif"+"\t"+"average density"+"\t"+str(float(int(d11)/int(d55)))+"\taverage G4 motif/interval length"+"\t"+"52"+"\n")
    w.write("chr{}".format(i)+"\t"+"G4 motif all"+"\t"+"average density"+"\t"+str(float(int(d22)/int(d4)))+"\taverage G4 motif/interval length"+"\t"+str(float(int(d4)/int(d66)))+"\n")
w.close()


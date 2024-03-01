import os
#for file1 in os.listdir("/data/nooroka/grant/punkt3/fasta/"):
for i in range(1,25,1):
    os.system("python windowcoords13.py /data/nooroka/grant/punkt3/comp{}_gene_GC.fasta".format(i))
    

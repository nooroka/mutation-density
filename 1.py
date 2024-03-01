import subprocess
from Bio import SeqIO
import sys
handle = open("../grant/punkt3/comp{}_gene_rev.fasta".format(sys.argv[1])) 
for rec in SeqIO.parse(handle, "fasta"):
    w = open("tmp.fasta","w")
    w.write(">"+str(rec.id)+"\n"+str(rec.seq))
    w.close()
    with open("comp{}_out_gene_rev.txt".format(sys.argv[1]),"a") as outfile:
        outfile.write("\n\n"+str(rec.id)+"\n")
        outfile.flush()
        command = ("qgrs -t 3 -i tmp.fasta")
        subprocess.call(command,stdout = outfile,shell=True)
handle.close()

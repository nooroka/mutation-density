import sys
op = open("comp{}_out_gene_rev.txt".format(sys.argv[1]),"r")
w = open("comp{}_out_gene_quadr_rev.txt".format(sys.argv[1]),"w")
i = 0
for line in op:
    line = line.strip()
    line = line.split()
    if len(line)>0:
        if "-" in line[0]:
           line22 = line[0].split("-")
           if line22[0].isdigit():
               coord1 = line22[1]
               inter = line[0]
        if len(line) == 8 and "ID" not in line:
            
                   a = int(coord1)-int(line[1])+10
                   b = int(coord1)-int(line[4])-10
                   w.write("chr{}:".format(sys.argv[1])+str(inter)+"\t"+"chr{}".format(sys.argv[1])+"\t"+str(a)+"-"+str(b)+"\n")
                   i+=1
        #print(line)
w.close()
op.close()

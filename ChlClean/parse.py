
import re


def parse_sam(fi='', identity=0.8, min_alignment=25, fox=''):
    BH={}
    for line in open(fi):
        values=line.replace("\n","").split("\t")
        matchedbp=sum([int(x.strip('M')) for x in re.findall(r'(\d*M)', values[5])])
        if  matchedbp<min_alignment: continue
        try:
            current_best_hit=int(line.split("NM:i:")[1].split()[0])
            prev_best_hit=int(BH[values[0]].split("NM:i:")[1].split()[0])
            if current_best_hit<prev_best_hit:
                BH[values[0]]=line
        except:
            BH[values[0]]=line
    
    fo = open(fox, 'w')
    for i in BH:
        line = BH[i]
        values=line.replace("\n","").split("\t")
        matchedbp=sum([int(x.strip('M')) for x in re.findall(r'(\d*M)', values[5])])
        # alignlen=float(len(values[9]))
        # read_identity = matchedbp/alignlen
        # print(values[0], values[5], matchedbp, alignlen, read_identity)
        # if read_identity < identity: continue
        if matchedbp < min_alignment: continue
        fo.write(values[0]+"\n")
    
    fo.close()
        


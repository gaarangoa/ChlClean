import sys
from Bio import SeqIO

taxa = {i.split("\t")[0]: i.split('\t')[1] for i in open('99_otu_taxonomy.txt') if 'plast' in i}

for record in SeqIO.parse(open('99_otus.fasta'), "fasta"):
    try:
        txa = taxa[record.id]
        print('>'+record.id +'\n' + str(record.seq))
    except Exception as e:
        pass
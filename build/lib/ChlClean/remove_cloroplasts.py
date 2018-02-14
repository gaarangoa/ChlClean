from parse import parse_sam
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import os

class Cleaner():

    def __init__(self, reference='', paired_1='', paired_2='', output_path="", cores=8):
        self.reference = reference
        self.paired_1 = paired_1
        self.paired_2 = paired_2
        self.output_path = output_path
        self.cores = cores
        self.bowtie_out_file = self.output_path+'/bowtie.gg.sam'
        self.best_hit_file = self.output_path+'/bowtie.gg.sam.bh'

    def call_bowtie(self):
        # assumes bowtie is installed in your machine
        cmd=" ".join([
            'bowtie2', 
            '--fast-local --no-discordant -p ', str(self.cores),
            ' --no-unal --no-hd --no-sq -x ', self.reference, 
            '-1', self.paired_1, 
            '-2', self.paired_2, 
            '-S', self.bowtie_out_file, '>>', self.bowtie_out_file+'.log', '2>&1'
        ])
        os.system(cmd)
        parse_sam(fi = self.bowtie_out_file, fox = self.best_hit_file)
        listf = {i.split()[0]:True for i in open(self.best_hit_file)}
        return listf

    def retrive(self, fi='', listf={}):
        fo = open(fi+".no-chl.fastq", "w")
        for _id,seq,qual in FastqGeneralIterator(open(fi)):
            header = _id.split(' ')[0] 
            read = '@%s\n%s\n+\n%s' %(_id, seq, qual)
            try:
                listf[header]
            except Exception as e:
                fo.write(read+"\n")
    
    def process(self):
        self.call_bowtie()
        listf = self.call_bowtie()
        self.retrive(fi = self.paired_1, listf=listf)
        self.retrive(fi = self.paired_2, listf=listf)


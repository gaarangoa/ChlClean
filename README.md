## Chloroplast removal tool

This is a simple tool that removes all 16s rRNAs-like reads from a paired-end sample. By using Bowtie2 paired end reads are screened against the 16S-rRNAs from the greengenes database and removed from the samples. 

### Requirements
Make sure you have installed the following software (packages):
    Bowtie2
<!-- BioPython -->

### Instalation

    pip install chfilter --user

<!-- python setup.py install -->
<!-- pip install . --upgrade -->

### Usage
    usage: chfiler remove [-h] --paired-1 PAIRED_1 --paired-2 PAIRED_2 --out-dir OUT_DIR

    optional arguments:
    -h, --help           show this help message and exit
    --paired-1 PAIRED_1  paired read 1
    --paired-2 PAIRED_2  paired read 2
    --out-dir OUT_DIR    output directory

#### Usage example
    clremove clear --paired-1 ./test/r1.fq --paired-2 ./test/r2.fq --out-dir ./test/

### output files
The files with filtered chloroplast reads are stored as 
    
    *.no-chl.fastq

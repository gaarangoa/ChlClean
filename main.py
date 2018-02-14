from remove_cloroplasts import Cleaner

reference = "./ggenes/gg_chloroplasts"
paired_1 = 'r1.fq'
paired_2 = 'r2.f1'
output_path = '.'

cleaner = Cleaner(  reference = reference, 
                    paired_1 = paired_1,
                    paired_2 = paired_2,
                    output_path = output_path                    
)


cleaner.call_bowtie()
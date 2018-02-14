from remove_cloroplasts import Cleaner

reference = "./ggenes/gg_chloroplasts"
paired_1 = './test/r1.fq'
paired_2 = './test/r2.fq'
output_path = './test/'

cleaner = Cleaner(  reference = reference, 
                    paired_1 = paired_1,
                    paired_2 = paired_2,
                    output_path = output_path                    
)


cleaner.process()
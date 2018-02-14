import argparse
from remove_cloroplasts import Cleaner
import pkg_resources


def process(args):
    # print('loading reference: ', pkg_resources.resource_filename(__name__, 'ggenes/gg_chloroplasts'))
    cleaner = Cleaner(  reference = pkg_resources.resource_filename(__name__, 'ggenes/gg_chloroplasts'), 
                        paired_1 = args.paired_1,
                        paired_2 = args.paired_2,
                        output_path = args.out_dir                    
    )

    cleaner.process()

def main():
    parser = argparse.ArgumentParser(prog="chfilter", description="welcome to cloroplast clear program")
    subparsers = parser.add_subparsers(help="type the command name for help", title="commands", description="valid subcomands")
    
    # parser for the motif2json utility
    main_parser = subparsers.add_parser('remove', help='This program takes the results from the motif finding and parses that file into a json file')
    main_parser.add_argument('--paired-1', help='paired read 1', required=True)
    main_parser.add_argument('--paired-2', help="paired read 2", required=True)
    main_parser.add_argument('--out-dir', help="output directory", required=True)
    main_parser.set_defaults(func=process)

    args = parser.parse_args()
    args.func(args)






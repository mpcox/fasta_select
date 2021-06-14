#!/usr/bin/env python3

# fasta_select.py
# Murray Cox <murray.p.cox@gmail.com>
# 11 Oct 2018 and 6 December 2018

# extract sequence records from a fasta file by size or name

# load packages
import sys
import argparse
from Bio import SeqIO

# argument parsing
parser = argparse.ArgumentParser(description="extract sequences from a fasta file by size or name")

parser.add_argument('fasta', metavar='fasta_file', type=str, help = "fasta sequence file (must be specified)")
parser.add_argument('-r', '--range', metavar=('lower', 'upper'), type=int, required=False, nargs=2, help="lower and upper bounds of sequence length")

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-s', '--selected', metavar='text_file', type=str, required=False, help="text file of sequences IDs (before first whitespace) to extract, OR")
group.add_argument('-e', '--excluded', metavar='text_file', type=str, required=False, help="text file of sequences IDs (before first whitespace) not to extract")

args = parser.parse_args()

# check range parameters
def test_range():
    if(args.range[0] > args.range[1]):
        raise RuntimeError('lower bound must be less than upper bound\n')

if(args.range is not None):
    try:
        test_range()
    except RuntimeError as err:
        sys.stderr.write('Runtime Error: %s' % str(err))

# read selected or excluded sequence IDs and remove flanking whitespace
if args.selected is not None:
    with open(args.selected) as f:
        IDs = f.readlines()
    IDs = [x.strip() for x in IDs]

if args.excluded is not None:
    with open(args.excluded) as f:
        IDs = f.readlines()
    IDs = [x.strip() for x in IDs]

# process fasta file
for record in SeqIO.parse(args.fasta, "fasta"):
    
    # without selection or exclusion file
    if(args.selected is None and args.excluded is None):
        if(args.range is None):
            print(">", record.id, sep='')
            print(record.seq)
        else:
            if(len(record.seq) >= args.range[0] and len(record.seq) <= args.range[1]):
                print(">", record.id, sep='')
                print(record.seq)
            else:
                continue

    # with selection file
    if(args.selected is not None and record.id in IDs):
        if(args.range is None):
            print(">", record.id, sep='')
            print(record.seq)
        else:
            if(len(record.seq) >= args.range[0] and len(record.seq) <= args.range[1]):
                print(">", record.id, sep='')
                print(record.seq)
            else:
                continue

    # with exclusion file
    if(args.excluded is not None and not record.id in IDs):
        if(args.range is None):
            print(">", record.id, sep='')
            print(record.seq)
        else:
            if(len(record.seq) >= args.range[0] and len(record.seq) <= args.range[1]):
                print(">", record.id, sep='')
                print(record.seq)
            else:
                continue

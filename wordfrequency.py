#!/usr/bin/python

from collections import defaultdict
import json
import optparse
import re
import string
import sys

def increment_count(word_counts_dict, word):
    word_counts_dict[word] += 1

def scan_line(line, word_counts_dict):
    pattern = re.compile('[\W_]+')
    map(lambda word:increment_count(word_counts_dict, filter(str.isalpha, word).lower()), line.split())

def scan_file(file):
    word_counts_dict = defaultdict(int)
    map(lambda(line):scan_line(line, word_counts_dict), file)
    return word_counts_dict

def main():
     p = optparse.OptionParser()
     p.add_option('--infile', '-i')
     p.add_option('--outfile', '-o')
     options, arguments = p.parse_args()
     ifile = sys.stdin
     ofile = sys.stdout
     if options.infile is not None:
         ifile = open(options.infile, 'r')
     
     if options.outfile is not None:
         ofile = open(options.outfile, 'w')
     
     
     word_count_dict = scan_file(ifile)
     #json.dump(word_count_dict, ofile)
     filter(lambda item:item[1]>100,word_count_dict.items()) 

if __name__ == '__main__':
     main()




#!/usr/bin/python3
import sys

if(len(sys.argv) != 2):
	sys.exit('python3 %s <two_strings.txt>')

fh = open(sys.argv[1])
seq1 = fh.readline()
seq1 = seq1.rstrip()
seq2 = fh.readline()
seq2 = seq2.rstrip()

n = 0
for i in range(len(seq1)):
	if(seq1[i] != seq2[i]):
		n += 1

print(n)
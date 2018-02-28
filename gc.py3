#!/usr/bin/python3
import sys

if(len(sys.argv) != 2):
	sys.exit('python3 %s <fasta>' % (sys.argv[0]))

dic = {}

fh = open(sys.argv[1])
for line in fh:
	line = line.rstrip()
	if(line[0] == '>'):
		line = line[1:]
		id = line
		dic[id] = [0, 0]
	else:
		line = line.upper()
		dic[id][0] += line.count('G')
		dic[id][0] += line.count('C')
		dic[id][1] += len(line)

highest = 0.0
highestID = ''
for id in dic.keys():
	content = float(dic[id][0])/float(dic[id][1])*100
	if(highest < content):
		highestID = id
		highest = content

print('%s\n%f' % (highestID, highest))
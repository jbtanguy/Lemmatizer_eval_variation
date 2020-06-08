import io
import sys

infile_path = sys.argv[1]
outFile_path = sys.argv[2]

inFile = io.open(infile_path, mode='r', encoding='utf-8')
outFile = io.open(outFile_path, mode='w', encoding='utf-8')
line = inFile.readline()
while line != '':
	if len(line.split('\t'))>1:
		outFile.write(line.split('\t')[0] + '\n')
	else:
		outFile.write(line)
	line = inFile.readline()
inFile.close()
outFile.close()
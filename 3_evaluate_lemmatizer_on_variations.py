import io
import sys

def get_data(file):
	l = []
	for line in file:
		if line == '\n' or 'lemma' in line or '\'' in line or '\"' in line or '-' in line:
			continue
		else:
			l.append(line.strip().split('\t'))
	return l

def get_variantes(inFile):
	variantes = []
	line = inFile.readline().strip()
	while line != '':
		var = line.split('\t')
		variantes.append((var[0], var[1]))
		line = inFile.readline().strip()
	return variantes



variantes_path = sys.argv[1]
var1_path = sys.argv[2] # V1-pie.txt'
var2_path = sys.argv[3] # V2-pie.txt'

variantes = get_variantes(io.open(variantes_path, mode='r', encoding='utf-8'))
all_var = []
for v in variantes:
	all_var.append(v[0])
	all_var.append(v[1])
var1_corpus = get_data(io.open(var1_path, mode='r', encoding='utf-8'))
var2_corpus = get_data(io.open(var2_path, mode='r', encoding='utf-8'))



res = {}
for var in variantes:
	res[var] = {'same_lemma': [], 'diff_lemma': []}
	for i in range(len(var1_corpus)):
		if var1_corpus[i][0] in var and var2_corpus[i][0] in var: # graphic variation
			if var1_corpus[i][1] ==  var2_corpus[i][1]: #same lemma
				res[var]['same_lemma'].append(i)
			else:
				res[var]['diff_lemma'].append(i)

nb_var, nb_diff, nb_same, nb_same_diff, nb_same_diff_occ, nb_diff_occ, nb_same_occ = (0,0,0,0,0,0,0)
for var, ids in res.items():
	if len(ids['same_lemma']) == 0 and len(ids['diff_lemma']) != 0:
		nb_diff += 1
		nb_diff_occ += len(ids['diff_lemma'])
		nb_var += 1
	if len(ids['same_lemma']) != 0 and len(ids['diff_lemma']) == 0:
		nb_same += 1
		nb_same_occ += len(ids['same_lemma'])
		nb_var += 1
	if len(ids['same_lemma']) != 0 and len(ids['diff_lemma']) != 0:
		nb_same_diff += 1
		nb_same_diff_occ += len(ids['diff_lemma'])
		nb_same_diff_occ += len(ids['same_lemma'])
		nb_var += 1
	
	

print('Nb var in presto testo: ' + str(nb_var))
print('Nb pairs same lemma: ' + str(nb_same))
print('Nb pairs diff lemma: ' + str(nb_diff))
print('Nb pairs same n diff lemma: ' + str(nb_same_diff))
print('Nb occ same lemma: ' + str(nb_same_occ))
print('Nb occ diff lemma: ' + str(nb_diff_occ))
print('Nb occ same n diff lemma: ' + str(nb_same_diff_occ))
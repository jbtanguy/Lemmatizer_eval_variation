import io
import sys

variantes_file = io.open('./variantes_clean_clean.txt', mode='r', encoding='utf-8')
variantes = []
line = variantes_file.readline()
while line != '':
	variantes.append((line.strip().split('\t')[0].lower(), line.strip().split('\t')[1].lower()))
	line = variantes_file.readline()
variantes_file.close()

print(len(variantes))

path_corpus = sys.argv[1]
variantes_founded = []
corpus_var1 = io.open(path_corpus.replace('.txt', '_V1.txt'), mode='w', encoding='utf-8')
corpus_var2 = io.open(path_corpus.replace('.txt', '_V2.txt'), mode='w', encoding='utf-8')
cpt = 0
corpus_file = io.open(path_corpus, mode='r', encoding='utf-8')
corpus = []
line = corpus_file.readline()
while line != '':
	word = line.strip()
	var = [pair for pair in variantes if word.lower() in pair]
	if len(var) >= 1:
		v = var[0]
		corpus_var1.write(v[0] + '\n')
		corpus_var2.write(v[1] + '\n')
		cpt += 1
		variantes_founded.append(v)
	else:
		corpus_var1.write(word + '\n')
		corpus_var2.write(word + '\n')
	line = corpus_file.readline()

corpus_file.close()
corpus_var1.close()
corpus_var2.close()

variantes_founded = set(variantes_founded)
for elm in variantes_founded:
	print(elm)
print('Nombre de variates trouvées : ' + str(cpt))
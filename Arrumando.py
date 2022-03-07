import os, fnmatch

capitulos = []
listOfFiles = os.listdir('.')
pattern = "*.xhtml"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            capitulos.append(entry)

for capitulo in capitulos:
	
	remover = []
	
	with open(capitulo, 'r') as reader:
		linhas = reader.readlines()
		
		paragrafos = linhas[0].split('<p')
		remover = []
		for i, paragrafo in enumerate(paragrafos):
			if 'lightnovelworld[.]com' in paragrafo:
				remover.append(i)
		correção = 0
		for remove in remover:
			del paragrafos[remove - correção]
			correção += 1
		linhas[0] = '<p'.join(paragrafos)
		
	with open('editado/' + capitulo, 'w') as writer:
		for linha in linhas:
			writer.write(linha)
			
	print('Capítulo -' + capitulo + '- concluído!')
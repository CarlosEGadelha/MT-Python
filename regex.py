import re 

#FUNÇÃO QUE LÊ O ARQUIVO DE ENTRADA 
def Regex(nome_arquivo):
	f = open(nome_arquivo,'r')
	conteudo = f.read()
	linhas = re.split("\n",conteudo)
	transicao = []
	palavra = []

	#VERIFICAÇÃO POR LINHA
	for linha in linhas:
		# print(linha)
		if(not linha.startswith("#")):
			if(linha.startswith("A ")): alfabeto = linha[2:]
			if(linha.startswith("Q ")): estados = linha[2:]
			if(linha.startswith("q ")): e_inicial = linha[2:]
			if(linha.startswith("F ")): e_final = linha[2:]
			if(linha.startswith("T ")): transicao.append(linha[2:])
			if(linha.startswith("P ")): palavra.append(linha[2:])

	#RETORNA COMO VARIAVEIS
	return alfabeto, estados, e_inicial, e_final, transicao, palavra

#FUNÇÃO QUE TRANSFORMA AS SAÍDAS DE UM AFD PARA UM ARQUIVO TXT
def Salva(saidas, nome_arquivo):
	str_saida = ""
	for saida in saidas: str_saida = str_saida + str(saida) + "\n"
		
	with open(nome_arquivo, 'w') as f:
		f.write(str_saida)
def CriarAFD(alfabeto, estados, q_inicial, q_final, tabela_transicao, palavras):

	#VERIFICA SE TODAS AS LETRAS DA PALAVRA ESTÃO NO ALFABETO DO AFD
	print("TRANSIÇÃO: ",tabela_transicao, "\n")
	saida =[]
	for palavra in palavras:
		aceitacao = 0
		for letra in palavra:	
			for caracter in alfabeto:
				if caracter == letra: 
					aceitacao += 1
		if (aceitacao < len(palavra)):
			return palavra, "NOT OK: LETRA NÃO PERTENCE AO ALFABETO"
			
		#--ESTADOS---
		estado_atual = q_inicial
		fita = []
		posicao_fita = 1
		contador = 0
		# Q_estados = int(Q_estados)
	
		#---CRIACAO DA FITA---
		fita.insert(0, "-")
		for x in range(len(palavra)):
			fita.insert(x+1,palavra[x])
		fita.insert(len(palavra) + 2, "-")
		# print("\n FITA", q_final, "\n")

		#RODA PELA FITA FAZENDO AS ALTERÇÕES
		# print("TAMANHO PALAVRA", len(palavra))
		try:
			while (estado_atual not in q_final and fita[posicao_fita] != "-"):
				for transicao in tabela_transicao:
					estado_transicao = transicao.split(' ')[0]
					letra_transicao = transicao.split(' ')[1]
					passagem_transicao = transicao.split(' ')[2]
					if estado_atual == estado_transicao: 
						fita[posicao_fita] = letra_transicao
						estado_atual = passagem_transicao
						posicao_fita+=1

			#VERIFICAÇÃO SE ACEITA OU NÃO A PALAVRA
			saida_str = palavra + " ", fita, " OK: aceito"
		except:
				saida_str = palavra + " ", fita, " NÃO ACEITO"
			
		# print("SAIDA", saida_str)
		saida.append(saida_str)
	return saida

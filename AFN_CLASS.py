class AFN:

		#DEFINIÇÃO DE UM AFD PELA QUINTUPLHA
    def __init__(self, alfabeto_entrada, Q_estados, e_inicial, e_final,
                 tabela_transicao, palavras):
        self.alfabeto_entrada = alfabeto_entrada
        self.Q_estados = Q_estados
        self.e_inicial = e_inicial
        self.e_final = e_final
        self.tabela_transicao = tabela_transicao
        self.palavras = palavras

		#CONVERTE DO AFN-E PARA AFN
    def AFNE_convert(self):
        nova_transicao = []
        indice = 0
        for transicao in self.tabela_transicao:
            estado_atual = transicao[0]
            caracter = transicao[2]
            estado_seguinte = transicao[4]

						#VERIFICA QUANDO TEM UM CARACTER DE VAZIO 
            if (caracter == "ê"):
                for estado in self.tabela_transicao:
                    if (estado[4] == estado_atual):
                        estado_novo = estado[0] + " " + estado[
                            2] + " " + estado_seguinte
                        nova_transicao.insert(indice, estado_novo)

            else:
                nova_transicao.insert(indice, transicao)

            indice += 1

        return nova_transicao

		#CONVERVE DE AFN PARA AFD
    def AFN_convert(self):
        vetor_estados = []
        novas_transicoes = []

        for letra in self.alfabeto_entrada:
            for estado in self.Q_estados:

                tabela = []

                for transicao in self.tabela_transicao:
                    if transicao.startswith(estado + " " + letra):
                        tabela += transicao[4]

                if len(tabela) == 1 and tabela[0] != '':
                    novas_transicoes.append(estado + " " + letra + " " +
                                            tabela[0])
                else:
                    if len(tabela) != 0:
                        novo_estado = ''.join(map(str, sorted(tabela)))
                        novas_transicoes.append(estado + " " + letra + " " +
                                                novo_estado)
                        vetor_estados.append(novo_estado)

        tamanho_fita = 0

				#CRIAÇÃO DAS NOVAS TRANSIÇÕES
        while True:

            estado_final = []
            tamanho_fita = len(novas_transicoes)
            armazenamento = []
            estados = []

            armazenamento, estados, armazena_estados = self.atualiza_estado(
                vetor_estados, novas_transicoes)

            novas_transicoes = list(
                dict.fromkeys(novas_transicoes + armazenamento))

            vetor_estados = list(dict.fromkeys(vetor_estados + estados))

            for transicao in novas_transicoes:
                transicao = transicao.split(" ")

                if self.e_final in transicao[0]:
                    if (transicao[0] in estado_final) == False:
                        estado_final.append(transicao[0])

            if tamanho_fita == len(novas_transicoes):
                break

				#DEFINE PARA O AFD NOVAS TRANSIÇÕES, ESTADOS E ESTADO FINAL
        self.tabela_transicao = novas_transicoes
        self.e_final = estado_final
        self.Q_estados = armazena_estados

		#ATUALIZA OS ESTADOS PARA O AFD
    def atualiza_estado(self, Q_estados, transicoes):
        armazena_estados = []

        for x in self.Q_estados:
            armazena_estados.append(x)

        for estado in Q_estados:
            armazena = list(estado)

            for letra in self.alfabeto_entrada:
                tabela = []

                for caracter in armazena:

                    for transicao in transicoes:
                        if transicao.startswith(caracter + " " + letra):
                            tabela += transicao[4:]
                        tabela = list(dict.fromkeys(tabela))

                novo_estado = ''.join(map(str, sorted(tabela)))

                if len(novo_estado) != 0:
                    transicoes.append(estado + " " + letra + " " + novo_estado)

                if (novo_estado in armazena_estados) == False:
                    if len(novo_estado) != 0:
                        armazena_estados.append(novo_estado)

        Q_estados = list(dict.fromkeys(armazena_estados + Q_estados))

        return transicoes, Q_estados, armazena_estados

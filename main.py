import regex as r
import AFD
import AFN_CLASS as AFN_C


def main():
	#RETIRA AS INFORMAÇÕES PARA OA AFN DO REGEX
	alfabeto_entrada,Q_estados,e_inicial,e_final, tabela_transicao,palavras = r.Regex("texto.txt") 

	#CRIA O AFN-E
	AFN = AFN_C.AFN(alfabeto_entrada,Q_estados,e_inicial,e_final, tabela_transicao,palavras)
	
	#CONVERSÃO DO AFN-E PARA AFN
	AFN.tabela_transicao = AFN.AFNE_convert()

	#CONVERSÃO DO AFN PARA AFD
	AFN.AFN_convert()

	#ENVIA AS PALAVRAS PARA O AFD E GERA UM TXT COM O RETORNO DA SAÍDA
	r.Salva(AFD.CriarAFD(AFN.alfabeto_entrada, AFN.Q_estados, AFN.e_inicial, AFN.e_final, AFN.tabela_transicao, AFN.palavras), "saida.txt")

if __name__ == "__main__":
    main()

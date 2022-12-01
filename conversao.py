import re

# ------------------ Função principal de conversão e decisão de qual conversão fazer ------------------

def converte_para_numero(texto):
	# Padroniza texto em minúsculo
	texto = texto.lower()
	# Remove espaços em brancos no início e fim da frase
	texto_sem_espaco = remove_espaco(texto)
	#Remove os acentos no caso de número em extenso eretira espaço em branco para verificação com .isalpha()
	texto_sem_acento = remove_acento(texto_sem_espaco)
	auxiliar = texto.replace(' ','')
	# Verificar se é um texto com 'k, m, g' ou não
	if (auxiliar.isalpha()):
		numero_convertido = converter_frase_para_numero(texto_sem_acento)
	else:
		numero_convertido = converter_frase_com_kmg_para_numero(texto_sem_espaco)

	return numero_convertido

# ------------------ Função comum às duas conversões ------------------

def remove_espaco(texto):
	# Remove espaços no início e fim do texto
	texto_sem_espaco = texto.strip()
	return texto_sem_espaco

	
# ------------------ Funções para conversão de número em extenso para algarismo ------------------

def converter_frase_para_numero(texto_sem_acento):
	texto_em_lista = transforma_em_lista(texto_sem_acento)
	lista_sem_e = remove_e(texto_em_lista)
	lista_com_numeros = converte_em_lista_tipo_numero(lista_sem_e)
	numero_convertido = converte_lista_em_numero(lista_com_numeros)
	return numero_convertido
	
def remove_e(lista):
	# Retorna lista sem os caracteres 'e' para posterior conversão direta
	lista = [value for value in lista if value != 'e']
	return lista

def remove_acento(texto):
	# Subsitui as vogais com acento pelas vogais sem acento
  texto = re.sub('[áàãâ]','a',texto)
  texto = re.sub('[éèê]','e',texto)
  texto = re.sub('[íìî]','i',texto)
  texto = re.sub('[óòôõ]','o',texto)
  texto = re.sub('[úùû]','u',texto)
  return texto

def transforma_em_lista(texto):
	# Divide a string em formato de lista para posterior conversão direta
	texto = texto.split()
	return texto

def converte_em_lista_tipo_numero(lista):
	# Dicionario usado para converter números em extenso para algarismos
	dicionario={
		'um': 1,
		'dois': 2,    
		'tres': 3,
		'quatro': 4,
		'cinco': 5,
		'seis': 6,
		'sete': 7,
		'oito': 8,
		'nove': 9,
		'dez': 10,
		'onze': 11,
		'doze': 12,
		'treze': 13,
		'catorze': 14,
		'quinze': 15,
		'dezesseis': 16,
		'dezessete': 17,
		'dezoito': 18, 
		'dezenove': 19,
		'vinte': 20,
		'trinta': 30,
		'quarenta': 40,
		'cinquenta': 50,
		'sessenta': 60,
		'setenta': 70,
		'oitenta': 80,
		'noventa': 90,
		'cem': 100,
		'cento': 100,
		'duzentos': 200,
	  'trezentos': 300,
	  'quatrocentos': 400,
	  'quinhentos': 500,
	  'seiscentos': 600,
	  'setecentos': 700,
	  'oitocentos': 800,
	  'novecentos': 900,
		'mil': 1000,
		'milhao': 1000000,
	  'milhoes': 1000000,
		'bilhao': 1000000000,
	  'bilhoes': 1000000000,
	}
	
	# Realiza conversão direta saindo da chave (número em extenso) para o valor (algarismo)
	lista_numero = [dicionario[item] for item in lista if item in dicionario.keys()]
	return lista_numero


def converte_lista_em_numero(lista_convertida):  
	unidade_de_medida_numero = [1000, 1000000, 1000000000]
	
	auxiliar = 0
	numero_convertido = 0
	# Cria-se uma lista auxiliar pois as operações são realizadas com base na deleção de números e por isso precisa-se de duas listas iguais: uma pra percorrer e outra para operar
	lista_auxiliar = lista_convertida.copy()

	# Percorre a lista com os valores em formato de numero (Exemplo: [1000, 900, 90, 8])
	for item in lista_convertida:
		if item in unidade_de_medida_numero:

			# Caso o primeiro item já seja uma unidade de medida, acresce-se o número 1 no início da lista
			if lista_auxiliar.index(item) == 0:
				lista_auxiliar.insert(0, 1)

			#Ao achar um index cujo valor é unidade de medida, soma-se todos os valores de 0 até esse valor (ou seja até index-1) e multiplica-se pela unidade de medida correspondente 
			auxiliar=sum(lista_auxiliar[:lista_auxiliar.index(item)])*item

			# Esse valor é acrescido ao valor do numero_convertido que será exibido no final
			numero_convertido+=auxiliar

			# Deleta-se essa sublista da operação anterior para sempre que a operação seja feita não sejam utilizados números que já foram operados antes
			del lista_auxiliar[:lista_auxiliar.index(item)+1]

	# Se ao percorrer a lista no final ainda existam itens sem deletar significa que o último elemento da lista não foi uma unidade de medida, então basta acrescer à variável de numero_convertido o resto da soma da lista
	if len(lista_convertida) > 0:
		numero_convertido += sum(lista_auxiliar)
			
	return numero_convertido

# Funções para conversão de número com 'k, m, g' para algarismo

def converter_frase_com_kmg_para_numero(texto_sem_espaco):
	texto_sem_virgula = remove_virgula(texto_sem_espaco)
	texto_em_lista = transforma_em_lista_kmg(texto_sem_virgula)
	numero_convertido = converte_lista_kmg_em_numero(texto_em_lista)
	return numero_convertido

def remove_virgula(texto):
	# Substitui a ',' substituindo por '.'
	if (',' in texto):
		texto_sem_virgula = texto.replace(',','.')
	else:
		texto_sem_virgula = texto
	
	return texto_sem_virgula

def transforma_em_lista_kmg(texto):
	texto_em_lista = []
	# Verifica se existe unidade de medida no texto, caso haja remove e adiciona depois já como número
	if ('k' in texto):
		auxiliar = texto.replace('k','')
		texto_em_lista.append(auxiliar)
		texto_em_lista.append(1000)
	elif ('m' in texto):
		auxiliar = texto.replace('m','')
		texto_em_lista.append(auxiliar)
		texto_em_lista.append(1000000)
	elif ('g' in texto):
		auxiliar = texto.replace('g','')
		texto_em_lista.append(auxiliar)
		texto_em_lista.append(1000000000)
	
	return texto_em_lista

def converte_lista_kmg_em_numero(lista_convertida):
	# Multiplica o número e a unidade de medida correspondente
	numero_convertido = float(lista_convertida[0])*lista_convertida[-1]
	return int(numero_convertido)
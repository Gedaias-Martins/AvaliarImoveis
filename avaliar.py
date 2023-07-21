casa = int
apart = int
quarto = int
garage = int
tImovel = int

rj = 5.102 #Valor do metro quadrado no Rio de Janeiro com excessão da Zona Sul

print("Código Avaliador de Imóveis")
print("***INFORME O ENDEREÇO DO IMÓVEL***")
Estado=(input ("ESTADO: "))
Municipio=(input ("MUNICIPIO: "))
Bairro=(input("BAIRRO: "))
tImovel=(input("TIPO DO IMÓVEL: "))
lFrente=int(input("INFORME A LARGURA DA FRENTE: "))
lFundos=int(input("INFORME A LARGURA DE FUNDOS: "))
comp=int(input("INFORME O COMPRIMENTO: "))

print("A LOCALIZAÇÃO DO IMÓVEL: ")
print( "***LOCALIZAÇÃO*** ", Estado, Municipio, Bairro)
print("O TIPO DE IMÓVEL: ", tImovel)
print("MEDIDAS DO IMÓVEL: ", (lFrente + lFundos*comp))
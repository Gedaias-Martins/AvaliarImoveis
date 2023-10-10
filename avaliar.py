casa = int
apart = int
quarto = int
garage = int
tImovel = float

#PREÇO DE IMÓVEIS EM BELFORD ROXO (METRO QUADRADO)

Albuquerque = 225.000
AldeiadaFelicidade = 180.000
AreiaBranca = 130.000
AndradeAraújo = 150.000
Apolo11 = 150.000
Benfica = 250.000
BoaEsperança = 180.000
Boasorte = 120.000
Bacia = 85.000
Boaventura = 85.000
Buriti = 290.000
BairrodasGraças = 150.000
BairrodasLuzes = 90.000
BairrodasOrquídeas = 140.000
BairrodoOuteiro = 150.000
BairrodoVasco = 130.000
BairroDoisIrmãos = 150.000
BairroHinterlândia = 150.000
BairroModelo = 150.000
BairroNossaSenhoradasGraças = 150.000
BarroVermelho = 300.000
BomPastor = 200.000
BuracodaOnça = 85.000
Centro = 60.000
DoisIrmãos = 170.000
EstorilCarioca = 240.000
Foice = 125.000
General = 219.990
GogódaEma = 85.000 
Guaraciaba = 70.000
Heliópolis = 50.000
Itaipu = 450.000
JardimAmapá = 180.000
JardimAmérica = 150.000
JardimAnápolis = 120.000
JardimBrasil = 120.000
JardimCristina = 70.000
JardimdasAcácias = 300.000
JardimdasEstrelas = 120.000
JardimDimasFilho = 449.020 
JardimdoIpê = 35.000
JardimdosPinheiros = 220.000
JardimGláucia = 150.000
JardimIdealI = 125.000
JardimIdealII = 125.000
JardimLisboa = 120.000
JardimMarajó = 120.000
JardimMarquêsdoPombal = 80.000
JardimPanorama = 120.000
JardimPatrícia = 200.000
JardimPiedade = 170.000
JardimPortugal = 200.000
JardimRedentor = 70.000
JardimRoseiral = 110.000
JardimSantaMarta = 290.000
JardimSãoFranciscodeAssis = 200.000
JardimSilvana = 14.000
JardimTonalegre = 170.000
JardimXavantes = 220.000
JosédaPlanície = 70.000
LoteXV = 85.000
MariaAmália = 235.000
Machado = 380.000
MeuCantinho = 70.000
NovaAurora = 130.000
#Segunda parte de Cadastro de imóveis em Belford Roxo 
Nova Piam
Nossa Senhora do Carmo
Parque Alvorada
Parque Americano
Parque Amorim
Parque Boa-Sorte
Parque das Fontes
Parque dos Ferreiras
Parque Aida
Parque Esperança
Parque Floresta
Parque Fluminense
Parque Itambé
Parque Jordão
Parque Jupirangai
Parque Maringá
Parque Nossa Senhora Aparecida
Parque Nossa Senhora da Paz
Parque Ouvidor
Parque Real
Parque das Flores
Parque Santa
Parque Santa Rita
Parque São Bento
Parque São José
Parque Pica Pau
Parque São Vicente
Parque Suécia
Parque Umari
Parque União
Parque Veneza
Piam (Vila Medeiros)
Primus
Ponto 5
Ponto 2
Prata
Recantus (ex Babi)
Ribaslândia
Shangri-la
Sicelândia
Santa Tereza
São Bernardo
São Francisco de Assis
São Geraldo
São Jorge
São Leopoldo
São Lucas
Santa Amélia
Santa Cecília
Santa Helena
Santa Maria
Santa Mônica
Santo Antônio da Prata
Santo Reis
Sargento Roncalli
Sítio do Livramento
Sítio Retiro Feliz
Tamoios
Três Setas
Vale das Mangueiras
Vale do Ipê
Valparaíso
Vergél dos Félix
Vila Palmares
Vila Pauline
Vila Rica
Vila Sagres
Vila Santa Mercedes
Vila Santa Rita
Vila Santa Teresa
Vila Santo Antônio
Vila Santo Antônio da Prata
Vila São Sebastião
Vila São Sebastião de Nova Aurora
Vila Seabra
Vila Verde
Vila Vitório
Vilage da Emancipação
Vilar Novo
Wona
Parque colonial
Parque amorim

rj = 5.102 #Valor do metro quadrado no Rio de Janeiro com excessão da Zona Sul
broxo=int(input(""))

print("Código Avaliador de Imóveis")
print("***INFORME O ENDEREÇO DO IMÓVEL***")
Estado=(input ("ESTADO: "))
Municipio=(input ("MUNICIPIO: "))
Bairro=(input("BAIRRO: "))
tImovel=(input("TIPO DO IMÓVEL: "))
lFrente=int(input("INFORME A LARGURA DA FRENTE: "))
lFundos=float(input("INFORME A LARGURA DE FUNDOS: "))
comp=float(input("INFORME O COMPRIMENTO: "))

print("A LOCALIZAÇÃO DO IMÓVEL: ")
print( "***LOCALIZAÇÃO*** ", Estado, Municipio, Bairro)
print("O TIPO DE IMÓVEL: ", tImovel)

print("***MEDIDAS DO IMÓVEL:*** ")
print("SEU IMÓVEL MÉDI:",lFrente + lFundos*comp,"M²")

print("***VALOR DO IMÓVEL:***")
print(lFrente + lFundos*comp*rj) 
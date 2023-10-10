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
NovaPiam = 300.000
NossaSenhoradoCarmo = 200.000
ParqueAlvorada = 79.799
ParqueAmorim = 125.000
ParqueBoaSorte = 358.000
ParquedasFontes = 185.000
ParquedosFerreiras = 160.000
ParqueAida = 70.000
ParqueEsperança = 165.000
ParqueFloresta = 85.000
ParqueFluminense = 160.000
ParqueItambé = 70.000
ParqueJordão = 70.000
ParqueJupirangai = 125.000
ParqueMaringá = 125.000
ParqueNossaSenhoraAparecida = 70.000
ParqueNossaSenhoradaPaz = 70.000 
ParqueOuvidor = 70.000
ParqueReal = 134.900
ParquedasFlores = 165.000
ParqueSanta = 164.200
ParqueSantaRita = 70.000
ParqueSãoBento = 320.000 
ParqueSãoJosé = 125.000
ParquePicaPau = 85.000
ParqueSãoVicente = 320.000
ParqueSuécia = 29.999
ParqueUmari = 165.000 
ParqueUnião = 70.000
ParqueVeneza = 80.000
Piam = 94.967
Primus = 165.000
Ponto5 = 95.000
Ponto2 = 160.000
Prata = 85.000
Recantus = 180.000
Ribaslândia = 85.000
Shangrila = 250.000
Sicelândia = 65.000
SantaTereza = 125.000
SãoBernardo = 79.840
SãoFranciscodeAssis = 145.000
SãoGeraldo = 70.000
SãoJorge = 130.000
SãoLeopoldo = 70.000
SãoLucas = 85.000 
SantaAmélia = 123.000
SantaCecília = 160.000
SantaHelena = 160.000
SantaMaria = 120.000
SantaMônica = 68.620
SantoAntôniodaPrata = 150.000
SantoReis = 198.000
SargentoRoncalli = 107.500
SítiodoLivramento = 85.000
SítioRetiroFeliz =  75.798,95
Tamoios = 159.000
TrêsSetas = 70.000
ValedasMangueiras = 70.000
ValedoIpê = 89.900
Valparaíso = 60.000
VergéldosFélix = 192.000
VilaPalmares = 70.000
VilaPauline = 195.000
VilaRica = 70.000
VilaSagres = 310.000
VilaSantaMercedes = 165.000
VilaSantaRita = 250.000
VilaSantaTeresa = 200.000
VilaSantoAntônio = 270.000
VilaSantoAntôniodaPrata = 249.641
VilaSãoSebastião = 165.000
VilaSãoSebastiãodeNovaAurora = 180.000
VilaSeabra = 70.000 
VilaVerde = 170.000
VilaVitório = 94.637
VilagedaEmancipação = 192.000
VilarNovo = 250.000
Wona = 400.000
Parquecolonial = 120.000
Parqueamorim = 125.000

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
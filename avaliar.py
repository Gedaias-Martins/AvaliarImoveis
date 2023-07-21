casa = int
apart = int
quarto = int
garage = int
tImovel = float

#PREÇO DE IMÓVEIS EM BELFORD ROXO (METRO QUADRADO)

Albuquerque
Aldeia da Felicidade
Areia Branca
Andrade Araújo
Apolo 11
Benfica
Boa Esperança
Boassorte
Bacia
Boaventura
Buriti
Bairro das Graças
Bairro das Luzes
Bairro das Orquídeas
Bairro do Outeiro
Bairro do Vasco
Bairro Dois Irmãos
Bairro Hinterlândia
Bairro Modelo
Bairro Nossa Senhora das Graças
Barro Vermelho
Bom Pastor
Buraco da Onça
Centro
Dois Irmãos
Estoril Carioca
Foice
General
Gogó da Ema
Guaraciaba
Heliópolis
Itaipu
Jardim Amapá
Jardim América
Jardim Anápolis
Jardim Brasil
Jardim Cristina
Jardim das Acácias
Jardim das Estrelas
Jardim Dimas Filho
Jardim do Ipê
Jardim dos Pinheiros
Jardim Gláucia
Jardim Ideal I
Jardim Ideal II
Jardim Lisboa
Jardim Marajó
Jardim Marquês do Pombal
Jardim Panorama
Jardim Patrícia
Jardim Piedade
Jardim Portugal
Jardim Redentor
Jardim Roseiral
Jardim Santa Marta
Jardim São Francisco de Assis
Jardim Silvana
Jardim Tonalegre
Jardim Xavantes
José da Planície
Lote XV
Maria Amália
Machado
Meu Cantinho
nAurora = 1.764,7
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
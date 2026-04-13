#Buscando uma palavra específica
nome = str(input('Digite um nome:')).strip().upper()
print('SILVA' in nome)

#Versão 2
nome = str(input('Digite um nome:')).strip()
print('SILVA' in nome.upper())
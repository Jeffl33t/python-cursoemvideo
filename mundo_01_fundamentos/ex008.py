#Mostrar todas as unidades de distância
m = float(input('Insira distância em metros:'))

km = m / 1000
hm = m /100
dam = m /10
dm = m * 10
cm = m * 100
mm = m * 1000

print('Em {}m existem: \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, km, hm, dam, dm, cm, mm))

#Versão 2
m = float(input('Insira distância em metros:'))

print('Em {}m existem: \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, m/1000, m/100, m/10, m*10, m*100, m*1000))
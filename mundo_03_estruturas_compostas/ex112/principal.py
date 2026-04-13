from mundo_03_estruturas_compostas.ex112.utilidadesCev import dados
from mundo_03_estruturas_compostas.ex112.utilidadesCev import moeda


preco = dados.leia_dinheiro('Digite o valor: R$')
moeda.resumo(preco, 35, 22)
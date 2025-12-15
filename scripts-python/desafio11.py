altura = float(input('Digite a altura de uma parede em metros: '))
largura = float(input('Digite a largura de uma parede em metros: '))
area = altura * largura
print('A área da parede é {:.2f} metros quadrados.'.format(area))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta, sabendo que cada litro pinta 2 metros quadrados.'.format(area/2)) 
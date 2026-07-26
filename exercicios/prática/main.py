from carro import Carro
from moto import Moto

carro1 = Carro('Toyota', 'Corolla', 4)
carro2 = Carro('Volkswagen', 'Gol', 2)
carro3 = Carro('Fiat', 'Argo', 3)

moto1 = Moto('Honda', 'CG 160', 'Street')
moto2 = Moto('Yamaha', 'FZ25 Fazer', 'Naked')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')

carro1.ligar()
moto3.ligar()

print(carro1)
print(carro2)
print(f'{carro3}\n')
print(moto1)
print(moto2)
print(moto3)

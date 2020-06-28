# class Computador:
#     def __init__(self):
#         self.marca = 'Asus'
#         self.memoria_ram = '8gb'
#         self.placa_video = 'Nvidia'
# 
# computador1 = Computador()
# print(computador1.marca)
# computador2 = Computador()
# computador3 = Computador()

class Computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
    def Ligar(self):
        print('Ligado!')
    def Desligar(self):
        print('Desligando!')
    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_video)

computador1 = Computador('Asus', '8gb', 'Nvidia')
computador2 = Computador('Dell', '10gb', 'Geforce')
computador3 = Computador('Acer', '16gb', 'ATM')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoes()

# print(computador1.marca, computador1.memoria_ram, computador1.placa_video)
# print(computador2.marca, computador2.memoria_ram, computador2.placa_video)
# print(computador3.marca, computador3.memoria_ram, computador3.placa_video)

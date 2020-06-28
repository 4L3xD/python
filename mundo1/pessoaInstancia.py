from pessoa import Pessoa

pessoa1 = Pessoa('Iracema', 54)
pessoa2 = Pessoa('Joana', 27)

pessoa1.comer('maçã')
pessoa1.falar('POO')
pessoa1.parar_comer()
pessoa1.falar('POO')
pessoa1.comer('maçã')
print(pessoa1.ano_atual)
print(pessoa1.get_ano_nascimento())
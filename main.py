from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('111.222.333-44', nome='Alfredo', idade=22)

print(a.getCPF())
print(a.getNome())
print(a.getIdade())
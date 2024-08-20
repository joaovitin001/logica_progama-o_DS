print("Hellow word") 

nome = 'joao'
idade = 16
peso = 70
altura = 1.70
instrutor = True


# FIXME:visualizando os tipos de dados
print (type(nome))
print(type(idade))
print(type(peso))
print(type(altura))
print(type(instrutor))

# FIXME:entrada de dados

sobrenome = input('Digite o seu sobrenome: ')

print (nome, sobrenome)
print (type(sobrenome))

#convertendo o valor do input

idade = input('Digite a sua idade: ')
print(type(idade))
idade = (int(idade))

ano = int(input('Em qual ano estamos: '))
print(type(ano))

if ano > 2024:
    pass
print ('dentro do if')
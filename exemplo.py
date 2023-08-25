#cadastro de cliente
#codigo do cliete / ome do cliente

cadastro = {123: 'joao', 
            534: 'paulo', 
            897: 'maria'}
print(cadastro)
print(cadastro[534])

#alterar item 
cadastro[534] = 'pedro crispim'
print(cadastro)

#inserir um item
cadastro[132] = 'joelinton'
print(cadastro)

#remover um item
cadastro.pop(897)
print(cadastro)


'''
#busca de uma chave especifica
codigo = int(input('codigo: '))
if 132 in cadastro:
    print(f'cliente cadastrado {cadastro[codigo]}')
else:
   print('cliente nao cadastrado')
'''

#percorrer chaves do dicionario 
for codigo in cadastro.keys():
    print(codigo)

#percorrer valores do dicionario
for nome in cadastro.values():
    print(nome)

#percorrer itens do dicionario (chave e valor)
for codigo, nome in cadastro.items():
    print(codigo, nome)

'''
#preencher dicionario com inputs 
dados_cliente = {}
while len(dados_cliente) < 3:
    codigo = int(input("digite o codigo do cliente: "))
    nome = input("digite o nome o cliente: ")
    if codigo not in dados_cliente:
        dados_cliente[codigo] = nome
    else:
        print('codigo ja cadastrado. insira novamente.')
print(dados_cliente)
'''

#dicionarios armazenando listas
#cadastro de alunos (RM / lista de notas)
alunos = {1234: [9, 7, 8],
          4565: [6, 7, 5],
          2233: [8, 10, 9]}
print(alunos[1234][0])
alunos[1234][0] = 10
alunos[1234].append(6)
print(alunos)

lista = [alunos, cadastro]
print(lista)
lista[0][1234][0] = 5
print(lista)

alunos = {123: {'nome': 'paulo', 'idade': 30},
          456: {'nome': 'maria', 'idade': 25}}

print(alunos[123]['idade'])
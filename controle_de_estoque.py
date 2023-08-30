# Criando arrays para armazenar os prodrutos
camisas_de_clubes = [('América-MG', 20), ('Athletico', 25), ('Atlético-MG', 35), ('Bahia', 15), ('Botafogo', 50), ('Bragantino', 65), ('Corinthians', 55), ('Flamengo', 65), ('Fluminense', 47), ('Grêmio', 38), ('Internacional', 63), ('Palmeiras', 38), ('Santos', 61), ('São Paulo', 90), ('Vasco', 80)]

# Mostrando as camisas de clubes disponíveis
def listar_estoque():
  print('Camisas de clubes disponíveis:')
  for clubes, _ in camisas_de_clubes:
    print(clubes)

# Quantidade de camisas por clubes
def quantidade_de_camisas():
  print('Quantidade Disponível por cada Clube:')
  for camisa, quantidade in camisas_de_clubes:
    print(f'A camisa do time: {camisa}, possuí: {quantidade} unidade(s)')

# Adicionar mais camisas
def adicionar_camisa():
  nova_camisa = input('Você gostaria adicionar camisas de qual Clube?: ')
  camisas_de_clubes.append(nova_camisa)
  print('Parabéns, nova camisa adicionada!')


# Substituir camisas
def substituir_camisa():
  camisa_antiga = input('Qual camisa você quer substituir? ')
  if camisa_antiga in camisas_de_clubes:
    index = camisas_de_clubes.index(camisa_antiga)
    nova_camisa = input('Digite o nome do Clube da Nova Camisa')
    camisas_de_clubes[index] = nova_camisa
    print(f'A camisa {camisa_antiga} foi substituída por {nova_camisa}.')
  else:
    print('Camisa não encontrada!!!')


# Opção de Menu
while True:
    print('1 - Mostrar Camisas em Estoque')
    print('2 - Quantidade de Camisa por Clube')
    print('3 - Adicionar mais produtos')
    print('4 - Substituir produtos')

    menu = input('O que deseja acessar no momento: ')
    if menu == '1':
      listar_estoque ()
    elif menu == '2':
      quantidade_de_camisas ()
    elif menu == '3':
      adicionar_camisa ()
    elif menu == '4':
      substituir_camisa ()
      break
    else:
      print('Não existe essa opção!')

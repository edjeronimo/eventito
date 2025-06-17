def criarAquivo():
  import os.path
  if not os.path.exists('eventos.txt'):
    with open("eventos.txt", "w") as arquivo:
      arquivo.write("EVENTOS: \n")

def atualizarArquivo(nome, descricao, data, hora, local, valoringresso, atracoes):
    with open("eventos.txt", "a") as arquivo:
      arquivo.write("------------------------------ \n")
      arquivo.write(f"Nome: {nome} \nDescrição: {descricao} \nData: {data} \nHora: {hora} \nLocal: {local} \nValor do Ingresso: {valoringresso} \nAtrações: {atracoes} \n")

def menuEvento():
  print("-"*30)
  print("Bem vindo ao EVENTITO, seu gerenciador de eventos favorito!")
  print(" ")
  print("""
  O que deseja?
  1 - Criar evento
  2 - Visualizar eventos
  3 - Excluir evento
  4 - Sair
  """)
  try:
    opcao = int(input(" "))
    if opcao == 1:
      print(" ")
      print("Carregando...")
      print(" ")
      criarEvento()
    elif opcao == 2:
      print(" ")
      print("Carregando...")
      print(" ")
      visualizarEvento()
    elif opcao == 3:
      print(" ")
      print("Carregando...")
      print(" ")
      excluirEvento()
    elif opcao == 4:
      print(" ")
      print("Obrigado por usar o EVENTITO!")
      print(" ")
      exit()
    else:
      print(" ")
      print("Entrada inválida, tente novamente")
      menuEvento()
  except ValueError:
    print(" ")
    print("Entrada inválida, tente novamente")
    menuEvento()

def criarEvento():
  eventosLista  = []
  eventosLista.clear()

  nomeEvento = input("Insira o nome do evento: ").upper()
  descricaoEvento = input("Insira a descrição do evento: ").upper()
  dataEvento = input("Insira a data do evento no formato DD/MM/AAAA: ")
  horaEvento = input("Insira a hora do evento no formato HH:MM: ")
  localEvento = input("Insira o local do evento: ").upper()
  valorIngresso = input("Insira o valor do ingresso: ")
  while True:
    atracao = input("Insira uma atração por vez ou 'fim' para finalizar: ").upper()
    if atracao == "FIM":
      break
    else:
      eventosLista.append(atracao)
      continue

  criarAquivo()
  atualizarArquivo(nomeEvento, descricaoEvento, dataEvento, horaEvento, localEvento, valorIngresso, eventosLista)

  print("-"*30)
  print("Evento criado com sucesso!")
  print(" ")

  return menuEvento()

def visualizarEvento():
  import os.path
  if not os.path.exists('eventos.txt'):
    print(" ")
    print("Não há eventos cadastrados!")
    print(" ")
    print("Voltando ao menu principal...")
    print(" ")
    menuEvento()
  if os.path.exists('eventos.txt'):
    todos = open("eventos.txt", "r")
    print(todos.read())
    todos.close()
    print(" ")
    print("Voltando ao menu principal...")
    return menuEvento()

def excluirEvento():
  import os.path
  if not os.path.exists('eventos.txt'):
    print(" ")
    print("Não há eventos cadastrados!")
    print(" ")
    print("Voltando ao menu principal...")
    print(" ")
    menuEvento()
  if os.path.exists('eventos.txt'):
    print("""
    Tem certeza que deseja excluir o arquivo?
    1 - Sim
    2 - Não
    """)
    try:
      opcao = int(input(" "))
      if opcao == 1:
        print(" ")
        validacao = input("Digite 'apagar' para confirmar a exclusão: ").upper()
        if validacao == "APAGAR":
          os.remove("eventos.txt")
          print(" ")
          print("Arquivo excluído com sucesso!")
          menuEvento()
        else:
          print(" ")
          print("Voltando ao menu principal...")
          menuEvento()
      elif opcao == 2:
        menuEvento()
      else:
        print(" ")
        print("Entrada inválida, tente novamente")
        excluirEvento()
    except ValueError:
      print(" ")
      print("Entrada inválida, tente novamente")
      excluirEvento()

menuEvento()

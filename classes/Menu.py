import os
import csv

class Menu:
   
  def opcoes(self):
    """Lê as opções do menu e força o usuário a escolher um número válido"""
    with open("texts/menu.txt", "r", encoding="utf-8") as m:
      menuopcoes = [linha.strip() for linha in m if linha.strip()]

    escolha = 0
    while escolha < 1 or escolha > len(menuopcoes):
      os.system('cls' if os.name == 'nt' else 'clear')
      for i, menuopcao in enumerate(menuopcoes, start=1):
        print(f"{menuopcao}")

      try:
        escolha = int(input("\nDigite o número da opção: "))
        if escolha <= 0:
          raise ValueError
      except ValueError:
        print("Digite apenas números positivos válidos.")
        escolha = 0

    return escolha
    
  def listar_pets(self):
    nome_arquivo = 'petsCadastrados/Pets.csv'
    try:
        # Abrir o arquivo CSV
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Ler e imprimir o cabeçalho (opcional)
            header = next(reader)
            print("Cabeçalho:", header)

            # Imprimir cada linha do CSV
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
      
  def alterar_info_pet(self, caminho_arquivo="petsCadastrados/Pets.csv"):
    """
    Permite alterar qualquer informação de um pet no arquivo CSV.
    O usuário escolhe o pet pelo ID e depois escolhe o atributo a ser alterado.
    """
    try:
        # Ler as linhas do arquivo CSV
        with open(caminho_arquivo, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            linhas = list(leitor)

        # Perguntar o ID do pet que o usuário deseja alterar
        id_pet = input("\nDigite o ID do pet que você deseja alterar: ").strip()

        # Verifica se o pet com o id fornecido existe
        pet_encontrado = False
        pet = {}  # Inicializando como um dicionário vazio
        for linha in linhas:
            if linha['id_pet'] == id_pet:
                pet_encontrado = True
                pet = linha  # Atribui a linha encontrada a 'pet'
                break

        if not pet_encontrado:
            print(f"\n❌ Pet com ID {id_pet} não encontrado.")
            return

        # Perguntar ao usuário qual informação ele deseja alterar
        print("\nO que você deseja alterar?")
        print("1 - Nome")
        print("2 - Tipo (Cachorro/Gato)")
        print("3 - Sexo (Macho/Fêmea)")
        print("4 - Endereço")
        print("5 - Idade")
        print("6 - Peso")
        print("7 - Raça")
        print("8 - Porte (pequeno/médio/grande)")
        print("9 - PCD (Sim/Não)")
        print("10 - Status de Adoção (disponível/adotado)")
        print("11 - Voltar ao menu anterior")

        try:
            opcao = int(input("\nEscolha a opção de alteração: "))
        except ValueError:
            print("⚠️ Opção inválida! Por favor, digite um número válido.")
            return

        if opcao == 11:
            print("\nRetornando ao menu anterior...")
            return

        # Alterar o valor conforme a opção escolhida
        if opcao == 1:
            novo_nome = input(f"Digite o novo nome do pet (atual: {pet['nome']}): ").strip()
            pet['nome'] = novo_nome if novo_nome else pet['nome']
        elif opcao == 2:
            novo_tipo = input(f"Digite o novo tipo do pet (atual: {pet['tipo']}): ").strip()
            if novo_tipo.lower() not in ['cachorro', 'gato']:
                print("⚠️ Tipo inválido! Deve ser 'Cachorro' ou 'Gato'.")
                return
            pet['tipo'] = novo_tipo.capitalize()
        elif opcao == 3:
            novo_sexo = input(f"Digite o novo sexo do pet (atual: {pet['sexo']}): ").strip()
            if novo_sexo.lower() not in ['macho', 'fêmea']:
                print("⚠️ Sexo inválido! Deve ser 'Macho' ou 'Fêmea'.")
                return
            pet['sexo'] = novo_sexo.capitalize()
        elif opcao == 4:
            novo_endereco = input(f"Digite o novo endereço do pet (atual: {pet['endereco']}): ").strip()
            pet['endereco'] = novo_endereco if novo_endereco else pet['endereco']
        elif opcao == 5:
            while True:
                novo_idade_input = input(f"Digite a nova idade do pet (atual: {pet['idade']}): ").strip()
                try:
                    novo_idade = float(novo_idade_input)
                    if novo_idade < 0:
                        print("⚠️ Idade não pode ser negativa!")
                        continue
                    pet['idade'] = novo_idade
                    break
                except ValueError:
                    print("⚠️ Idade inválida! Digite um número válido.")
        elif opcao == 6:
            while True:
                novo_peso_input = input(f"Digite o novo peso do pet (atual: {pet['peso']}): ").strip()
                try:
                    novo_peso = float(novo_peso_input)
                    if novo_peso < 0.5 or novo_peso > 60:
                        print("⚠️ Peso inválido! O peso deve estar entre 0.5kg e 60kg.")
                        continue
                    pet['peso'] = novo_peso
                    break
                except ValueError:
                    print("⚠️ Peso inválido! Digite um número válido.")
        elif opcao == 7:
            novo_raca = input(f"Digite a nova raça do pet (atual: {pet['raca']}): ").strip()
            pet['raca'] = novo_raca if novo_raca else pet['raca']
        elif opcao == 8:
            novo_porte = input(f"Digite o novo porte do pet (atual: {pet['porte']}): ").strip()
            pet['porte'] = novo_porte if novo_porte else pet['porte']
        elif opcao == 9:
            novo_pcd = input(f"O pet tem deficiência? (atual: {'Sim' if pet['petPcd'] else 'Não'}): ").strip().lower()
            if novo_pcd not in ['sim', 'não']:
                print("⚠️ Opção inválida! Responda com 'sim' ou 'não'.")
                return
            pet['petPcd'] = True if novo_pcd == 'sim' else False
        elif opcao == 10:
            novo_status = input(f"Digite o novo status de adoção do pet (atual: {pet['isAdotado']}): ").strip().lower()
            if novo_status not in ['disponível', 'adotado']:
                print("⚠️ Status inválido! Deve ser 'disponível' ou 'adotado'.")
                return
            pet['isAdotado'] = novo_status.capitalize()
        else:
            print("⚠️ Opção inválida!")
            return

        # Sobrescrever o arquivo CSV com as linhas atualizadas
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
            campos = [
                "id_pet", "nome", "tipo", "sexo", "endereco", "idade",
                "peso", "raca", "porte", "petPcd", "isAdotado"
            ]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()  # Escrever cabeçalho
            escritor.writerows(linhas)  # Escrever as linhas com a alteração

        print(f"\n✅ Informação do pet com ID {id_pet} alterada com sucesso!")

    except FileNotFoundError:
        print("\n❌ Arquivo não encontrado! Cadastre algum pet primeiro.")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")

                 
  def criar_arquivo_pessoa(self):

    pasta = "adotantesCadastrados"
    os.makedirs(pasta, exist_ok=True)
    
    nome_arquivo = "Adotantes.csv"
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho_arquivo):
      with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        gravar = csv.writer(arquivo)
        gravar.writerow(["Nome", "CPF", "Email", "Telefone", "Endereço"])
    else:
      pass

  def salvar_pessoa_em_arquivo(self, pessoa):
    
     pasta = "adotantesCadastrados"
     os.makedirs(pasta, exist_ok=True)

     nome_arquivo = "Adotantes.csv"
     caminho_arquivo = os.path.join(pasta, nome_arquivo)

     self.criar_arquivo_pessoa()

     with open(caminho_arquivo, "a", newline="", encoding="utf-8") as f:
        gravar = csv.writer(f)
        gravar.writerow([
          pessoa.nome,
          pessoa.cpf,
          pessoa.email,
          pessoa.telefone,
          pessoa.endereco,
        ])         
       
     print(f"\nArquivo salvo em: {caminho_arquivo}")

  
  def criar_arquivo_pet(self):

    pasta = "petsCadastrados"
    os.makedirs(pasta, exist_ok=True)

    nome_arquivo = "Pets.csv"
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho_arquivo):
      with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        gravar = csv.writer(arquivo)
        gravar.writerow(["Nome", "Tipo", "Sexo", "Endereço", "Idade", "Peso", "Raça", "Porte", "PCD"])
    else:
      pass

  def salvar_pet_em_arquivo(self, pet):

     pasta = "petsCadastrados"
     os.makedirs(pasta, exist_ok=True)

     nome_arquivo = "Pets.csv"
     caminho_arquivo = os.path.join(pasta, nome_arquivo)

     self.criar_arquivo_pet()

     with open(caminho_arquivo, "a", newline="", encoding="utf-8") as f:
        gravar = csv.writer(f)
        gravar.writerow([
          pet.nome,
          pet.tipo.value if pet.tipo else "NÃO INFORMADO",
          pet.sexo.value if pet.sexo else "NÃO INFORMADO",
          pet.endereco,
          pet.idade,
          pet.peso,
          pet.raca,
          pet.porte,
          "Sim" if pet.petPcd else "Não"
        ])         

     print(f"\nArquivo salvo em: {caminho_arquivo}")
    
  def deletar_pet(self, caminho_arquivo="petsCadastrados/Pets.csv"):
    """
    Permite deletar um pet do arquivo CSV.
    O usuário escolhe o pet pelo ID e o pet é removido do arquivo,
    com remoção da linha completa.
    """
    try:
        # Ler as linhas do arquivo CSV
        with open(caminho_arquivo, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            linhas = list(leitor)

        # Perguntar o ID do pet que o usuário deseja deletar
        id_pet = input("\nDigite o ID do pet que você deseja deletar: ").strip()

        # Verifica se o pet com o id fornecido existe
        pet_encontrado = False
        for linha in linhas:
            if linha['id_pet'] == id_pet:
                pet_encontrado = True
                linhas.remove(linha)  # Remove a linha com o pet encontrado
                break

        if not pet_encontrado:
            print(f"\n❌ Pet com ID {id_pet} não encontrado.")
            return

        # Verifica se ainda há linhas no CSV
        if len(linhas) == 0:
            print("\n⚠️ Não há mais pets registrados no sistema.")

        # Sobrescrever o arquivo CSV com as linhas restantes (sem o pet deletado)
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
            campos = [
                "id_pet", "nome", "tipo", "sexo", "endereco", "idade",
                "peso", "raca", "porte", "petPcd", "isAdotado"
            ]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()  # Escrever cabeçalho
            escritor.writerows(linhas)  # Escrever as linhas restantes (sem o pet deletado)

        print(f"\n✅ Pet com ID {id_pet} deletado com sucesso!")

    except FileNotFoundError:
        print("\n❌ Arquivo não encontrado! Cadastre algum pet primeiro.")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")
      
  def buscar_pet(self, caminho_arquivo="petsCadastrados/Pets.csv"):
      while True:
          print("\n=== BUSCA DE PETS ===")
          print("1 - Buscar por sexo")
          print("2 - Buscar por raça")
          print("3 - Buscar por idade")
          print("4 - Buscar por ID")
          print("5 - Buscar por Disponibilidade")
          print("6 - Voltar ao menu principal")

          try:
              opcao = int(input("\nEscolha uma opção: "))
          except ValueError:
              print("Digite apenas números válidos.")
              continue

          if opcao == 6:
              print("\nRetornando ao menu principal...\n")
              break

          # Definição dos filtros
          sexo = ""
          raca = ""
          idade = None
          id_pet = None
          disponibilidade = None

          if opcao == 1:
              sexo = input("Digite o sexo do pet (macho/fêmea): ").strip().lower()
          elif opcao == 2:
              raca = input("Digite a raça (ou parte dela): ").strip().lower()
          elif opcao == 3:
              idade_input = input("Digite a idade (ex: 2 ou 0.5): ").strip()
              try:
                  idade = float(idade_input)
              except ValueError:
                  print("⚠️ Idade inválida! Tente novamente.")
                  continue
          elif opcao == 4:
              id_pet = input("Digite o ID do pet (ex: 00001): ").strip()
              if len(id_pet) != 5 or not id_pet.isdigit():
                  print("⚠️ ID inválido! O ID deve conter 5 dígitos numéricos.")
                  continue
          elif opcao == 5:
              disponibilidade = input("Digite a disponibilidade do pet (adotado/disponível): ").strip().lower()
              if disponibilidade not in ["adotado", "disponível"]:
                  print("⚠️ Opção inválida! Tente novamente.")
                  continue
          else:
              print("Opção inválida! Tente novamente.")
              continue

          resultados = []

          try:
              with open(caminho_arquivo, newline='', encoding='utf-8') as f:
                  leitor = csv.DictReader(f)
                  for linha in leitor:
                      # Usar as chaves exatamente como estão no CSV
                      sexo_pet = linha.get("sexo", "").strip().lower()
                      raca_pet = linha.get("raca", "").strip().lower()
                      idade_pet = linha.get("idade", "").strip()
                      id_pet_csv = linha.get("id_pet", "").strip()
                      disponibilidade_pet = linha.get("isAdotado", "").strip().lower()

                      try:
                          idade_pet = float(idade_pet)
                      except ValueError:
                          idade_pet = None

                      # Verificação dos filtros
                      if sexo and sexo_pet != sexo:
                          continue
                      if raca and raca not in raca_pet:
                          continue
                      if idade is not None and idade_pet != idade:
                          continue
                      if id_pet and id_pet != id_pet_csv:
                          continue
                      if disponibilidade and disponibilidade != disponibilidade_pet:
                          continue

                      resultados.append(linha)

          except FileNotFoundError:
              print("\n❌ Arquivo não encontrado! Cadastre algum pet primeiro.")
              return

          if resultados:
              print(f"\n✅ {len(resultados)} pet(s) encontrado(s):\n")
              for pet in resultados:
                  print(f"ID: {pet['id_pet']}")
                  print(f"Nome: {pet['nome']}")
                  print(f"Tipo: {pet['tipo']}")
                  print(f"Sexo: {pet['sexo']}")
                  print(f"Raça: {pet['raca']}")
                  print(f"Idade: {pet['idade']} anos")
                  print(f"Peso: {pet['peso']} kg")
                  print(f"Porte: {pet['porte']}")
                  print(f"Endereço: {pet['endereco']}")
                  print(f"PCD: {pet['petPcd']}")
                  print(f"Disponibilidade: {pet['isAdotado']}")
                  print("-" * 40)
          else:
              print("\n❌ Nenhum pet encontrado com esses critérios.")


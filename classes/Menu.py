import os
import csv
from classes.Pet import CAMPOS_PET_CSV

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
  
  def listar_adotantes(self):
    nome_arquivo = 'adotantesCadastrados/Adotantes.csv'
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            adotantes = list(reader)

            if not adotantes:
                print("\n⚠️ Nenhum adotante cadastrado no sistema.")
                return

            print("\n" + "="*60)
            print(f"{'LISTA DE ADOTANTES CADASTRADOS':^60}")
            print("="*60)
            print(f"\nTotal de adotantes cadastrados: {len(adotantes)}\n")

            for adotante in adotantes:
                print("-" * 60)
                print(f"👤 Nome: {adotante['Nome']}")
                print(f"📄 CPF: {adotante['CPF']}")
                print(f"📧 Email: {adotante['Email']}")
                print(f"📞 Telefone: {adotante['Telefone']}")
                print(f"📍 Endereço: {adotante['Endereço']}")
            
            print("-" * 60)

    except FileNotFoundError:
        print(f"\n❌ Arquivo {nome_arquivo} não encontrado. Cadastre algum adotante primeiro.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")
    
  def listar_pets(self):
    nome_arquivo = 'petsCadastrados/Pets.csv'
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            pets = list(reader)

            if not pets:
                print("\n⚠️ Nenhum pet cadastrado no sistema.")
                return

            print("\n" + "="*60)
            print(f"{'LISTA DE PETS CADASTRADOS':^60}")
            print("="*60)
            print(f"\nTotal de pets cadastrados: {len(pets)}\n")

            for pet in pets:
                print("-" * 60)
                print(f"🆔 ID: {pet['id_pet']}")
                print(f"🐾 Nome: {pet['nome']}")
                print(f"🐕 Tipo: {pet['tipo']}")
                print(f"⚥ Sexo: {pet['sexo']}")
                print(f"📍 Endereço: {pet['endereco']}")
                print(f"📅 Idade: {pet['idade']} anos")
                print(f"⚖️ Peso: {pet['peso']} kg")
                print(f"🎨 Raça: {pet['raca']}")
                print(f"📏 Porte: {pet['porte']}")
                print(f"♿ PCD: {pet['petPcd']}")
                print(f"💚 Status: {pet['isAdotado']}")
                
                if pet.get('isAdotado', '').lower() == 'adotado':
                    print(f"👤 Adotado por: {pet.get('nome_adotante', 'N/A')}")
                    print(f"📄 CPF do adotante: {pet.get('cpf_adotante', 'N/A')}")
                    print(f"📞 Telefone do adotante: {pet.get('telefone_adotante', 'N/A')}")
            
            print("-" * 60)

    except FileNotFoundError:
        print(f"\n❌ Arquivo {nome_arquivo} não encontrado. Cadastre algum pet primeiro.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")
      
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

        # Garantir que todos os pets tenham os campos de adotante
        for linha in linhas:
            if 'nome_adotante' not in linha:
                linha['nome_adotante'] = "N/A"
            if 'cpf_adotante' not in linha:
                linha['cpf_adotante'] = "N/A"
            if 'telefone_adotante' not in linha:
                linha['telefone_adotante'] = "N/A"

        # Sobrescrever o arquivo CSV com as linhas atualizadas
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS_PET_CSV)
            escritor.writeheader()  # Escrever cabeçalho
            escritor.writerows(linhas)  # Escrever as linhas com a alteração

        print(f"\n✅ Informação do pet com ID {id_pet} alterada com sucesso!")

    except FileNotFoundError:
        print("\n❌ Arquivo não encontrado! Cadastre algum pet primeiro.")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")

  
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

        # Garantir que todos os pets restantes tenham os campos de adotante
        for linha in linhas:
            if 'nome_adotante' not in linha:
                linha['nome_adotante'] = "N/A"
            if 'cpf_adotante' not in linha:
                linha['cpf_adotante'] = "N/A"
            if 'telefone_adotante' not in linha:
                linha['telefone_adotante'] = "N/A"

        # Sobrescrever o arquivo CSV com as linhas restantes (sem o pet deletado)
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS_PET_CSV)
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

  def adotar_pet(self, caminho_arquivo="petsCadastrados/Pets.csv"):
    """
    Permite adotar um pet disponível.
    Lista pets disponíveis, cadastra adotante e vincula ao pet.
    """
    try:
        with open(caminho_arquivo, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            linhas = list(leitor)

        # Garantir que todos os pets tenham os campos de adotante
        for linha in linhas:
            if 'nome_adotante' not in linha:
                linha['nome_adotante'] = "N/A"
            if 'cpf_adotante' not in linha:
                linha['cpf_adotante'] = "N/A"
            if 'telefone_adotante' not in linha:
                linha['telefone_adotante'] = "N/A"

        pets_disponiveis = [pet for pet in linhas if pet.get('isAdotado', '').lower() == 'disponível']

        if not pets_disponiveis:
            print("\n❌ Não há pets disponíveis para adoção no momento.")
            return

        print("\n" + "="*60)
        print(f"{'PETS DISPONÍVEIS PARA ADOÇÃO':^60}")
        print("="*60 + "\n")

        for pet in pets_disponiveis:
            print(f"🆔 ID: {pet['id_pet']} | 🐾 Nome: {pet['nome']} | 🐕 Tipo: {pet['tipo']}")
            print(f"   ⚥ Sexo: {pet['sexo']} | 🎨 Raça: {pet['raca']} | 📅 Idade: {pet['idade']} anos")
            print("-" * 60)

        id_pet = input("\nDigite o ID do pet que deseja adotar (ou 0 para cancelar): ").strip()

        if id_pet == "0":
            print("\nAdoção cancelada.")
            return

        pet_encontrado = False
        nome_pet = ""
        nome_adotante_salvo = ""
        
        for linha in linhas:
            if linha['id_pet'] == id_pet:
                if linha.get('isAdotado', '').lower() != 'disponível':
                    print(f"\n❌ O pet com ID {id_pet} já foi adotado!")
                    return
                pet_encontrado = True
                nome_pet = linha['nome']
                
                print(f"\n🐾 Você escolheu adotar: {nome_pet}")
                print("\nAgora vamos cadastrar os dados do adotante:\n")

                from classes.Pessoa import Pessoa
                pessoa = Pessoa()
                adotante = pessoa.cadastrar_pessoa()

                linha['isAdotado'] = 'adotado'
                linha['nome_adotante'] = adotante.nome
                linha['cpf_adotante'] = adotante.cpf
                linha['telefone_adotante'] = adotante.telefone
                nome_adotante_salvo = adotante.nome
                break

        if not pet_encontrado:
            print(f"\n❌ Pet com ID {id_pet} não encontrado.")
            return

        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS_PET_CSV)
            escritor.writeheader()
            escritor.writerows(linhas)

        print(f"\n✅ Adoção realizada com sucesso! 🎉")
        print(f"O pet {nome_pet} agora tem um novo lar com {nome_adotante_salvo}! 💚")

    except FileNotFoundError:
        print("\n❌ Arquivo não encontrado! Cadastre algum pet primeiro.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")


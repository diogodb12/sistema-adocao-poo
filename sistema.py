import os
from enum import Enum
from datetime import datetime

NAO_INFORMADO = "NÃO INFORMADO" 

class TipoAnimal(Enum):
  CACHORRO = "Cachorro"
  GATO = "Gato"

class SexoAnimal(Enum):
  
  MACHO = "Macho"
  FEMEA = "Fêmea"


class Pessoa:

    NAO_INFORMADO = "NÃO INFORMADO"

    def __init__(self, nome, cpf, email, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def cadastrar_pessoa(self):
        print("\n=== CADASTRO DE NOVA PESSOA ===")

        nome = input("Digite o nome da pessoa: ").strip()

        if not nome:
            nome = self.NAO_INFORMADO
        elif not nome.replace(" ", "").isalpha():
            raise Exception("O nome não pode conter números ou caracteres especiais.")

        cpf = input("Digite o CPF da pessoa (somente números): ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            raise Exception("CPF inválido. O CPF deve conter 11 números.")

        email = input("Digite o e-mail da pessoa: ").strip()
        telefone = input("Digite o telefone da pessoa (com DDD, ex: 11987654321): ").strip()

        if not telefone.isdigit() or len(telefone) < 10:
            raise Exception("Telefone inválido. O número deve conter ao menos 10 dígitos.")

        print("\n=== Endereço ===")
        numero = input("Número da casa: ").strip()
        cidade = input("Cidade: ").strip()
        rua = input("Rua: ").strip()

        numero = numero if numero else self.NAO_INFORMADO
        cidade = cidade if cidade else self.NAO_INFORMADO
        rua = rua if rua else self.NAO_INFORMADO

        endereco = f"{rua}, {numero}, {cidade}"

        pessoa = Pessoa(nome, cpf, email, telefone, endereco)

        menu = Menu()
        menu.salvar_pessoa_em_arquivo(pessoa)

        print("\nPessoa cadastrada e salva com sucesso!")

class Pet:
  
  def __init__(self, nome = None, tipo = None, sexo = None, endereco = None, idade = None, peso = None, raca = None, porte = None, petPcd = None):
    self.nome = nome
    self.tipo = tipo
    self.sexo = sexo
    self.endereco = endereco
    self.idade = idade
    self.peso = peso
    self.raca = raca
    self.porte = porte
    self.petPcd = petPcd

  def cadastro_pet(self):
    print("\n=== CADASTRO DE NOVO PET ===")

    nome = input("Digite o nome do pet: ").strip()

    if not nome:
      nome = NAO_INFORMADO
    elif not nome.replace(" ", "").isalpha():
      raise Exception(
          "O nome não pode conter números ou caracteres especiais.")


    tipo = None
    while tipo is None:
      try:
        print("\nSelecione o tipo do pet:")
        print("1 - Cachorro")
        print("2 - Gato")
        op = int(input("Opção: "))

        if op == 1:
          tipo = TipoAnimal.CACHORRO
        elif op == 2:
          tipo = TipoAnimal.GATO
        else:
          print("Escolha 1 ou 2.")
      except ValueError:
        print("Digite apenas números (1 ou 2).")


    sexo = None
    while sexo is None:
      try:
        print("\nSelecione o sexo do pet:")
        print("1 - Macho")
        print("2 - Fêmea")
        sexo = int(input("Opção: "))
        if sexo == 1:
          sexo = SexoAnimal.MACHO
        elif sexo == 2:
          sexo = SexoAnimal.FEMEA
        else:
          print("Escolha 1 ou 2.")
          sexo = None
      except ValueError:
        print("Digite apenas números (1 ou 2).")


    print("\n=== Endereço de Encontro ===")
    numero = input("Número da casa: ").strip()
    cidade = input("Cidade: ").strip()
    rua = input("Rua: ").strip()

    numero = numero if numero else NAO_INFORMADO
    cidade = cidade if cidade else NAO_INFORMADO
    rua = rua if rua else NAO_INFORMADO

    endereco = f"{rua}, {numero}, {cidade}"


    while True:
      idade_input = input(
          "\nIdade aproximada (em anos ou meses, ex: 2 ou 0.5): ").replace(
              ",", ".").strip()
      if not idade_input:
        idade = NAO_INFORMADO
        break
      try:
        idade = float(idade_input)
        if idade > 20:
          raise Exception(
              "Idade inválida: o pet não pode ter mais de 20 anos.")
        if idade < 1:
          idade = round(idade, 2)
        break
      except ValueError:
        print("Digite um número válido para idade (use ponto ou vírgula).")


    while True:
      peso_input = input("\nPeso aproximado (em kg, ex: 5.2): ").replace(
          ",", ".").strip()
      if not peso_input:
        peso = NAO_INFORMADO
        break
      try:
        peso = float(peso_input)
        if peso < 0.5 or peso > 60:
          raise Exception("Peso inválido: deve estar entre 0.5kg e 60kg.")
        break
      except ValueError:
        print("Digite um número válido para peso (use ponto ou vírgula).")


    raca = input("\nRaça do pet: ").strip()
    if not raca:
      raca = NAO_INFORMADO
    elif not raca.replace(" ", "").isalpha():
      raise Exception(
          "A raça não pode conter números ou caracteres especiais.")

    porte = input("\nPorte do pet (pequeno/médio/grande): ").strip()
    if not porte:
      porte = NAO_INFORMADO

    pcd_input = input(
        "\nO pet possui alguma deficiência? (s/n): ").strip().lower()
    petPcd = pcd_input == "s"

    pet = Pet(nome, tipo, sexo, endereco, idade, peso, raca, porte, petPcd)

    menu = Menu()
    menu.salvar_pet_em_arquivo(pet)

    print("\nPet cadastrado e salvo com sucesso!")


class Menu:
   
  def opcoes(self):
    """Lê as opções do menu e força o usuário a escolher um número válido"""
    with open("menu.txt", "r", encoding="utf-8") as m:
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

  
  def salvar_pet_em_arquivo(self, pet):
    """Salva as informações do pet em um arquivo formatado"""

    timestamp = datetime.now().strftime("%Y%m%dT%H%M")

    nome_formatado = pet.nome.replace(" ", "").upper()

    nome_arquivo = f"{timestamp}-{nome_formatado}.txt"

    pasta = "petsCadastrados"
    os.makedirs(pasta, exist_ok=True)

    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
      f.write(f"{pet.nome}\n")
      f.write(f"{pet.tipo.value}\n")
      f.write(f"{pet.sexo.value}\n")
      f.write(f"{pet.endereco}\n")
      f.write(f"{pet.idade}\n")
      f.write(f"{pet.peso}\n")
      f.write(f"{pet.raca}\n")
      f.write(f"{pet.porte}\n")
      f.write(f"{'Sim' if pet.petPcd else 'Não'}\n")

    print(f"\nArquivo salvo em: {caminho_arquivo}")

  def salvar_pessoa_em_arquivo(self, pessoa):
     """Salva as informações da pessoa em um arquivo formatado"""

     timestamp = datetime.now().strftime("%Y%m%dT%H%M")

     nome_formatado = pessoa.nome.replace(" ", "").upper()

     nome_arquivo = f"{timestamp}-{nome_formatado}.txt"

     pasta = "pessoasCadastradas"
     os.makedirs(pasta, exist_ok=True)

     caminho_arquivo = os.path.join(pasta, nome_arquivo)

     with open(caminho_arquivo, "w", encoding="utf-8") as f:
         f.write(f"{pessoa.nome}\n")
         f.write(f"{pessoa.cpf}\n")
         f.write(f"{pessoa.email}\n")
         f.write(f"{pessoa.telefone}\n")
         f.write(f"{pessoa.endereco}\n")

     print(f"\nArquivo salvo em: {caminho_arquivo}")
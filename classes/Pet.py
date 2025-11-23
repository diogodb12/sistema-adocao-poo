import os
import csv
from enum import Enum

NAO_INFORMADO = "NÃO INFORMADO"

CAMPOS_PET_CSV = [
    "id_pet", "nome", "tipo", "sexo", "endereco", "idade",
    "peso", "raca", "porte", "petPcd", "isAdotado",
    "nome_adotante", "cpf_adotante", "telefone_adotante"
] 

class TipoAnimal(Enum):
  CACHORRO = "Cachorro"
  GATO = "Gato"

class SexoAnimal(Enum):

  MACHO = "Macho"
  FEMEA = "Fêmea"


class Pet:

  def __init__(self, id_pet=None, nome=None, tipo=None, sexo=None, endereco=None, idade=None, peso=None, raca=None, porte=None, petPcd=None, isAdotado="disponível"):
    self.id_pet = id_pet
    self.nome = nome
    self.tipo = tipo
    self.sexo = sexo
    self.endereco = endereco
    self.idade = idade
    self.peso = peso
    self.raca = raca
    self.porte = porte
    self.petPcd = petPcd
    self.isAdotado = isAdotado

  def gerar_id_pet(self, arquivo_csv="petsCadastrados/Pets.csv"):
    """
    Gera um novo id_pet incremental com base no último ID existente no CSV.
    Retorna sempre um ID único e sequencial no formato 00001, 00002, etc.
    """
    # Se o arquivo não existe, o primeiro ID é 00001
    if not os.path.exists(arquivo_csv):
        return "00001"

    ultimo_id = 0

    with open(arquivo_csv, "r", newline='', encoding="utf-8") as f:
        leitor = csv.DictReader(f)

        for linha in leitor:
            if not linha:  # ignora linhas vazias
                continue
            try:
                id_atual = int(linha['id_pet'])  # lê o campo id_pet corretamente
                if id_atual > ultimo_id:
                    ultimo_id = id_atual
            except (ValueError, KeyError):
                continue

    novo_id = ultimo_id + 1
    return f"{novo_id:05d}"


  def cadastro_pet(self):
    print("\n=== CADASTRO DE NOVO PET ===")

    nome = input("Digite o nome do pet: ").strip()

    if not nome:
      nome = NAO_INFORMADO
    elif not nome.replace(" ", "").isalpha():
      raise Exception("O nome não pode conter números ou caracteres especiais.")

    tipo = None
    while tipo is None:
      try:
        print("\nSelecione o tipo do pet:")
        print("1 - Cachorro")
        print("2 - Gato")
        op = int(input("Opção: "))

        if op == 1:
          tipo = "Cachorro"
        elif op == 2:
          tipo = "Gato"
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
        op = int(input("Opção: "))
        if op == 1:
          sexo = "Macho"
        elif op == 2:
          sexo = "Fêmea"
        else:
          print("Escolha 1 ou 2.")
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
      idade_input = input("\nIdade aproximada (em anos ou meses, ex: 2 ou 0.5): ").replace(",", ".").strip()
      if not idade_input:
        idade = NAO_INFORMADO
        break
      try:
        idade = float(idade_input)
        if idade > 20:
          raise Exception("Idade inválida: o pet não pode ter mais de 20 anos.")
        if idade < 1:
          idade = round(idade, 2)
        break
      except ValueError:
        print("Digite um número válido para idade (use ponto ou vírgula).")

    while True:
      peso_input = input("\nPeso aproximado (em kg, ex: 5.2): ").replace(",", ".").strip()
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
      raise Exception("A raça não pode conter números ou caracteres especiais.")

    porte = input("\nPorte do pet (pequeno/médio/grande): ").strip()
    if not porte:
      porte = NAO_INFORMADO

    pcd_input = input("\nO pet possui alguma deficiência? (s/n): ").strip().lower()
    petPcd = pcd_input == "s"

    id_pet = self.gerar_id_pet()
    isAdotado = "disponível"

    novo_pet = self.__class__(id_pet, nome, tipo, sexo, endereco, idade, peso, raca, porte, petPcd, isAdotado)

    self.salvar_pet_em_arquivo(novo_pet)
    print(f"\n✅ Pet cadastrado com sucesso! ID gerado: {novo_pet.id_pet}")

  def salvar_pet_em_arquivo(self, pet, arquivo_csv="petsCadastrados/Pets.csv"):
    """
    Salva os dados do pet no CSV dentro da pasta 'petsAdotados'.
    Cria o diretório e o cabeçalho se ainda não existirem.
    """

    # Cria a pasta se não existir
    pasta = os.path.dirname(arquivo_csv)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    arquivo_existe = os.path.exists(arquivo_csv)

    with open(arquivo_csv, "a", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CAMPOS_PET_CSV)

        # Escreve o cabeçalho apenas se o arquivo for novo
        if not arquivo_existe:
            writer.writeheader()

        # Escreve os dados do pet
        writer.writerow({
            "id_pet": pet.id_pet,
            "nome": pet.nome,
            "tipo": pet.tipo,
            "sexo": pet.sexo,
            "endereco": pet.endereco,
            "idade": pet.idade,
            "peso": pet.peso,
            "raca": pet.raca,
            "porte": pet.porte,
            "petPcd": pet.petPcd,
            "isAdotado": pet.isAdotado,
            "nome_adotante": "N/A",
            "cpf_adotante": "N/A",
            "telefone_adotante": "N/A"
        })
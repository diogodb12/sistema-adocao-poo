import sys

class Pet:
  nome: str
  tipo: str
  sexo: str
  enderecoEncontro: str
  idade: int
  peso: float
  raca: str
  petPcd: bool


class Menu:

  def menu(self):
    print("Oi")
  
  def perguntasCadastro(self):
    with open("perguntas.txt", "r", encoding="utf-8") as f:
      perguntas = f.readlines()  # lê todas as linhas do arquivo

    respostas = {}

    # Percorre cada pergunta
    for pergunta in perguntas:
      pergunta = pergunta.strip()
      if not pergunta:
          continue

      # Exibe a pergunta (sem print)
      sys.stdout.write(pergunta + " ")
      sys.stdout.flush()

      # Lê a resposta
      resposta = input()
      respostas[pergunta] = resposta

    # Retorna as respostas
    return respostas
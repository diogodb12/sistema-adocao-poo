from sistema import Menu

if __name__ == "__main__":
  form = Menu()             # cria o objeto da classe
  respostas = form.perguntasCadastro()  # executa o método e captura as respostas

  # Exibe as respostas no final
  print("\n🐾 Respostas coletadas:")
  for pergunta, resposta in respostas.items():
      print(f"{pergunta} -> {resposta}")
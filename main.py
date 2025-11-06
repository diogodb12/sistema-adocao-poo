from sistema import Menu, Pet

if __name__ == "__main__":
    menu = Menu()
    opcao = menu.opcoes()
    pet = Pet()

    try:
        if opcao == 1:
              pet.cadastro_pet()
        if opcao == 2:
              pass  # TODO: Implementar edição de pet
    except Exception as e:
      print(f"\nErro ao cadastrar pet: {e}")


 
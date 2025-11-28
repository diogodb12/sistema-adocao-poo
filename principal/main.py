from classes.Menu import Menu
from classes.Pet import Pet
from classes.Pessoa import Pessoa

if __name__ == "__main__":
    menu = Menu()
    pet = Pet()
    pessoa = Pessoa()

    while True:
        opcao = menu.opcoes()

        try:
            if opcao == 1:
                pet.cadastro_pet()
            elif opcao == 2:
                menu.alterar_info_pet()
            elif opcao == 3:
                menu.deletar_pet()
            elif opcao == 4:
                menu.listar_pets()
            elif opcao == 5:
                menu.buscar_pet()
            elif opcao == 6:
                menu.adotar_pet()
            elif opcao == 7:
                print("\nEncerrando o sistema... Até logo!")
                break
            else:
                print("\nOpção não implementada ainda.")
        except Exception as e:
            print(f"\n❌ Erro: {e}")

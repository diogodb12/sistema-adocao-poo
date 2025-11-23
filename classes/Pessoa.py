import Menu

NAO_INFORMADO = "NÃO INFORMADO" 

class Pessoa:

    def __init__(self, nome = None, cpf = None, email = None, telefone = None, endereco = None, pets=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.pets = pets if pets is not None else []
    
    def cadastrar_pessoa(self):
        print("\n=== CADASTRO DE NOVA PESSOA ===")
    
        nome = input("Digite o nome da pessoa: ").strip()
    
        if not nome:
            nome = NAO_INFORMADO
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
        rua = input("Rua: ").strip()
        numero = input("Número da casa: ").strip()
        cidade = input("Cidade: ").strip()
    
        numero = numero if numero else NAO_INFORMADO
        cidade = cidade if cidade else NAO_INFORMADO
        rua = rua if rua else NAO_INFORMADO
    
        endereco = f"{rua}, {numero}, {cidade}"
    
        pessoa = Pessoa(nome, cpf, email, telefone, endereco)

        menu = Menu()
        
        menu.salvar_pessoa_em_arquivo(pessoa)
    
        print("\nPessoa cadastrada e salva com sucesso!")
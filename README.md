# Sistema de Adoção de Animais 🐾

## AdoPet
Sistema de Adoção de Pets

**Universidade Católica de Santos**  
**Disciplina:** Programação Orientada a Objetos (POO)  
**Docente:** Dr. [Thiago Ferauche](https://github.com/ferauche)

## Integrantes:

- [Diogo Dantas Botelho](https://github.com/diogodb12) — Sistemas de Informação  
- Eduardo de Melo Flam — Ciências da Computação  
- [Giovana de Oliveira Machado](https://github.com/Gio-Mach) — Ciências da Computação

---

## Resumo do projeto

Este projeto é um protótipo de um sistema de adoção de animais desenvolvido em Python usando Programação Orientada a Objetos (POO). O sistema permite cadastrar pets, listar pets cadastrados, buscar pets, adotar pets e cadastrar adotantes. O projeto inclui duas interfaces: uma linha de comando (CLI) e uma interface gráfica (Tkinter).

### Motivação para escolher Python:

- A linguagem foi escolhida pela familiaridade do grupo com Python.  
- Sintaxe concisa e baixa tipagem facilitam prototipação rápida.  
- O conteúdo da disciplina foi ministrado em Python, o que manteve congruência pedagógica.

---

## Features

- Cadastro de pets (com validações básicas para idade, peso, dados de endereço).  
- Armazenamento em arquivos CSV (persistência simples e auditável).  
- Cadastro de adotantes (pessoa).  
- Listagem e busca de pets por critérios simples.  
- Adoção de pet (associa adotante ao pet e marca o pet como adotado).  
- Interface gráfica com Tkinter para operação amigável.  
- Menu em linha de comando para operação via terminal.

---

## Requisitos

- Python >= 3.11 (o projeto usa `requires-python = ">=3.11"` no pyproject.toml).  
- Biblioteca padrão do Python: `csv`, `tkinter` (para GUI).  
- Sistema de arquivos com permissões de escrita (os dados são salvos em pastas `petsCadastrados/` e `adotantesCadastrados/`).

---

## Como executar

### 1) Linha de comando (CLI)

Abra o terminal na pasta do projeto (PROJETO-POO) e rode:

```bash
python main.py
```

O menu em modo texto será exibido com opções numeradas (cadastrar pet, deletar, listar etc.). Siga as instruções na tela.

### 2) Interface gráfica (GUI)

Execute:

```bash
python interface_grafica.py
```

A janela do Tkinter abrirá com campos de busca, botões de cadastro, listagem e adoção. Ideal para uso mais intuitivo.

---

## Arquitetura orientada a objetos — explicação completa

O sistema foi implementado com três classes principais:

### 1. Pet (arquivo classes/Pet.py)

**Responsabilidade:** representar um animal disponível para adoção e prover funções para cadastro e persistência.

**Atributos principais (exemplos):**

- `id_pet` — identificador único do pet (gerado automaticamente)  
- `nome` — nome do pet  
- `tipo` — Tipo do animal (Ex.: "Cachorro", "Gato")  
- `sexo` — "Macho" / "Fêmea"  
- `endereco` — endereço do encontro / local do pet  
- `idade` — idade em anos (float)  
- `peso` — peso em kg (float)  
- `raca` — raça  
- `porte` — porte do animal (pequeno, médio, grande)  
- `petPcd` — campo para indicar se pet precisa de cuidado especial  
- `isAdotado` — flag (True/False)  
- `nome_adotante`, `cpf_adotante`, `telefone_adotante` — informações do adotante quando adotado

**Métodos principais:**

- `__init__(...)` — inicializa atributos (com valores padrão ou recebidos).  
- `gerar_id_pet(arquivo_csv="petsCadastrados/Pets.csv")` — gera um `id_pet` sequencial lendo o CSV. Se o CSV não existir, inicia em "00001". Garante formato fixo (ex.: 00001, 00002).  
- `cadastro_pet()` — função interativa (CLI) que pede dados ao usuário, valida entradas (idade, peso, campos de endereço) e cria um objeto `Pet` com `id_pet` gerado; ao final chama `salvar_pet_em_arquivo`.  
- `salvar_pet_em_arquivo(pet, arquivo_csv="petsCadastrados/Pets.csv")` — escreve/append os dados do pet no CSV com cabeçalho `CAMPOS_PET_CSV`.

**Validações importantes encontradas:**

- Idade: permite números decimais, não permite valores > 20 anos. Aceita valores menores que 1 (ex.: 0.5) para filhotes.  
- Peso: esperado um número float; validações para limites razoáveis.  
- Endereço: campo composto por rua, número e cidade — preenche com "NÃO INFORMADO" caso em branco.  
- Geração de ID: ignora linhas vazias no CSV; transforma o último `id_pet` em inteiro, incrementa e formata.

---

### 2. Pessoa (arquivo classes/Pessoa.py)

**Responsabilidade:** representar um adotante (dados básicos) e salvar em CSV.

**Atributos:**

- `nome`, `cpf`, `email`, `telefone`, `endereco`, `pets` (lista opcional de pets do adotante)

**Métodos principais:**

- `__init__(...)` — inicializa atributos.  
- `criar_arquivo_pessoa()` — cria pasta `adotantesCadastrados` e arquivo `Adotantes.csv` com cabeçalho, caso não exista.  
- `salvar_pessoa_em_arquivo()` — grava/append os dados do adotante no CSV.  
- `cadastrar_pessoa()` — rotina interativa (CLI) para entrada dos dados do adotante e chamada de persistência.

---

### 3. Menu (arquivo classes/Menu.py)

**Responsabilidade:** interface de alto nível para a aplicação CLI — mostra menu, lê opção e encaminha para operações.

**Métodos principais:**

- `opcoes()` — exibe o menu (leitura do arquivo `texts/menu.txt`) e valida entrada do usuário; retorna a opção escolhida.  
- `listar_pets()` — lê arquivo `petsCadastrados/Pets.csv` e imprime pets no console.  
- `listar_adotantes()` — lê `adotantesCadastrados/Adotantes.csv` e imprime.  
- `buscar_pet()` — busca por critério (ex.: nome, id) e exibe resultados.  
- `adotar_pet()` — procedimento para adotar: pede CPF/telefone do adotante, verifica pet existente, grava dados do adotante no CSV e atualiza o pet (marca `isAdotado` e preenche campos de adotante no CSV do pet).  
- `alterar_info_pet()` — (funcionalidade para alterar dados de um pet já cadastrado).  
- `deletar_pet()` — remove pet (implementado removendo linha do CSV ou marcando?) — (veja o método no `Menu.py` para detalhes exatos).

---

## Dados persistidos (CSV)

### petsCadastrados/Pets.csv

Cabeçalho definido por `CAMPOS_PET_CSV` (arquivo `classes/Pet.py`):

```
id_pet, nome, tipo, sexo, endereco, idade, peso, raca, porte, petPcd, isAdotado, nome_adotante, cpf_adotante, telefone_adotante
```

- `id_pet` é gerado automaticamente no formato `00001, 00002, ...`  
- `isAdotado` é escrito como True/False

### adotantesCadastrados/Adotantes.csv

Cabeçalho:

```
Nome, CPF, Email, Telefone, Endereço
```

Ambos os arquivos são criados pela aplicação na primeira gravação caso não existam (funções `criar_arquivo_*`).

---

## Fluxo de execução (visão geral)

1. Inicialização: `main.py` cria instâncias de Menu, Pet e Pessoa.  
2. Loop principal: `menu.opcoes()` exibe o menu; o usuário escolhe uma operação.  
3. Operações:

- `1: cadastro_pet()` → chama `Pet.cadastro_pet` → valida entradas → `salvar_pet_em_arquivo`.  
- `2: deletar_pet()` → remove registro do CSV (ou marca).  
- `3: listar_pets()` → lê CSV e imprime.  
- `4: buscar_pet()` → filtra por nome/id/atributo e exibe.  
- `5: adotar_pet()` → liga `Pessoa.cadastrar_pessoa` e atualiza pet no CSV.  
- `6: sair` → encerra.

4. GUI alternative: `interface_grafica.py` oferece botões/controles que chamam funções semelhantes (CRUD) e salvam/atualizam os CSVs.

---

## Validações e Tratamento de Erros

- O código contém `try/except` para capturar exceções e retornar mensagens amigáveis.  
- Entrada do usuário é limpa (`.strip()`), valores numéricos são convertidos com verificação de erros (`float()` com `replace(',', '.')`).  
- Uso de `os.makedirs(..., exist_ok=True)` para garantir que pastas de dados existam.  
- As funções que geram/interpretam IDs tratam linhas vazias e falhas no arquivo CSV.

---

## Arquivos importantes (rápido guia)

- `main.py` → loop CLI; utiliza Menu, Pet, Pessoa.  
- `interface_grafica.py` → janela Tkinter com formulário e listagens.  
- `classes/Pet.py` → lógica de Pet, geração de ID, validações, escrita em CSV.  
- `classes/Pessoa.py` → lógica do adotante e persistência em CSV.  
- `classes/Menu.py` → funções de listagem, busca, adoção, exclusão e menu CLI.  
- `texts/menu.txt` → texto exibido no menu CLI.

## Demonstração da Interface

<img width="1096" height="676" alt="image" src="https://github.com/user-attachments/assets/0cd15366-e9b2-4461-9649-ef9444113717" />

<img width="1098" height="677" alt="image" src="https://github.com/user-attachments/assets/abaaa63e-dbd4-4b90-9e02-244bec144bfa" />

<img width="1099" height="677" alt="image" src="https://github.com/user-attachments/assets/d4c489f3-52a3-4ec1-ab50-2437e881ec65" />


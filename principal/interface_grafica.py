import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os


try:
    from classes.Pet import CAMPOS_PET_CSV
except ImportError:
    CAMPOS_PET_CSV = [
        'id_pet', 'nome', 'tipo', 'sexo', 'raca', 'idade', 'peso', 
        'porte', 'endereco', 'petPcd', 'isAdotado', 
        'nome_adotante', 'cpf_adotante', 'telefone_adotante'
    ]


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PETS = os.path.join(DIRETORIO_ATUAL, "petsCadastrados", "Pets.csv")
CAMINHO_ADOTANTES = os.path.join(DIRETORIO_ATUAL, "adotantesCadastrados", "Adotantes.csv")

class PetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Adoção de Pets 🐾")
        self.root.geometry("1100x650")
        
       
        style = ttk.Style()
        style.theme_use("clam")

        self.verificar_arquivos()

        
        frame_busca = tk.Frame(self.root, bg="#eee", pady=10)
        frame_busca.pack(fill=tk.X)

        tk.Label(frame_busca, text="Buscar por:", bg="#eee").pack(side=tk.LEFT, padx=5)
        self.combo_tipo_busca = ttk.Combobox(frame_busca, values=["Nome", "Raça", "ID", "Status"], state="readonly", width=10)
        self.combo_tipo_busca.current(0)
        self.combo_tipo_busca.pack(side=tk.LEFT, padx=5)

        self.entry_busca = tk.Entry(frame_busca, width=30)
        self.entry_busca.pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_busca, text="🔍 Buscar", command=self.filtrar_dados).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busca, text="🔄 Limpar Filtros", command=self.carregar_dados).pack(side=tk.LEFT, padx=5)

        
        frame_botoes = tk.Frame(self.root, bg="white", pady=10)
        frame_botoes.pack(fill=tk.X)

        btn_style = {"font": ("Arial", 10), "width": 15}
        
        tk.Button(frame_botoes, text="+ Novo Pet", bg="#90EE90", command=self.janela_cadastro, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="✏ Editar Pet", bg="#FFE4B5", command=self.janela_edicao, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="❤ Adotar", bg="#87CEEB", command=self.janela_adocao, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="🗑 Deletar", bg="#FFB6C1", command=self.deletar_pet, **btn_style).pack(side=tk.LEFT, padx=10)
        
        
        tk.Button(frame_botoes, text="📋 Ver Adotantes", bg="#D3D3D3", command=self.janela_listar_adotantes, **btn_style).pack(side=tk.RIGHT, padx=10)

       
        colunas = ("id", "nome", "tipo", "raca", "sexo", "idade", "status", "adotante")
        self.tree = ttk.Treeview(self.root, columns=colunas, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("raca", text="Raça")
        self.tree.heading("sexo", text="Sexo")
        self.tree.heading("idade", text="Idade")
        self.tree.heading("status", text="Status")
        self.tree.heading("adotante", text="Adotante")

        
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("status", width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.carregar_dados()

    
    def verificar_arquivos(self):
        os.makedirs(os.path.dirname(CAMINHO_PETS), exist_ok=True)
        os.makedirs(os.path.dirname(CAMINHO_ADOTANTES), exist_ok=True)
        
        if not os.path.exists(CAMINHO_PETS):
            with open(CAMINHO_PETS, 'w', newline='', encoding='utf-8') as f:
                csv.DictWriter(f, fieldnames=CAMPOS_PET_CSV).writeheader()

    def ler_todos_pets(self):
        if not os.path.exists(CAMINHO_PETS): return []
        with open(CAMINHO_PETS, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def salvar_todos_pets(self, lista):
        try:
            with open(CAMINHO_PETS, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=CAMPOS_PET_CSV)
                writer.writeheader()
                writer.writerows(lista)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")
            return False

    def carregar_dados(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        
        pets = self.ler_todos_pets()
        for p in pets:
            
            adotante = p.get('nome_adotante', '') if p.get('isAdotado', '').lower() == 'adotado' else '-'
            self.tree.insert("", tk.END, values=(
                p.get('id_pet'), p.get('nome'), p.get('tipo'), p.get('raca'),
                p.get('sexo'), p.get('idade'), p.get('isAdotado'), adotante
            ))

    # --- LÓGICA DE BUSCA (buscar_pet) ---
    def filtrar_dados(self):
        termo = self.entry_busca.get().lower()
        tipo_busca = self.combo_tipo_busca.get() # Nome, Raça, ID, Status
        
        pets = self.ler_todos_pets()
        for i in self.tree.get_children(): self.tree.delete(i)

        for p in pets:
            valor_campo = ""
            if tipo_busca == "Nome": valor_campo = p.get('nome', '').lower()
            elif tipo_busca == "Raça": valor_campo = p.get('raca', '').lower()
            elif tipo_busca == "ID": valor_campo = p.get('id_pet', '').lower()
            elif tipo_busca == "Status": valor_campo = p.get('isAdotado', '').lower()

            if termo in valor_campo:
                adotante = p.get('nome_adotante', '') if p.get('isAdotado', '').lower() == 'adotado' else '-'
                self.tree.insert("", tk.END, values=(
                    p.get('id_pet'), p.get('nome'), p.get('tipo'), p.get('raca'),
                    p.get('sexo'), p.get('idade'), p.get('isAdotado'), adotante
                ))

    def janela_cadastro(self):
        self.abrir_formulario("Cadastrar Novo Pet")

    def abrir_formulario(self, titulo, dados_atuais=None):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.geometry("400x600")

        campos = ["ID", "Nome", "Raça", "Idade", "Peso", "Endereço"]
        entradas = {}

        for campo in campos:
            tk.Label(top, text=campo).pack(pady=2)
            e = tk.Entry(top)
            e.pack(pady=2)
            
            if dados_atuais:
                chave_csv = "id_pet" if campo == "ID" else campo.lower().replace("ç", "c").replace("ç", "c")
                if campo == "Endereço": chave_csv = "endereco"
                e.insert(0, dados_atuais.get(chave_csv, ""))
                if campo == "ID": e.config(state="disabled") # Não deixa mudar ID na edição
            entradas[campo] = e

        
        tk.Label(top, text="Tipo").pack()
        c_tipo = ttk.Combobox(top, values=["Cachorro", "Gato"])
        c_tipo.pack()
        if dados_atuais: c_tipo.set(dados_atuais.get('tipo', ''))

        tk.Label(top, text="Sexo").pack()
        c_sexo = ttk.Combobox(top, values=["Macho", "Fêmea"])
        c_sexo.pack()
        if dados_atuais: c_sexo.set(dados_atuais.get('sexo', ''))
        
        tk.Label(top, text="Status").pack()
        c_status = ttk.Combobox(top, values=["Disponível", "Adotado"])
        c_status.pack()
        if dados_atuais: 
            c_status.set(dados_atuais.get('isAdotado', 'Disponível'))
        else:
            c_status.set("Disponível")

        def salvar():
            novo_dado = {
                "id_pet": entradas["ID"].get(),
                "nome": entradas["Nome"].get(),
                "tipo": c_tipo.get(),
                "sexo": c_sexo.get(),
                "raca": entradas["Raça"].get(),
                "idade": entradas["Idade"].get(),
                "peso": entradas["Peso"].get(),
                "endereco": entradas["Endereço"].get(),
                "porte": "Médio",
                "petPcd": "Não",
                "isAdotado": c_status.get(),
        
                "nome_adotante": dados_atuais.get('nome_adotante', 'N/A') if dados_atuais else 'N/A',
                "cpf_adotante": dados_atuais.get('cpf_adotante', 'N/A') if dados_atuais else 'N/A',
                "telefone_adotante": dados_atuais.get('telefone_adotante', 'N/A') if dados_atuais else 'N/A'
            }

            if not novo_dado["id_pet"] or not novo_dado["nome"]:
                messagebox.showwarning("Erro", "ID e Nome são obrigatórios.")
                return

            pets = self.ler_todos_pets()
            
            if dados_atuais:
               
                pets = [p for p in pets if str(p['id_pet']) != str(novo_dado['id_pet'])]
                pets.append(novo_dado)
                msg = "Pet atualizado com sucesso!"
            else: 
                if any(str(p['id_pet']) == str(novo_dado['id_pet']) for p in pets):
                    messagebox.showerror("Erro", "ID já existe!")
                    return
                pets.append(novo_dado)
                msg = "Pet cadastrado com sucesso!"

            if self.salvar_todos_pets(pets):
                messagebox.showinfo("Sucesso", msg)
                top.destroy()
                self.carregar_dados()

        tk.Button(top, text="SALVAR", bg="#90EE90", command=salvar).pack(pady=20)

    # --- LÓGICA DE EDIÇÃO (alterar_info_pet) ---
    def janela_edicao(self):
        sel = self.tree.selection()
        if not sel: 
            messagebox.showwarning("Aviso", "Selecione um pet na tabela para editar.")
            return
        
        id_pet = str(self.tree.item(sel[0])['values'][0])
        pets = self.ler_todos_pets()
        pet_alvo = next((p for p in pets if str(p['id_pet']) == id_pet), None)
        
        if pet_alvo:
            self.abrir_formulario("Editar Pet", dados_atuais=pet_alvo)

   
    def deletar_pet(self):
        sel = self.tree.selection()
        if not sel: return
        id_pet = str(self.tree.item(sel[0])['values'][0])

        if messagebox.askyesno("Confirmar", f"Tem certeza que deseja apagar o pet ID {id_pet}?"):
            pets = self.ler_todos_pets()
            novos_pets = [p for p in pets if str(p['id_pet']) != id_pet]
            
            if self.salvar_todos_pets(novos_pets):
                messagebox.showinfo("Sucesso", "Pet deletado.")
                self.carregar_dados()

    
    def janela_adocao(self):
        sel = self.tree.selection()
        if not sel: 
            messagebox.showwarning("Aviso", "Selecione um pet DISPONÍVEL para adotar.")
            return

        item = self.tree.item(sel[0])
        id_pet = str(item['values'][0])
        status = item['values'][6]

        if status.lower() != "disponível":
            messagebox.showerror("Erro", "Este pet já foi adotado!")
            return

        
        top = tk.Toplevel(self.root)
        top.title("Dados do Adotante")
        top.geometry("300x350")

        tk.Label(top, text="Nome Completo").pack(pady=5)
        e_nome = tk.Entry(top)
        e_nome.pack()
        
        tk.Label(top, text="CPF").pack(pady=5)
        e_cpf = tk.Entry(top)
        e_cpf.pack()
        
        tk.Label(top, text="Telefone").pack(pady=5)
        e_tel = tk.Entry(top)
        e_tel.pack()

        def confirmar_adocao():
            nome, cpf, tel = e_nome.get(), e_cpf.get(), e_tel.get()
            if not nome or not cpf:
                messagebox.showwarning("Erro", "Nome e CPF são obrigatórios.")
                return

            pets = self.ler_todos_pets()
            for p in pets:
                if str(p['id_pet']) == id_pet:
                    p['isAdotado'] = 'Adotado'
                    p['nome_adotante'] = nome
                    p['cpf_adotante'] = cpf
                    p['telefone_adotante'] = tel
                    break
            
            
            self.salvar_todos_pets(pets)
            
            
            try:
                existe = os.path.exists(CAMINHO_ADOTANTES)
                with open(CAMINHO_ADOTANTES, 'a', newline='', encoding='utf-8') as f:
                    campos_adotante = ["Nome", "CPF", "Email", "Telefone", "Endereço"]
                    writer = csv.DictWriter(f, fieldnames=campos_adotante)
                    if not existe: writer.writeheader()
                    writer.writerow({
                        "Nome": nome, "CPF": cpf, "Telefone": tel, 
                        "Email": "N/A", "Endereço": "N/A"
                    })
            except Exception as e:
                print(f"Erro ao salvar histórico de adotante: {e}")

            messagebox.showinfo("Parabéns!", f"Adoção realizada com sucesso!")
            top.destroy()
            self.carregar_dados()

        tk.Button(top, text="CONFIRMAR ADOÇÃO", bg="#87CEEB", command=confirmar_adocao).pack(pady=20)

    
    def janela_listar_adotantes(self):
        top = tk.Toplevel(self.root)
        top.title("Lista de Adotantes")
        top.geometry("600x400")
        
        colunas = ("Nome", "CPF", "Telefone")
        tree_ad = ttk.Treeview(top, columns=colunas, show="headings")
        for col in colunas:
            tree_ad.heading(col, text=col)
            tree_ad.column(col, width=150)
        
        tree_ad.pack(fill=tk.BOTH, expand=True)

        
        if os.path.exists(CAMINHO_ADOTANTES):
            with open(CAMINHO_ADOTANTES, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tree_ad.insert("", tk.END, values=(row.get('Nome'), row.get('CPF'), row.get('Telefone')))
        else:
            
            pets = self.ler_todos_pets()
            adotantes_unicos = set()
            for p in pets:
                if p.get('isAdotado', '').lower() == 'adotado':
                    chave = (p['nome_adotante'], p['cpf_adotante'], p['telefone_adotante'])
                    if chave not in adotantes_unicos:
                        tree_ad.insert("", tk.END, values=chave)
                        adotantes_unicos.add(chave)

if __name__ == "__main__":
    root = tk.Tk()
    app = PetApp(root)
    root.mainloop()
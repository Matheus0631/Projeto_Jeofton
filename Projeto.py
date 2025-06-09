import tkinter as tk
from tkinter import ttk, messagebox

# Mantendo a variável principal para armazenar a lista de notas
notas_dos_alunos = []

def inserir_nota(entry_nota, listbox_notas):    #adicina nota na box.
    
    global notas_dos_alunos
    try:
        nota_str = entry_nota.get()
        if not nota_str:
            messagebox.showwarning("Atenção", "O campo da nota não pode estar vazio.")
            return

        nota = float(nota_str)
        if 0 <= nota <= 10:
            notas_dos_alunos.append(nota)
            listbox_notas.insert(tk.END, f"{nota:.1f}")
            entry_nota.delete(0, tk.END)
            entry_nota.focus_set()
        else:
            messagebox.showerror("Erro de Validação", "A nota deve estar entre 0 e 10.")
    except ValueError:
        messagebox.showerror("Erro de Formato", "Por favor, digite um número válido para a nota.")

def calcular_medias(notas):     #Calcula a media do aluno.
   
    if not notas:
        return 0
    return sum(notas) / len(notas)      #soma a quantidade de notas que tem e divide pela quantidade que quem.

def ajeitar_resultados(nome, notas, media):        #adaptação da antiga função para retornar uma string formatada
    
    texto_resultado = f"--- Resultados para o(a) aluno(a) {nome} ---\n"
    texto_resultado += f"Notas inseridas: {', '.join(map(str, notas))}\n"
    texto_resultado += f"Média final: {media:.2f}"
    return texto_resultado

def executar_calculo_e_exibir(entry_nome, label_resultado):         #essa função executa o calculo quando é chamada pelo butão
  
    global notas_dos_alunos
    
   
    nome_aluno = entry_nome.get().strip()       #pega o nome dos alunos
    if not nome_aluno:
        messagebox.showwarning("Atenção", "O nome do aluno não pode estar vazio.")      #if not para dar um aviso que não há nome e que nenhuma nota está registrada
        return

    if not notas_dos_alunos:
        messagebox.showwarning("Atenção", "Nenhuma nota foi adicionada.")
        return

   
    media_das_notas = calcular_medias(notas_dos_alunos)     #essas variavéis vão usar todas as funções, e informações armazenadas e depois exibir formatadas
    texto_final = ajeitar_resultados(nome_aluno, notas_dos_alunos, media_das_notas)
    
    label_resultado.config(text=texto_final)

def limpar_tudo(entry_nome, entry_nota, listbox_notas, label_resultado): #limpa tudo pra um novo calculo
   
    global notas_dos_alunos
    entry_nome.delete(0, tk.END)
    entry_nota.delete(0, tk.END)
    listbox_notas.delete(0, tk.END)
    label_resultado.config(text="")
    
    notas_dos_alunos = []       #limpa as notas
    entry_nome.focus_set()

def main():
    """Função que cria e configura a janela principal e todos os seus componentes."""
    root = tk.Tk()
    root.title("Calculadora de Médias")
    root.geometry("400x500")
    root.resizable(False, False) #os dois falses são para evitar da janela ser responsiva

   #criando os componentes, os wight

    main_frame = ttk.Frame(root, padding="20") #frame principal
    main_frame.pack(fill="both", expand=True) #controla a direção em que o widget vai e se ele vai preencher as sobras

    ttk.Label(main_frame, text="Digite o nome do(a) aluno(a):").grid(row=0, column=0, sticky="w", pady=(0, 5))
    entry_nome = ttk.Entry(main_frame, width=40, font=("Helvetica", 11))
    entry_nome.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))

    ttk.Label(main_frame, text="Digite uma nota:").grid(row=2, column=0, sticky="w", pady=(0, 5))
    entry_nota = ttk.Entry(main_frame, width=20, font=("Helvetica", 11))
    entry_nota.grid(row=3, column=0, sticky="ew", pady=(0, 10))
    
    ttk.Label(main_frame, text="Notas Adicionadas:").grid(row=4, column=0, sticky="w", pady=(0, 5))
    listbox_notas = tk.Listbox(main_frame, height=6, font=("Helvetica", 11))
    listbox_notas.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(0, 15))

    label_resultado = ttk.Label(main_frame, text="", font=("Helvetica", 12, "bold"), justify="left", wraplength=350)
    label_resultado.grid(row=8, column=0, columnspan=2, pady=(15, 0), sticky="w")

    # --- Configuração dos Botões ---
    btn_adicionar = ttk.Button(main_frame, text="Adicionar Nota", command=lambda: inserir_nota(entry_nota, listbox_notas))
    btn_adicionar.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=(0, 10))

    btn_calcular = ttk.Button(main_frame, text="Calcular Média", command=lambda: executar_calculo_e_exibir(entry_nome, label_resultado))
    btn_calcular.grid(row=6, column=0, columnspan=2, sticky="ew", pady=5)

    btn_limpar = ttk.Button(main_frame, text="Limpar", command=lambda: limpar_tudo(entry_nome, entry_nota, listbox_notas, label_resultado))
    btn_limpar.grid(row=7, column=0, columnspan=2, sticky="ew", pady=5)
    
    entry_nome.focus_set()
    root.mainloop()

# Ponto de entrada que chama a função principal para iniciar a interface
if __name__ == "__main__":
    main()
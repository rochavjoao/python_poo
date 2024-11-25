import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle
from eleicao import Eleitor, Urna

class UrnaEletronica:
    def __init__(self, root):
        self.root = root
        self.root.title("Urna Eletrônica")
        self.root.configure(background='#ffffff')
        self.root.geometry("780x430")
        self.root.resizable(True, True)
        self.root.minsize(width=400, height=300)

        self.urna = None
        self.candidatos = []
        self.eleitores = []
        self.e_atual = None

        self.dados()
        self.interface()

    def dados(self):
        try:
            with open("candidatos.pkl", "rb") as c_file:
                self.candidatos = pickle.load(c_file)
            with open("eleitores.pkl", "rb") as e_file:
                self.eleitores = pickle.load(e_file)

            self.urna = Urna(list(self.eleitores.values()), list(self.candidatos.values()))
            messagebox.showinfo("Sucesso", "Urna iniciada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar os dados: {e}")

    def interface(self):
        self.urna_frame = Frame(self.root, bd=4, bg='#D3D3D3', highlightbackground='#759fe6', highlightthickness=3)
        self.urna_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.urna_info = Frame(self.urna_frame, bd=4, bg='#ffffff')
        self.urna_info.place(relx=0.02, rely=0.05, relwidth=0.5, relheight=0.9)

        self.urna_teclado = Frame(self.urna_frame, bd=4, bg='#1C1C1C')
        self.urna_teclado.place(relx=0.55, rely=0.05, relwidth=0.43, relheight=0.9)

        self.display = Entry(self.urna_info, font=("Helvetica", 18), justify="center", bg="black", fg="white", insertbackground="white")
        self.display.pack(pady=10)

        self.text_label = Label(self.urna_info, text="Informe o título do eleitor", font=("Helvetica", 12), bg="#ffffff", fg="black")
        self.text_label.pack(pady=10)

        self.cand_label = Label(self.urna_info, text="", font=("Helvetica", 12), bg="#ffffff", fg="white", wraplength=200, justify="center")
        self.cand_label.pack(pady=10)

        self.teclado()
        self.botoes()


    def teclado(self):
        botoes = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1),
        ]

        for texto, linha, coluna in botoes:
            Button(self.urna_teclado, text=texto, font=("Arial", 10, "bold"), bg="#000000", fg="#FFFFFF",
                command=lambda t=texto: self.add_to_display(t)).place(
                relx=0.05 + coluna * 0.3, rely=0.1 + linha * 0.15, relwidth=0.25, relheight=0.1
            )

    def listar_eleitores(self):
        if not self.eleitores:
            messagebox.showerror("Erro", "Nenhum dado encontrado.")
            return

        E_str = "Eleitores Disponíveis:\n"
        for eleitor in self.eleitores:
            E_str += f"Título: {eleitor.get_titulo()} - Nome: {eleitor.get_nome()}\n"

        messagebox.showinfo("Eleitores", E_str)

    def buscar_eleitor(self):
        if self.urna is None:
            messagebox.showerror("Erro", "Os dados ainda não foram encontrados.")
            return

        tit = self.display.get()
        if not tit.isdigit():
            messagebox.showerror("Erro", "Título do eleitor deve ser um número.")
            return

        eleitor = self.urna.get_eleitor(int(tit))
        if eleitor:
            if eleitor.ja_votou:
                messagebox.showerror("Erro", "Esse eleitor já realizou o voto.")
                self.e_atual = None
                self.txt_label.config(text="Nenhum eleitor selecionado.")
            else:
                self.e_atual = eleitor
                self.update_side_window(eleitor)
        else:
            self.e_atual = None
            messagebox.showerror("Erro", "Eleitor não encontrado.")
        self.display.delete(0, END)

    def botoes(self):
        Button(self.urna_teclado, text='BRANCO', font=("Arial", 12, "bold"), bg='#ffffff', fg='black',
            command=lambda: self.voto_especial('BRANCO')).place(relx=0.02, rely=0.7, relwidth=0.29, relheight=0.1)
        
        Button(self.urna_teclado, text='CORRIGE', font=("Arial", 12, "bold"), bg='#FF4500', fg='black',
            command=self.corrige).place(relx=0.34, rely=0.7, relwidth=0.29, relheight=0.1)
        
        Button(self.urna_teclado, text='CONFIRMA', font=("Arial", 12, "bold"), bg='#3CB371', fg='black',
            command=self.confirmar).place(relx=0.66, rely=0.7, relwidth=0.33, relheight=0.1) # alterar altura do botao

        Button(self.urna_teclado, text='LISTAR ELEITORES', font=("Arial", 10, "bold"), bg='#1E90FF', fg='black',
            command=self.listar_eleitores).place(relx=0.02, rely=0.82, relwidth=0.96, relheight=0.08)

        Button(self.urna_teclado, text='SELECIONAR ELEITOR', font=("Arial", 10, "bold"), bg='#FFFF00', fg='black',
            command=self.buscar_eleitor).place(relx=0.02, rely=0.91, relwidth=0.96, relheight=0.08)
    
    def add_to_display(self, value):
        self.display.insert(END, value)

    def corrige(self):
        self.display.delete(0, END)

    def branco(self):
        self.registrar_voto_especial(0)

    def confirmar(self):
        if not self.e_atual:
            messagebox.showerror("Erro", "Nenhum eleitor foi selecionado.")
            return

        try:
            num_cand = int(self.display.get())
            self.urna.registrar_voto(self.e_atual, num_cand)

            self.salvar()

            messagebox.showinfo("Sucesso", "Seu voto foi registrado!") 

            self.e_atual = None
            self.txt_label.config(text="Nenhum eleitor selecionado.")
            self.cand_label.config(text="")

            self.display.delete(0, END)
        except ValueError:
            messagebox.showerror("Erro", "Número inválido!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def voto_especial(self, tipo):
        if not self.e_atual:
            messagebox.showerror("Erro", "Nenhum eleitor foi selecionado.")
            return

        try:
            if tipo == "BRANCO":
                self.urna.registrar_voto(self.e_atual, 0)
            elif tipo == "NULO":
                self.urna.registrar_voto(self.e_atual, -1)

            self.salvars()

            messagebox.showinfo("Sucesso", f"Seu voto {tipo.lower()} foi registrado!")

            self.e_atual = None
            self.txt_label.config(text="Nenhum eleitor selecionado.")
            self.cand_label.config(text="")

            self.display.delete(0, END)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def update_side_window(self, eleitor):
        self.txt_label.config(text=f"Eleitor: {eleitor.get_nome()}\nTítulo: {eleitor.get_titulo()}")
        self.cand_label.config(
            text="Escolha o candidato a votar:\n" + "\n".join([f"{c.get_numero()} - {c.get_nome()}" for c in self.candidatos])
        )
    
    def salvar(self):
        with open("votos.pkl", "wb") as arquivo:
            pickle.dump(self.urna._Urna__votos, arquivo)

        with open("votos.txt", "w") as arquivo_txt:
            arquivo_txt.write("Resultado da Votação:\n")
            for candidato, votos in self.urna._Urna__votos.items():
                arquivo_txt.write(f"{candidato}: {votos} votos\n")

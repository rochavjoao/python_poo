import tkinter as tk

root = tk.Tk()

# titulo da janela principal
root.title('Urna')

l_janela = 600
a_janela = 400

# obtém a dimensão da tela
l_tela = root.winfo_screenwidth()
a_tela = root.winfo_screenheight()

# encontrar o ponto central
x = int(l_tela/2 - l_janela/2)
y = int(a_tela/2 - a_janela/2)

# definir a posição da janela para o centro da tela
root.geometry(f'{l_janela}x{a_janela}+{x}+{y}')

# deixa a janela com tamanho fixo sem poder redimensionar
root.resizable(False, False)

# inserir uma logo para a janela !!!!! ESTÁ DANDO ERRO !!!!!
# root.iconbitmap('./assets/logo.ico')

# mantenha a janela exibindo
root.mainloop()
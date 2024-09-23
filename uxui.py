import tkinter
import customtkinter
import sys
import os
from app import startDisconnect  # Importa a função de lógica

#Importa o caminho absoluto para o apk
if getattr(sys, 'frozen', False):
        # O executável gerado pelo Nuitka usa sys.frozen para indicar que foi empacotado
        caminho_base = sys._MEIPASS  # Usado para empacotamento como executável

else:
        caminho_base = os.path.dirname(os.path.abspath(__file__))
    # Define o caminho absoluto do ícone
icon_path = os.path.join(caminho_base, "derruba.ico")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("300x250")
app.title("Desconectar Usuário")
app.iconbitmap(icon_path)
font = customtkinter.CTkFont(family="Cascadia", size=16)


# UI Elements
# Texto Inserir usuário
insiratxt = customtkinter.CTkLabel(app, text="Insira seu usuário:")
insiratxt.pack(padx=10, pady=20, anchor=tkinter.CENTER)

# Input usuário
user_entry = customtkinter.CTkEntry(app, width=150, height=10)
user_entry.pack(padx=5, pady=5, anchor=tkinter.CENTER)

# Barra de Progresso
progress = customtkinter.CTkProgressBar(app)
progress.pack(padx=5, pady=10, anchor=tkinter.CENTER)
progress.set(0)

#Log de Sucesso
success_label = customtkinter.CTkLabel(app, text="")
success_label.pack(padx=10, pady=10, anchor=tkinter.CENTER)

# Função para ser chamada pelo botão
def on_disconnect():
    target_user = user_entry.get()
    startDisconnect(target_user, progress, success_label)

# Texto Desconectar
disconnect = customtkinter.CTkButton(app, text="Desconectar", command=on_disconnect)
disconnect.pack(padx=5, pady=5, anchor=tkinter.CENTER)

#Atalho de tecla
app.bind('<Return>', lambda event: on_disconnect())

# Run App
app.mainloop()
import tkinter
import customtkinter
import subprocess
import os


def startDisconnect():
    target_user = user.get()
    host_list = [
        '172.16.0.201',
        '172.16.0.202',
        '172.16.0.203',
        '172.16.0.204',
        '172.16.0.205',
        '172.16.0.206'
    ]

    for host in host_list:
        progress.start()
        progress.set(value=25)
        try:
            #Caminho para o script para encontrar/resetar usuário
            script_path = 'find_sessionid.ps1'
            reset_path = 'reset_session.ps1'
            command = [
                "powershell.exe",
                 "-WindowStyle",
                 "Hidden",
                 "-NoProfile",
                 "-ExecutionPolicy",
                 "Bypass",
                 "-File",os.path.join(os.getcwd(), script_path),
                 '-arg_user', target_user.lower(),
                 '-arg_host',host
            ]
            result = subprocess.run(command,
                                    capture_output=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW)
            data = int(result.stdout.decode('utf-8'))
            command_kill = [
                "powershell.exe",
                "-WindowStyle",
                "Hidden",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File", os.path.join(os.getcwd(),reset_path),
                '-sessionId', str(data),
                '-arg_host', host
            ]
            subprocess.run(command_kill,
                           capture_output=True,
                           creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as e:
            print(f"Usuário não encontrado no servidor {host}")
            progress.set(value=100)
        progress.stop()


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
#App Frame
app = customtkinter.CTk()
app.geometry("300x250")
app.title("Desconectar Usuário")
font = customtkinter.CTkFont(family="Cascadia", size=16)
app.iconbitmap("derruba.ico")
#UI Elements
#Texto Inserir usuário
insiratxt = customtkinter.CTkLabel(app, text="Insira seu usuário:")
insiratxt.pack(padx=10, pady=20, anchor=tkinter.CENTER)
#Input usuário
user = customtkinter.CTkEntry(app, width=150, height=10)
user.pack(padx=5, pady=5, anchor=tkinter.CENTER)
#Texto Desconectar
disconnect = customtkinter.CTkButton(app, text="Desconectar", command=startDisconnect)
disconnect.pack(padx=5, pady=5, anchor=tkinter.CENTER)
#Barra de Progresso
progress = customtkinter.CTkProgressBar(app)
progress.pack(padx=5, pady=10, anchor=tkinter.CENTER)
progress.set(0)
#Run App
app.mainloop()

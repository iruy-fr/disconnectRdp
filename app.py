import subprocess

host_list = [
    '172.16.0.201',
    '172.16.0.202',
    '172.16.0.203',
    '172.16.0.204',
    '172.16.0.205',
    '172.16.0.206'
]


def startDisconnect(target_user, progress, success_label):
    user_found = False  #Parâmetro para a success_label

    for host in host_list:
        progress.set(value=0)
        progress.set(value=25)

        try:
            # Busca o usuário no servidor
            command = [
                "powershell.exe",
                '-ExecutionPolicy',
                'Unrestricted',
                '-File', '//SRVDA01/Pictures/Derruba/find_sessionid.ps1',
                '-arg_user', target_user.lower(),
                '-arg_host', host
            ]
            progress.set(value=50)
            result = subprocess.run(command,
                                    capture_output=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW)
            data = result.stdout.decode('utf-8').strip()

            # Se o usuário foi encontrado (se a saída contiver um sessionId válido) mata
            if data.isdigit():

                command_kill = [
                    "powershell.exe",
                    '-ExecutionPolicy',
                    'Unrestricted',
                    '-File', '//SRVDA01/Pictures/Derruba/reset_session.ps1',
                    '-sessionId', str(data),
                    '-arg_host', host
                ]

                progress.set(value=75)
                subprocess.run(command_kill,
                               capture_output=True,
                               creationflags=subprocess.CREATE_NO_WINDOW)
                progress.set(value=100)
                user_found = True
                success_label.configure(text=f"Usuário {target_user} \n desconectado do servidor {host}")

                break

        except Exception as e:
            success_label.configure(text=f"Erro ao desconectar usuário {target_user} no servidor {host}: {e}", fg="red")

    # Se o usuário não foi encontrado em nenhum servidor
    if not user_found:
        success_label.configure(text=f"Usuário {target_user} \n não encontrado em nenhum servidor")

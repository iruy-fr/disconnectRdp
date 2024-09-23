import subprocess

def startDisconnect(target_user, progress, success_label):
    host_list = [
        '172.16.0.201',
        '172.16.0.202',
        '172.16.0.203',
        '172.16.0.204',
        '172.16.0.205',
        '172.16.0.206'
    ]

    user_found = False  # Variável para rastrear se o usuário foi encontrado

    for host in host_list:
        progress.set(value=0)
        progress.set(value=25)
        try:
            # Caminho para o script para encontrar/resetar usuário
            script_path = "find_sessionid.ps1"
            reset_path = "reset_session.ps1"
            command = [
                "powershell.exe",
                "-File", script_path,
                '-arg_user', target_user.lower(),
                '-arg_host', host
            ]
            progress.set(value=50)
            result = subprocess.run(command,
                                    capture_output=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW)
            data = result.stdout.decode('utf-8').strip()

            # Verifica se o usuário foi encontrado (se a saída contiver um sessionId válido)
            if data.isdigit():
                command_kill = [
                    "powershell.exe",
                    "-File", reset_path,
                    '-sessionId', str(data),
                    '-arg_host', host
                ]
                progress.set(value=75)
                subprocess.run(command_kill,
                               capture_output=True,
                               creationflags=subprocess.CREATE_NO_WINDOW)
                progress.set(value=100)
                success_label.configure(text=f"Usuário {target_user} \n desconectado do servidor {host}")
                user_found = True  # Usuário foi encontrado e desconectado
                break  # Para de procurar em outros hosts após desconectar o usuário

        except Exception as e:
            print(f"Erro ao desconectar usuário no servidor {host}: {e}")

    # Se o usuário não foi encontrado em nenhum servidor
    if not user_found:
        success_label.configure(text=f"Usuário {target_user} \n não encontrado em nenhum servidor")

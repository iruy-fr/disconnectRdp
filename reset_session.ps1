param (
[string]$sessionId,
[string]$arg_host
)

# Executa o comando query user e filtra o resultado para obter o ID da sessão do usuário
$queryResult = reset session $sessionId /server:$arg_host

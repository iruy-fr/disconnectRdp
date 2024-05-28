param (
[int]$sessionId,
[string]$arg_host
)
# Executa o comando reset session para derrubar o usuario
reset session $sessionId /server:$arg_host
param (
[string]$arg_user,
[string]$arg_host)

# Executa o comando query user e filtra o resultado para obter o ID da sessão do usuário
$queryResult = query user $arg_user /server:$arg_host

if ($queryResult) {
    $words = $queryResult -split '\s+'
    # Extrai o ID da sessão do resultado
    $sessionId = $words | Where-Object { $_ -match '^\d{3}$' }
    Write-Output $sessionId
} else {
    Write-Output "Usuário não encontrado"
}
param (
[string]$arg_user,
[string]$arg_host)

# Executa o comando query session e filtra o resultado para obter o ID da sessão do usuário
$queryResult = query session $arg_user /server:$arg_host

if ($queryResult) {
    $words = $queryResult -split '\s+'
    # Extrai o ID da sessão do resultado
    $sessionId = $words | Where-Object { $_ -match '^\d{2,3}$' }
    Write-Output $sessionId
} else {
    Write-Output "Usuário não encontrado"
}
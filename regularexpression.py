import re

texto = "joao teste1@gmail.co maria teste2@gmail.com adolfo teste3@protonmail.com"

padrao_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3,}"

emails_encontrados = re.findall(padrao_email, texto)

print(emails_encontrados)

# Neste exemplo, utilizamos uma expressão regular para encontrar todos os endereços de e-mail em um texto. O padrão r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3,}" é projetado para corresponder a uma ampla variedade de endereços de e-mail, incluindo domínios com três ou mais caracteres após o ponto. Note que o primeiro caso teste1@gmail.co não retomará nada, tendo em vista que procuramos o conjunto com domínio de três ou mais caracteres


# Exemplo de Uso de Regex para Encontrar CPFs:

import re

lista_cpfs = [
    "Fjwf: 000.000.000-11",
    "rfjkfrfjk 239.458.234-10",
    "ejkjefke 09812345691",
    "cpf invalido 984395930111",
]

padrao_cpf = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"

cpfs = []

for texto in lista_cpfs:
    cpfs.append(re.findall(padrao_cpf, texto))

print(cpfs)

# Neste exemplo, usamos uma expressão regular para encontrar CPFs em uma lista de strings. O padrão r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b" corresponde a CPFs em diferentes formatos, incluindo aqueles com ou sem pontos e hífen.

import re

class Linha():
    animais = []
    def __init__(self):
        self.animais = []

def cpf_valido(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Verificar o primeiro dígito verificador
    if int(cpf[9]) != digito1:
        return False

    # Calcular o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verificar o segundo dígito verificador
    if int(cpf[10]) != digito2:
        return False

    # CPF válido
    return True

def email_valido(email):
    # Expressão regular para validar o formato do e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verificar se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
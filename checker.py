# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:29:19 2024

@author: Eduardo
"""
import re
from datetime import datetime

def verificar_cpf(cpf: str) -> bool:
    # Verificar se o CPF tem 11 dígitos e é composto apenas de números
    if not cpf.isdigit() or len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0

    # Calcular o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0

    # Verificar se os dígitos calculados são iguais aos dígitos do CPF
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"



def verificar_email(email: str) -> bool:
    # Expressão regular para verificar a sintaxe do email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Verificar se o email corresponde ao padrão da regex
    if re.match(regex, email):
        return True
    else:
        return False
    
def verificar_nome_completo(nome: str) -> bool:
    # Dividir o nome em palavras
    palavras = nome.split()
    
    # Verificar se há pelo menos duas palavras
    if len(palavras) < 2:
        return False

    # Verificar se todas as palavras contêm apenas letras e começam com maiúsculas
    for palavra in palavras:
        if not palavra.isalpha() or not palavra.istitle():
            return False
    
    return True


def verificar_endereco(endereco: str) -> bool:
    # Dividir o endereço em partes
    partes = endereco.split(',')
    
    # Verificar se há pelo menos cinco partes
    if len(partes) < 5:
        return False
    
    # Remover espaços extras
    partes = [parte.strip() for parte in partes]
    
    # Verificar nome da rua
    nome_rua = partes[0]
    if not re.match(r'^[A-Za-z\s]+$', nome_rua):
        return False
    
    # Verificar número
    numero = partes[1]
    if not numero.isdigit():
        return False
    
    # Verificar bairro
    bairro = partes[2]
    if not re.match(r'^[A-Za-z\s]+$', bairro):
        return False
    
    # Verificar cidade
    cidade = partes[3]
    if not re.match(r'^[A-Za-z\s]+$', cidade):
        return False
    
    # Verificar estado
    estado = partes[4]
    if not re.match(r'^[A-Za-z]{2}$', estado):
        return False
    
    return True

def verificar_cidade(endereco: str) -> bool:
    if not re.match(r'^[A-Za-z\s]+$', endereco):
        return False
    return  True

def verificar_estado(endereco: str) -> bool:
    if not re.match(r'^[A-Za-z]{2}$', endereco):
        return False
    
    return True

def verificar_telefone(telefone: str) -> bool:
    # Expressão regular para verificar os formatos de telefone
    regex = r'^(0?\d{2}|\(\d{2}\))\s?\d{4,5}-\d{4}$'
    
    # Verificar se o telefone corresponde ao padrão da regex
    if re.match(regex, telefone):
        return True
    else:
        return False
    
def verificar_data_nascimento(data: str) -> bool:
    # Verificar se o formato está correto usando regex
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        return False
    
    try:
        # Tentar converter a string para um objeto datetime
        data_nascimento = datetime.strptime(data, '%d/%m/%Y')
        
        # Verificar se a data está no passado
        if data_nascimento >= datetime.now():
            return False
        
        # Verificar se a data faz sentido (ex: não pode ser 31/02/2020)
        data_formatada = data_nascimento.strftime('%d/%m/%Y')
        if data != data_formatada:
            return False
    except ValueError:
        return False
    
    return True

def verificar_data(data: str) -> bool:
    # Verificar se o formato está correto usando regex
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        return False
    
    try:
        # Tentar converter a string para um objeto datetime
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        
        # Verificar se a data não é no passado
        if data_obj <= datetime.now():
            return False

        # Verificar se a data faz sentido (ex: não pode ser 31/02/2020)
        # Ao converter e reformatar, a data deve permanecer a mesma
        data_formatada = data_obj.strftime('%d/%m/%Y')
        if data != data_formatada:
            return False
    except ValueError:
        return False
    
    return True

def verificar_cartao_credito(numero: str) -> bool:
    # Remover espaços e hífens do número do cartão
    numero = numero.replace(' ', '').replace('-', '')
    
    # Verificar se o número contém apenas dígitos e tem entre 13 e 19 dígitos
    if not re.match(r'^\d{13,19}$', numero):
        return False
    
    # Implementar o algoritmo de Luhn para validar o número do cartão
    total = 0
    reverso = numero[::-1]  # Inverter o número do cartão para processar da direita para a esquerda
    
    for i, digito in enumerate(reverso):
        n = int(digito)
        
        # Dobrar cada segundo dígito
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        
        total += n
    
    # O número do cartão é válido se a soma total for um múltiplo de 10
    return total % 10 == 0

if __name__ == "__main__":
    print(verificar_data("03/05/2025"))


    
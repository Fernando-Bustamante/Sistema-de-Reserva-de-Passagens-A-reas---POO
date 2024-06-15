# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:49:23 2024

@author: Eduardo
"""
from typing import List, Dict, Union

class CartaoDeCredito:
    def __init__(self, numero: str, cpf: str) -> None:
        self.numero = numero
        self.cpf = cpf
        self.operacoes: List[Dict[str, Union[str, float]]] = []

    def adicionar_operacao(self, descricao: str, valor: float) -> None:
        operacao = {"descricao": descricao, "valor": valor}
        self.operacoes.append(operacao)

    def listar_operacoes(self) -> List[Dict[str, Union[str, float]]]:
        return self.operacoes

    def excluir_operacao(self, descricao: str, valor: float) -> bool:
        for operacao in self.operacoes:
            if operacao['descricao'] == descricao and operacao['valor'] == valor:
                self.operacoes.remove(operacao)
                return True
        return False


class GerenciadorCartaoDeCredito:
    def __init__(self, arquivo_cartoes: str) -> None:
        self.cartoes = {}
        self._carregar_cartoes(arquivo_cartoes)

    def _adicionar_cartao(self, numero_cartao: str, cpf: str) -> None:
        if numero_cartao not in self.cartoes:
            self.cartoes[numero_cartao] = CartaoDeCredito(numero_cartao, cpf)
            print(f"Cartão {numero_cartao} adicionado com sucesso.")
        else:
            print(f"Cartão {numero_cartao} já existe.")

    def _carregar_cartoes(self, arquivo_cartoes: str) -> None:
        try:
            with open(arquivo_cartoes, 'r') as file:
                linhas = file.readlines()
                for linha in linhas:
                    numero_cartao, cpf = linha.strip().split(',')
                    self._adicionar_cartao(numero_cartao, cpf)
        except FileNotFoundError:
            print(f"Arquivo {arquivo_cartoes} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar cartões: {e}")

    def adicionar_operacao(self, numero_cartao: str, descricao: str, valor: float) -> None:
        if numero_cartao in self.cartoes:
            self.cartoes[numero_cartao].adicionar_operacao(descricao, valor)
            print(f"Operação adicionada ao cartão {numero_cartao}.")
        else:
            print(f"Cartão {numero_cartao} não encontrado.")

    def listar_operacoes(self, numero_cartao: str) -> List[Dict[str, Union[str, float]]]:
        if numero_cartao in self.cartoes:
            return self.cartoes[numero_cartao].listar_operacoes()
        else:
            print(f"Cartão {numero_cartao} não encontrado.")
            return []

    def listar_cartoes(self) -> List[str]:
        return list(self.cartoes.keys())

    def listar_cartoes_por_cpf(self, cpf: str) -> List[str]:
        return [numero for numero, cartao in self.cartoes.items() if cartao.cpf == cpf]

    def cartao_existe(self, numero_cartao: str, cpf: str) -> bool:
        return numero_cartao in self.cartoes and self.cartoes[numero_cartao].cpf == cpf
    

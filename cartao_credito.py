from typing import List, Dict, Union
import json

class CartaoDeCredito:
    def __init__(self, numero: str, cpf: str, operacoes: List[Dict[str, Union[str, float]]] = None) -> None:
        self.numero = numero
        self.cpf = cpf
        self.operacoes = operacoes if operacoes else []

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
        self.arquivo_cartoes = arquivo_cartoes
        self.cartoes: Dict[str, CartaoDeCredito] = {}
        self.__carregar_cartoes()

    def __adicionar_cartao(self, numero_cartao: str, cpf: str, operacoes: List[Dict[str, Union[str, float]]] = None) -> None:
        if numero_cartao not in self.cartoes:
            self.cartoes[numero_cartao] = CartaoDeCredito(numero_cartao, cpf, operacoes)
        else:
            print(f"Cartão {numero_cartao} já existe.")

    def __carregar_cartoes(self) -> None:
        try:
            with open(self.arquivo_cartoes, 'r') as file:
                linhas = file.readlines()
                for linha in linhas:
                    linha = linha.strip()
                    if not linha:
                        continue
                    partes = linha.split(',', 2)
                    if len(partes) < 2:
                        print(f"Linha inválida no arquivo: {linha}")
                        continue
                    numero_cartao = partes[0]
                    cpf = partes[1]
                    operacoes = json.loads(partes[2]) if len(partes) > 2 else []
                    self.__adicionar_cartao(numero_cartao, cpf, operacoes)
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_cartoes} não encontrado.")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        except Exception as e:
            print(f"Erro ao carregar cartões: {e}")

    def _atualizar_arquivo(self) -> None:
        try:
            with open(self.arquivo_cartoes, 'w') as file:
                for numero, cartao in self.cartoes.items():
                    linha = f"{cartao.numero},{cartao.cpf},{json.dumps(cartao.operacoes)}\n"
                    file.write(linha)
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

    def adicionar_operacao(self, numero_cartao: str, descricao: str, valor: float) -> None:
        if numero_cartao in self.cartoes:
            self.cartoes[numero_cartao].adicionar_operacao(descricao, valor)
            self._atualizar_arquivo()
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
        return list(self.cartoes)

    def listar_cartoes_por_cpf(self, cpf: str) -> List[str]:
        return [numero for numero, cartao in self.cartoes.items() if cartao.cpf == cpf]

    def cartao_existe(self, numero_cartao: str, cpf: str) -> bool:
        return numero_cartao in self.cartoes and self.cartoes[numero_cartao].cpf == cpf

"""
ccmanager=GerenciadorCartaoDeCredito("dados/cartão_de_credito.txt")
print(ccmanager.listar_cartoes())
"""
    def listar_cartoes_por_cpf(self, cpf: str) -> List[str]:
        return [numero for numero, cartao in self.cartoes.items() if cartao.cpf == cpf]

    def cartao_existe(self, numero_cartao: str, cpf: str) -> bool:
        return numero_cartao in self.cartoes and self.cartoes[numero_cartao].cpf == cpf

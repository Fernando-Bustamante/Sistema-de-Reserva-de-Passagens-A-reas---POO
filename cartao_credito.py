
from typing import List, Dict, Union

class CartaoDeCredito:
    def __init__(self, numero: str = "", cpf: str = ""):
        self.numero = numero
        self.cpf = cpf
        self.operacoes: List[Dict[str, Union[str, float]]] = []

    def adicionar_operacao(self, descricao: str, valor: float) -> None:
        operacao = {"descricao": descricao, "valor": valor}
        self.operacoes.append(operacao)

    def listar_operacoes(self) -> List[Dict[str, Union[str, float]]]:
        return self.operacoes

    def excluir_operacao(self, descricao: str) -> bool:
        for operacao in self.operacoes:
            if operacao['descricao'] == descricao:
                self.operacoes.remove(operacao)
                return True
        return False

class GerenciadorCartaoDeCredito:
    def __init__(self, arquivo_cartoes: str = "" ):
        self.arquivo_cartoes = arquivo_cartoes
        self.cartoes: List[CartaoDeCredito] = []
        self.__carregar_cartoes()

    def __adicionar_cartao(self, numero_cartao: str, cpf: str, operacoes: List[Dict[str, Union[str, float]]] = None) -> None:
        if not self.cartao_existe(numero_cartao, cpf):
            cc = CartaoDeCredito(numero_cartao, cpf)
            if operacoes:
                for op in operacoes:
                    cc.adicionar_operacao(op["descricao"], op["valor"])
            self.cartoes.append(cc)
        else:
            print(f"Cartão {numero_cartao} já existe.")

    def __carregar_cartoes(self) -> None:
        if self.arquivo_cartoes == "":
            print("CCM vazio")
            return None
        try:
            with open(self.arquivo_cartoes, 'r') as file:
                linhas = file.readlines()
                i = 0
                while i < len(linhas):
                    partes = linhas[i].strip().split(',')
                    numero_cartao = partes[0]
                    cpf = partes[1]
                    qoperacoes = int(partes[2])
                    operacoes = []
                    for j in range(qoperacoes):
                        operacao = linhas[i + 1 + j].strip().split(',')
                        operacoes.append({"descricao": operacao[0], "valor": float(operacao[1])})
                    i += qoperacoes + 1
                    self.__adicionar_cartao(numero_cartao, cpf, operacoes)
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_cartoes} não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar cartões: {e}")

    def atualizar_arquivo(self) -> None:
        try:
            with open(self.arquivo_cartoes, 'w') as file:
                for cartao in self.cartoes:
                    linha = f"{cartao.numero},{cartao.cpf},{len(cartao.operacoes)}\n"
                    file.write(linha)
                    for operacao in cartao.operacoes:
                        linha = f"{operacao['descricao']},{operacao['valor']}\n"
                        file.write(linha)
        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_cartoes} não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

    def adicionar_operacao(self, numero_cartao: str, cpf: str, descricao: str, valor: float) -> None:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao and cartao.cpf == cpf:
                cartao.adicionar_operacao(descricao, valor)
                self.atualizar_arquivo()
                print(f"Operação adicionada ao cartão {numero_cartao}.")
                return
        print(f"Cartão {numero_cartao} não encontrado.")

    def excluir_operacao(self, numero_cartao: str, cpf: str, descricao: str) -> bool:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao and cartao.cpf == cpf:
                sucesso = cartao.excluir_operacao(descricao)
                if sucesso:
                    self.atualizar_arquivo()
                return sucesso
        print("Não excluiu")
        return False

    def listar_operacoes(self, numero_cartao: str) -> List[Dict[str, Union[str, float]]]:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao:
                return cartao.listar_operacoes()
        print(f"Cartão {numero_cartao} não encontrado.")
        return []

    def listar_cartoes(self) -> List[str]:
        return [cartao.numero for cartao in self.cartoes]

    def listar_cartoes_por_cpf(self, cpf: str) -> List[str]:
        return [cartao.numero for cartao in self.cartoes if cartao.cpf == cpf]

    def cartao_existe(self, numero_cartao: str, cpf: str) -> bool:
        return any(cartao.numero == numero_cartao and cartao.cpf == cpf for cartao in self.cartoes)


if __name__ == "__main__":
    ccmanager = GerenciadorCartaoDeCredito("dados/cartão_de_credito.txt")
    #print(ccmanager.listar_cartoes())
    ccmanager.excluir_operacao("1234-5678-9101-1121","12", "vsf")
    ccmanager.atualizar_arquivo()

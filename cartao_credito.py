from typing import List, Dict, Union

class CartaoDeCredito:
    def __init__(self, numero: str = "", cpf: str = ""):
        self.numero = numero
        self.cpf = cpf
        self.operacoes: List[Dict[str, Union[str, float]]] = []
    
    # Método para adicionar uma operação ao cartão
    def adicionar_operacao(self, descricao: str, valor: float) -> None:
        operacao = {"descricao": descricao, "valor": valor}
        self.operacoes.append(operacao)

    # Método para listar todas as operações do cartão
    def listar_operacoes(self) -> List[Dict[str, Union[str, float]]]:
        return self.operacoes

    # Método para excluir uma operação específica com base na descrição
    def excluir_operacao(self, descricao: str) -> bool:
        for operacao in self.operacoes:
            if operacao['descricao'] == descricao:
                self.operacoes.remove(operacao)
                return True
        return False

class GerenciadorCartaoDeCredito:
    def __init__(self, arquivo_cartoes: str = ""):
        self.arquivo_cartoes = arquivo_cartoes
        self.cartoes: List[CartaoDeCredito] = []
        self.__carregar_cartoes()

    # Método privado para adicionar um cartão ao gerenciador
    def __adicionar_cartao(self, numero_cartao: str, cpf: str, operacoes: List[Dict[str, Union[str, float]]] = None) -> None:
        if not self.cartao_existe(numero_cartao, cpf):
            cc = CartaoDeCredito(numero_cartao, cpf)
            if operacoes:
                for op in operacoes:
                    cc.adicionar_operacao(op["descricao"], op["valor"])
            self.cartoes.append(cc)
        else:
            print(f"Cartão {numero_cartao} já existe.")

    # Método privado para carregar os cartões a partir de um arquivo
    def __carregar_cartoes(self) -> None:
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

    # Método para atualizar o arquivo com as informações dos cartões
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

    # Método para adicionar uma operação a um cartão específico
    def adicionar_operacao(self, numero_cartao: str, cpf: str, descricao: str, valor: float) -> bool:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao and cartao.cpf == cpf:
                cartao.adicionar_operacao(descricao, valor)
                self.atualizar_arquivo()
                print(f"Operação adicionada ao cartão {numero_cartao}.")
                return True
        print(f"Cartão {numero_cartao} não encontrado.")
        return False

    # Método para excluir uma operação de um cartão específico
    def excluir_operacao(self, numero_cartao: str, cpf: str, descricao: str) -> bool:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao and cartao.cpf == cpf:
                sucesso = cartao.excluir_operacao(descricao)
                if sucesso:
                    self.atualizar_arquivo()
                return sucesso
        print("Não excluiu")
        return False

    # Método para listar todas as operações de um cartão específico
    def listar_operacoes(self, numero_cartao: str) -> List[Dict[str, Union[str, float]]]:
        for cartao in self.cartoes:
            if cartao.numero == numero_cartao:
                return cartao.listar_operacoes()
        print(f"Cartão {numero_cartao} não encontrado.")
        return []

    # Método para listar todos os cartões
    def listar_cartoes(self) -> List[str]:
        return [cartao.numero for cartao in self.cartoes]

    # Método para listar todos os cartões associados a um CPF específico
    def listar_cartoes_por_cpf(self, cpf: str) -> List[str]:
        return [cartao.numero for cartao in self.cartoes if cartao.cpf == cpf]

    # Método para verificar se um cartão existe
    def cartao_existe(self, numero_cartao: str, cpf: str) -> bool:
        return any(cartao.numero == numero_cartao and cartao.cpf == cpf for cartao in self.cartoes)

if __name__ == "__main__":
    ccmanager = GerenciadorCartaoDeCredito("dados/cartão_de_credito.txt")
    ccmanager.listar_cartoes()
    ccmanager.atualizar_arquivo()

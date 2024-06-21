import tkinter as tk
from tkinter import messagebox
from typing import List, Dict, Optional
import checker as ck  

class Passagem:
    def __init__(self, codigo_voo: str, data: str, horario: str, modelo_aviao: str, portao_embarque: str,
                 cidade_origem: str, estado_origem: str, cidade_destino: str, estado_destino: str,
                 assentox: str, assentoy: str):
        self.codigo_voo = codigo_voo
        self.data = data
        self.horario = horario
        self.modelo_aviao = modelo_aviao
        self.portao_embarque = portao_embarque
        self.cidade_origem = cidade_origem
        self.estado_origem = estado_origem
        self.cidade_destino = cidade_destino
        self.estado_destino = estado_destino
        self.assentox = assentox
        self.assentoy = assentoy

    def to_dict(self) -> Dict[str, str]:
        return {
            'codigo_voo': self.codigo_voo,
            'data': self.data,
            'horario': self.horario,
            'modelo_aviao': self.modelo_aviao,
            'portao_embarque': self.portao_embarque,
            'cidade_origem': self.cidade_origem,
            'estado_origem': self.estado_origem,
            'cidade_destino': self.cidade_destino,
            'estado_destino': self.estado_destino,
            'assentox': self.assentox,
            'assentoy': self.assentoy
        }

class Usuario:
    def __init__(self, nome: str = "", cpf: str = "", data_nascimento: str = "", email: str = "",
                 endereco: str = "", telefone: str = "", cartao_credito: str = "", senha: str = ""):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
        self.cartao_credito = cartao_credito
        self.senha = senha  # Consider hashing the password in real applications
        self.passagens: List[Passagem] = []

    def adicionar_passagem(self, passagem: Passagem) -> None:
        self.passagens.append(passagem)

    def listar_passagens(self) -> List[Dict[str, str]]:
        return [passagem.to_dict() for passagem in self.passagens]

    def to_dict(self) -> Dict[str, str]:
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento,
            'email': self.email,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'cartao': self.cartao_credito,
            'senha': self.senha,
            'passagens': self.listar_passagens(),
        }

    def comparar_cpf(self, cpf: str) -> bool:
        return self.cpf == cpf

    def comparar_nome(self, nome: str) -> bool:
        return self.nome == nome

    def comparar_senha(self, senha: str) -> bool:
        return self.senha == senha

class UsuarioManager:
    def __init__(self, root: tk.Tk, arquivo_usuarios: str):
        self.__usuarios: List[Usuario] = []
        self.root = root
        self.carregar_usuarios_do_arquivo(arquivo_usuarios)

    def carregar_usuarios_do_arquivo(self, arquivo_usuarios: str) -> None:
        try:
            with open(arquivo_usuarios, 'r') as file:
                linhas = file.readlines()
                usuario = None
                for linha in linhas:
                    dados = linha.strip().split(';')
                    if len(dados) == 8:  # Linha de usuário
                        if usuario:
                            self.__usuarios.append(usuario)
                        usuario = Usuario(*dados)
                    elif len(dados) == 11:  # Linha de passagem
                        if usuario:
                            passagem = Passagem(*dados)
                            usuario.adicionar_passagem(passagem)
                if usuario:
                    self.__usuarios.append(usuario)
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de usuários não encontrado")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler arquivo de usuários: {e}")

    def adicionar_usuario(self, nome: str, cpf: str, data_nascimento: str, email: str, endereco: str, telefone: str,
                           cartao_credito: str, senha: str, re_senha: str) -> bool:
        """
        Adiciona um novo usuário à lista de usuários.

        Args:
            nome (str): Nome completo do usuário.
            cpf (str): CPF do usuário.
            data_nascimento (str): Data de nascimento do usuário.
            email (str): E-mail do usuário.
            endereco (str): Endereço do usuário.
            telefone (str): Telefone do usuário.
            cartao_credito (str): Cartão de crédito do usuário.
            senha (str): Senha do usuário.
            re_senha (str): Repetição da senha do usuário.

        Returns:
            bool: True se o usuário for adicionado com sucesso, False caso contrário.
        """

        # Verifica se o nome é válido
        if not ck.verificar_nome_completo(nome):
            messagebox.showerror("Erro", "Nome inválido")
            return False

        # Verifica se o CPF é válido
        if not ck.verificar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido")
            return False

        # Verifica se o CPF já foi utilizado
        if any(usuario.cpf == cpf for usuario in self.__usuarios):
            messagebox.showerror("Erro", "CPF já foi utilizado")
            return False

        # Verifica se a data de nascimento é válida
        if not ck.verificar_data_nascimento(data_nascimento):
            messagebox.showerror("Erro", "Data de nascimento inválida")
            return False

        # Verifica se o e-mail é válido
        if not ck.verificar_email(email):
            messagebox.showerror("Erro", "E-mail inválido")
            return False

        # Verifica se o endereço é válido
        if not ck.verificar_endereco(endereco):
            messagebox.showerror("Erro", "Endereço inválido")
            return False

        # Verifica se o cartão de crédito é válido
        if not ck.verificar_cartao_credito(cartao_credito):
            messagebox.showerror("Erro", "Cartão de crédito inválido")
            return False

        # Verifica se o telefone é válido
        if not ck.verificar_telefone(telefone):
            messagebox.showerror("Erro", "Telefone inválido")
            return False

        # Verifica se as senhas coincidem
        if senha != re_senha:
            messagebox.showerror("Erro", "Senhas diferentes")
            return False 

        # Normaliza o telefone
        telefone = ck.normalizar_telefone(telefone)

        # Cria um novo usuário
        novo_usuario = Usuario(nome, cpf, data_nascimento, email, endereco, telefone, cartao_credito, senha)

        # Adiciona o novo usuário à lista de usuários
        self.__usuarios.append(novo_usuario)
        return True

    def checar_usuario(self, nome: str, senha: str) -> bool:
        if not any(usuario.comparar_nome(nome) for usuario in self.__usuarios):
            messagebox.showerror("Erro", "Nome inválido")
            return False
        elif not any(usuario.comparar_nome(nome) and usuario.comparar_senha(senha) for usuario in self.__usuarios):
            messagebox.showerror("Erro", "Senha inválido")
            return False
        return True

    def adicionar_passagem(self, cpf_usuario: str, passagem: Passagem) -> bool:
        """
        Adiciona uma passagem a um usuário específico.

        Args:
            cpf_usuario (str): CPF do usuário.
            passagem (Passagem): Passagem a ser adicionada.

        Returns:
            bool: True se a passagem foi adicionada com sucesso, False caso contrário.
        """
        usuario = next((u for u in self.__usuarios if u.cpf == cpf_usuario), None)
        if usuario:
            usuario.adicionar_passagem(passagem)
            return True
        else:
            messagebox.showerror("Erro", "Usuário não encontrado")
            return False

    def listar_usuarios(self) -> List[Dict[str, str]]:
        return [usuario.to_dict() for usuario in self.__usuarios]

    def get_usuario_logado(self, nome: str) -> Optional[Usuario]:
        """
        Obtém o usuário logado com base no nome de usuário fornecido.

        Args:
            nome (str): Nome do usuário logado.

        Returns:
            Optional[Usuario]: O objeto de usuário se encontrado, None caso contrário.
        """
        for usuario in self.__usuarios:
            if usuario.comparar_nome(nome):
                return usuario
        return None

    def salvar_usuarios_no_arquivo(self, arquivo_usuarios: str) -> None:
        try:
            with open(arquivo_usuarios, 'w') as file:
                for usuario in self.__usuarios:
                    file.write(';'.join(usuario.to_dict().values()) + '\n')
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar usuários no arquivo: {e}")
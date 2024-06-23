# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:14:16 2024

@author: Eduardo
"""

import tkinter as tk
from tkinter import messagebox
from typing import List, Dict
import checker as ck
from cartao_credito import GerenciadorCartaoDeCredito

class Passagem:
    def __init__(self, codigo_voo: str, data: str, horario: str, modelo_aviao: str, portao_embarque: str,
                 cidade_origem: str, estado_origem: str, cidade_destino: str, estado_destino: str, assentox: str, assentoy: str):
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
    def __init__(self, nome: str = "", cpf: str= "", data_nascimento: str= "", email: str= "", endereco: str= "", telefone: str= "", cartao_credito: str= "", senha: str= ""):
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
        
    def remover_passagem(self, codigo_voo: str, assentox: str, assentoy: str) -> None:
        for p in self.passagens:
            if p.codigo_voo==codigo_voo and p.assentox==assentox and p.assentoy==assentoy:
                self.passagens.remove(p)
                return None
        print("nao excluiu2")

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
            'cartao_credito': self.cartao_credito,
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
    def __init__(self, arquivo_usuarios: str = "", CCM: GerenciadorCartaoDeCredito = GerenciadorCartaoDeCredito()):
        self.__usuarios: List[Usuario] = []
        self.__ccmananger = CCM
        self.arquivo_usuarios=arquivo_usuarios
        self.__carregar_usuarios_do_arquivo(arquivo_usuarios)

    def __carregar_usuarios_do_arquivo(self, arquivo_usuarios: str) -> None:
        try:
            with open(arquivo_usuarios, 'r') as file:
                linhas = file.readlines()
                i = 0
                while i < len(linhas):
                    partes = linhas[i].strip().split(';')
                    nome = partes[0]
                    cpf = partes[1]
                    data_nascimento = partes[2]
                    email = partes[3]
                    endereco = partes[4]
                    telefone = partes[5]
                    cartao_credito = partes[6]
                    senha = partes[7]
                    qpassagem = int(partes[8])
                    passagens: List[Passagem] = []
                    for j in range(qpassagem):
                        p = linhas[i + 1 + j].strip().split(';')
                        passagens.append(Passagem(codigo_voo=p[0], data=p[1], horario=p[2], modelo_aviao=p[3], portao_embarque=p[4], cidade_origem=p[5], estado_origem=p[6], cidade_destino=p[7], estado_destino=p[8], assentox=p[9], assentoy=p[10]))
                    usuario = Usuario(nome, cpf, data_nascimento, email, endereco, telefone, cartao_credito, senha)
                    usuario.passagens.extend(passagens)
                    self.__usuarios.append(usuario)
                    i += qpassagem + 1
                    
        except FileNotFoundError:
            print("Erro", "Arquivo de usuários não encontrado")
        except Exception as e:
            print("Erro", f"Erro ao ler arquivo de usuários: {e}")
            
    def adicionar_usuario(self, nome: str, cpf: str, data_nascimento: str, email: str, endereco: str, telefone: str, cartao_credito: str, senha: str, re_senha: str) -> bool:
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
        
        # Verifica se o cartão de crédito é válido
        if not self.__ccmananger.cartao_existe(cartao_credito, cpf) :
            messagebox.showerror("Erro", "Cartão de crédito não é do usuario")
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
        #telefone = ck.normalizar_telefone(telefone)
        
        # Cria um novo usuário
        novo_usuario = Usuario(nome, cpf, data_nascimento, email, endereco, telefone, cartao_credito, senha)
        
        # Adiciona o novo usuário à lista de usuários
        self.__usuarios.append(novo_usuario)
        return True

    def checar_usuario(self, nome: str,cpf:str, senha: str) -> bool:
        if not any(usuario.comparar_nome(nome) for usuario in self.__usuarios):
            messagebox.showerror("Erro", "Nome inválido")
            return False
        elif not any(usuario.comparar_nome(nome) and usuario.comparar_cpf(cpf) for usuario in self.__usuarios):
            messagebox.showerror("Erro", "CPF inválido")
            return False
        elif not any(usuario.comparar_nome(nome) and usuario.comparar_cpf(cpf) and usuario.comparar_senha(senha) for usuario in self.__usuarios):
            messagebox.showerror("Erro", "Senha inválido")
            return False
        return True
    
        
    def modificar_usuario(self, nome_inicial: str, cpf_inicial: str, senha_inicial: str, nome: str, cpf: str,
                      data_nascimento: str, email: str, endereco: str, telefone: str,
                      cartao_credito: str, senha: str, nova_senha: str) -> bool:
        u = self.retornar_usuario(nome_inicial, cpf_inicial, senha_inicial)
        
        if u is None:  # Assuming retornar_usuario returns None if user is not found
            messagebox.showerror("Erro", "Não há usuário")
            return False

        validation_checks = [
            (ck.verificar_nome_completo, nome, "Nome inválido"),
            (ck.verificar_cpf, cpf, "CPF inválido"),
            (ck.verificar_data_nascimento, data_nascimento, "Data de nascimento inválida"),
            (ck.verificar_email, email, "E-mail inválido"),
            (ck.verificar_endereco, endereco, "Endereço inválido"),
            (ck.verificar_cartao_credito, cartao_credito, "Cartão de crédito inválido"),
            (ck.verificar_telefone, telefone, "Telefone inválido")
        ]
        
        for check, value, error_message in validation_checks:
            if value and not check(value):
                messagebox.showerror("Erro", error_message)
                return False
            
        # Verifica se o cartão de crédito é válido
        if  not (cartao_credito=="" or self.__ccmananger.cartao_existe(cartao_credito, cpf)):
            messagebox.showerror("Erro", "Cartão de crédito não é do usuario")
            return False
        
        if cpf and cpf != cpf_inicial and any(usuario.cpf == cpf for usuario in self.__usuarios):
            messagebox.showerror("Erro", "CPF já foi utilizado")
            return False
        
        if senha != senha_inicial:
            messagebox.showerror("Erro", "Senha incorreta")
            return False

        updates = {
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'email': email,
            'endereco': endereco,
            'telefone': telefone,
            'cartao_credito': cartao_credito,
            'senha': nova_senha if nova_senha else u.senha
        }
        
        for attribute, value in updates.items():
            if value:
                setattr(u, attribute, value)
        
        return True
        
        
    def retornar_usuario(self,nome:str, cpf: str, senha:str) -> Usuario:
        """
        if any(usuario.comparar_nome(nome) and usuario.comparar_cpf(cpf) and usuario.comparar_senha(senha) for usuario in self.__usuarios):
             return Usuario()
         """
        return next((usuario for usuario in self.__usuarios if (usuario.comparar_nome(nome) and usuario.comparar_cpf(cpf) and usuario.comparar_senha(senha))), Usuario())
     
    def listar_usuarios(self) -> List[Dict[str, str]]:
        return [usuario.to_dict() for usuario in self.__usuarios]
    
    def adicionar_passagem(self, cpf_usuario: str, passagem: Passagem) -> None:
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
            print("Usuário não encontrado")
            return False
        
    def excluir_passagem(self, cpf_usuario: str, numero_cc: str , inf: str) -> None:
        if(self.__ccmananger.excluir_operacao(numero_cc , cpf_usuario , inf)):
            for u in self.__usuarios:
                if u.cartao_credito==numero_cc and u.cpf==cpf_usuario :
                    info=inf.split(';')
                    u.remover_passagem(info[0], info[1], info[2])
                    self.atualizar_arquivo_usuarios()
                    return None
        print("nao excluiu")
                    
            
    
    def atualizar_arquivo_usuarios(self) -> None:
        try:
            with open(self.arquivo_usuarios, 'w') as file:
                for usuario in self.__usuarios:
                    linha_usuario = f"{usuario.nome};{usuario.cpf};{usuario.data_nascimento};{usuario.email};{usuario.endereco};{usuario.telefone};{usuario.cartao_credito};{usuario.senha};{len(usuario.passagens)}\n"
                    file.write(linha_usuario)
                    for passagem in usuario.passagens:
                        linha_passagem = f"{passagem.codigo_voo};{passagem.data};{passagem.horario};{passagem.modelo_aviao};{passagem.portao_embarque};{passagem.cidade_origem};{passagem.estado_origem};{passagem.cidade_destino};{passagem.estado_destino};{passagem.assentox};{passagem.assentoy}\n"
                        file.write(linha_passagem)
        except FileNotFoundError:
            print("Erro", "Arquivo de usuários não encontrado")
        except Exception as e:
            print("Erro", f"Erro ao atualizar arquivo de usuários: {e}")
            
    def ocupacao(self, codigo: str ="") -> List[str]:
        config =[]
        for usuario in self.__usuarios:
            for p in usuario.passagens:
                if p.codigo_voo==codigo:
                    config.append(p.assentox+","+p.assentoy)
        return config

if __name__ == "__main__":
    u=UsuarioManager( arquivo_usuarios= "dados/usuarios.txt")
    print(u.listar_usuarios())
    u.atualizar_arquivo_usuarios()

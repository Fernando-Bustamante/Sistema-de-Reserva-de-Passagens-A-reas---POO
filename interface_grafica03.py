# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:02:47 2024

@author: Eduardo
"""

from tkinter import font as tkfont
import tkinter as tk
from usuarios import UsuarioManager, Usuario, Passagem
from typing import List, Dict
from cartao_credito import GerenciadorCartaoDeCredito
from aviões.Airbus320 import Airbus320
from voo import gerenciador_voos

class Display:
    def __init__(self, root: tk.Tk):
        #construção
        self.root = root
        self.CCManager = GerenciadorCartaoDeCredito("dados/cartão_de_credito.txt")
        self.UManager = UsuarioManager("dados/usuarios.txt",self.CCManager)  # Alterar o nome do arquivo conforme necessário
        self.FManager = gerenciador_voos(root,self.UManager,self.CCManager)
        self.__user: List[str, str] = {
                'nome': "",
                'cpf': "",
                'senha': ""
            }
        self.__usuario=Usuario()
        #self.aviao=Plane(root)
        
        # começa a rodar o codigo
        self.initialize_widgets()
        self.set_start()
        
    def initialize_widgets(self):
        #my_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        # Start screen widgets
        self.mylabel1 = tk.Label(self.root, text="Aproveite nossas ofertas de passagens aéreas e programe toda a sua viagem com a GoldTrip. Aqui você vai encontrar diversas opções de voos para diversos lugares e com as melhores companhias aéreas nacionais.")
        self.mylabel2 = tk.Label(self.root, text="Consulte todas as disponibilidades e realize sua compra de maneira fácil, rápida e sem precisar sair de casa. Além das melhores tarifas, na GoldTrip você encontra dicas para deixar sua viagem ainda mais completa.")
        self.mylabel3 = tk.Label(self.root, text="Não perca tempo, reserve agora mesmo sua passagem e embarque nessa nova aventura. Reserve suas passagens no maior e melhor sistema de reservas de passagens! Planejar sua próxima viagem nunca foi tão fácil!")
        self.mylabel4 = tk.Label(self.root, text="Agora o que deseja fazer?")
        self.mybutton01 = tk.Button(self.root, text="Cadastro", command=self.set_cadastrar)
        self.mybutton02 = tk.Button(self.root, text="Login", command=self.set_logar)
        self.mybutton03 = tk.Button(self.root, text="Sair", command=self.root.destroy)

        # Login screen widgets
        self.mylabel11 = tk.Label(self.root, text="Usuário:")
        self.e1 = tk.Entry(self.root, width=50)
        self.mylabel12 = tk.Label(self.root, text="CPF(numeros apenas):")
        self.e2 = tk.Entry(self.root, width=50)
        self.mylabel13 = tk.Label(self.root, text="Senha:")
        self.e3 = tk.Entry(self.root, width=50, show='*')
        self.button04 = tk.Button(self.root, text="Retornar", command=self.set_start)
        self.button05 = tk.Button(self.root, text="Entrar", command=self.check_logar)
        
        # Register screen widgets
        self.reg_label11 = tk.Label(self.root, text="Nome completo:")
        self.reg_e1 = tk.Entry(self.root, width=50)
        self.reg_label12 = tk.Label(self.root, text="CPF (apenas os números):")
        self.reg_e2 = tk.Entry(self.root, width=50)
        self.reg_label13 = tk.Label(self.root, text="Data de nascimento (DD/MM/AAAA):")
        self.reg_e3 = tk.Entry(self.root, width=50)
        self.reg_label14 = tk.Label(self.root, text="E-mail:")
        self.reg_e4 = tk.Entry(self.root, width=50)
        self.reg_label15 = tk.Label(self.root, text="Endereço:")
        self.reg_label151 = tk.Label(self.root, text="(nome da rua, número, bairro, cidade, estado reduzido):")
        self.reg_e5 = tk.Entry(self.root, width=50)
        self.reg_label16 = tk.Label(self.root, text="Telefone:")
        self.reg_e6 = tk.Entry(self.root, width=50)
        self.reg_label17 = tk.Label(self.root, text="Cartão de crédito:")
        self.reg_e7 = tk.Entry(self.root, width=50)
        self.reg_label18 = tk.Label(self.root, text="Senha:")
        self.reg_e8 = tk.Entry(self.root, width=50, show='*')
        self.reg_label19 = tk.Label(self.root, text="Confirmar Senha:")
        self.reg_e9 = tk.Entry(self.root, width=50, show='*')
        self.reg_button04 = tk.Button(self.root, text="Retornar", command=self.set_start)
        self.reg_button05 = tk.Button(self.root, text="Criar Usuário", command=self.check_cadastrar)
        
        
        # config screen widgets
        
        self.config_label1 = tk.Label(self.root, text="Decida configurar seu perfil \n caso não queira modificar o campo deixe em branco para garantir")
        self.config_label11 = tk.Label(self.root, text="Nome completo:")
        self.config_e1 = tk.Entry(self.root, width=50)
        self.config_label12 = tk.Label(self.root, text="CPF (apenas os números):")
        self.config_e2 = tk.Entry(self.root, width=50)
        self.config_label13 = tk.Label(self.root, text="Data de nascimento (DD/MM/AAAA):")
        self.config_e3 = tk.Entry(self.root, width=50)
        self.config_label14 = tk.Label(self.root, text="E-mail:")
        self.config_e4 = tk.Entry(self.root, width=50)
        self.config_label15 = tk.Label(self.root, text="Endereço:")
        self.config_label151 = tk.Label(self.root, text="(nome da rua, número, bairro, cidade, estado reduzido):")
        self.config_e5 = tk.Entry(self.root, width=50)
        self.config_label16 = tk.Label(self.root, text="Telefone:")
        self.config_e6 = tk.Entry(self.root, width=50)
        self.config_label17 = tk.Label(self.root, text="Cartão de crédito:")
        self.config_e7 = tk.Entry(self.root, width=50)
        self.config_label18 = tk.Label(self.root, text="Senha original:")
        self.config_e8 = tk.Entry(self.root, width=50, show='*')
        self.config_label19 = tk.Label(self.root, text="Nova senha*:")
        self.config_e9 = tk.Entry(self.root, width=50, show='*')
        self.config_button1 = tk.Button(self.root, text="Retornar", command=self.set_main)
        self.config_button2 = tk.Button(self.root, text="Modificar", command=self.check_config)
        
        #passagens widgets
        self.passagem_button=tk.Button(self.root, text="Retornar", command=self.set_main)
        self.passagens_button:List[tk.Button] =[]
        
        #comprar passagem 
        self.buy_return_button=tk.Button(self.root, text="Retornar", command=self.set_main)
        self.buy_label1 = tk.Label(self.root, text="cidade,Estado(reduzido) de origem:")
        self.buy_e1 = tk.Entry(self.root, width=50)
        self.buy_label2 = tk.Label(self.root, text="cidade,Estado(reduzido) de destino:")
        self.buy_e2 = tk.Entry(self.root, width=50)
        self.buy_label3 = tk.Label(self.root, text="data:")
        self.buy_e3 = tk.Entry(self.root, width=50)
        self.buy_try=tk.Button(self.root, text="Opções", command=self.set_procurar_passagem)
        
        # Main screen widgets
        self.textmain = tk.StringVar(self.root, self.__user['nome'] +",o que deseja fazer agora?")
        self.mylabel21 = tk.Label(self.root, textvariable=self.textmain)
        self.mybutton11 = tk.Button(self.root, text="Procurar Voo", command=self.set_comprar_passagem)
        self.mybutton12 = tk.Button(self.root, text="Ver minhas passagens", command=self.set_passagens)
        self.mybutton13 = tk.Button(self.root, text="Configurar conta", command= self.set_config)
        self.mybutton14 = tk.Button(self.root, text="Deslogar", command=self.set_start)
        self.mybutton15 = tk.Button(self.root, text="Sair", command=self.root.destroy)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.grid_forget()
            #limpa as lists
        for button in self.passagens_button:
            button.destroy()
            
        self.passagens_button.clear()

        #limpa as entrys a cada passagem de tela
        self.e1.delete(0 ,tk.END)
        self.e2.delete(0 ,tk.END)
        self.e3.delete(0 ,tk.END)
        
        self.reg_e1.delete(0 ,tk.END)
        self.reg_e2.delete(0 ,tk.END)
        self.reg_e3.delete(0 ,tk.END)
        self.reg_e4.delete(0 ,tk.END)
        self.reg_e5.delete(0 ,tk.END)
        self.reg_e6.delete(0 ,tk.END)
        self.reg_e7.delete(0 ,tk.END)
        self.reg_e8.delete(0 ,tk.END)
        self.reg_e9.delete(0 ,tk.END)
        
        self.config_e1.delete(0 ,tk.END)
        self.config_e2.delete(0 ,tk.END)
        self.config_e3.delete(0 ,tk.END)
        self.config_e4.delete(0 ,tk.END)
        self.config_e5.delete(0 ,tk.END)
        self.config_e6.delete(0 ,tk.END)
        self.config_e7.delete(0 ,tk.END)
        self.config_e8.delete(0 ,tk.END)
        self.config_e9.delete(0 ,tk.END)

    def set_start(self):
        self.__usuario=Usuario()
        self.__user = {
                'nome': "",
                'cpf': "",
                'senha': ""
            }
        self.clear_widgets()
        self.mylabel1.pack()
        self.mylabel2.pack()
        self.mylabel3.pack()
        self.mylabel4.pack()
        self.mybutton01.pack()
        self.mybutton02.pack()
        self.mybutton03.pack()

    def set_logar(self):
        self.clear_widgets()
        self.mylabel11.grid(column=1, row=1)
        self.e1.grid(column=2, row=1)
        self.mylabel12.grid(column=1, row=2)
        self.e2.grid(column=2, row=2)
        self.mylabel13.grid(column=1, row=3)
        self.e3.grid(column=2, row=3)
        self.button04.grid(column=1, row=4)
        self.button05.grid(column=3, row=4)

    def check_logar(self):
        if self.UManager.checar_usuario(self.e1.get(), self.e2.get(), self.e3.get()):
           self.__usuario=self.UManager.retornar_usuario(self.e1.get(), self.e2.get(), self.e3.get())
           #print(self.__usuario.to_dict())
           self.__user['nome']=self.e1.get()
           #print(self.__user['nome'])
           self.__user['cpf']=self.e2.get()
           self.__user['senha']=self.e3.get()
           self.textmain.set(self.__user['nome'] +",o que deseja fazer agora?")
           self.set_main()

    def set_cadastrar(self):
        self.clear_widgets()
        self.reg_label11.grid(column=1, row=1)
        self.reg_e1.grid(column=2, row=1)
        self.reg_label12.grid(column=1, row=2)
        self.reg_e2.grid(column=2, row=2)
        self.reg_label13.grid(column=1, row=3)
        self.reg_e3.grid(column=2, row=3)
        self.reg_label14.grid(column=1, row=4)
        self.reg_e4.grid(column=2, row=4)
        self.reg_label15.grid(column=1, row=5)
        self.reg_label151.grid(column=1, row=6)
        self.reg_e5.grid(column=2, row=5)
        self.reg_label16.grid(column=1, row=7)
        self.reg_e6.grid(column=2, row=7)
        self.reg_label17.grid(column=1, row=8)
        self.reg_e7.grid(column=2, row=8)
        self.reg_label18.grid(column=1, row=9)
        self.reg_e8.grid(column=2, row=9)
        self.reg_label19.grid(column=1, row=10)
        self.reg_e9.grid(column=2, row=10)
        self.reg_button04.grid(column=1, row=11)
        self.reg_button05.grid(column=3, row=11)

    def check_cadastrar(self):
       if self.UManager.adicionar_usuario(
            self.reg_e1.get(),
            self.reg_e2.get(),
            self.reg_e3.get(),
            self.reg_e4.get(),
            self.reg_e5.get(),
            self.reg_e6.get(),
            self.reg_e7.get(),
            self.reg_e8.get(),
            self.reg_e9.get()
        ):
           self.__usuario=self.UManager.retornar_usuario(self.reg_e1.get(), self.reg_e2.get(), self.reg_e8.get())
           #print(self.__usuario.to_dict())
           self.__user['nome']=self.reg_e1.get()
           #print(self.__user['nome'])
           self.__user['cpf']=self.reg_e2.get()
           self.__user['senha']=self.reg_e8.get()
           self.textmain.set(self.__user['nome'] +",o que deseja fazer agora?")
           self.set_main()

    def set_main(self):
        self.clear_widgets()
        #self.__usuario=
        self.mylabel21.pack()
        self.mybutton11.pack()
        self.mybutton12.pack()
        self.mybutton13.pack()
        self.mybutton14.pack()
        self.mybutton15.pack()
        
    def set_config(self):
        self.clear_widgets()
        self.config_e1.insert(0, self.__usuario.nome)
        self.config_e2.insert(0, self.__usuario.cpf)
        self.config_e3.insert(0, self.__usuario.data_nascimento)
        self.config_e4.insert(0, self.__usuario.email)
        self.config_e5.insert(0, self.__usuario.endereco)
        self.config_e6.insert(0, self.__usuario.telefone)
        self.config_e7.insert(0, self.__usuario.cartao_credito)

        self.config_label11.grid(column=1, row=1)
        self.config_e1.grid(column=2, row=1)
        self.config_label12.grid(column=1, row=2)
        self.config_e2.grid(column=2, row=2)
        self.config_label13.grid(column=1, row=3)
        self.config_e3.grid(column=2, row=3)
        self.config_label14.grid(column=1, row=4)
        self.config_e4.grid(column=2, row=4)
        self.config_label15.grid(column=1, row=5)
        self.config_label151.grid(column=1, row=6)
        self.config_e5.grid(column=2, row=5)
        self.config_label16.grid(column=1, row=7)
        self.config_e6.grid(column=2, row=7)
        self.config_label17.grid(column=1, row=8)
        self.config_e7.grid(column=2, row=8)
        self.config_label18.grid(column=1, row=9)
        self.config_e8.grid(column=2, row=9)
        self.config_label19.grid(column=1, row=10)
        self.config_e9.grid(column=2, row=10)
        self.config_button1.grid(column=1, row=11)
        self.config_button2.grid(column=3, row=11)
        
    def check_config(self):
        if(self.UManager.modificar_usuario(nome_inicial=self.__user['nome'],
                                        cpf_inicial=self.__user['cpf'],
                                        senha_inicial=self.__user['senha'],
                                        nome=self.config_e1.get(),
                                        cpf=self.config_e2.get(),
                                        data_nascimento=self.config_e3.get(),
                                       email=self.config_e4.get(),
                                       endereco=self.config_e5.get(),
                                       telefone=self.config_e6.get(),
                                       cartao_credito=self.config_e7.get(),
                                       senha=self.config_e8.get(),
                                       nova_senha=self.config_e9.get())):
            if(self.config_e9.get()==""):
                self.__user['nome']=self.config_e1.get()
                self.__user['cpf']=self.config_e2.get()
            else:
                self.__user['nome']=self.config_e1.get()
                #print(self.__user['nome'])
                self.__user['cpf']=self.config_e2.get()
                self.__user['senha']=self.config_e9.get()
            self.UManager.atualizar_arquivo_usuarios()
            self.__usuario=self.UManager.retornar_usuario(self.__user['nome'],self.__user['cpf'],self.__user['senha'])
            self.set_main()
            
    def set_passagens(self):
        self.clear_widgets()
        
        self.passagem_button.grid(column=1, row=1)
        
        # Canvas and Scrollbar
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=2, column=1, columnspan=2, sticky="nsew")
        self.scrollbar.grid(row=2, column=3, sticky="ns")

        for passagem in self.__usuario.passagens:
            button = tk.Button(
                self.scrollable_frame,
                height=10,
                width=20,
                command=lambda inf=passagem.codigo_voo + ' ' + passagem.assentox + '' + passagem.assentoy: self.cancelar_passagem(inf),
                text=f"Código do Voo: {passagem.codigo_voo}\nData: {passagem.data}\nHorário: {passagem.horario}\nModelo do Avião: {passagem.modelo_aviao}\nPortão de Embarque: {passagem.portao_embarque}\nOrigem: {passagem.cidade_origem}/{passagem.estado_origem}\nDestino: {passagem.cidade_destino}/{passagem.estado_destino}\nAssento: {passagem.assentox}{passagem.assentoy}"
            )
            self.passagens_button.append(button)

        for i, button in enumerate(self.passagens_button):
            button.grid(column=0, row=i, padx=5, pady=5)
            

       
    def set_comprar_passagem(self):
        self.clear_widgets()
        self.buy_return_button.grid(column=1, row=1)
        self.buy_label1.grid(column=2, row=2)
        self.buy_e1.grid(column=3, row=2)
        self.buy_label2.grid(column=2, row=3)
        self.buy_e2.grid(column=3, row=3)
        self.buy_label3.grid(column=2, row=4)
        self.buy_e3.grid(column=3, row=4)
        self.buy_try.grid(column=4, row=5)
        
    def set_procurar_passagem(self):
        12
        
    def set_aviao(self):
        12
        #self.aviao.create_plane_widget()
        

if __name__ == "__main__":
    root = tk.Tk()
    display = Display(root)
    root.mainloop()

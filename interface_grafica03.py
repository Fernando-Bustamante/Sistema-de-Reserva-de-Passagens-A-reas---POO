# -*- coding: utf-8 -*-


import tkinter as tk
from usuarios import UsuarioManager, Usuario, Passagem
from typing import List, Dict
from cartao_credito import GerenciadorCartaoDeCredito
from aviões.Airbus320 import Airbus320
from tkinter import messagebox
from tkinter import font as tkfont
from voo import gerenciador_voos
import checker as ck

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
        
        # começa a rodar o codigo
        self.initialize_widgets()
        self.set_start()
        
    def initialize_widgets(self)-> None:
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
        self.buy_label21= tk.Label(self.root, text="Obs.: sem espaco fora se tiver no meio do nome das cidades")
        self.buy_e2 = tk.Entry(self.root, width=50)
        self.buy_label3 = tk.Label(self.root, text="data(DD/MM/AAAA):")
        self.buy_e3 = tk.Entry(self.root, width=50)
        self.buy_try=tk.Button(self.root, text="Opções", command=self.set_procurar_passagem)
        self.passagens_comprar_button:List[tk.Button] =[]
        self.passagens_comprar:List[Dict[str,str]] = []
        
        # Main screen widgets
        self.textmain = tk.StringVar(self.root, self.__user['nome'] +",o que deseja fazer agora?")
        self.mylabel21 = tk.Label(self.root, textvariable=self.textmain)
        self.mybutton11 = tk.Button(self.root, text="Procurar Voo", command=self.set_comprar_passagem)
        self.mybutton12 = tk.Button(self.root, text="Ver minhas passagens", command=self.set_passagens)
        self.mybutton13 = tk.Button(self.root, text="Configurar conta", command= self.set_config)
        self.mybutton14 = tk.Button(self.root, text="Deslogar", command=self.set_start)
        self.mybutton15 = tk.Button(self.root, text="Sair", command=self.root.destroy)

    def clear_widgets(self)-> None:
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.grid_forget()
            #limpa as lists
        for button in self.passagens_button:
            button.destroy()
        self.passagens_button.clear()
        for button in self.passagens_comprar_button:
            button.destroy()
        self.passagens_comprar_button.clear()

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
        
        self.config_e2.configure(state="normal")
        self.config_e2.configure(state="normal")
        self.config_e2.configure(state="normal")
        
        self.config_e1.delete(0 ,tk.END)
        self.config_e2.delete(0 ,tk.END)
        self.config_e3.delete(0 ,tk.END)
        self.config_e4.delete(0 ,tk.END)
        self.config_e5.delete(0 ,tk.END)
        self.config_e6.delete(0 ,tk.END)
        self.config_e7.delete(0 ,tk.END)
        self.config_e8.delete(0 ,tk.END)
        self.config_e9.delete(0 ,tk.END)
        

    def set_start(self)-> None:
        self.__usuario=Usuario()
        self.__user = {
                'nome': "",
                'cpf': "",
                'senha': ""
            }
        self.buy_e1.delete(0 ,tk.END)
        self.buy_e2.delete(0 ,tk.END)
        self.buy_e3.delete(0 ,tk.END)
        self.clear_widgets()
        self.mylabel1.pack()
        self.mylabel2.pack()
        self.mylabel3.pack()
        self.mylabel4.pack()
        self.mybutton01.pack()
        self.mybutton02.pack()
        self.mybutton03.pack()

    def set_logar(self)-> None:
        self.clear_widgets()
        self.mylabel11.grid(column=1, row=1)
        self.e1.grid(column=2, row=1)
        self.mylabel12.grid(column=1, row=2)
        self.e2.grid(column=2, row=2)
        self.mylabel13.grid(column=1, row=3)
        self.e3.grid(column=2, row=3)
        self.button04.grid(column=1, row=4)
        self.button05.grid(column=3, row=4)

    def check_logar(self)-> None:
        if self.UManager.checar_usuario(self.e1.get(), self.e2.get(), self.e3.get()):
           self.__usuario=self.UManager.retornar_usuario(self.e1.get(), self.e2.get(), self.e3.get())
           #print(self.__usuario.to_dict())
           self.__user['nome']=self.e1.get()
           #print(self.__user['nome'])
           self.__user['cpf']=self.e2.get()
           self.__user['senha']=self.e3.get()
           self.textmain.set(self.__user['nome'] +",o que deseja fazer agora?")
           self.set_main()

    def set_cadastrar(self)-> None:
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

    def check_cadastrar(self)-> None:
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

    def set_main(self)-> None:
        self.clear_widgets()
        self.buy_e1.delete(0 ,tk.END)
        self.buy_e2.delete(0 ,tk.END)
        self.buy_e3.delete(0 ,tk.END)
        #self.__usuario=
        self.mylabel21.pack()
        self.mybutton11.pack()
        self.mybutton12.pack()
        self.mybutton13.pack()
        self.mybutton14.pack()
        self.mybutton15.pack()
        
    def set_config(self)-> None:
        self.clear_widgets()
        self.config_e1.insert(0, self.__usuario.nome)
        self.config_e1.configure(state="disabled")
        self.config_e2.insert(0, self.__usuario.cpf)
        self.config_e2.configure(state="disabled")
        self.config_e3.insert(0, self.__usuario.data_nascimento)
        self.config_e3.configure(state="disabled")
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
        
    def check_config(self) -> None:
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
        
    def set_passagens(self) -> None:
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
                width=25,
                command=lambda inf=passagem.codigo_voo +';'+ passagem.assentox +';'+ passagem.assentoy: self.cancelar_passagem(inf),
                text=f"Código do Voo: {passagem.codigo_voo}\nData: {passagem.data}\nHorário: {passagem.horario}\nModelo do Avião: {passagem.modelo_aviao}\nPortão de Embarque: {passagem.portao_embarque}\nOrigem: {passagem.cidade_origem}/{passagem.estado_origem}\nDestino: {passagem.cidade_destino}/{passagem.estado_destino}\nAssento: {passagem.assentox}{passagem.assentoy}"
            )
            self.passagens_button.append(button)

        for i, button in enumerate(self.passagens_button):
            button.grid(column=0, row=i, padx=5, pady=5)
            
    def cancelar_passagem(self, inf: str) -> None:
        result = tk.messagebox.askquestion("Cancelamento", "Você realmente deseja cancelar essa passagem?")
        if result == 'yes':
            print(inf)
            self.UManager.excluir_passagem(self.__usuario.cpf,self.__usuario.cartao_credito , inf)
            self.FManager.autualizar_voo()
            self.set_main()
            
            
    def set_comprar_passagem(self) -> None:
        self.clear_widgets()
        self.buy_return_button.grid(column=1, row=1)
        self.buy_label1.grid(column=2, row=2)
        self.buy_e1.grid(column=3, row=2)
        self.buy_label2.grid(column=2, row=3)
        self.buy_label21.grid(column=2, row=4)
        self.buy_e2.grid(column=3, row=3)
        self.buy_label3.grid(column=2, row=5)
        self.buy_e3.grid(column=3, row=5)
        self.buy_try.grid(column=4, row=6)
        
    def set_procurar_passagem(self) -> None:
        end1=(self.buy_e1.get()).split(',')
        end2=(self.buy_e2.get()).split(',')
        if not ck.verificar_cidade(end1[0].strip()):
            messagebox.showerror("Erro", "cidade de origem invalida")
            return None
        elif not ck.verificar_estado(end1[1].strip()):
            messagebox.showerror("Erro", "estado de origem invalido")
            return None
        elif not ck.verificar_cidade(end2[0].strip()):
            messagebox.showerror("Erro", "cidade de destino invalida")
            return None
        elif not ck.verificar_estado(end2[1].strip()):
            messagebox.showerror("Erro", "estado de destino invalido")
            return None
        elif not ck.verificar_data(self.buy_e3.get()):
            messagebox.showerror("Erro", "data invalida")
            return None
        
        
        if self.FManager.Procurar_voo(data=self.buy_e3.get(), c_origem=end1[0].strip(), e_origem=end1[1].strip(), c_destino=end2[0].strip(), e_destino=end2[1].strip()):
           for button in self.passagens_comprar_button:
               button.destroy()
           self.passagens_comprar_button.clear()
           self.passagens_comprar = self.FManager.Listar_voos(data=self.buy_e3.get(), c_origem=end1[0], e_origem=end1[1], c_destino=end2[0], e_destino=end2[1])

           for i, passagem in enumerate(self.passagens_comprar):
               button = tk.Button(
                   self.root,
                   height=10,
                   width=25,
                   command=lambda inf=passagem['codigo_voo']: self.comprar_passagem(inf),
                   text=f"Código do Voo: {passagem['codigo_voo']}\nData: {passagem['data']}\n Valor: {passagem['valor']}\nHorário: {passagem['horario']}\nModelo do Avião: {passagem['modelo_aviao']}\nPortão de Embarque: {passagem['portao_embarque']}\nOrigem: {passagem['cidade_origem']}/{passagem['estado_origem']}\nDestino: {passagem['cidade_destino']}/{passagem['estado_destino']}"
               )
               self.passagens_comprar_button.append(button)
               button.grid(column=5+int(i/3), row=i + 6, padx=5, pady=5)
        else:
           messagebox.showinfo("Indisponível", "Infelizmente não possuímos passagem para esse dia e rota")
            
    def comprar_passagem(self, codigo:str) -> None:
        result = messagebox.askquestion( "","Você deseja comprar um assento nesse voo mesmo?")
        if result == 'yes':
            info=self.FManager.get_informacao_voo(codigo)
            self.clear_widgets()
            seat=self.FManager.get_aviao(codigo).comprar_passagem()
            if seat:
                assento=seat.split(',')
                p=Passagem(codigo_voo=info['codigo_voo'], data=info['data'], horario=info['horario'], modelo_aviao=info['modelo_aviao'], portao_embarque=info['portao_embarque'], cidade_origem=info['cidade_origem'], estado_origem=info['estado_origem'], cidade_destino=info['cidade_destino'], estado_destino=info['estado_destino'], assentox=assento[0] , assentoy=assento[1])
                self.UManager.adicionar_passagem(self.__user['cpf'], p,info['valor'])
                self.FManager.autualizar_voo()
                self.set_main()
                self.UManager.atualizar_arquivo_usuarios()
            else:
                self.set_comprar_passagem()
                
        
    

if __name__ == "__main__":
    root = tk.Tk()
    display = Display(root)
    root.mainloop()

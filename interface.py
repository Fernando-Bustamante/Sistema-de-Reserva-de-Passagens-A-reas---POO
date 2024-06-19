import tkinter as tk
from tkinter import messagebox
from usuarios import UsuarioManager

class Display:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.UManager = UsuarioManager(root, "Data/usuarios.txt")  # Alterar o nome do arquivo conforme necessário
        self.initialize_widgets()
        self.set_start()
    
    def initialize_widgets(self):
        # Start screen widgets
        self.mylabel1 = tk.Label(self.root, text="Aproveite nossas ofertas de passagens aéreas e programe toda a sua viagem com a GoldTrip. Aqui você vai encontrar diversas opções de voos para diversos lugares e com as melhores companhias aéreas nacionais e internacionais.")
        self.mylabel2 = tk.Label(self.root, text="Consulte todas as disponibilidades e realize sua compra de maneira fácil, rápida e sem precisar sair de casa. Além das melhores tarifas, na GoldTrip você encontra dicas para deixar sua viagem ainda mais completa.")
        self.mylabel3 = tk.Label(self.root, text="Não perca tempo, reserve agora mesmo sua passagem e embarque nessa nova aventura. Reserve suas passagens no maior e melhor sistema de reservas de passagens! Planejar sua próxima viagem nunca foi tão fácil!")
        self.mylabel4 = tk.Label(self.root, text="Agora o que deseja fazer?")
        self.mybutton01 = tk.Button(self.root, text="Cadastro", command=self.set_cadastrar)
        self.mybutton02 = tk.Button(self.root, text="Login", command=self.set_logar)
        self.mybutton03 = tk.Button(self.root, text="Sair", command=self.root.destroy)

        # Login screen widgets
        self.mylabel11 = tk.Label(self.root, text="Usuário:")
        self.e1 = tk.Entry(self.root, width=50)
        self.mylabel12 = tk.Label(self.root, text="Senha:")
        self.e2 = tk.Entry(self.root, width=50, show='*')
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
        
        # Main screen widgets
        self.mylabel21 = tk.Label(self.root, text="Agora o que deseja fazer?")
        self.mybutton11 = tk.Button(self.root, text="Procurar Voo")
        self.mybutton12 = tk.Button(self.root, text="Ver minhas passagens", command=self.ver_passagens)
        self.mybutton13 = tk.Button(self.root, text="Configurar conta")
        self.mybutton14 = tk.Button(self.root, text="Deslogar", command=self.set_start)
        self.mybutton15 = tk.Button(self.root, text="Sair", command=self.root.destroy)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.grid_forget()

    def set_start(self):
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
        self.button04.grid(column=1, row=3)
        self.button05.grid(column=3, row=3)

    def check_logar(self):
        if self.UManager.checar_usuario(self.e1.get(), self.e2.get()):
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
            self.set_main()

    def set_main(self):
        self.clear_widgets()
        self.mylabel21.pack()
        self.mybutton11.pack()
        self.mybutton12.pack()
        self.mybutton13.pack()
        self.mybutton14.pack()
        self.mybutton15.pack()

    def ver_passagens(self):
        username = self.e1.get()
        usuario = self.UManager.get_usuario_logado(username)
        if usuario:
            self.clear_widgets()
            passagens = usuario.listar_passagens()
            if passagens:
                self.passagens_label = tk.Label(self.root, text="Suas Passagens:")
                self.passagens_label.pack()
                for passagem in passagens:
                    passagem_str = f"Voo: {passagem['codigo_voo']}, Data: {passagem['data']}, Hora: {passagem['horario']}, Origem: {passagem['cidade_origem']}, Destino: {passagem['cidade_destino']}"
                    passagem_label = tk.Label(self.root, text=passagem_str)
                    passagem_label.pack()
            else:
                self.passagens_label = tk.Label(self.root, text="Você não possui passagens cadastradas.")
                self.passagens_label.pack()
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    display = Display(root)
    root.mainloop()

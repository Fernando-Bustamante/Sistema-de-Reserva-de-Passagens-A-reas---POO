# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:35:09 2024

@author: Eduardo
"""
import tkinter as tk
class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.mylabel1=tk.Label(self.root, text="Aproveite nossas ofertas de passagens aéreas e programe toda a sua viagem com a GoldTrip. Aqui você vai encontrar diversas opções de voos para diversos lugares e com as melhores companhias aéreas nacionais e internacionais.")
        self.mylabel1.pack()
        self.mylabel2=tk.Label(self.root, text="Consulte todas as disponibilidades e realize sua compra de maneira fácil, rápida e sem precisar sair de casa. Além das melhores tarifas, na GoldTrip você encontra dicas para deixar sua viagem ainda mais completa.")
        self.mylabel2.pack()
        self.mylabel3=tk.Label(self.root, text=" Não perca tempo, reserve agora mesmo sua passagem e embarque nessa nova aventura. Reserve suas passagens no maior e melhor sistema de reservas de passagens! Planejar sua próxima viagem nunca foi tão fácil!")
        self.mylabel3.pack()
        self.mylabel4=tk.Label(self.root, text="Agora oque deseja fazer?")
        self.mylabel4.pack()
        self.mybutton01=tk.Button(self.root,text="Cadastro",command= self.set_cadastrar)
        self.mybutton01.pack()
        self.mybutton02=tk.Button(self.root,text="Login",command= self.set_logar)
        self.mybutton02.pack()
        self.mybutton03=tk.Button(self.root,text="Sair", command= self.root.destroy)
        self.mybutton03.pack()
        
        self.root.mainloop()
 
    def clear_start(self):
        self.mylabel1.pack_forget()
        self.mylabel2.pack_forget()
        self.mylabel3.pack_forget()
        self.mylabel4.pack_forget()
        self.mybutton01.pack_forget()
        self.mybutton02.pack_forget()
        self.mybutton03.pack_forget()
        
    def set_start(self):
        self.mylabel1.pack()
        self.mylabel2.pack()
        self.mylabel3.pack()
        self.mylabel4.pack()
        self.mybutton01.pack()
        self.mybutton02.pack()
        self.mybutton03.pack()
             
    def set_logar(self):
        self.clear_start()
        self.mylabel11=tk.Label(self.root, text="Usuário:")
        self.mylabel11.grid(column=1, row=1)
        self.e1=tk.Entry(self.root, width= 50)
        self.e1.grid(column=2, row=1)
        self.mylabel12=tk.Label(self.root, text="Senha:")
        self.mylabel12.grid(column=1, row=2)
        self.e2=tk.Entry(self.root, width= 50)
        self.e2.grid(column=2, row=2)
        self.button04=tk.Button(self.root,text="Retornar", command= self.return_logar_start)
        self.button04.grid(column=1, row=3)
        self.button05=tk.Button(self.root,text="Entrar", command= self.check_logar)
        self.button05.grid(column=3, row=3)
       
    def clear_logar(self):
        self.mylabel11.grid_forget()
        self.e1.grid_forget()
        self.mylabel12.grid_forget()
        self.e2.grid_forget()
        self.button04.grid_forget()
        self.button05.grid_forget()
       
    def return_logar_start(self):
        self.clear_logar()
        self.set_start()
        
    def check_logar(self):
        self.clear_logar()
        self.set_main()
        
    def set_cadastrar(self):
        self.clear_start()
        self.mylabel11=tk.Label(self.root, text="Usuário:")
        self.mylabel11.grid(column=1, row=1)
        self.e1=tk.Entry(self.root, width= 50)
        self.e1.grid(column=2, row=1)
        self.mylabel12=tk.Label(self.root, text="Senha:")
        self.mylabel12.grid(column=1, row=2)
        self.e2=tk.Entry(self.root, width= 50, show='*')
        self.e2.grid(column=2, row=2)
        self.button04=tk.Button(self.root,text="Retornar", command= self.return_cadastrar_start)
        self.button04.grid(column=1, row=3)
        self.button05=tk.Button(self.root,text="Criar Usuário", command= self.check_cadastrar)
        self.button05.grid(column=3, row=3)
    
    def clear_cadastrar(self):
        self.mylabel11.grid_forget()
        self.e1.grid_forget()
        self.mylabel12.grid_forget()
        self.e2.grid_forget()
        self.button04.grid_forget()
        self.button05.grid_forget()
        
    def return_cadastrar_start(self):
        self.clear_cadastrar()
        self.set_start()
        
    def check_cadastrar(self):
        self.clear_cadastrar()
        self.set_main()
        
    def set_main(self):
        self.mylabel21=tk.Label(self.root, text="Agora oque deseja fazer?")
        self.mylabel21.pack()
        self.mybutton11=tk.Button(self.root,text="Procurar Voo")
        self.mybutton11.pack()
        self.mybutton12=tk.Button(self.root,text="Ver minhas passagens")
        self.mybutton12.pack()
        self.mybutton13=tk.Button(self.root,text="Configurar conta")
        self.mybutton13.pack()
        self.mybutton14=tk.Button(self.root,text="Deslogar", command= self.return_start_main)
        self.mybutton14.pack()
        self.mybutton15=tk.Button(self.root,text="Sair", command= self.root.destroy)
        self.mybutton15.pack()
        
    def clear_main(self):
        self.mylabel21.pack_forget()
        self.mybutton11.pack_forget()
        self.mybutton12.pack_forget()
        self.mybutton13.pack_forget()
        self.mybutton14.pack_forget()
        self.mybutton15.pack_forget()
        
    def return_start_main(self):
        self.clear_main()
        self.set_start()
        
       
       
display = Display()
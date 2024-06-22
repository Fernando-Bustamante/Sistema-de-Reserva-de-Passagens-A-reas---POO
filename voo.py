# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 07:24:55 2024

@author: Eduardo
"""
import tkinter as tk
from typing import List, Dict,Union, Tuple
from aviões.Airbus320 import Airbus320
from cartao_credito import GerenciadorCartaoDeCredito
from usuarios import UsuarioManager
from typing import Type

class gerenciador_voos:
    def __init__(self, root: tk.Tk, UM: UsuarioManager = UsuarioManager(), CCM: GerenciadorCartaoDeCredito = GerenciadorCartaoDeCredito()):
        self.root = root
        self.CCM = CCM
        self.UM = UM
        self.__voos: List[Dict[str,Union[Dict[str, str], List[str]]]] = []   
        self.__carregar__voos("dados/voos.txt")
        self.aviao=Airbus320(root)

    
    def __carregar__voos(self, arquivo_voos: str):
        try:
            with open(arquivo_voos, 'r') as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados = linha.strip().split(',')
                    v = {
                        'codigo_voo': dados[0].strip(),
                        'data': dados[1].strip(),
                        'horario': dados[2].strip(),
                        'modelo_aviao': dados[3].strip(),
                        'portao_embarque': dados[4].strip(),
                        'cidade_origem': dados[5].strip(),
                        'estado_origem': dados[6].strip(),
                        'cidade_destino': dados[7].strip(),
                        'estado_destino': dados[8].strip(),
                        'valor': dados[9].strip(),
                    }
                    # Instantiate Airbus320 assuming correct usage of arguments
                    self.__voos.append({"config":v,"ocupacao":self.UM.ocupacao(dados[0].strip())})

        except FileNotFoundError:
            print("Arquivo de usuários não encontrado")
        except Exception as e:
            print(f"Erro ao ler arquivo de voos: {e}")
    
    def to_dict(self):
        for i in self.__voos:
            print(i['config']['codigo_voo'] + i['config']['data'])
            
    def get_aviao(self, codigo: str) -> Airbus320:#chama e configura o aviao a ser usado
        for v in self.__voos:
            if v['config']['codigo_voo'] == codigo:
                self.aviao.set_seat(v['ocupacao'])
                return self.aviao
        return None  # Return None if not found
    
    def __adicionar_passagem(self):
        # Implement logic to add a ticket/passenger
        pass
        
    def comprar_passagem(self):
        # Implement logic to buy a ticket
        pass
    
    def excluir_passagem(self):
        # Implement logic to delete a ticket/passenger
        pass
                        
if __name__ == "__main__":
    root = tk.Tk()
    CCM = GerenciadorCartaoDeCredito("dados/cartão_de_credito.txt")
    UM = UsuarioManager("dados/usuarios.txt", CCM)
    gv = gerenciador_voos(root, UM, CCM)
    gv.to_dict()
    
    selected_seat = gv.get_aviao("GOL1234").comprar_passagem()  # Implement comprar_passagem() in Airbus320
    if selected_seat:
        print(f"Assento selecionado: {selected_seat}")
    else:
        print("Nenhum assento selecionado.")
    
    root.mainloop()
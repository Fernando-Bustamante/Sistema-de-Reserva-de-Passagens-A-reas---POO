# -*- coding: utf-8 -*-

import tkinter as tk
from typing import List, Dict,Union, Tuple
#from aviões.Airbus320 import Airbus320
from aviões.Avioes_config import Airbus320,Boeing777
from aviões.Avioes_set import Aviao
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
        self.avioes:Dict[str,Aviao]= {'Airbus320':Airbus320(root),'Boeing777':Boeing777(root)}
        self.aviao:Aviao 
        self.configuracao:str = ""

    
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
                    # instancie infas informacoes do aviao
                    self.__voos.append({"config":v,"ocupacao":self.UM.ocupacao(dados[0].strip())})

        except FileNotFoundError:
            print("Arquivo de usuários não encontrado")
        except Exception as e:
            print(f"Erro ao ler arquivo de voos: {e}")
    
    def to_dict(self):
        for i in self.__voos:
            print(i['config']['codigo_voo'] +""+ i['config']['data'])
            
    def get_aviao(self, codigo: str) -> Aviao: #chama e configura o aviao a ser usado
        for v in self.__voos:
            if v['config']['codigo_voo'] == codigo:
                self.aviao=self.avioes[v['config']['modelo_aviao']]
                self.aviao.set_seat(v['ocupacao'])
                return self.aviao
        return None  # Return None if not found
    
    def get_informacao_voo(self, codigo:str) -> Dict[str,str]:
        for v in self.__voos:
            if v['config']['codigo_voo']==codigo:
                return v['config']
    
    def Procurar_voo(self, data:str, c_origem:str, e_origem:str, c_destino:str, e_destino:str) -> bool:
        for v in self.__voos:
            if v['config']['cidade_origem']==c_origem and v['config']['estado_origem']==e_origem and v['config']['cidade_destino']==c_destino and v['config']['estado_destino']==e_destino:
                self.__atual_configuracao=v['config']['codigo_voo']
                return True
        return False
    
    def Listar_voos(self, data:str, c_origem:str, e_origem:str, c_destino:str, e_destino:str) -> List[Dict[str, str]]:
        L :List[Dict[str, str]]= []
        for v in self.__voos:
            if v['config']['cidade_origem']==c_origem and v['config']['estado_origem']==e_origem and v['config']['cidade_destino']==c_destino and v['config']['estado_destino']==e_destino:
                L.append(v['config'])
        return L
        
    def autualizar_voo(self)-> None:
        for v in self.__voos:
            v['ocupacao']=self.UM.ocupacao(v['config']['codigo_voo'])
            
                        
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
